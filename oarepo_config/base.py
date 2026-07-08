import functools
import inspect
import json
import os
import re
import sys
from collections.abc import Mapping, Sequence, Set
from io import StringIO
from pathlib import Path
from typing import Any

import yaml
from dotenv import dotenv_values
from flask.config import Config


def set_constants_in_caller(constants):
    """
    Sets the constants in the caller's globals.

    Example:

    mymodule:
      import config
      config.doit()
      print(MY_CONSTANT)

    config:
        def doit():
            set_constants_in_caller({"MY_CONSTANT": 42})
    """
    # Get the caller's frame
    current_frame = inspect.currentframe()
    assert current_frame is not None, "Cannot get the current frame"

    config_func_frame = current_frame.f_back
    assert config_func_frame is not None, "Cannot get the config function frame"

    invenio_cfg_frame = config_func_frame.f_back
    assert invenio_cfg_frame is not None, "Cannot get the invenio.cfg frame"

    # Get the caller's globals
    caller_globals = invenio_cfg_frame.f_globals

    for key, value in constants.items():
        if re.match(r"^[A-Z0-9_]+$", key):
            caller_globals[key] = value

    del invenio_cfg_frame
    del config_func_frame
    del current_frame


def get_constant_from_caller(name, default=None):
    """
    Get constant from the caller frame and optionally return a default value
    if not found.

    Example:

    mymodule:
      import config

      MY_CONSTANT = 42
      config.doit()

    config:
        def doit():
            # prints 42
            print(getet_constant_from_caller("MY_CONSTANT", 20))

    """
    current_frame = inspect.currentframe()
    assert current_frame is not None, "Cannot get the current frame"

    config_func_frame = current_frame.f_back
    assert config_func_frame is not None, "Cannot get the config function frame"

    invenio_cfg_frame = config_func_frame.f_back
    assert invenio_cfg_frame is not None, "Cannot get the invenio.cfg frame"

    caller_globals = invenio_cfg_frame.f_globals
    del invenio_cfg_frame
    del config_func_frame
    del current_frame

    return caller_globals.get(name, default)

def merge_with_caller(name, to_merge):
    current_frame = inspect.currentframe()
    assert current_frame is not None, "Cannot get the current frame"

    config_func_frame = current_frame.f_back
    assert config_func_frame is not None, "Cannot get the config function frame"

    invenio_cfg_frame = config_func_frame.f_back
    assert invenio_cfg_frame is not None, "Cannot get the invenio.cfg frame"

    caller_globals = invenio_cfg_frame.f_globals
    del invenio_cfg_frame
    del config_func_frame
    del current_frame

    if name not in caller_globals:
        return to_merge
    existing = caller_globals[name]
    if isinstance(to_merge, Mapping):
        return type(to_merge)({**existing, **to_merge})
    elif isinstance(to_merge, Set):
        return type(to_merge)(existing | to_merge)
    elif isinstance(to_merge, Sequence):
        return type(to_merge)([*existing, *to_merge])

def get_invenio_cfg_path():
    if os.environ.get("INVENIO_INSTANCE_PATH"):
        return Path(os.environ["INVENIO_INSTANCE_PATH"]) / "invenio.cfg"

    cf = inspect.currentframe()
    while cf:
        if cf.f_code.co_filename.endswith("invenio.cfg"):
            return cf.f_code.co_filename
        cf = cf.f_back
    del cf
    raise ValueError("Cannot find invenio.cfg file in the stack")


@functools.lru_cache(maxsize=1)
def load_configuration_overrides():
    """Read deployment configuration values from the current directory and the process environment.

    This is the part of :func:`load_configuration_variables` that does
    *not* depend on the location of ``invenio.cfg``: it merges, lowest
    to highest priority, a ``variables`` file in the current working
    directory, a ``.env`` file in the current working directory, any
    ``.json``/``.yaml``/``.yml`` files under the directory named by the
    ``INVENIO_CONFIG_PATH`` environment variable (if set), and finally
    the actual process environment variables whose name starts with
    ``INVENIO_``.
    """
    env = Config(os.path.dirname(__file__))

    # import the contents of the "variables" file in the root of the repository
    # note: we suppose that we are always started from the root of the repository
    if Path("variables").exists():
        vals = dotenv_values("variables")
        env.from_mapping(vals)

    # then overwrite it with .env file in the local directory
    if Path(".env").exists():
        vals = dotenv_values(".env")
        env.from_mapping(vals)

    if os.environ.get("INVENIO_CONFIG_PATH"):
        load_config_from_directory(os.environ.get("INVENIO_CONFIG_PATH"), env)

    # finally overwrite it with environment variables
    env.from_mapping({k: v for k, v in os.environ.items() if k.startswith("INVENIO_")})

    # transform values from strings to their actual types
    for k, v in list(env.items()):
        env[k] = transform_value(v)
        setattr(env, k, transform_value(v))

    return env


