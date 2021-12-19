.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c
   
.. role:: implicit



.. _MLLNavigating:
   
Navigating a CGNS File
----------------------


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Accessing a Node`_
   * - ``cg_goto`` 
     - Access a node via label/name, index pairs
   * - ``cg_gorel``
     - Access a node via relative path
   * - ``cg_gopath`` 
     - Access a node via pathname
   * - ``cg_golist``
     - Access a node via arrays of labels and indices
   * - ``cg_where``
     - Get path to current node
   
       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Deleting a Node`_
   * - ``cg_delete_node`` 
     - Delete a node

Accessing a Node
^^^^^^^^^^^^^^^^

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`ier` = :sig-name:`cg_goto` (:in:`int fn`, :in:`int B`, ..., :in:`"end"`);                                                | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_gorel` (:in:`int fn`, ..., :in:`"end"`);                                                            | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_gopath` (:in:`int fn`, :in:`const char *path`);                                                     | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_golist` (:in:`int fn`, :in:`int B`, :in:`int depth`, :in:`char **label`, :in:`int *index`);         | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_where` (:out:`int *fn`, :in:`int *B`, :out:`int *depth`, :out:`char **label`, :out:`int *index`);   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call :implicit:`cg_goto_f` (:in:`fn`, :in:`B`, :out:`ier`, ..., :in:`'end'`)                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call :implicit:`cg_gorel_f` (:in:`fn`, :out:`ier`, ..., :in:`'end'`)                                                           | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call `cg_gopath_f` (:in:`fn`, :in:`path`, :out:`ier`)                                                                          | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:fn:  CGNS file index number.

:B:   Base index number, where 1 ≤ B ≤ nbases.

:`...`:   Variable argument list used to specify the path to a node. It is composed of an unlimited list of pair-arguments identifying each node in the path. Nodes may be identified by their label or name. Thus, a pair-argument may be of the form

       "CGNS_NodeLabel", NodeIndex

    where CGNS_NodeLabel is the node label and NodeIndex is the node index, or

        "CGNS_NodeName", 0

    where CGNS_NodeName is the node name. The 0 in the second form is required, to indicate that a node name is being specified rather than a node label. In addition, a pair-argument may be specified as

         "..", 0

    indicating the parent of the current node. The different pair-argument forms may be intermixed in the same function call.

    There is one exception to this rule. When accessing a BCData_t node, the index must be set to either Dirichlet or Neumann since only these two types are allowed. (Note that Dirichlet and Neumann are defined in the include files cgnslib.h and cgnslib_f.h). Since "Dirichlet" and "Neuman" are also the names for these nodes, you may also use the "Dirichlet", 0 or "Neuman", 0 to access the node. See the example below.

:end:		The character string "end" (or 'end' for the Fortran function) must be the last argument. It is used to indicate the end of the argument list. You may also use the empty string, "" ('' for Fortran), or the NULL string in C, to terminate the list.

:path:		The pathname for the node to go to. If a position has been already set, this may be a relative path, otherwise it is an absolute path name, starting with "/Basename", where Basename is the base under which you wish to move.

:depth:		Depth of the path list. The maximum depth is defined in cgnslib.h by CG_MAX_GOTO_DEPTH, and is currently equal to 20.

:label:		Array of node labels for the path. This argument may be passed as NULL to cg_where(), otherwise it must be dimensioned by the calling program. The maximum size required is label[MAX_GO_TO_DEPTH][33]. You may call cg_where() with both label and index set to NULL in order to get the current depth, then dimension to that value.

:index: 	Array of node indices for the path. This argument may be passed as NULL to cg_where(), otherwise it must be dimensioned by the calling program. The maximum size required is index[MAX_GO_TO_DEPTH]. You may call cg_where() with both label and index set to NULL in order to get the current depth, then dimension to that value.

:ier:  Error status. The possible values, with the corresponding C names (or Fortran parameters) defined in cgnslib.h (or cgnslib_f.h) are listed below.

   .. table::

     =======    ===================
      Value      Name/Parameter
     =======    ===================
      0          CG_OK
      1          CG_ERROR
      2          CG_NODE_NOT_FOUND
      3          CG_INCORRECT_PATH
     =======    ===================

   For non-zero values, an error message may be printed using cg_error_print().

This function allows access to any parent-type nodes in a CGNS file. A parent-type node is one that can have children. Nodes that cannot have children, like Descriptor_t, are not supported by this function. 

To illustrate the use of the above routines, assume you have a file with CGNS index number filenum, a base node named Base with index number basenum, 2 zones (named Zone1 and Zone2, with indices 1 and 2), and user-defined data (User, index 1) below each zone. To move to the user-defined data node under zone 1, you may use any of the following:

.. code-block::

   cg_goto(filenum, basenum, "Zone_t", 1, "UserDefinedData_t", 1, NULL);
   cg_goto(filenum, basenum "Zone1", 0, "UserDefinedData_t", 1, NULL);
   cg_goto(filenum, basenum, "Zone_t", 1, "User", 0, NULL);
   cg_goto(filenum, basenum, "Zone1", 0, "User", 0, NULL);
   cg_gopath(filenum, "/Base/Zone1/User");

Now, to change to the user-defined data node under zone 2, you may use the full path specification as above, or else a relative path, using one of the following:

.. code-block::

   cg_gorel(filenum, "..", 0, "..", 0, "Zone_t", 2, "UserDefinedData_t", 1, NULL);
   cg_gorel(filenum, "..", 0, "..", 0, "Zone2", 0, "UserDefinedData_t", 1, NULL);
   cg_gorel(filenum, "..", 0, "..", 0, "Zone_t", 2, "User", 0, NULL);
   cg_gorel(filenum, "..", 0, "..", 0, "Zone2", 0, "User", 0, NULL);
   cg_gopath(filenum, "../../Zone2/User");

Shown below are some additional examples of various uses of these routines, in both C and Fortran, where fn, B, Z, etc., are index numbers.

.. code-block::

   ier = cg_goto(fn, B, "Zone_t", Z, "FlowSolution_t", F, "..", 0, "MySolution", 0, "end");

   ier = cg_gorel(fn, "..", 0, "FlowSolution_t", F, NULL);

   ier = cg_gopath(fn, "/MyBase/MyZone/MySolution");

   ier = cg_gopath(fn, "../../MyZoneBC");

.. code-block::

   call cg_goto_f(fn, B, ier, 'Zone_t', Z, 'GasModel_t', 1, 'DataArray_t', A, 'end')

   call cg_goto_f(fn, B, ier, 'Zone_t', Z, 'ZoneBC_t', 1, 'BC_t', BC, 'BCDataSet_t', S,
                  'BCData_t', Dirichlet, 'end')

   call cg_gorel_f(fn, ier, '..', 0, 'Neumann', 0, '')

   call cg_gopath_f(fn, '../../MyZoneBC', ier)


Deleting a Node
^^^^^^^^^^^^^^^

.. table:: Configuring CGNS Internals
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                    | Modes   |
   +================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_delete_node` (:in:`char *NodeName`)                                                                 | `- - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                             | Modes   |
   +================================================================================================================================+=========+
   | call ``cg_delete_node`` (:in:`NodeName`, :out:`ier`)                                                                           | `- - m` |
   +--------------------------------------------------------------------------------------------------------------------------------+---------+


:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
  :NodeName:    Name of the child to be deleted.
  :ier:         Error status.


The function cg_delete_node is used is conjunction with cg_goto. Once positioned at a parent node with cg_goto, a child of this node can be deleted with cg_delete_node. This function requires a single argument, NodeName, which is the name of the child to be deleted.

Since the highest level that can be pointed to with cg_goto is a base node for a CGNS database (CGNSBase_t), the highest-level nodes that can be deleted are the children of a CGNSBase_t node. In other words, nodes located directly under the ADF (or HDF) root node (CGNSBase_t and CGNSLibraryVersion_t) can not be deleted with cg_delete.

A few other nodes are not allowed to be deleted from the database because these are required nodes as defined by the SIDS, and deleting them would make the file non-CGNS compliant.
These are:

- Under Zone_t: ZoneType
- Under GridConnectivity1to1_t: PointRange, PointRangeDonor, Transform
- Under OversetHoles_t: PointList and any IndexRange_t
- Under GridConnectivity_t: PointRange, PointList, CellListDonor, PointListDonor
- Under BC_t: PointList, PointRange
- Under GeometryReference_t: GeometryFile, GeometryFormat
- Under Elements_t: ElementRange, ElementConnectivity
- Under Gravity_t: GravityVector
- Under Axisymmetry_t: AxisymmetryReferencePoint, AxisymmetryAxisVector
- Under RotatingCoordinates_t: RotationCenter, RotationRateVector
- Under Periodic_t: RotationCenter, RotationAngle, Translation
- Under AverageInterface_t: AverageInterfaceType
- Under WallFunction_t: WallFunctionType
- Under Area_t: AreaType, SurfaceArea, RegionName 

When a child node is deleted, both the database and the file on disk are updated to remove the node. One must be careful not to delete a node from within a loop of that node type. For example, if the number of zones below a CGNSBase_t node is nzones, a zone should never be deleted from within a zone loop! By deleting a zone, the total number of zones (nzones) changes, as well as the zone indexing. Suppose for example that nzones is 5, and that the third zone is deleted. After calling cg_delete_node, nzones is changed to 4, and the zones originally indexed 4 and 5 are now indexed 3 and 4. 
 
.. last line
