.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLFamilies:
   
Families
--------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Family Definition`_
   * - ``cg_family_write``
     - Create a Family_t node (CGNSBase_t level)
   * - ``cg_nfamilies``
     - Get number of families (CGNSBase_t level)
   * - ``cg_family_read``
     - Read family info (CGNSBase_t level)
   * - ``cg_family_name_write``
     - Write multiple family names under Family_t (CGNSBase_t level)
   * - ``cg_nfamily_names``
     - Get number of family names under Family_t (CGNSBase_t level)
   * - ``cg_family_name_read``
     - Read multiple family names under Family_t (CGNSBase_t level) 

       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Family Hierarchy Tree`_
   * - ``cg_node_family_write``
     - Create a Family_t node (Family_t level)
   * - ``cg_node_nfamilies``
     - Get number of families (Family_t level)
   * - ``cg_node_family_read``
     - Read family info (Family_t level)
   * - ``cg_node_family_name_write``
     - Write multiple family names under Family_t (Family_t level)
   * - ``cg_node_nfamily_names``
     - Get number of family names under Family_t (Family_t level)
   * - ``cg_node_family_name_read``
     - Read multiple family names under Family_t (Family_t level)


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Geometry Reference`_
   * - ``cg_geo_write``
     - Create a GeometryReference_t node
   * - ``cg_geo_read``
     - Read geometry reference info
   * - ``cg_part_write``
     - Write geometry entity name
   * - ``cg_part_read``
     - Get geometry entity name 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Family Boundary Condition`_
   * - ``cg_fambc_write``
     - Write boundary condition type for a family
   * - ``cg_fambc_read``
     - Read boundary condition type for a family 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Family Name`_
   * - ``cg_get_cgio`` 
     - get the CGIO index number
   * - ``cg_root_id`` 
     - get the root node ID


Family Definition
^^^^^^^^^^^^^^^^^
Node: Family_t (SIDS, File Mapping) 


Family Hierarchy Tree
^^^^^^^^^^^^^^^^^^^^^
Node: Family_t (SIDS, File Mapping) 


Geometry Reference
^^^^^^^^^^^^^^^^^^
Node: GeometryReference_t (SIDS, File Mapping) 


Family Boundary Condition
^^^^^^^^^^^^^^^^^^^^^^^^^
Node: FamilyBC_t (SIDS, File Mapping)


Family Name
^^^^^^^^^^^
Node: FamilyName_t (SIDS, File Mapping)


.. last line
