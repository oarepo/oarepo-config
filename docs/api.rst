API Reference
=============

This page is generated automatically from the docstrings in the
``oarepo_config`` source code, so it always matches the installed
version of the package.

Top-level package
------------------

Everything below is what you get from ``import oarepo_config as config``
and call as ``config.configure_ui(...)``, ``config.configure_cron(...)``,
etc. in ``invenio.cfg``. This is the list of functions most people
writing an ``invenio.cfg`` will actually use - see the
`README <index.html>`_ for a guided tour and a full example.

.. automodule:: oarepo_config
   :members:
   :undoc-members:
   :show-inheritance:

Module reference
-----------------

The sections below document every module individually, including
internal helpers that are not re-exported from the top-level
``oarepo_config`` package. This is mostly useful if you are extending
``oarepo_config`` itself, or writing your own ``configure_*()``-style
helper following the same pattern.

``oarepo_config.base``
~~~~~~~~~~~~~~~~~~~~~~~

The low-level machinery (environment-variable loading, and the
"write constants into invenio.cfg" mechanism) that every ``configure_*()``
function is built on top of.

.. automodule:: oarepo_config.base
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.communities``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.communities
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.cron``
~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.cron
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.datastreams``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.datastreams
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.einfra``
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.einfra
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.generic_parameters``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.generic_parameters
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.i18n``
~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.i18n
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.initial_configuration``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plain module-level settings, not a ``configure_*()`` function - see the
"``initial_configuration.py`` / ``initial_rdm_config.py``" section of the
`README <index.html>`_ for how (and whether) this currently gets loaded
automatically.

.. automodule:: oarepo_config.initial_configuration
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.initial_rdm_config``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plain module-level settings, not a ``configure_*()`` function - see the
same note as above.

.. automodule:: oarepo_config.initial_rdm_config
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.jobs``
~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.jobs
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.models``
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.models
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.oai``
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.oai
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.stats``
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.stats
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.ui``
~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.ui
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.vocabulary``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: oarepo_config.vocabulary
   :members:
   :undoc-members:
   :show-inheritance:

``oarepo_config.workflows``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``register_workflow``, ``configure_workflows``, ``CommunityWorkflow``,
``IndividualWorkflow`` and ``BaseWorkflowSettings`` are already documented
above under the top-level package; ``:no-index:`` avoids re-registering
those (Sphinx errors on class descriptions - unlike functions - being
registered twice) while still showing them here too.

.. automodule:: oarepo_config.workflows
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:
