.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLStructuralNodes:
   
Structural Nodes
----------------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `CGNS Base Information`_
   * - ``cg_base_write`` 
     - Create and/or write to a CGNS base node 
   * - ``cg_nbases``
     - Get number of CGNS base nodes in file 
   * - ``cg_base_read`` 
     -  Read CGNS base information
   * - ``cg_cell_dim``
     - Get the cell dimension for the CGNS base
       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Zone Information`_
   * - ``cg_zone_write`` 
     - Create and/or write to a zone node
   * - ``cg_nzones`` 
     - Get number of zones in base 
   * - ``cg_zone_read`` 
     - Read zone information
   * - ``cg_zone_type`` 
     - Get type of zone (structured or unstructured)
   * - ``cg_index_dim`` 
     - Get the index dimension for the CGNS zone
   
.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Simulation Type`_
   * - ``cg_simulation_type_write`` 
     - Write simulation type
   * - ``cg_simulation_type_read`` 
     - Read simulation type


CGNS Base Information
^^^^^^^^^^^^^^^^^^^^^
Node: CGNSBase_t (SIDS, File Mapping)

.. table::
   :widths: 110 15
   
   +---------------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                           | Modes   |
   +=======================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_base_write` (:in:`int fn`, :in:`char *basename`, :in:`int cell_dim`, :in:`int phys_dim`, :out:`int *B`);   | `- w m` |
   +---------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_nbases` (:in:`int fn`, :out:`int *nbases`);                                                                | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_base_read` (:in:`int fn`, :in:`int B`, :out:`char *basename`, :out:`int *cell_dim`, :out:`int *phys_dim`); | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_cell_dim` (:in:`int fn`, :in:`int B`, :out:`int *cell_dim`);                                               | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------+---------+
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                             | Modes   |
   +================================================================================================================================+=========+
   | call ``cg_base_write_f`` (:in:`fn`, :in:`basename`, :in:`cell_dim`, :in:`phys_dim`, :out:`B`, :out:`ier`)                      | `- w m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_nbases_f`` (:in:`fn`, :out:`nbases`, :out:`ier`)                                                                     | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_base_read_f`` (:in:`fn`, :in:`B`, :out:`basename`, :out:`cell_dim`, :out:`phys_dim`, :out:`ier`)                     | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_cell_dim_f`` (:in:`fn`, :in:`B`, :out:`cell_dim`, :out:`ier`)                                                        | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   
:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:fn:	   	CGNS file index number.
:B:         Base index number, where 1 ≤ B ≤ nbases.
:nbases:	Number of bases present in the CGNS file fn.
:basename:	Name of the base.
:cell_dim:	Dimension of the cells; 3 for volume cells, 2 for surface cells and 1 for line cells.
:phys_dim:	Number of coordinates required to define a vector in the field.
:ier:		Error status. 

Zone Information
^^^^^^^^^^^^^^^^
Node: Zone_t (SIDS, File Mapping) 

.. table::
   :widths: 110 15
   
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                                                   | Modes   |
   +===============================================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_zone_write` (:in:`int fn`, :in:`int B`, :in:`char *zonename`, :in:`cgsize_t *size`, :in:`ZoneType_t zonetype`, :out:`int *Z`);     | `- w m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_nzones` (:in:`int fn`, :in:`int B`, :out:`int *nzones`);                                                                           | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_zone_read` (:in:`int fn`, :in:`int B`, :in:`int Z`, :out:`char *zonename`, :out:`cgsize_t *size`);                                 | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_zone_type` (:in:`int fn`, :in:`int B`, :in:`int Z`, :out:`ZoneType_t *zonetype`);                                                  | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_index_dim` (:in:`int fn`, :in:`int B`, :in:`int Z`, :out:`int *index_dim`);                                                        | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
.. table::
   :widths: 110 15
   
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                                                            | Modes   |
   +===============================================================================================================================================================+=========+
   | call ``cg_zone_write_f`` (:in:`fn`, :in:`B`, :in:`zonename`, :in:`size`, :in:`zonetype`, :out:`Z`, :out:`ier`)                                                | `- w m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_nzones_f`` (:in:`fn`, :in:`B`, :out:`nzones`, :out:`ier`)                                                                                           | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_zone_read_f`` (:in:`fn`, :in:`B`, :in:`Z`, :out:`zonename`, :out:`size`, :out:`ier`)                                                                | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_zone_type_f`` (:in:`fn`, :in:`B`, :in:`Z`, :out:`zonetype`, :out:`ier`)                                                                             | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_index_dim_f`` (:in:`fn`, :in:`B`, :in:`Z`, :out:`index_dim`, :out:`ier`)                                                                            | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:fn:	   	CGNS file index number.
