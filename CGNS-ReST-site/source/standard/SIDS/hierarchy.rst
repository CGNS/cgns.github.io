.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

Hierarchical Structures
+++++++++++++++++++++++

This section presents the structure-type definitions for the top levels of the CGNS hierarchy. As stated in the :ref:`SIDS design philosophy <design>`, the hierarchy is :ref:`topologically based <topology>`, where the overall organization is by zones. All information pertaining to a given zone, including grid coordinates, flow solution, and other related data, is contained within that zone's structure entity. This section describes the :ref:`CGNS version number <CGNS Version>`, defines the :ref:`CGNS database entry level structure <CGNSBase_t>` and the :ref:`zone structure <Zone_t>`, and concludes with a discussion of :ref:`globally applicable data <precedence>`.

CGNS Version
^^^^^^^^^^^^

CGNS is an evolving standard. Although great care is taken to make CGNS databases backward-compatible with previous versions whenever possible, new nodes and new features are still being added that make them non-forward-compatible. To address this issue, each new version of the standard is labeled with a version number that should be written in the file. This version number corresponds to the version of the SIDS and is an essential part of the file containing the CGNS database. The file can not be interpreted properly without knowledge of this version number.

Physically, this version number is located directly under the root node of the file. The :ref:`SIDS File Mapping Manual <CGNSLibraryVersion_t>` defines this location more precisely.

Historically, the version number was used to describe the version of the :ref:`Mid-Level Library <CGNS_MLL>` used to write or modify the file. The corresponding node was thus named :sidskey:`CGNSLibraryVersion_t`. With the advent of new libraries that can read and write CGNS databases, the node is now defined as the version of the CGNS standard. The Mid-Level Library modifies its interpretation of node data according to the CGNS version number, and other libraries should also.

CGNS Entry Level Structure Definition: ``CGNSBase_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The highest level structure in a CGNS database is :sidskey:`CGNSBase_t`. This top level entity is designed to be self-contained, a complete CFD computation can be archived and reproduced using the data defined in the CGNSBase. However a CGNS tree can contain more than one base, these can be related to the same CFD case or not. The behavior of a multi-base CGNS tree is application dependant, even if inter-base relationships are authorized in three cases:

 * A reference to another base's zone name (including its sub-nodes' names) as defined in the multi-zone connectivities (see :ref:`Multizone Interface Connectivity <cnct>` and time-dependant pointers :ref:`Time-Dependent Flow <timedep>`);
 * A reference to another base's family name (see :ref:`Family Data Structure Definition <Family_t>`: :sidsref:`Family_t`) as as :sidskey:`FamilyName_t` data;
 * A LogicalLink() from one base to another on any kind of node;

