# SPDX-FileCopyrightText: 2026 CESNET z.s.p.o
# SPDX-License-Identifier: MIT

"""Tests for configuration loading utilities."""

from __future__ import annotations

import pytest
from flask.config import Config

from oarepo_config import base


def test_overrides(tmp_path, monkeypatch):
    """Configuration sources are merged in their documented priority order."""
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    (tmp_path / "variables").write_text("INVENIO_VALUE=variables\nINVENIO_LIST=[1]\n")
    (tmp_path / ".env").write_text("INVENIO_VALUE=dotenv\nINVENIO_ENABLED=True\n")
    (config_dir / "config.yaml").write_text("value: directory\nnumber: 2\n")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("INVENIO_CONFIG_PATH", str(config_dir))
    monkeypatch.setenv("INVENIO_VALUE", "environment")
    base.load_configuration_overrides.cache_clear()

    env = base.load_configuration_overrides()

    assert env["INVENIO_VALUE"] == "environment"
    assert env["INVENIO_ENABLED"] is True
    assert env["INVENIO_LIST"] == [1]
    assert env["INVENIO_NUMBER"] == 2
    base.load_configuration_overrides.cache_clear()


def test_variables(tmp_path, monkeypatch):
    """Instance variables are available through dictionary and attribute access."""
    instance = tmp_path / "instance"
    instance.mkdir()
    (instance / "invenio.cfg").touch()
    (instance / "variables").write_text("INVENIO_INSTANCE_VALUE=1\n")
    monkeypatch.setenv("INVENIO_INSTANCE_PATH", str(instance))
    base.load_configuration_overrides.cache_clear()
    base.load_configuration_variables.cache_clear()

    env = base.load_configuration_variables()

    assert env["INVENIO_INSTANCE_VALUE"] == 1
    assert env.INVENIO_INSTANCE_VALUE == 1
    with pytest.raises(AttributeError):
        _ = env.MISSING
    base.load_configuration_overrides.cache_clear()
    base.load_configuration_variables.cache_clear()


def test_directory(tmp_path):
    """JSON and YAML configuration files are loaded, and a missing path fails clearly."""
    (tmp_path / "one.json").write_text('{"one": 1}')
    (tmp_path / "two.yml").write_text("invenio_two: true\n")

    config = base.load_config_from_directory(tmp_path, Config(tmp_path))

    assert config["INVENIO_ONE"] == 1
    assert config["INVENIO_TWO"] is True
    with pytest.raises(FileNotFoundError):
        base.load_config_from_directory(tmp_path / "missing", Config(tmp_path))


def test_override():
    """Only prefixed variables are copied into the caller configuration."""
    base.override_configuration({"INVENIO_ANSWER": 42, "IGNORED": "value"})

    assert globals()["ANSWER"] == 42
    assert "IGNORED" not in globals()


def test_path(monkeypatch):
    """Finding an instance path without configuration context raises an error."""
    monkeypatch.delenv("INVENIO_INSTANCE_PATH", raising=False)

    with pytest.raises(ValueError, match=r"Cannot find invenio\.cfg"):
        base.get_invenio_cfg_path()
