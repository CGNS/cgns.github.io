.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLBoundaryConditions:
   
Boundary Conditions
-------------------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Boundary Condition Type and Location`_
   * - ``cg_boco_write``
     - Write boundary condition type and data
   * - ``cg_boco_normal_write``
     - Write boundary condition normals
   * - ``cg_nbocos``
     - Get number of boundary condition in zone
   * - ``cg_boco_info``
     - Get boundary condition info
   * - ``cg_boco_read``
     - Read boundary condition data and normals
   * - ``cg_boco_gridlocation_write``
     - Write boundary condition location
   * - ``cg_boco_gridlocation_read``
     - Read boundary condition location

       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Boundary Condition Datasets`_
   * - ``cg_dataset_write``
     - Write boundary condition dataset info
   * - ``cg_dataset_read``
     - Read boundary condition dataset info
   * - ``cg_bcdataset_write``
     - Write family boundary condition dataset info
   * - ``cg_bcdataset_info``
     - Get number of family boundary condition datasets
   * - ``cg_bcdataset_read``
     - Read family boundary condition dataset info


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Boundary Condition Data`_
   * - ``cg_bcdata_write``
     - Write boundary condition data 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Special Boundary Condition Properties`_
   * - ``cg_bc_wallfunction_write``
     - Write wall function data
   * - ``cg_bc_area_write``
     - Write area-related data
   * - ``cg_bc_wallfunction_read``
     - Read wall function data
   * - ``cg_bc_area_read``
     - Read area-related data 
   


Boundary Condition Type and Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Node: BC_t (SIDS, File Mapping)

 
Boundary Condition Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Node: BCDataSet_t (SIDS, File Mapping)


Boundary Condition Data
^^^^^^^^^^^^^^^^^^^^^^^
Node: BCData_t (SIDS, File Mapping) 


Special Boundary Condition Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Node: BCProperty_t (SIDS, File Mapping)


.. last line