Care must be taken on precedence rules and scope in the case of parsing multiple CGNS bases (see :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`).

The CGNS Base contains the cell dimension and physical dimension of the computational grid and lists of zones and families making up the domain. Globally applicable information, including a reference state, a set of flow equations, dimensional units, time step or iteration information, and convergence history are also attached. In addition, structures for describing or annotating the database are also provided; these same descriptive mechanisms are provided for structures at all levels of the hierarchy.

.. code-block:: sids

  CGNSBase_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    int CellDimension ;                                                (r)
    int PhysicalDimension ;                                            (r)

    BaseIterativeData_t BaseIterativeData ;                            (o)

    List( Zone_t<CellDimension, PhysicalDimension> Zone1 ... ZoneN ) ; (o)

    ReferenceState_t ReferenceState ;                                  (o)

    Axisymmetry_t Axisymmetry ;                                        (o)

    RotatingCoordinates_t RotatingCoordinates ;                        (o)

    Gravity_t Gravity ;                                                (o)

    SimulationType_t SimulationType ;                                  (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    FlowEquationSet_t<CellDimension> FlowEquationSet ;                 (o)

    ConvergenceHistory_t GlobalConvergenceHistory ;                    (o)

    List( IntegralData_t IntegralData1... IntegralDataN ) ;            (o)

    List( Family_t Family1... FamilyN ) ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`Zone_t`, :sidsref:`IntegralData_t`, :sidsref:`Family_t` and :sidsref:`UserDefinedData_t` lists are as shown;
       users may choose other legitimate names. Legitimate names must be unique at this level and shall not include the names :sidskey:`Axisymmetry`, :sidskey:` BaseIterativeData`, :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FlowEquationSet`, :sidskey:`GlobalConvergenceHistory`, :sidskey:`Gravity`, :sidskey:`ReferenceState`, :sidskey:`RotatingCoordinates` or :sidskey:`SimulationType`.
    2. The number of entities of type :sidskey:`Zone_t` defines the number of zones in the domain.
    3. :sidskey:`CellDimension` and :sidskey:`PhysicalDimension` are the only required fields. The :sidskey:`Descriptor_t`, :sidskey:`Zone_t` and :sidskey:`IntegralData_t` lists may be empty, and all other optional fields absent.

Note that we make the distinction between the following:

============================ ===
:sidskey:`IndexDimension`    Number of different indices required to reference a node (e.g., 1 = :math:`i`, 2 = :math:`i,j`, 3 = :math:`i,j,k`)

:sidskey:`CellDimension`     Dimensionality of the cell in the mesh (e.g., 3 for a volume cell, 2 for a face cell)

:sidskey:`PhysicalDimension` Number of coordinates required to define a node position (e.g., 1 for 1-D, 2 for 2-D, 3 for 3-D)
============================ ===

These three dimensions may differ depending on the mesh. For example, an unstructured triangular surface mesh representing the wet surface of an aircraft will have:

 - :sidskey:`IndexDimension` = 1 (always for unstructured)
 - :sidskey:`CellDimension` = 2 (face elements)
 - :sidskey:`PhysicalDimension` = 3 (needs :math:`x`, :math:`y`, :math:`z` coordinates since it is a 3D surface)

For a structured zone, the quantities :sidskey:`IndexDimension` and :sidskey:`CellDimension` are always equal. For an unstructured zone, :sidskey:`IndexDimension` always equals 1. Therefore, storing :sidskey:`CellDimension` at the :sidskey:`CGNSBase_t` level will automatically define the :sidskey:`IndexDimension` value for each zone.

On the other hand we assume that all zones of the base have the same :sidskey:`CellDimension`, e.g. if :sidskey:`CellDimension` is 3, all zones must be composed of 3D cells within the :sidskey:`CGNSBase_t`.

We need :sidskey:`IndexDimension` for both structured and unstructured zones in order to use original data structures such as :sidsref:`GridCoordinates_t`, :sidsref:`FlowSolution_t`, :sidsref:`DiscreteData_t`, etc.
:sidskey:`CellDimension` is necessary to express the interpolants in :sidskey:`ZoneConnectivity` with an unstructured zone (mismatch or overset connectivity). When the cells are bidimensional, two interpolants per node are required, whereas when the cells are tridimensional, three interpolants per node must be provided. :sidskey:`PhysicalDimension` becomes useful when expressing quantities such as the :sidskey:`InwardNormalList` in the :sidsref:`BC_t` data structure. It's possible to have a mesh where :sidskey:`IndexDimension` = 2 but the normal vectors still require :math:`x`, :math:`y`, :math:`z` components in order to be properly defined. Consider, for example, a structured surface mesh in the 3D space.

Information about the number of time steps or iterations being recorded, and the time and/or iteration values at each step, may be contained in the :sidsref:`BaseIterativeData` structure.

Data specific to each zone in a multizone case is contained in the list of :sidsref:`Zone_t` structure entities.

Reference data applicable to the entire CGNS database is contained in the :sidsref:`ReferenceState` structure; quantities such as Reynolds number and freestream Mach number are contained here (for external flow problems).

:sidsref:`Axisymmetry` may be used to specify the axis of rotation and the circumferential extent for an axisymmetric database.

If a rotating coordinate system is being used, the rotation center and rotation rate vector may be specified using the :sidsref:`RotatingCoordinates` structure.

:sidsref:`Gravity` may be used to define the gravitational vector.

:sidskey:`SimulationType` is an enumeration type identifying the type of simulation. The default value is :sidskey:`SimulationTypeNull`.

.. code-block:: sids

  SimulationType_t := Enumeration (
    SimulationTypeNull,
    SimulationTypeUserDefined,
    TimeAccurate,
    NonTimeAccurate ) ;

:sidsref:`DataClass` describes the global default for the class of data contained in the CGNS database. If the CGNS database contains dimensional data (e.g., velocity with units of :math:`m/s`), :sidsref:`DimensionalUnits` may be used to describe the system of units employed.

:sidsref:`FlowEquationSet` contains a description of the governing flow equations associated with the entire CGNS database. This structure contains information on the general class of governing equations (e.g., Euler or Navier-Stokes), equation sets required for closure, including turbulence modeling and equations of state, and constants associated with the equations.

:sidsref:`DataClass`, :sidsref:`DimensionalUnits`, :sidsref:`ReferenceState`, and :sidsref:`FlowEquationSet` have special function in the CGNS hierarchy. They are globally applicable throughout the database, but their precedence may be superseded by local entities (e.g., within a given zone). The scope of these entities and the rules for determining precedence are treated in the section on :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`.

Globally relevant convergence history information is contained in :sidsref:`GlobalConvergenceHistory`. This convergence information includes total configuration forces, moments, and global residual and solution-change norms taken over all the zones.

Miscellaneous global data may be contained in the :sidsref:`IntegralData_t` list. Candidates for inclusion here are global forces and moments.

Base Level Families
~~~~~~~~~~~~~~~~~~~

The :sidsref:`Family_t` data structure is used to record geometry reference data.
It may also include boundary conditions linked to geometry patches. For the purpose of defining material properties, families may also be defined for groups of elements.
The family-mesh association is defined under the :sidskey:`Zone_t`, the :sidskey:`ZoneSubRegion_t` and :sidskey:`BC_t` data structures by specifying the family name corresponding to a zone or a boundary patch. The familyname can refer to a :sidskey:`Family_t` defined in a :sidskey:`CGNSBase_t` other than the referring :sidskey:`Zone_t`, the :sidskey:`ZoneSubRegion_t` or :sidskey:`BC_t`.
In this case, the actual name of the :sidskey:`Family_t` has to be prefixed by the :sidskey:`CGNSBase_t` name.
The pattern is then :literal:`BaseName/FamilyName`, only one single :literal:`/` character is allowed, and neither of :literal:`BaseName` nor :literal:`FamilyName` should be empty. This :sidskey:`Family_t` node can be a direct child of the :sidskey:`CGNSBase_t` or a child of another :sidskey:`Family_t`.
The actual family name has the pattern :literal:`/<CGNSBase_t>/<FamilyName1>/<FamilyName2>/.../<FamilyNameN>`.
The family-mesh association is defined under the :sidsref:`Zone_t`, :sidsref:`ZoneSubRegion_t` and :sidsref:`BC_t` data structures by specifying the family name corresponding to a zone, a zone sub-region or a boundary patch in a :sidskey:`FamilyName_t` node. If the value of the :sidskey:`FamilyName_t` node does not have a :literal:`/` character in it, then the name refers to a family being a direct child of its CGNS base. Otherwise, if this value has at least one :literal:`/` in it, the pattern :literal:`/<CGNSBase_t>/<FamilyName1>/<FamilyName2>/.../<FamilyNameN>` is mandatory.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidsref:`Descriptor_t` and :sidsref:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Zone Structure Definition: ``Zone_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidskey:`Zone_t` structure contains all information pertinent to an individual zone. This information includes the zone type, the number of cells and vertices making up the grid in that zone, the physical coordinates of the grid vertices, grid motion information, the family, the flow solution, zone interface connectivity, boundary conditions, and zonal convergence history data. Zonal data may be recorded at multiple time steps or iterations. In addition, this structure contains a reference state, a set of flow equations and dimensional units that are all unique to the zone. For unstructured zones, the element connectivity may also be recorded.

.. code-block:: sids

  ZoneType_t := Enumeration(
    ZoneTypeNull,
    ZoneTypeUserDefined,
    Structured,
    Unstructured ) ;

  Zone_t< int CellDimension, int PhysicalDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ZoneType_t ZoneType ;                                              (r)

    int[IndexDimension] VertexSize ;                                   (r)
    int[IndexDimension] CellSize ;                                     (r)
    int[IndexDimension] VertexSizeBoundary ;                           (o/d)

    List( GridCoordinates_t<IndexDimension, VertexSize>
          GridCoordinates MovedGrid1 ... MovedGridN ) ;                (o)

    List( Elements_t Elements1 ... ElementsN ) ;                       (o)

    List( RigidGridMotion_t RigidGridMotion1 ... RigidGridMotionN ) ;  (o)

    List( ArbitraryGridMotion_t<IndexDimension, VertexSize, CellSize>
          ArbitraryGridMotion1 ... ArbitraryGridMotionN ) ;            (o)

    FamilyName_t FamilyName ;                                          (o)

    List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ; (o)

    List( FlowSolution_t<CellDimension, IndexDimension, VertexSize, CellSize>
          FlowSolution1 ... FlowSolutionN ) ;                          (o)

    List( DiscreteData_t<CellDimension, IndexDimension, VertexSize, CellSize>
          DiscreteData1 ... DiscreteDataN ) ;                          (o)

    List( IntegralData_t IntegralData1 ... IntegralDataN ) ;           (o)

    List( ZoneGridConnectivity_t<IndexDimension, CellDimension>
          ZoneGridConnectivity1 ... ZoneGridConnectivityN ) ;          (o)

    List( ZoneSubRegion_t<IndexDimension, VertexSize, CellSize>
          ZoneSubRegion1 ... ZoneSubRegionN ) ;                        (o)

    ZoneBC_t<CellDimension, IndexDimension, PhysicalDimension> ZoneBC ;(o)

    ZoneIterativeData_t<NumberOfSteps> ZoneIterativeData ;             (o)

    ReferenceState_t ReferenceState ;                                  (o)

    RotatingCoordinates_t RotatingCoordinates ;                        (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    FlowEquationSet_t<CellDimension> FlowEquationSet ;                 (o)

    ConvergenceHistory_t ZoneConvergenceHistory ;                      (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;


.. note::

  1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`Elements_t`, :sidsref:`FlowSolution_t`, :sidsref:`DiscreteData_t`, :sidsref:`IntegralData_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`Zone_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FamilyName`, :sidskey:`FlowEquationSet`, :sidskey:`GridCoordinates`, :sidskey:`Ordinal`, :sidskey:`ReferenceState`, :sidskey:`RotatingCoordinates`, :sidskey:`ZoneBC`, :sidskey:`ZoneConvergenceHistory`, :sidskey:`ZoneGridConnectivity`, :sidskey:`ZoneIterativeData`, or :sidskey:`ZoneType`.
  2. The original grid coordinates should have the name :sidskey:`GridCoordinates`. Default names for the remaining entities in the :sidsref:`GridCoordinates_t` list are as shown; users may choose other legitimate names, subject to the restrictions listed in the previous note.
  3. :sidskey:`ZoneType`, :sidskey:`VertexSize`, and :sidskey:`CellSize` are the only required fields within the :sidskey:`Zone_t` structure.

:sidskey:`Zone_t` requires the parameters :sidskey:`CellDimension` and :sidskey:`PhysicalDimension`. :sidskey:`CellDimension`, along with the type of zone, determines :sidskey:`IndexDimension`; if the zone type is Unstructured, :sidskey:`IndexDimension` = 1, and if the zone type is :sidskey:`Structured`, :sidskey:`IndexDimension` = :sidskey:`CellDimension`. These three structure parameters identify the dimensionality of the grid-size arrays. One or more of them are passed on to the grid coordinates, flow solution, interface connectivity, boundary condition and flow-equation description structures.

:sidskey:`VertexSize` is the number of vertices in each index direction, and :sidskey:`CellSize` is the number of cells in each direction. For example, for structured grids in 3-D, :sidskey:`CellSize = VertexSize - [1,1,1]`, and for unstructured grids in 3-D, :sidskey:`CellSize` is simply the total number of 3-D cells. :sidskey:`VertexSize` is the number of vertices defining "the grid" or the domain (i.e., without rind points); :sidskey:`CellSize` is the number of cells on the interior of the domain. These two grid-size arrays are passed onto the grid-coordinate, flow-solution and discrete-data substructures.

If the nodes are sorted between internal nodes and boundary nodes, then the optional parameter :sidskey:`VertexSizeBoundary` must be set equal to the number of boundary nodes. If the nodes are sorted, the grid coordinate vector must first include the boundary nodes, followed by the internal nodes. By default, :sidskey:`VertexSizeBoundary` equals zero, meaning that the nodes are unsorted. This option is only useful for unstructured zones. For structured zones, :sidskey:`VertexSizeBoundary` always equals 0 in all index directions.

The :sidsref:`GridCoordinates_t` structure defines "the grid"; it contains the physical coordinates of the grid vertices, and may optionally contain physical coordinates of rind or ghost points. The original grid is contained in :sidskey:`GridCoordinates`. Additional :sidskey:`GridCoordinates_t` data structures are allowed, to store the grid at multiple time steps or iterations.

When the grid nodes are sorted, the :sidsref:`DataArray_t` in :sidsref:`GridCoordinates_t` lists first the data for the boundary nodes, then the data for the internal nodes.

The :sidsref:`Elements_t` data structure contains unstructured elements data such as connectivity, element type, parent elements, etc.

The :sidsref:`RigidGridMotion_t` and :sidsref:`ArbitraryGridMotion_t` data structures contain information defining rigid and arbitrary (i.e., deforming) grid motion.

:sidskey:`FamilyName` identifies to which family a zone belongs. Families may be used to define material properties. Where multiple families are desired, :sidskey:`AdditionalFamilyName` nodes may be used to specify them. Both :sidskey:`FamilyName` and :sidskey:`AdditionalFamilyName` should refer to a :sidskey:`CGNSBase_t` level :sidskey:`Family_t`, in the parent base of the zone or in another sibbling base (see :ref:`Base Level Families`).

Flow-solution quantities are contained in the list of :sidsref:`FlowSolution_t` structures. Each instance of the :sidskey:`FlowSolution_t` structure is only allowed to contain data at a single grid location (vertices, cell-centers, etc.); multiple :sidskey:`FlowSolution_t` structures are provided to store flow-solution data at different grid locations, to record different solutions at the same grid location, or to store solutions at multiple time steps or iterations. These structures may optionally contain solution data defined at rind points.

Miscellaneous discrete field data is contained in the list of :sidsref:`DiscreteData_t` structures. Candidate information includes residuals, fluxes and other related discrete data that is considered auxiliary to the flow solution. Likewise, miscellaneous zone-specific global data, other than reference-state data and convergence history information, is contained in the list of :sidsref:`IntegralData_t` structures. It is envisioned that these structures will be seldom used in practice but are provided nonetheless.

The :sidsref:`ZoneSubRegion_t` node allows flowfield or other information to be specified over a subset of the entire zone.

For unstructured zones only, the node-based :sidsref:`DataArray_t` vectors (:sidskey:`GridLocation = Vertex`) in :sidsref:`FlowSolution_t` or :sidsref:`DiscreteData_t` must follow exactly the same ordering as the :sidsref:`GridCoordinates` vector. If the nodes are sorted (:sidskey:`VertexSizeBoundary` is non-zero), the data on the boundary nodes must be listed first, followed by the data on the internal nodes.
Note that the order in which the node-based data are recorded must follow exactly the node ordering in :sidsref:`GridCoordinates_t`, to be able to associate the data to the correct nodes.
For element-based data (:sidskey:`GridLocation = CellCenter`), the :sidsref:`FlowSolution_t` or :sidsref:`DiscreteData_t` data arrays must list the data values for each element, in the same order as the elements are listed in :sidsref:`ElementConnectivity`.

All interface connectivity information, including identification of overset-grid holes, for a given zone is contained in :sidsref:`ZoneGridConnectivity`.

All boundary condition information pertaining to a zone is contained in :sidsref:`ZoneBC_t`.

The :sidsref:`ZoneIterativeData_t` data structure may be used to record pointers to zonal data at multiple time steps or iterations.

Reference-state data specific to an individual zone is contained in the :sidsref:`ReferenceState` structure.

:sidsref:`RotatingCoordinates` may be used to specify the rotation center and rotation rate vector of a rotating coordinate system.

:sidsref:`DataClass` defines the zonal default for the class of data contained in the zone and its substructures. If a zone contains dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.

If a set of flow equations are specific to a given zone, these may be described in :sidsref:`FlowEquationSet`. For example, if a single zone within the domain is inviscid, whereas all other are turbulent, then this zone-specific equation set could be used to describe the special zone.

:sidsref:`DataClass`, :sidsref:`DimensionalUnits`, :sidsref:`ReferenceState`, and :sidsref:`FlowEquationSet` have special function in the hierarchy. They are applicable throughout a given zone, but their precedence may be superseded by local entities contained in the zone's substructures. If any of these entities are present within a given instance of :sidskey:`Zone_t`, they take precedence over the corresponding global entities contained in database's :sidskey:`CGNSBase_t` entity. These precedence rules are further discussed in the section on :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`

Convergence history information applicable to the zone is contained in :sidsref:`ZoneConvergenceHistory`; this includes residual and solution-change norms.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

:sidskey:`Ordinal` is user-defined and has no restrictions on the values that it can contain. It is included for backward compatibility to assist implementation of the CGNS system into applications whose I/O depends heavily on the numbering of zones. Since there are no restrictions on the values contained in :sidskey:`Ordinal` (or that :sidskey:`Ordinal` is even provided), there is no guarantee that the zones in an existing CGNS database will have sequential values from 1 to *N* without holes or repetitions. Use of :sidskey:`Ordinal` is discouraged and is on a user-beware basis.

.. _precedence:

Precedence Rules and Scope Within the Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Single Base
~~~~~~~~~~~

The dependence of a structure entity's information on data contained at higher levels of the hierarchy is typically explicitly expressed through structure parameters. For example, all arrays within :sidsref:`Zone_t` depend on the dimensionality of the computational grid. This dimensionality is passed down to a :sidskey:`Zone_t` entity through a structure parameter in the definition of :sidskey:`Zone_t`.

We have established an alternate dependency for a limited number of entities that is not explicitly stated in the structure type definitions. These special situations include entities for describing data class, system of dimensional units, reference states and flow equation sets. At each level of the hierarchy (where appropriate), entities for describing this information are defined, and if present they take precedence over all corresponding information existing at higher levels of the CGNS hierarchy. Essentially, we have established globally applicable data with provisions for recursively overriding it with local data.

Specifically, the entities that follow this alternate dependency are:

 * :sidskey:`FlowEquationSet_t` :sidskey:`FlowEquationSet`,
 * :sidskey:`ReferenceState_t` :sidskey:`ReferenceState`,
 * :sidskey:`DataClass_t` :sidskey:`DataClass`,
 * :sidskey:`DimensionalUnits_t` :sidskey:`DimensionalUnits`.

:sidsref:`FlowEquationSet` contains a description of the governing flow equations;
:sidsref:`ReferenceState` describes a set of reference state flow conditions;
:sidsref:`DataClass` defines the class of data (e.g., :ref:`dimensional <dim>` or :ref:`nondimensional <normbydim>`);
and :sidsref:`DimensionalUnits` specifies the system of units used for dimensional data.

All of these entities may be defined within the highest level :sidsref:`CGNSBase_t` structure, and if present in a given database, establish globally applicable information; these may also be considered to be global defaults. Each of these four entities may also be defined within the :sidsref:`Zone_t` structure. If present in a given instance of :sidskey:`Zone_t`, they supersede the global data and establish new defaults that apply only within that zone.

For example, if a different set of flow equations is solved within a given zone than is solved in the rest of the flowfield, then this can be conveyed through :sidsref:`FlowEquationSet`. In this case, one :sidskey:`FlowEquationSet` entity would be placed within :sidskey:`CGNSBase_t` to state the globally applicable flow equations, and a second :sidskey:`FlowEquationSet` entity would be placed within the given zone (within its instance of :sidskey:`Zone_t`); this second :sidskey:`FlowEquationSet` entity supersedes the first only within the given zone.

In addition to its presence in :sidsref:`CGNSBase_t` and :sidsref:`Zone_t`, :sidsref:`ReferenceState` may also be defined within the boundary-condition structure types to establish reference states applicable to one or more boundary-condition patches. Actually, :sidskey:`ReferenceState` entities can be defined at several levels of the :ref:`boundary-condition hierarchy <bc>` to allow flexibility in setting the appropriate reference state conditions.

:sidsref:`DataClass` and :sidsref:`DimensionalUnits` are used within entities describing data arrays. They classify the data and specify its system of units if dimensional. If these entities are absent from a particular instance of :sidsref:`DataArray_t`, the information is derived from appropriate global data. :sidskey:`DataClass` and :sidskey:`DimensionalUnits` are also declared in all intermediate structure types that directly or indirectly contain :sidskey:`DataArray_t` entities. Examples include :sidsref:`GridCoordinates_t`, :sidsref:`FlowSolution_t`, :sidsref:`BC_t`, and :sidsref:`ReferenceState_t`. The same precedence rules apply - lower-level entities supersede higher-level entities.

It is envisioned that in practice, the use of globally applicable data will be the norm rather than the exception. It provides a measure of economy throughout the CGNS database in many situations. For example, when creating a database where the vast majority of data arrays are dimensional and use a consistent set of units, :sidsref:`DataClass` and :sidsref:`DimensionalUnits` can be set appropriately at the :sidsref:`CGNSBase_t` level and thereafter omitted when outputting data.


Multiple Bases
~~~~~~~~~~~~~~

With a multiple-bases CGNS tree, some nodes defined at the base level may lead to an inconsistent CGNS set of data. In that case it is up to the application using the CGNS tree to define its own understanding of the data. In particular, the following nodes are not required to be the same in all bases of a CGNS tree, thus inter-base references may lead to inconsistency:

  * :sidskey:`CellDimension` and :sidskey:`PhysicalDimension`
  * :sidskey:`ReferenceState`
  * :sidskey:`Axisymmetry`
  * :sidskey:`RotatingCoordinates`
  * :sidskey:`Gravity`
  * :sidskey:`SimulationType`
  * :sidskey:`DataClass`
  * :sidskey:`DimensionalUnits`
  * :sidskey:`FlowEquationSet`
  * :sidskey:`Family_t`

The application has to take into account the corresponding base definition for the referred-to node.

.. last line