class DictWithGetAttr(dict):
    """Dictionary that allows access to its items as attributes."""

    def __getattr__(self, item):
        if item in self:
            return self[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )


# Import the configuration from the local .env if it exists
# and overwrite it with environment variables
# Loading it this way so could interpolate values
@functools.lru_cache(maxsize=1)
def load_configuration_variables():
    """Read the deployment's configuration values (``INVENIO_...`` variables).

    Collects configuration values set by the deployment, from multiple
    places, each one able to override the previous (lowest to highest
    priority):

    1. a ``variables`` file next to ``invenio.cfg`` (the instance
       directory);
    2. a ``variables`` file in the current working directory;
    3. a ``.env`` file in the current working directory;
    4. any ``.json``/``.yaml``/``.yml`` files under the directory named
       by the ``INVENIO_CONFIG_PATH`` environment variable, if set;
    5. the actual process environment variables (always wins).

    Values such as ``"True"``/``"False"`` or JSON snippets are converted
    to real Python types (booleans, numbers, lists, dicts) where
    possible. The result can be accessed both as a dictionary and via
    attribute access (e.g. ``env.INVENIO_SECRET_KEY``); accessing a
    variable that was never set raises ``AttributeError``.
    """
    env = Config(os.path.dirname(__file__))
    # lowest priority are variables
    bundled_env = Path(get_invenio_cfg_path()).parent / "variables"
    if bundled_env.exists():
        vals = dotenv_values(str(bundled_env))
        env.from_mapping(vals)

    env.update(load_configuration_overrides())

    # transform values from strings to their actual types
    for k, v in list(env.items()):
        env[k] = transform_value(v)
        setattr(env, k, transform_value(v))

    return DictWithGetAttr(**env)


def transform_value(x):
    """Convert string from environment to python type."""
    if not isinstance(x, str):
        return x
    if x == "False":
        return False
    if x == "True":
        return True
    try:
        return json.loads(x)
    except:
        return x


def find_files(directory, extension):
    for root, _, files in os.walk(directory, followlinks=True):
        for file in files:
            if file.endswith(extension):
                yield Path(root) / file


def load_config_from_directory(config_dir, env):
    print("Loading configuration from directory", config_dir, file=sys.stderr)
    root_path = Path(config_dir)
    if not root_path.exists():
        raise FileNotFoundError(f"Configuration directory {root_path} not found")

    # look for all .json & .yaml & .yml files in the directory
    config_files = (
        list(find_files(root_path, ".json"))
        + list(find_files(root_path, ".yaml"))
        + list(find_files(root_path, ".yml"))
    )

    # resolve to absolute paths, deduplicate and sort alphabetically
    config_files = list(sorted(set(str(f.resolve()) for f in config_files)))

    # load the configuration files
    for cfg in config_files:
        print("  processing file", cfg, file=sys.stderr)
        loaded_config_text = Path(cfg).read_text().lstrip()
        if loaded_config_text.startswith("{"):
            loaded_config = json.loads(loaded_config_text)
        else:
            loaded_config = yaml.safe_load(StringIO(loaded_config_text))
        for k, v in loaded_config.items():
            k = k.upper()
            if not k.startswith("INVENIO_"):
                k = f"INVENIO_{k}"
            print("    setting key ", k, file=sys.stderr)
            env[k] = v

    print("Configuration loaded", file=sys.stderr)
    return env


def override_configuration(env: dict[str, Any] | None = None) -> None:
    """Apply ad-hoc configuration overrides from the environment, without writing Python code.

    Lets a deployment set (or override) any Invenio configuration value
    directly from the ``variables``/``.env`` files or the process
    environment, by prefixing its name with ``INVENIO_``. For example,
    setting ``INVENIO_RDM_ARCHIVE_DOWNLOAD_ENABLED=false`` in the
    deployment's configuration will set the ``RDM_ARCHIVE_DOWNLOAD_ENABLED``
    setting to ``False``, without needing to change ``invenio.cfg``.

    This is not applied automatically - call it explicitly from
    ``invenio.cfg``, typically as the very last step, so that these
    overrides win over anything set by the ``configure_*()`` functions
    above it.

    Args:
        env: Normally left unset, in which case the values loaded from
            ``variables``/``.env``/the process environment are used.
    """
    if env is None:
        env = load_configuration_overrides()
    constants_to_override: dict[str, Any] = {}
    for k, v in env.items():
        if k.startswith("INVENIO_"):
            k = k[8:]
            constants_to_override[k] = v
    set_constants_in_caller(constants_to_override)
