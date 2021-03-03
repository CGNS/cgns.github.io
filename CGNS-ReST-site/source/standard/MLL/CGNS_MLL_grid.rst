.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLGridSpecification:
   
Grid Specification
------------------

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Zone Grid Coordinates`_
   * - ``cg_grid_write``
     - Create a GridCoordinates_t node
   * - ``cg_ngrids``
     - Get number of GridCoordinates_t nodes
   * - ``cg_grid_read``
     - Get name of a GridCoordinates_t node
   * - ``cg_grid_bounding_box_read``
     - Get bounding box associated to a GridCoordinates_t node
   * - ``cg_grid_bounding_box_write``
     - Write bounding box associated to a GridCoordinates_t node
   * - ``cg_coord_write``
     - Write grid coordinates
   * - ``cg_coord_partial_write``
     - Write subset of grid coordinates
   * - ``cg_coord_general_write``
     - Write shaped array to a subset of grid coordinates
   * - ``cg_ncoords``
     - Get number of coordinate arrays
   * - ``cg_coord_info``
     - Get info about a coordinate array
   * - ``cg_coord_read``
     - Read grid coordinates
   * - ``cg_coord_general_read``
     - Read subset of grid coordinates to a shaped array 
       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Element Connectivity`_
   * - ``cg_section_write``
     - Write fixed size element data
   * - ``cg_poly_section_write``
     - Write element data
   * - ``cg_section_general_write``
     - Write section data without element data
   * - ``cg_section_initialize``
     - Initialize element data for not fixed size elements
   * - ``cg_section_partial_write``
     - Write subset of element data
   * - ``cg_elements_partial_write``
     - Write element data for a fixed size element section
   * - ``cg_poly_elements_partial_write``
     - Write element data for an element section
   * - ``cg_elements_general_write``
     - Write element data for a fixed size element section
   * - ``cg_poly_elements_general_write``
     - Write element data for an element section
   * - ``cg_parent_data_write``
     - Write parent info for an element section
   * - ``cg_parent_data_partial_write``
     - Write subset of parent info for an element section
   * - ``cg_nsections``
     - Get number of element sections
   * - ``cg_section_read``
     - Get info for an element section
   * - ``cg_ElementDataSize``
     - Get size of element connectivity data array
   * - ``cg_ElementPartialSize``
     - Get size of element connectivity data array for partial read
   * - ``cg_elements_read``
     - Read fixed size element data
   * - ``cg_elements_partial_read``
     - Read subset of fixed size element data
   * - ``cg_elements_general_read``
     - Read subset of fixed size element data to a typed array
   * - ``cg_poly_elements_read``
     - Read element data
   * - ``cg_poly_elements_partial_read``
     - Read subset of element data
   * - ``cg_poly_elements_general_read``
     - Read subset of element data to typed arrays
   * - ``cg_parent_elements_general_read``
     - Read parent info for an element section
   * - ``cg_parent_elements_position_general_read``
     - Read parent position info for an element section
   * - ``cg_npe``
     - Get number of nodes for an element type 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Axisymmetry`_
   * - ``cg_axisym_write``
     - Create axisymmetry data
   * - ``cg_axisym_read``
     - Read axisymmetry data

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Rotating Coordinates`_
   * - ``cg_rotating_write``
     - Create rotating coordinates data
   * - ``cg_rotating_read``
     - Read rotating coordinates data


Zone Grid Coordinates
^^^^^^^^^^^^^^^^^^^^^
Node: GridCoordinates_t (SIDS, File Mapping)

GridCoordinates_t nodes are used to describe grids associated with a particular zone. The original grid must be described by a GridCoordinates_t node named GridCoordinates. Additional GridCoordinates_t nodes may be used, with user-defined names, to store grids at multiple time steps or iterations. In addition to the discussion of the GridCoordinates_t node in the SIDS and File Mapping manuals, see the discussion of the ZoneIterativeData_t and ArbitraryGridMotion_t nodes in the SIDS manual.

 
Element Connectivity
^^^^^^^^^^^^^^^^^^^^
Node: Elements_t (SIDS, File Mapping) 


Axisymmetry
^^^^^^^^^^^
Node: Axisymmetry_t (SIDS, File Mapping)


Rotating Coordinates
^^^^^^^^^^^^^^^^^^^^
Node: RotatingCoordinates_t (SIDS, File Mapping)


.. last line
