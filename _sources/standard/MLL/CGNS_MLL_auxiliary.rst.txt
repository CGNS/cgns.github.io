.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLAuxiliaryData:
   
Auxiliary Data
--------------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Reference State`_
   * - ``cg_state_write``
     - Create ReferenceState_t node
   * - ``cg_state_size``
     - Get length of reference state description string.
   * - ``cg_state_read``
     - Read text description of reference state.


.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Gravity`_
   * - ``cg_gravity_write``
     - Create Gravity_t node
   * - ``cg_gravity_read``
     - Read Gravity_t node 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Convergence History`_
   * - ``cg_convergence_write``
     - Create ConvergenceHistory_t node
   * - ``cg_convergence_read``
     - Read ConvergenceHistory_t node

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Integral Data`_
   * - ``cg_integral_write``
     - Create IntegralData_t node
   * - ``cg_nintegrals``
     - Get number of IntegralData_t nodes
   * - ``cg_integral_read``
     - Get name of an IntegralData_t node 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `User-Defined Data`_
   * - ``cg_user_data_write``
     - Create UserDefinedData_t node
   * - ``cg_nuser_data``
     - Get number of UserDefinedData_t nodes
   * - ``cg_user_data_read``
     - Get name of an UserDefinedData_t node


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Freeing Memory`_
   * - ``cg_free``
     - Release library-allocated memory 


Reference State
^^^^^^^^^^^^^^^
Node: ReferenceState_t (SIDS, File Mapping)


Gravity
^^^^^^^
Node: Gravity_t (SIDS, File Mapping)

Convergence History
^^^^^^^^^^^^^^^^^^^
Node: ConvergenceHistory_t (SIDS, File Mapping)

Integral Data
^^^^^^^^^^^^^
Node: IntegralData_t (SIDS, File Mapping) 

User-Defined Data
^^^^^^^^^^^^^^^^^
Node: UserDefinedData_t (SIDS, File Mapping)

Freeing Memory
^^^^^^^^^^^^^^



.. last line
