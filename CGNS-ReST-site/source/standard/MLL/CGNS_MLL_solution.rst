.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLSolutionData:
   
Solution Data
-------------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Flow Solution`_
   * - ``cg_sol_write``
     - Create and/or write to a FlowSolution_t node
   * - ``cg_nsols``
     - Get number of FlowSolution_t nodes
   * - ``cg_sol_info``
     - Get info about a FlowSolution_t node
   * - ``cg_sol_ptset_write``
     - Create a point set FlowSolution_t node
   * - ``cg_sol_ptset_info``
     - Get info about a point set FlowSolution_t node
   * - ``cg_sol_ptset_read``
     - Read a point set FlowSolution_t node
   * - ``cg_sol_size``
     - Get the dimensions of a FlowSolution_t node

       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Flow Solution Data`_
   * - ``cg_field_write``
     - Write flow solution
   * - ``cg_field_partial_write``
     - Write subset of flow solution
   * - ``cg_field_general_write``
     - Write shaped array to a subset of flow solution
   * - ``cg_nfields``
     - Get number of flow solution arrays
   * - ``cg_field_info`` 
     - Get info about a flow solution array
   * - ``cg_field_read``
     - Read flow solution
   * - ``cg_field_general_read``
     - Read subset of flow solution to a shaped array


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Discrete Data`_
   * - ``cg_discrete_write``
     - Create a DiscreteData_t node
   * - ``cg_ndiscrete``
     - Get number of DiscreteData_t nodes
   * - ``cg_discrete_read``
     - Get name of a DiscreteData_t node
   * - ``cg_discrete_ptset_write``
     - Create a point set DiscreteData_t node
   * - ``cg_discrete_ptset_info``
     - Get info about a point set DiscreteData_t node
   * - ``cg_discrete_ptset_read``
     - Read a point set DiscreteData_t node
   * - ``cg_discrete_size``
     - Get the dimensions of a DiscreteData_t node 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Zone Subregions`_
   * - ``cg_nsubregs``
     - Get number of ZoneSubRegion_t nodes
   * - ``cg_subreg_info``
     - Get info about a ZoneSubRegion_t node
   * - ``cg_subreg_ptset_read``
     - Read point set data for a ZoneSubRegion_t node
   * - ``cg_subreg_bcname_read``
     - Read the BC_t node name for a ZoneSubRegion_t node
   * - ``cg_subreg_gcname_read``
     - Read the GridConnectivity_t node name for a ZoneSubRegion_t node
   * - ``cg_subreg_ptset_write``
     - Create a point set ZoneSubRegion_t node
   * - ``cg_subreg_bcname_write``
     - Create a ZoneSubRegion_t node that references a BC_t node
   * - ``cg_subreg_gcname_write``
     - Create a ZoneSubRegion_t node that references a GridConnectivity_t node 




Flow Solution
^^^^^^^^^^^^^
Node: FlowSolution_t (SIDS, File Mapping) 


Flow Solution Data
^^^^^^^^^^^^^^^^^^

Discrete Data
^^^^^^^^^^^^^
Node: DiscreteData_t (SIDS, File Mapping) 


Zone Subregions
^^^^^^^^^^^^^^^
Node: ZoneSubRegion_t (SIDS, File Mapping) 


.. last line
