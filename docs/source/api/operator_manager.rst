Operator Manager
================
.. warning:: This class should not be used directly,
             but should be accessed by om
.. automodule:: uv_align_distribute.operator_manager
    :members:
    :private-members:
    :undoc-members:

**Usage:**

Import the module and use the symbol 'om'.
'om' is a static global instance of :class:`.OperatorManger`.
Then call 'addOperator(YourOperator)'.

**Example:**

.. code-block:: python

    from . import make_islands, templates, utils, operator_manager

    class MyOperator(templates.UvOperatorTemplate):
      # operator logic


    _om = operator_manager.om
    _om.addOperator(MyOperator)