:B:		Base index number, where 1 ≤ B ≤ nbases.
:Z:		Zone index number, where 1 ≤ Z ≤ nzones.
:nzones:		Number of zones present in base B.
:zonename:		Name of the zone.
:size: Number of vertices, cells, and boundary vertices in each (index)-dimension. For structured grids, the dimensions have unit stride in the array (e.g., [NVertexI, NVertexJ, NVertexK, NCellI, NCellJ, NCellK, NBoundVertexI, NBoundVertexJ, NBoundVertexK]).

       Note that for unstructured grids, the number of cells is the number of highest order elements. Thus, in three dimensions it's the number of 3-D cells, and in two dimensions it's the number of 2-D cells.

       Also for unstructured grids, if the nodes are sorted between internal nodes and boundary nodes, the optional parameter NBoundVertex must be set equal to the number of boundary nodes. By default, NBoundVertex equals zero, meaning that the nodes are unsorted.

       Note that a non-zero value for NBoundVertex only applies to unstructured grids. For structured grids, the NBoundVertex parameter always equals 0 in all directions.
       
       .. table::

          +------------------+-----------------------------------------------------------+
          | Mesh Type        | Size                                                      |
          +==================+===========================================================+
          | 3D structured    | | NVertexI, NVertexJ, NVertexK                            |
          |                  | | NCellI, NCellJ, NCellK                                  |
          |                  | | NBoundVertexI = 0, NBoundVertexJ = 0, NBoundVertexK = 0 |
          +------------------+-----------------------------------------------------------+
          | 2D structured    | | NVertexI, NVertexJ                                      |
          |                  | | NCellI, NCellJ                                          |
          |                  | | NBoundVertexI = 0, NBoundVertexJ = 0                    |
          +------------------+-----------------------------------------------------------+
          | 3D unstructured  |  NVertex, NCell3D, NBoundVertex                           |
          +------------------+-----------------------------------------------------------+
          | 2D unstructured  |  NVertex, NCell2D, NBoundVertex                           |
          +------------------+-----------------------------------------------------------+


:zonetype:		Type of the zone. The admissible types are Structured and Unstructured.
:index_dim:		Index dimension for the zone. For Structured zones, this will be the base cell dimension and for Unstructured zones it will be 1
:ier:		Error status.

.. note::

  When a CGNS file is opened via the cg_open() MLL function, the zones are sorted *alphanumerically* by name (the creation order is ignored/discarded). This mechanism is provided to enable ordinal zone indexing. Therefore, if ordinal zone indexing is desired, it is considered good standard practice to always **choose zone names to be alphabetically increasing**. For example, Zone0001, Zone0002, etc. is appropriate for up to 9999 zones.

  Important: Because the cgnsview tool uses the low-level cgio API, it does not sort the zones by name and zone order presented may not match that of the MLL API. Generally, cgnsview presents the zones in creation order for both ADF and HDF5 formats.


Simulation Type
^^^^^^^^^^^^^^^
Node: SimulationType_t (SIDS, File Mapping) 

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                    | Modes   |
   +================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_simulation_type_write` (:in:`int fn`, :in:`int B`, :in:`SimulationType_t SimulationType`);          | `- w m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_simulation_type_read` (:in:`int fn`, :in:`int B`, :out:`SimulationType_t *SimulationType`);         | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                             | Modes   |
   +================================================================================================================================+=========+
   | call ``cg_simulation_type_write_f`` (:in:`fn`, :in:`B`, :out:`SimulationType`, :out:`ier`)                                     | `- w m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_simulation_type_read_f``  (:in:`fn`, :in:`B`, :out:`SimulationType`, :out:`ier`)                                     | `r - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:fn:              CGNS file index number.
:B:               Base index number, where 1 ≤ B ≤ nbases.
:SimulationType:  Type of simulation. Valid types are CG_Null, CG_UserDefined, TimeAccurate, and NonTimeAccurate.
:ier:             Error status. 
 
.. last line
