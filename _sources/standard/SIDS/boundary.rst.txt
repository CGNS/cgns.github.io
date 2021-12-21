.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

Boundary Conditions
===================

This section is an attempt to unify boundary-condition specifications within Navier-Stokes codes. The structures and conventions developed are a compromise between simplicity and generality. It is imperative that they be easy to use initially, but that they are general enough to provide future flexibility and extensibility.

This section may be somewhat daunting initially. It is suggested that the reader refer to the :ref:`Boundary Condition Examples <BCExample>` during study of the following sections to help resolve any questions and confusions that might arise.

The difficulty with boundary conditions is that there is such a wide variety used, and even a single boundary-condition equation is often implemented differently in different codes. Some boundary conditions, such as a symmetry plane, are fairly well defined. Other boundary conditions are much looser in their definition and implementation. An inflow boundary is a good example. It is generally accepted how many solution quantities should be specified at an inflow boundary (from mathematical well-posedness arguments), but what those quantities are will change with the class of flow problems (e.g., internal flows vs. external flows), and they will also change from code to code.

An additional difficulty for CFD analysis is that in some situations different boundary-condition equations are applied depending on local flow conditions. Any boundary where the flow can change from inflow to outflow or supersonic to subsonic is a candidate for flow-dependent boundary-condition equations.

These difficulties have molded the design of our boundary-condition specification structures and conventions. We define :ref:`boundary-condition types <BCType>` that establish the equations to be enforced. However, for those more loosely defined boundary conditions, such as inflow/outflow, the boundary-condition type merely establishes general guidelines on the equations to be imposed. Augmenting (and superseding) the information provided by the boundary-condition type is precisely defined boundary-condition solution data. We rely on our :ref:`conventions for data-name identifiers <dataname>` to identify the exact quantities involved in the boundary conditions.

One flexibility that is provided by this approach is that boundary-condition information can easily be built during the course of an analysis. For example, during grid-generation phases minimal information (e.g., the boundary-condition type) may be given. Then prior to running of the flow solver, more specific boundary-condition information, such as Dirichlet or Neumann data, may be added to the database.

An additional flexibility provided by the structures of this section is that both uniform and non-uniform boundary-condition data can be described within the same framework.

We realize that most current codes allow little or no flexibility in choosing solution quantities to specify for a given boundary-condition type. We also realize the coding effort involved with checking for consistency between I/O specifications and internal boundary-condition routines. To make these boundary-condition structures more palatable initially, we adopt the convention that if no solution quantities are specified for a given boundary-condition type, then the code is free to enforce any appropriate boundary condition (see :ref:`Boundary Condition Specification Data <BC_specdata>`).

Note that there are no boundary-condition structures defined for abutting or overset interfaces, unless they involve cases of symmetry or degeneracy. In other words, it is a CGNS design intent that a given zone boundary segment or location should at most be defined (or covered) by either a boundary condition or a multizone interface connectivity, but not by both. There is also no separate boundary-condition structure for periodic boundary conditions (i.e., when a zone interfaces with itself). Both of these situations are addressed by :ref:`interface connectivity data structures <SIDS-connectivity>`.

In the sections to follow, the definitions of boundary-condition structures are presented in the first six sections. :ref:`Boundary-condition types <BCType>` are then discussed in detail, including a description of the boundary-condition equations to be enforced for each type; this section also describes the distinction between boundary-condition types that impose a set of equations regardless of local flow conditions and those that impose different sets of boundary-condition equations depending on the local flow solution. The rules for :ref:`matching boundary-condition types and the appropriate sets of boundary-condition equations <BCType-assoc>` are next discussed.
Details of :ref:`specifying data to be imposed in boundary-condition equations <BC-specdata>` are provided next.
Finally, several :ref:`examples of boundary conditions <BCexample>` are presented.

Boundary Condition Structures Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prior to presenting the detailed boundary condition structures, we give a brief overview of the hierarchy used to describe boundary conditions.

Boundary conditions are classified as either fixed or flow-dependent. Fixed boundary conditions enforce a given set of boundary-condition equations regardless of flow conditions; whereas, flow-dependent boundary conditions enforce different sets of boundary-condition equations depending on local flow conditions. We incorporate both fixed and flow-dependent boundary conditions into a uniform framework. This allows all boundary conditions to be described in a similar manner. We consider this functionally superior to separately treating fixed and flow-dependent boundary conditions, even though the latter allows a simpler description mechanism for fixed boundary conditions. The current organization also makes sense considering the fact that flow-dependent boundary conditions are composed of multiple sets of fixed boundary conditions.

.. figure:: ../../../images/sids/figs/bctree.gif
   :width: 600px
   :align: center
   :alt: CGNS hierarchy for a single boundary condition

   *Hierarchy for Boundary Condition Structures*


The above figure depicts the hierarchy used for prescribing a single boundary condition. Each boundary condition includes a type that describes the general equations to enforce, a patch specification, and a collection of data sets. The minimum required information for any boundary condition is the patch specification and the boundary-condition type (indicated by "BC type (compound)" in the figure). This minimum information is similar to that used in many existing flow solvers.

Generality in prescribing equations to enforce and their associated boundary-condition data is provided in the optional data sets.
Each data set contains all boundary condition data required for a given fixed or simple boundary condition.
Each data set is also tagged with a boundary-condition type.
For fixed boundary conditions, the hierarchical tree contains a single data set, and the two boundary-condition types shown in the above figure are identical.
Flow-dependent or compound boundary conditions contain multiple data sets, each to be applied separately depending on local flow conditions.
The compound boundary-condition type describes the general flow-dependent boundary conditions, and each data set contains associated simple boundary-condition types.
For example, a farfield boundary condition would contain four data sets, where each applies to the different combinations of subsonic and supersonic inflow and outflow.
See the sections :ref:`Boundary Condition Type Structure Definition <BCType>`: :sidsref:`BCType_t` and :ref:`Matching Boundary Condition Data Sets <BCType-assoc>` for more details.

Within a single data set, boundary condition data is grouped by equation type into Dirichlet and Neumann data.
The lower leaves of the above figure show data for generic flow-solution quantities :math:`\alpha` and :math:`\beta` to be applied in Dirichlet conditions, and data for :math:`\gamma` and :math:`\delta` to be applied in Neumann boundary conditions.
:sidsref:`DataArray_t` entities are employed to store these data and to identify the specific flow variables they are associated with.

In situations where the data sets (or any information contained therein) are absent from a given boundary-condition hierarchy, flow solvers are free to impose any appropriate boundary conditions.
Although not pictured in the above figure, it is also possible to specify the reference state from which the flow solver should extract the boundary-condition data.


Zonal Boundary Condition Structure Definition: ``ZoneBC_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All boundary-condition information pertaining to a given zone is contained in the :sidskey:`ZoneBC_t` structure.

.. code-block:: sids

  ZoneBC_t< int CellDimension, int IndexDimension, int PhysicalDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( BC_t<CellDimension, IndexDimension, int PhysicalDimension>
          BC1 ... BCN ) ;                                              (o)

    ReferenceState_t ReferenceState ;                                  (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`BC_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ZoneBC_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, or :sidskey:`ReferenceState`.

  #. All lists within a :sidskey:`ZoneBC_t` structure entity may be empty. 

:sidskey:`ZoneBC_t` requires three structure parameters, :sidskey:`CellDimension`, :sidskey:`IndexDimension` and :sidskey:`PhysicalDimension`, which are passed onto all :sidsref:`BC_t` substructures.

Boundary-condition information for a single patch is contained in the :sidsref:`BC_t` structure. All boundary-condition information pertaining to a given zone is contained in the list of :sidskey:`BC_t` structure entities.
If a zone contains *N* boundary-condition patches, then *N* (and only *N*) separate instances of :sidskey:`BC_t` must be provided in the :sidskey:`ZoneBC_t` entity for the zone.
That is, each boundary-condition patch must be represented by a single :sidskey:`BC_t` entity.

Reference data applicable to all boundary conditions of a zone is contained in the :sidsref:`ReferenceState` structure.
:sidskey:`DataClass` defines the zonal default for the class of data contained in the boundary conditions of a zone.
If the boundary conditions contain dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these three entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

Reference-state data is useful for situations where boundary-condition data is not provided, and flow solvers are free to enforce any appropriate boundary condition equations.
The presense of :sidsref:`ReferenceState` at this level or below specifies the appropriate flow conditions from which the flow solver should extract its boundary-condition data.
For example, when computing an external flowfield around an airplane, an engine nozzle exit is often simulated by imposing a stagnation pressure boundary condition (or some other stagnation quantity) different from freestream.
The nozzle-exit stagnation quantities could be specified in an instance of :sidskey:`ReferenceState` at this level or below in lieu of providing explicit Dirichlet or Neumann data. (See :ref:`Boundary Condition Specification Data. <BC-specdata>`)

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Boundary Condition Structure Definition: ``BC_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`BC_t` contains boundary-condition information for a single BC surface patch of a zone.
A BC patch is the subrange of the face of a zone where a given boundary condition is applied.

The structure contains a boundary-condition type, as well as one or more sets of boundary-condition data that are used to define the boundary-condition equations to be enforced on the BC patch.
For most boundary conditions, a single data set is all that is needed. The structure also contains information describing the normal vector to the BC surface patch.

.. code-block:: sids

  BC_t< int CellDimension, int IndexDimension, int PhysicalDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    BCType_t BCType ;                                                  (r)

    GridLocation_t GridLocation ;                                      (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (r:o)
    IndexArray_t<IndexDimension, ListLength[], int> PointList ;        (o:r)

    int[IndexDimension] InwardNormalIndex ;                            (o)

    IndexArray_t<PhysicalDimension, ListLength[], real>
       InwardNormalList ;                                              (o)

    List( BCDataSet_t<CellDimension, IndexDimension, ListLength[], GridLocation>
          BCDataSet1 ... BCDataSetN ) ;                                (o)

    BCProperty_t BCProperty ;                                          (o)

    FamilyName_t FamilyName ;                                          (o)

    List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ; (o)

    ReferenceState_t ReferenceState ;                                  (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;

.. note::

  #. Default names for the Descriptor_t, BCDataSet_t, and UserDefinedData_t lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of BC_t and shall not include the names BCProperty, BCType, DataClass, DimensionalUnits, FamilyName, GridLocation, InwardNormalIndex, InwardNormalList, Ordinal, PointList, PointRange, or ReferenceState.
  
  #. GridLocation is optional; if absent its default value is Vertex. For other allowble values, see the table below.
  
  #. One of PointRange or PointList must be specified but not both. They must define a subrange of the zone.
  
  #. InwardNormalIndex is only an option for structured grids. For unstructured grid boundaries, it should not be used. InwardNormalIndex may have only one nonzero element, whose sign indicates the computational-coordinate direction of the BC patch normal; this normal points into the interior of the zone.
  
  #. InwardNormalList contains a list of vectors normal to the BC patch pointing into the interior of the zone. It is a function of PhysicalDimension and ListLength[]. The vectors are located at the vertices of the BC patch when GridLocation is set to Vertex. Otherwise, they are located at edge/face midpoints. The vectors are not required to have unit magnitude.
  
  #. If PointRange and InwardNormalList are specified, an ordering convention is needed for indices on the BC patch. An ordering convention is also needed if a range is specified and local data is present in the BCDataSet_t substructures. FORTRAN multidimensional array ordering is used. 

:sidsref:`BCType` specifies the boundary-condition type, which gives general information on the boundary-condition equations to be enforced.

The BC patch may be specified by :sidskey:`PointRange` if it constitutes a logically rectangular region.
In all other cases, :sidskey:`PointList` should be used to list the vertices or cell edges/faces making up the BC patch.
When :sidskey:`GridLocation` is set to :sidskey:`Vertex`, then :sidskey:`PointList` or :sidskey:`PointRange` refer to vertex indices, for both structured and unstructured grids.
When :sidskey:`GridLocation` is set to :sidskey:`EdgeCenter`, then :sidskey:`PointRange/List` refer to edge elements.
For 3-D grids, when :sidskey:`GridLocation` is set to :sidskey:`FaceCenter`, :sidskey:`IFaceCenter`, etc., then :sidskey:`PointRange/List` refer to face elements.
The interpretation of :sidskey:`PointRange/List` is summarized in the table below:

.. table::
  :align: center

  +-------------------+------------------------------------------------------------------------------------------------+
  | **CellDimension** |  **GridLocation**                                                                              |
  |                   +--------------------+-----------------------+------------------------+--------------------------+
  |                   | :sidskey:`Vertex`  | :sidskey:`EdgeCenter` | :sidskey:`*FaceCenter` | :sidskey:`CellCenter`    |
  +===================+====================+=======================+========================+==========================+
  |   1               |  vertices          |  `-`                  | `-`                    | cells (line elements)    |
  +-------------------+--------------------+-----------------------+------------------------+--------------------------+
  |   2               |  vertices          |  edges                | `-`                    | cells (area elements)    |
  +-------------------+--------------------+-----------------------+------------------------+--------------------------+
  |   3               |  vertices          |  edges                | faces                  | cells (volume elements)  |
  +-------------------+--------------------+-----------------------+------------------------+--------------------------+

*Note*: In the table, :sidskey:`*FaceCenter` stands for the possible types: :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter`, :sidskey:`KFaceCenter`, or :sidskey:`FaceCenter`.

For structured grids, face centers are indexed using the minimum of the connecting vertex indices, as described in :ref:`Structured Grid Notation and Indexing Conventions <structgrid>`.
For unstructured grids, edge and face elements are indexed using their element numbering as defined in the :sidsref:`Elements_t` data structures.

The BC patch defined by :sidskey:`PointRange/List` is a surface region over which the particular set of boundary conditions is applied.
However, in the current standard there is no mechanism to specify whether boundary conditions are enforced in the weak or strong form.
If boundary conditions are imposed using collocation (i.e., strong form), there is also no requirement that they be imposed at the same locations used to define the BC patch (via :sidskey:`PointRange/List`).
In the case when BC patches are defined in terms of vertices (or edges in 3-D), then the bounding vertices will be located on multiple BC patches.
If boundary conditions are imposed using collocation at vertices, then for this case there is no mechanism to determine which BC patch takes precedence for any of these bounding vertices.

Some boundary conditions require a normal direction to be specified in order to be properly imposed.
For structured zones a computational-coordinate normal can be derived from the BC patch specification by examining redundant index components.
Alternatively, for structured zones this information can be provided directly by :sidskey:`InwardNormalIndex`.
From Note 4, this vector points into the zone and can have only one non-zero element.
For exterior faces of a zone in 3-D, :sidskey:`InwardNormalIndex` should take the following values:

.. table::
  :align: center
  
  +-----------+-------------------------------+----------+------------------------------+
  |  Face     | :sidskey:`InwardNormalIndex`  | Face     | :sidskey:`InwardNormalIndex` |
  +===========+===============================+==========+==============================+
  |  *i*-min  |   :code:`[+1,0,0]`            | *i*-max  |  :code:`[−1,0,0]`            |
  +-----------+-------------------------------+----------+------------------------------+
  |  *j*-min  |   :code:`[0,+1,0]`            | *j*-max  |  :code:`[0,−1,0]`            |
  +-----------+-------------------------------+----------+------------------------------+
  |  *k*-min  |   :code:`[0,0,+1]`            | *k*-max  |  :code:`[0,0,−1]`            |
  +-----------+-------------------------------+----------+------------------------------+

The physical-space normal vectors of the BC patch may be described by :sidskey:`InwardNormalList`; these are located at vertices or cell faces, consistent with the BC patch specification.
:sidskey:`InwardNormalList` is listed as an optional field because it is not always needed to enforce boundary conditions, and the physical-space normals of a BC patch can usually be constructed from the grid.
However, there are some situations, such as grid-coordinate singularity lines, where :sidskey:`InwardNormalList` becomes a required field, because it cannot be generated from other information.

The :sidskey:`BC_t` structure provides for a list of boundary-condition data sets, described in the next section.
In general, the proper :sidskey:`BCDataSet_t` instance to impose on the BC patch is determined by the :sidsref:`BCType` :ref:`association table <BCType-assoc>`.
The mechanics of determining the proper data set to impose is described in the section :ref:`Matching Boundary Condition Data Sets <BCType-assoc>`.

For a few boundary conditions, such as a symmetry plane or polar singularity, the value of :sidsref:`BCType` completely describes the equations to impose, and no instances of :sidsref:`BCDataSet_t` are needed.
For "simple" boundary conditions, where a single set of Dirichlet and/or Neumann data is applied, a single :sidskey:`BCDataSet_t` will likely appear (although this is not a requirement).
For "compound" boundary conditions, where the equations to impose are dependent on local flow conditions, several instances of :sidskey:`BCDataSet_t` will likely appear; the procedure for choosing the proper data set is more complex as described in the section :ref:`Matching Boundary Condition Data Sets <BCType-assoc>`.

A :sidsref:`BCProperty_t` data structure may be used to record special properties associated with particular boundary condition patches, such as wall functions or bleed regions.

:sidskey:`FamilyName` identifies the family to which the boundary belongs. Family names link the mesh boundaries to the CAD surfaces. (See the section on :ref:`Family Data Structure Definition <Family>` for more details.)
Boundary conditions may also be defined directly on families. In this case, the :sidsref:`BCType` must be :sidskey:`FamilySpecified`.
If, under a :sidskey:`BC_t` structure, both :sidskey:`FamilyName_t` and :sidskey:`BCType_t` are present, and the :sidskey:`BCType` is not :sidskey:`FamilySpecified`, then the :sidskey:`BCType` that is specified takes precedence over any :sidskey:`BCType` that might be stored in a :sidsref:`FamilyBC_t` structure under the specified :sidskey:`Family_t`.
The actual name of the referred-to :sidskey:`Family_t` can be in the same base or another base, as detailed in :ref:`Base Level Families <BaseLevelFamilies>`.

Reference data applicable to the boundary conditions of a BC patch is contained in the :sidsref:`ReferenceState` structure.
:sidsref:`DataClass` defines the default for the class of data contained in the boundary conditions.
If the boundary conditions contain dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these three entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

:sidskey:`Ordinal` is user-defined and has no restrictions on the values that it can contain. It is included for backward compatibility to assist implementation of the CGNS system into applications whose I/O depends heavily on the numbering of BC patches.
Since there are no restrictions on the values contained in :sidskey:`Ordinal` (or that :sidskey:`Ordinal` is even provided), there is no guarantee that the BC patches for a given zone in an existing CGNS database will have sequential values from 1 to *N* without holes or repetitions.
Use of :sidskey:`Ordinal` is discouraged and is on a user-beware basis.

.. c:function:: FUNCTION ListLength()

   :return value: ``int``
   :dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`BC_t` requires the structure function :sidskey:`ListLength`, which is used to specify the number of vertices or edge/face elements making up the BC patch.
   If :sidskey:`PointRange` is specified, then :sidskey:`ListLength` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`.
   If :sidskey:`PointList` is specified, then :sidskey:`ListLength` is the number of indices in the list of points. In this situation, :sidskey:`ListLength` becomes a user input along with the indices of the list :sidskey:`PointList`.
   By user we mean the application code that is generating the CGNS database.

   :sidskey:`ListLength` is also the number of elements in the list :sidskey:`InwardNormalList`.
   Note that syntactically :sidskey:`PointList` and :sidskey:`InwardNormalList` must have the same number of elements.

   If neither :sidskey:`PointRange` or :sidskey:`PointList` is specified in a particular :sidskey:`BCDataSet_t` substructure, :sidskey:`ListLength` must be passed into it to determine the length of BC data arrays.


Boundary Condition Data Set Structure Definition: ``BCDataSet_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`BCDataSet_t` contains Dirichlet and Neumann data for a single set of boundary-condition equations.
Its intended use is for simple boundary-condition types, where the equations imposed do not depend on local flow conditions.

.. code-block:: sids

  BCDataSet_t< int CellDimension, int IndexDimension,
    int ListLengthParameter, GridLocation_t GridLocationParameter > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    BCTypeSimple_t BCTypeSimple ;                                      (r)

    BCData_t<ListLengthBCData[]> DirichletData ;                       (o)
    BCData_t<ListLengthBCData[]> NeumannData ;                         (o)

    GridLocation_t GridLocation ;                                      (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (o)
    IndexArray_t<IndexDimension, ListLength, int> PointList ;          (o)

    ReferenceState_t ReferenceState ;                                  (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`BCDataSet_t` and shall not include the names :sidskey:`BCTypeSimple`, :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`DirichletData`, :sidskey:`GridLocation`, :sidskey:`NeumannData`, :sidskey:`PointList`, :sidskey:`PointRange`, or :sidskey:`ReferenceState`.
  #. :sidskey:`BCTypeSimple` is the only required field. All other fields are optional and the :sidskey:`Descriptor_t` list may be empty.
  #. :sidskey:`GridLocation` is optional; if absent its default value is :sidskey:`GridLocationParameter`. For 2-D grids (:sidskey:`CellDimension = 2`), :sidskey:`GridLocation` may take the values of :sidskey:`Vertex` or :sidskey:`EdgeCenter`. For 3-D grids (:sidskey:`CellDimension = 3`), :sidskey:`GridLocation` may take the values of :sidskey:`Vertex`, :sidskey:`EdgeCenter`, :sidskey:`FaceCenter`, :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter` or :sidskey:`KFaceCenter`.
  #. :sidskey:`PointRange` and :sidskey:`PointList` are both optional; only one of them may be specified. They must define a face subrange of the zone. 

:sidskey:`BCDataSet_t` requires the structure parameters :sidskey:`CellDimension`, :sidskey:`IndexDimension`, :sidskey:`ListLengthParameter`, and :sidskey:`GridLocationParameter`.
These are all used to control the grid location and length of data arrays in the :sidskey:`Dirichlet` and :sidskey:`Neumann` substructures.
They are inputs for the structure functions :sidskey:`ListLength[]` and :sidskey:`ListLengthBCData[]` defined below.

:sidskey:`BCTypeSimple` specifies the boundary-condition type, which gives general information on the boundary-condition equations to be enforced.
:sidskey:`BCTypeSimple` is also used for :ref:`matching boundary condition data sets <BCType-assoc>`.

Boundary-condition data is separated by equation type into Dirichlet and Neumann conditions. Dirichlet boundary conditions impose the value of the given variables, whereas Neumann boundary conditions impose the normal derivative of the given variables. The mechanics of specifying Dirichlet and Neumann data for boundary conditions is covered in the section :ref:`Boundary Condition Specification Data <BC-specdata>`.

The substructures :sidskey:`DirichletData` and :sidskey:`NeumannData` contain boundary-condition data that may be constant over the BC patch, or defined locally at each vertex or edge/face of the patch. Locally defined data may be specified in one of two ways.
If :sidskey:`GridLocation`, :sidskey:`PointRange` and :sidskey:`PointList` are all absent, then the data is defined consistent with the BC patch specification of the parent :sidskey:`BC_t` structure.
In this case, the location of the locally defined data is given by :sidskey:`GridLocationParameter` and the length of the data arrays are given by :sidskey:`ListLengthParameter`.
If :sidskey:`GridLocation` and one of :sidskey:`PointRange` or :sidskey:`PointList` is present, then the length of the data arrays is given by :sidskey:`ListLength[]`.

Reference quantities applicable to the set of boundary-condition data are contained in the :sidskey:`ReferenceState` structure. :sidskey:`DataClass` defines the default for the class of data contained in the boundary-condition data.
If the boundary conditions contain dimensional data, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these three entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. c:function:: FUNCTION ListLength()

   :return value: ``int``
   :dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`BCDataSet_t` requires the structure function :sidskey:`ListLength`, which is used to specify the length of locally defined Dirichlet and Neumann data arrays when the grid location of these quantities differs from that of the BC patch definition. If :sidskey:`PointRange` is specified, then :sidskey:`ListLength` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`. If :sidskey:`PointList` is specified, then :sidskey:`ListLength` is the number of indices in the list of points. In this situation, :sidskey:`ListLength` becomes a user input along with the indices of the list :sidskey:`PointList`. By user we mean the application code that is generating the CGNS database.
   
   If neither :sidskey:`PointRange` or :sidskey:`PointList` is specified in a particular :sidskey:`BCDataSet_t` substructure, :sidskey:`ListLength` must be passed into it to determine the length of BC data arrays.


.. c:function:: FUNCTION ListLengthBCData()

   :return value: ``int``
   :dependencies: :sidskey:`ListLengthParameter`, :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`BCDataSet_t` also requires the structure function :sidskey:`ListLengthBCData`. If :sidskey:`PointRange` or :sidskey:`PointList` is present, then :sidskey:`ListLengthBCData` takes the value of :sidskey:`ListLength`. If both are absent, then it takes the value :sidskey:`ListLengthParameter`. 


Boundary Condition Data Structure Definition: ``BCData_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`BCData_t` contains a list of variables and associated data for boundary-condition specification.
Each variable may be given as global data (i.e., a scalar) or local data defined at each grid point or cell face of the BC patch.
By convention all data specified in a given instance of :sidskey:`BCData_t` is to be used in the same *type* of boundary-condition equation.
For example, the use of separate :sidskey:`BCData_t` substructures for Dirichlet and Neumann equations in the :sidsref:`BCDataSet_t` structure of the previous section.

.. code-block:: sids

  BCData_t< int ListLength > :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    List( DataArray_t<DataType, 1, 1>
          DataGlobal1 ... DataGlobalN ) ;                              (o)

    List( DataArray_t<DataType, 1, ListLength>
          DataLocal1 ... DataLocalN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`BCData_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
    #. There are no required elements; all three lists may be empty. 

This structure definition shows separate lists for :ref:`global verses local <global-vs-local>` data.
The global data is essentially scalars, while the local data variables have size determined by the structure parameter :sidskey:`ListLength`.
For :sidskey:`DataArray_t` entities with :ref:`standardized data-name identifiers <dataname>`, :sidskey:`DataType` is determined by convention.
For user-defined variables, :sidskey:`DataType` is a user input.

Two important points need to be mentioned regarding this structure definition.
First, this definition allows a given instance of :sidskey:`BCData_t` to have a mixture of global and local data.
For example, if a user specifies Dirichlet data that has a uniform stagnation pressure but has a non-uniform velocity profile, this structure allows the user to describe the stagnation pressure by a scalar in the :sidskey:`DataGlobal` list and the velocity by an array in the :sidskey:`DataLocal` list.
Second, the only distinction between the lists (aside from default names, which will be seldom used) is the parameters passed into the :sidskey:`DataArray_t` structure.
Therefore, in actual implementation of this :sidskey:`BCData_t` structure it may not be possible to distinguish between members of the global and local lists without querying inside the :sidskey:`DataArray_t` substructures.
Straightforward mapping onto the ADF or HDF database will not provide any distinctions between the members of the two lists. This hopefully will not cause any problems.

:sidskey:`DataClass` defines the default for the class of data contained in the boundary-condition data.
If the boundary-condition data is dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 


Boundary Condition Property Structure Definition: ``BCProperty_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`BCProperty_t` allows the recording of special properties associated with particular boundary condition patches.
At the current time, only two properties (:sidskey:`WallFunction_t` and :sidskey:`Area_t`) are included, but extensions involving boundary conditions may be implemented as additional nodes under :sidskey:`BCProperty_t` in the future.

.. code-block:: sids

  BCProperty_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    WallFunction_t WallFunction ;                                      (o)
                
    Area_t Area ;                                                      (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`BCProperty_t` and shall not include the names :sidskey:`WallFunction` or :sidskey:`Area`. 

The :sidskey:`WallFunction_t` and :sidskey:`Area_t` data structures may be used to record properties associated with the use of wall functions, or area-related boundary conditions such as bleed, respectively.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 



Wall Function Structure Definition: ``WallFunction_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`WallFunction_t` data structure allows data associated with the use of wall function boundary conditions to be recorded.

.. code-block:: sids

  WallFunction_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    WallFunctionType_t WallFunctionType ;                              (r)
                
    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`WallFunction_t` and shall not include the name :sidskey:`WallFunctionType`. 

:sidskey:`WallFunctionType_t` is a required enumeration data structure that is used to define the type of wall functions being used.

.. code-block::

  WallFunctionType_t := Enumeration(
    WallFunctionTypeNull,
    WallFunctionTypeUserDefined,
    Generic ) ;

Because there is such a wide array of methods for employing wall functions (few of which are well-documented), the type :sidskey:`Generic` is used to simply indicate that a wall function is employed, without specifying details. 


Area Structure Definition: ``Area_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`Area_t` data structure allows data associated with area-related boundary conditions such as bleed to be recorded.

.. code-block:: sids

  Area_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    AreaType_t AreaType ;                                              (r)
    DataArray_t<real, 1, 1>  SurfaceArea ;                             (r)
    DataArray_t<real, 1, 32> RegionName ;                              (r)
                
    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`Area_t` and shall not include the names :sidskey:`AreaType`, :sidskey:`RegionName`, or :sidskey:`SurfaceArea`. 

:sidskey:`AreaType_t` is a required enumeration data structure that is used to define the type of area being defined.

.. code-block:: sids

  AreaType_t := Enumeration(
    AreaTypeNull,
    AreaTypeUserDefined,
    BleedArea,
    CaptureArea ) ;

If :sidskey:`AreaType` is set to :sidskey:`BleedArea`, the value of :sidskey:`SurfaceArea` is the size of the current bleed surface.
Note that bleed is commonly used with wall boundary conditions. The bleed area is the surface area of the boundary condition patch.

If :sidskey:`AreaType` is set to :sidskey:`CaptureArea`, then :sidskey:`SurfaceArea` represents the size of the current capture surface.
For inlet flows, for example, the capture area is the area of a fictitious surface in front of the inlet in which mass is pulled into the inlet.
This is used to calculate the mass flow for the boundary condition patch based on the formula:

.. math::

   \text{mass flow} = \mathit{MFR}\ \rho_\infty U_\infty A_{cap}

where :math:`\mathit{MFR}` is the desired mass flow ratio and :math:`A_{cap}` is the capture area.
Another interpretation is the far-upstream cross-sectional area of the stream tube that feeds the inlet.
Note that the capture area is usually defined with an outflow boundary condition, which is commonly used at an engine face.

The :sidskey:`RegionName` is character identifier, and is needed so that a specific region can span multiple surfaces over multiple zones. 

Boundary Condition Type Structure Definition: ``BCType_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`BCType_t` is an enumeration type that identifies the boundary-condition equations to be enforced at a given boundary location.

.. code-block:: sids

  BCType_t := Enumeration(
    BCTypeNull, BCTypeUserDefined, BCAxisymmetricWedge, BCDegenerateLine.
    BCDegeneratePoint, BCDirichlet, BCExtrapolate, BCFarfield, BCGeneral,
    BCInflow, BCInflowSubsonic, BCInflowSupersonic, BCNeumann,
    BCOutflow, BCOutflowSubsonic, BCOutflowSupersonic, BCSymmetryPlane,
    BCSymmetryPolar, BCTunnelInflow, BCTunnelOutflow, BCWall,
    BCWallInviscid, BCWallViscous, BCWallViscousHeatFlux,
    BCWallViscousIsothermal, FamilySpecified ) ;

The boundary-condition type is further defined as simple, :sidskey:`BCTypeSimple_t`, or compound, :sidskey:`BCTypeCompound_t`, which are subsets of the enumeration type :sidskey:`BCType_t`.

.. code-block:: sids

  BCTypeSimple_t := Enumeration(
    BCTypeNull, BCTypeUserDefined, BCAxisymmetricWedge, BCDegenerateLine.
    BCDegeneratePoint, BCDirichlet, BCExtrapolate, BCGeneral,
    BCInflowSubsonic, BCInflowSupersonic, BCNeumann,
    BCOutflowSubsonic, BCOutflowSupersonic, BCSymmetryPlane,
    BCSymmetryPolar, BCTunnelInflow, BCTunnelOutflow, BCWall,
    BCWallInviscid, BCWallViscous, BCWallViscousHeatFlux,
    BCWallViscousIsothermal, FamilySpecified ) ;

  BCTypeCompound_t := Enumeration(
    BCTypeNull, BCTypeUserDefined, BCInflow, BCOutflow,
    BCFarfield ) ;

The members of :sidskey:`BCTypeSimple_t` completely identify the equations to impose, while those of :sidskey:`BCTypeCompound_t` give a general description of the class of boundary-condition equations to impose.
The specific boundary-condition equations to enforce for each value of :sidskey:`BCType_t` are listed in separate tables for :ref:`Simple Boundary Condition Types <BCTypeSimple>` and :ref:`Compound Boundary Condition Types <BCTypeCompound>`.

The subdivision of :sidskey:`BCType_t` is based on function. For simple boundary conditions, the equations and data imposed are fixed; whereas, for compound boundary conditions different sets of equations are imposed depending on local flow conditions at the boundary. This distinction requires additional rules for dealing with simple and compound boundary-condition types.

For the inflow/outflow boundary-condition descriptions, 3-D inviscid compressible flow is assumed; the 2-D equivalent should be obvious. These same boundary conditions are typically used for viscous cases also. This "3-D Euler" assumption will be noted wherever used.

In the following tables, :math:`Q` is the solution vector, :math:`\mathbf{q}` is the velocity vector whose magnitude is :math:`q`, the unit normal to the boundary is :math:`\mathbf{n}`, and :math:`\partial () / \partial n =\mathbf{n} \cdot \nabla` is differentiation normal to the boundary.

.. |face2line| image:: ../../../images/sids/figs/face2line.gif
   :width: 100px
   :alt: 3-D region with a rectangular front face; top and bottom edges merge to a line at the back 'face'


.. |face2point| image:: ../../../images/sids/figs/face2point.gif
   :width: 100px
   :alt: 3-D region with a rectangular front face; all four edges merge to a point at the back 'face'



.. table:: **Simple Boundary Condition Types**

  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | :sidskey:`BCType_t` or :sidskey:`BCTypeSimple_t` Identifier  |  Boundary Condition Description                                                                                                                             |
  +==============================================================+=============================================================================================================================================================+
  | BCGeneral                                                    |  Arbitrary conditions on :math:`Q` or :math:`\partial Q / \partial n`                                                                                       |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+    
  | BCDirichlet                                                  |  Dirichlet condition on :math:`Q` vector                                                                                                                    |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+    
  | BCNeumann                                                    |  Neumann condition on :math:`\partial Q / \partial n`                                                                                                       |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCExtrapolate                                                |  Extrapolate :math:`Q` from interior                                                                                                                        |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCWallInviscid                                               |  Inviscid (slip) wall                                                                                                                                       |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * normal velocity specified (default: :math:`\mathbf{q} \cdot \mathbf{n} = 0`)                                                                             |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCWallViscousHeatFlux                                        |  Viscous no-slip wall with heat flux                                                                                                                        |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * velocity Dirichlet (default: :math:`q = 0`)                                                                                                              |
  |                                                              |  * temperature Neumann (default: adiabatic, :math:`\partial T / \partial n = 0`)                                                                            |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCWallViscousIsothermal                                      |  Viscous no-slip, isothermal wall                                                                                                                           |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * velocity Dirichlet (default: :math:`q = 0`)                                                                                                              |
  |                                                              |  * temperature Dirichlet                                                                                                                                    |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCWallViscous                                                |  Viscous no-slip wall; special cases are :sidskey:`BCWallViscousHeatFlux` and :sidskey:`BCWallViscousIsothermal`                                            |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * velocity Dirichlet (default: :math:`q = 0`)                                                                                                              |
  |                                                              |  * Dirichlet or Neumann on temperature                                                                                                                      |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCWall                                                       |  General wall condition; special cases are :sidskey:`BCWallInviscid`, :sidskey:`BCWallViscous`, :sidskey:`BCWallViscousHeatFlux`,                           |
  |                                                              |  and :sidskey:`BCWallViscousIsothermal`                                                                                                                     |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | BCInflowSubsonic                                             |  Inflow with subsonic normal velocity                                                                                                                       |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * specify 4; extrapolate 1 (3-D Euler)                                                                                                                     |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCInflowSupersonic                                           |  Inflow with supersonic normal velocity                                                                                                                     |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * specify 5; extrapolate 0 (3-D Euler)                                                                                                                     |
  |                                                              |                                                                                                                                                             |
  |                                                              |  Same as :sidskey:`BCDirichlet`                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCOutflowSubsonic                                            | Outflow with subsonic normal velocity                                                                                                                       |
  |                                                              |                                                                                                                                                             |
  |                                                              | * specify 1; extrapolate 4 (3-D Euler)                                                                                                                      |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
  | BCOutflowSupersonic                                          | Outflow with supersonic normal velocity                                                                                                                     |
  |                                                              |                                                                                                                                                             |
  |                                                              | * specify 0; extrapolate 5 (3-D Euler)                                                                                                                      |
  |                                                              |                                                                                                                                                             |
  |                                                              | Same as :sidskey:`BCExtrapolate`                                                                                                                            |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+   
  | BCTunnelInflow                                               | Tunnel inlet (subsonic normal velocity)                                                                                                                     |
  |                                                              |                                                                                                                                                             |
  |                                                              | * specify cross-flow velocity, stagnation enthalpy, entropy                                                                                                 |
  |                                                              | * extrapolate 1 (3-D Euler)                                                                                                                                 |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCTunnelOutflow                                              | Tunnel exit (subsonic normal velocity)                                                                                                                      |
  |                                                              |                                                                                                                                                             |
  |                                                              | * specify static pressure                                                                                                                                   |
  |                                                              | * extrapolate 4 (3-D Euler)                                                                                                                                 |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+  
  | BCDegenerateLine                                             |  Face degenerated to a line    |face2line|                                                                                                                  |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+  
  | BCDegeneratePoint                                            |  Face degenerated to a point   |face2point|                                                                                                                 |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+  
  | BCSymmetryPlane                                              |  Symmetry plane; face should be coplanar                                                                                                                    |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * density, pressure: :math:`\partial () / \partial n = \mathbf{n} \cdot \nabla = 0`                                                                        |
  |                                                              |  * tangential velocity: :math:`\partial (\mathbf{q} \times \mathbf{n}) / \partial n = 0`                                                                    |
  |                                                              |  * normal velocity: :math:`\mathbf{q} \cdot \mathbf{n} = 0`                                                                                                 |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCSymmetryPolar                                              |  Polar-coordinate singularity line; special case of :sidskey:`BCDegenerateLine` where degenerate face is a straight line and flowfield has polar symmetry;  |
  |                                                              |  :math:`\mathbf{s}` is singularity line tangential unit vector                                                                                              |
  |                                                              |                                                                                                                                                             |
  |                                                              |  * normal velocity: :math:`\mathbf{q} \times \mathbf{s} = 0`                                                                                                |
  |                                                              |  * all others: :math:`\partial () / \partial n = \mathbf{n} \cdot \nabla = 0`, :math:`\mathbf{n}` normal to :math:`\mathbf{s}`                              |
  |                                                              |                                                                                                                                                             |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCAxisymmetricWedge                                          |  Axisymmetric wedge; special case of :sidskey:`BCDegenerateLine` where degenerate face is a straight line                                                   |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+ 
  | FamilySpecified                                              |  A boundary condition type is being specified for the family to which the current boundary belongs. A :sidskey:`FamilyName_t` specification must exist      |
  |                                                              |  under :sidskey:`BC_t`, corresponding to a :sidskey:`Family_t` structure under :sidskey:`CGNSBase_t`.                                                       |
  |                                                              |  Under the :sidskey:`Family_t` structure there must be a :sidskey:`FamilyBC_t` structure specifying a valid :sidskey:`BCType`                               |
  |                                                              |  (other than :sidskey:`FamilySpecified`!). If any of these are absent, the boundary condition type is undefined.                                            |
  +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Compound Boundary Condition Types**

  +---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
  | :sidskey:`BCType_t` or :sidskey:`BCTypeCompound_t` Identifier |  Boundary Condition Description                                                                                                             |
  +===============================================================+=============================================================================================================================================+
  | BCInflow                                                      |  Inflow, arbitrary normal Mach; test on normal Mach, then perform one of: :sidskey:`BCInflowSubsonic`, :sidskey:`BCInflowSupersonic`        |
  +---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+ 
  | BCOutflow                                                     |  Outflow, arbitrary normal Mach; test on normal Mach, then perform one of: :sidskey:`BCOutflowSubsonic`, :sidskey:`BCOutflowSupersonic`     |
  +---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
  | BCFarfield                                                    |  Farfield inflow/outflow, arbitrary normal Mach; test on normal velocity and normal Mach, then perform one of: :sidskey:`BCInflowSubsonic`, |
  |                                                               |  :sidskey:`BCInflowSupersonic`, :sidskey:`BCOutflowSubsonic`, :sidskey:`BCOutflowSupersonic`                                                |
  +---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+


Matching Boundary Condition Data Sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidsref:`BC_t` structure allows for a arbitrary list of boundary-condition data sets, described by the :sidsref:`BCDataSet_t` structure.
For simple boundary conditions, a single data set must be chosen from a list that may contain more than one element.
Likewise, for a compound boundary condition, a limited number of data sets must be chosen and applied appropriately. 
The mechanism for the proper choice of data sets is controlled by the :sidsref:`BCType` field of the :sidskey:`BC_t` structure, the :sidskey:`BCTypeSimple` field of the :sidskey:`BCDataSet_t` structure, and the :ref:`boundary-condition type association table <BCType-assoc>`.
In the following discussion, we will use the "/" notation for fields or elements of a structure type.

:sidsref:`BC_t` is used for both simple and compound boundary conditions; hence, the field :sidskey:`BC_t`/:sidskey:`BCType` is of type :sidskey:`BCType`.
Conversely, the substructure :sidskey:`BCDataSet_t` is intended to enforce a single set of boundary-condition equations independent of local flow conditions (i.e., it is appropriate only for simple boundary conditions).
This is why the field :sidskey:`BCDataSet_t`/:sidskey:`BCTypeSimple` is of type :sidskey:`BCTypeSimple_t` and not :sidskey:`BCType_t`.
The appropriate choice of data sets is determined by matching the field :sidskey:`BC_t`/:sidskey:`BCType` with the field :sidskey:`BCDataSet_t/BCTypeSimple` as specified in the :ref:`boundary-condition type association table <BCType-assoc>`.

For simple boundary conditions, a single match from the list of :sidskey:`BCDataSet_t` instances is required.
For all :sidskey:`BCTypeSimple_t` identifiers, except :sidskey:`BCInflowSupersonic` and :sidskey:`BCOutflowSupersonic`, an exact match is necessary. :sidskey:`BCInflowSupersonic` will match itself or :sidskey:`BCDirichlet`; :sidskey:`BCOutflowSupersonic` will match itself or :sidskey:`BCExtrapolate`.

For compound boundary conditions, the association table specifies which simple boundary-condition types are appropriate.
Since compound boundary conditions enforce different boundary-condition equation sets depending on local flow conditions, several instances of :sidskey:`BCDataSet_t` will be matched for each :sidskey:`BCTypeCompound_t` identifier.
The accompanying rule determines which of the matching data sets to apply at a given location on the BC patch.

This provides a general procedure applicable to both :sidskey:`BCTypeSimple_t` and :sidskey:`BCTypeCompound_t` situations.
For a given :sidskey:`BC_t/BCType` use those instances of :sidskey:`BCDataSet_t` whose field :sidskey:`BCDataSet_t/BCTypeSimple` matches according to the following table.
Apply the matching data set or sets as prescribed by the appropriate usage rule.


.. table:: **Associated Boundary Condition Types and Usage Rules**

  +---------------------------------+--------------------------------------------------------------------------------------+
  | :sidskey:`BCType_t` Identifier  | Associated :sidskey:`BCTypeSimple_t` Identifiers and Usage Rules                     |
  +=================================+======================================================================================+
  | BCInflow                        || :sidskey:`BCInflowSupersonic`                                                       |
  |                                 || :sidskey:`BCInflowSubsonic`                                                         |
  |                                 |                                                                                      |
  |                                 |*Usage Rule:*                                                                         |
  |                                 |                                                                                      |
  |                                 |* if supersonic normal Mach, choose :sidskey:`BCInflowSupersonic`;                    |
  |                                 |* else, choose :sidskey:`BCInflowSubsonic`                                            |
  |                                 |                                                                                      |
  +---------------------------------+--------------------------------------------------------------------------------------+
  |                                 |                                                                                      | 
  | BCOutflow                       || :sidskey:`BCOutflowSupersonic`                                                      |
  |                                 || :sidskey:`BCOutflowSubsonic`                                                        |
  |                                 |                                                                                      |
  |                                 |*Usage Rule:*                                                                         |
  |                                 |                                                                                      |
  |                                 |* if supersonic normal Mach, choose :sidskey:`BCOutflowSupersonic`;                   |
  |                                 |* else, choose :sidskey:`BCOutflowSubsonic`                                           |
  |                                 |                                                                                      |
  +---------------------------------+--------------------------------------------------------------------------------------+ 
  | BCFarfield                      || :sidskey:`BCInflowSupersonic`                                                       |
  |                                 || :sidskey:`BCInflowSubsonic`                                                         |
  |                                 || :sidskey:`BCOutflowSupersonic`                                                      |
  |                                 || :sidskey:`BCOutflowSubsonic`                                                        |
  |                                 |                                                                                      |
  |                                 |*Usage Rule:*                                                                         |
  |                                 |                                                                                      |
  |                                 |* if inflow and supersonic normal Mach, choose :sidskey:`BCInflowSupersonic`;         |
  |                                 |* else if inflow, choose :sidskey:`BCInflowSubsonic`;                                 |
  |                                 |* else if outflow and supersonic normal Mach, choose :sidskey:`BCOutflowSupersonic`;  |
  |                                 |* else, choose :sidskey:`BCOutflowSubsonic`                                           |
  |                                 |                                                                                      |
  +---------------------------------+--------------------------------------------------------------------------------------+ 
  | BCInflowSupersonic              || :sidskey:`BCInflowSupersonic`                                                       |
  |                                 || :sidskey:`BCDirichlet`                                                              |
  |                                 |                                                                                      |
  |                                 |*Usage Rule:*                                                                         |
  |                                 |                                                                                      |
  |                                 |* choose either; :sidskey:`BCInflowSupersonic` takes precedence                       |
  |                                 |                                                                                      |
  +---------------------------------+--------------------------------------------------------------------------------------+ 
  | BCOutflowSupersonic             || :sidskey:`BCOutflowSupersonic`                                                      |
  |                                 || :sidskey:`BCExtrapolate`                                                            |
  |                                 |                                                                                      |
  |                                 |*Usage Rule:*                                                                         |
  |                                 |                                                                                      |
  |                                 |* choose either; :sidskey:`BCOutflowSupersonic` takes precedence                      |
  |                                 |                                                                                      |
  +---------------------------------+--------------------------------------------------------------------------------------+ 
  | All others                      | Self-matching                                                                        |
  +---------------------------------+--------------------------------------------------------------------------------------+

Although we present a strict division between the two categories of boundary-condition types, we realize that some overlap may exist.
For example, some of the more general simple boundary-condition types, such as :sidskey:`BCWall`, may include a situation of inflow/outflow (say if the wall is porous).
These complications require further guidelines on appropriate definition and use of boundary-condition types. The real distinctions between :sidskey:`BCTypeSimple_t` and :sidskey:`BCTypeCompound_t` are as follows:

* :sidskey:`BCTypeSimple_t` identifiers always match themselves; :sidskey:`BCTypeCompound_t` identifiers never match themselves.

* :sidskey:`BCTypeSimple_t` identifiers always produce a single match; :sidskey:`BCTypeCompound_t` will produce multiple matches.

* The usage rule for :sidskey:`BCTypeSimple_t` identifiers is always trivial - apply the single matching data set regardless of local flow conditions. 

Therefore, any boundary condition that involves application of different data sets depending on local flow conditions should be classified :sidskey:`BCTypeCompound_t`.
If a type that we have classified :sidskey:`BCTypeSimple_t` is used as a compound type (:sidskey:`BCWall` for a porous wall is an example), then it should somehow be reclassified.
One option is to define a new :sidskey:`BCTypeCompound_t` identifier and provide associated :sidskey:`BCTypeSimple_t` types and a usage rule.
Another option may be to allow some identifiers to be both :sidskey:`BCTypeSimple_t` and :sidskey:`BCTypeCompound_t` and let their appropriate use be based on context. This is still undetermined. 


Boundary Condition Specification Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a given simple boundary condition (i.e., one that is not dependent on local flow conditions), the database provides a set of boundary-condition equations to be enforced through the structure definitions for :sidskey:`BCDataSet_t` and :sidskey:`BCData_t`.
Apart from the boundary-condition type, the precise equations to be enforced are described by boundary-condition solution data.
These specified solution data are arranged by "equation type":

    :Dirichlet:      :math:`Q = Q_{specified}`

    :Neumann:        :math:`\partial Q / \partial n = (\partial Q / \partial n)_{specified}`

The :sidskey:`DirichletData` and :sidskey:`NeumannData` entities of :sidsref:`BCData_t` list both the solution variables involved in the equations (through the :ref:`data-name identifier conventions <dataname>`) and the specified solution data.

Two issues need to be addressed for specifying Dirichlet or Neumann boundary-condition data. The first is whether the data is global or local:

    :Global BC data:	   	Data applied globally to the BC patch; for example, specifying a uniform total pressure at an inflow boundary

    :Local BC data:		Data applied locally at each vertex or cell face of the BC patch; an example of this is varying total pressure specified at each grid point at an inflow boundary

The second issue is describing the actual solution quantities that are to be specified. Both of these issues are addressed by use of the :sidsref:`DataArray_t` structure.

For some types of boundary conditions, many different combinations of solution quantities could be specified.
For example, :sidskey:`BCInflowSubsonic` requires 4 solution quantities to be specified in 3-D, but what those 4 quantities are varies with applications (e.g., internal verses external flows) and codes.
We propose the convention that the actual data being specified for any :sidskey:`BCType` is given by the list of :sidsref:`DataArray_t` entities included in :ref:`DirichletData and NeumannData <BCData>` structures (actually by the identifier attached to each instance of :sidskey:`DataArray_t`).
This frees us from having to define *many* versions of a given :sidskey:`BCType` (e.g., :sidskey:`BCInflowSubsonic1`, :sidskey:`BCInflowSubsonic2`, etc.), where each has a precisely defined set of Dirichlet data.
We are left with the easier task of defining *how many* Dirichlet or Neumann quantities must be provided for each :sidskey:`BCType`.

An example of using :sidsref:`DataArray_t`-:ref:`identifier conventions <dataname>` to describe BC specification data is the following: subsonic inflow with uniform stagnation pressure, mass flow and cross-flow angle specified; the Dirichlet data are stagnation pressure = 2.56, mass flow = 1.34, and cross-flow angle has a y-component of 0.043 and a z-component of 0.02 (ignore dimensional-units or normalization for the present). The specified solution variables and associated data are described as shown:

.. code-block:: sids

  BCData_t<ListLength=?> DirichletData = 
    {{
    DataArray_t<real, 1, 1> PressureStagnation = {{ Data(real, 1, 1) = 2.56  }} ;
    DataArray_t<real, 1, 1> MassFlow           = {{ Data(real, 1, 1) = 1.34  }} ;
    DataArray_t<real, 1, 1> VelocityAngleY     = {{ Data(real, 1, 1) = 0.043 }} ;
    DataArray_t<real, 1, 1> VelocityAngleZ     = {{ Data(real, 1, 1) = 0.02  }} ;
    }} ;

Basically, this states that :sidskey:`DirichletData` contains four instances of :sidskey:`DataArray_t` with identifiers or names :sidskey:`PressureStagnation`, :sidskey:`MassFlow`, :sidskey:`VelocityAngleY` and :sidskey:`VelocityAngleZ`.
Each :sidskey:`DataArray_t` structure entity contains a single floating-point value; these are the Dirichlet data for the BC. Note that :sidskey:`Data(real, 1, 1)` means a single floating-point value.

The :ref:`global verses local <globalvslocal>` data issue can be easily handled by storing either a scalar, as shown above, for the global BC data case; or storing an array for the local BC data case.
Storing an array of local BC data allows the capability for specifying non-constant solution profiles, such as "analytic" boundary-layer profiles or profiles derived from experimental data.
For the above example, if the stagnation pressure is instead specified at every vertex of the boundary-condition patch the following results:

.. code-block:: sids

  BCData_t<ListLength=99> DirichletData = 
    {{
    DataArray_t<real, 1, 99> PressureStagnation = 
      {{ Data(real, 1, 99) = (PTOT(n), n=1,99) }} ;
    DataArray_t<real, 1, 1> MassFlow           = {{ Data(real, 1, 1) = 1.34  }} ;
    DataArray_t<real, 1, 1> VelocityAngleY     = {{ Data(real, 1, 1) = 0.043 }} ;
    DataArray_t<real, 1, 1> VelocityAngleZ     = {{ Data(real, 1, 1) = 0.02  }} ;
    }} ;

where, say, the boundary face is logically rectangular and contains :math:`11 \times 9` vertices and the stagnation pressure at the vertices is given by the array :sidskey:`PTOT()`.

To facilitate implementation of boundary conditions into existing flow solvers, we adopt the convention that if no boundary-condition data is specified, then flow solvers are free to enforce any appropriate boundary-condition equations.
This includes situations where entities of :sidskey:`BCDataSet_t`, :sidskey:`BCData_t` or :sidskey:`DataArray_t` are absent within the boundary-condition hierarchy.
By convention, if no :sidskey:`BCDataSet` entities are present, then application codes are free to enforce appropriate BCs for the given value of :sidskey:`BCType`.
Furthermore, if the entities :sidskey:`DirichletData` and :sidskey:`NeumannData` are not present in an instance of :sidskey:`BCDataSet_t`, or if insufficient data is present in :sidskey:`DirichletData` or :sidskey:`NeumannData` (e.g., if only one Dirichlet variable is present for a subsonic inflow condition), then application codes are free to fill out the boundary-condition data as appropriate for the :sidskey:`BCTypeSimple` identifier.

The various levels of BC implementation allowed are shown in the following figure, from the lowest level in which the application codes interpret the :sidsref:`BCType`, to the fully SIDS-compliant BC implementation that completely defines the BC within the CGNS file.

.. list-table:: **Boundary Condition Implementation Levels**

  * - .. figure:: ../../../images/sids/figs/bcimpl_low.gif
        :width: 170px
        :align: center
        :alt: CGNS dataset nodes for lowest boundary condition implementation level allowed

        *Lowest-level allowed (application code interprets meaning of* :sidskey:`BCType` *)*

    - .. figure:: ../../../images/sids/figs/bcimpl_full.gif
        :width: 370px
        :align: center
        :alt: CGNS dataset nodes for fully SIDS-compliant boundary condition implementation

        *Fully SIDS-compliant*


An alternative approach to the present design could be to list all the solution variables and data (as :sidskey:`DataArray_t`-like structures) for the boundary condition, and contain descriptive tags in each one to indicate if they are Dirichlet or Neumann data.
We have not taken this approach. We think grouping boundary-condition data by "equation type" as we have done better allows for future extension to other types of boundary conditions (e.g., 2nd-order non-reflecting BC's that result in partial differential equations to be solved at the boundary).


Boundary Condition Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section contains boundary-condition examples with increasing complexity. Included is the most simple :sidsref:`BC_t` entity and one of the most complex.
The examples show situations of :ref:`local and global <globalvslocal>` boundary-condition data, :ref:`simple <BCTypeSimple>` and :ref:`compound <BCTypeCompound>` boundary-condition types, and multiple boundary-condition data sets that must be matched with the appropriate boundary-condition type.

Example - Symmetry Plane
~~~~~~~~~~~~~~~~~~~~~~~~

Symmetry plane for a patch on the *i*-min face of a 3-D structured zone.

.. code-block:: sids

  !  CellDimension = 3, IndexDimension = 3
  BC_t<3,3,3> BC1 =
    {{
    BCType_t BCType = BCSymmetryPlane ;

    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1,1,1 ] ;
      int[3] End   = [1,9,17] ;
      }} ;
    }} ;

Since the boundary-condition equations to be enforced are completely defined by the boundary-condition type :sidskey:`BCSymmetryPlane`, no other information needs to be provided, except for the extent of the BC patch.
The BC patch is specified by :sidskey:`PointRange` with a beginning index of (1,1,1) and an ending index of (1,9,17). By default, these refer to vertices.

Example - Viscous Solid Wall I
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A viscous solid wall for a 3-D structured zone, where a Dirichlet condition is enforced for temperature; the wall temperature for the entire wall is specified to be 273 K. The BC patch is on the *j*-min face and is bounded by the indices (1,1,1) and (33,1,9).

.. code-block:: sids

  !  CellDimension = 3, IndexDimension = 3
  BC_t<3,3,3> BC2 =
    {{
    BCType_t BCType = BCWallViscousIsothermal ;

    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1 ,1,1] ;
      int[3] End   = [33,1,9] ;
      }} ;

    !  ListLength = 33*9 = 297
    BCDataSet_t<297> BCDataSet1 =
      {{
      BCTypeSimple_t BCTypeSimple = BCWallViscousIsothermal ;

      !  Data array length = ListLength = 297
      BCData_t<297> DirichletData =
        {{
        DataArray_t<real, 1, 1> Temperature =
          {{
          Data(real, 1, 1) = 273. ;

          DataClass_t DataClass = Dimensional ;

          DimensionalUnits_t DimensionalUnits =
            {{
            MassUnits        = MassUnitsNull ;
            LengthUnits      = LengthUnitsNull ;
            TimeUnits        = TimeUnitsNull ;
            TemperatureUnits = Kelvin ;
            AngleUnits       = AngleUnitsNull ;
            }} ;
          }} ;
        }} ;
      }} ;
    }} ;

This is an example of a :ref:`simple boundary-condition type <BCTypeSimple>`, :sidskey:`BCWallViscousIsothermal`.
By default there is a zero Dirichlet condition on the velocity, and :sidsref:`BCDataSet1` states there is a Dirichlet condition on temperature with a global value of 273 K.
The data set contains a single :sidsref:`BCData_t` entity, called :sidskey:`DirichletData`, meaning a (possibly empty) collection of Dirichlet conditions should be enforced.
Within :sidskey:`DirichletData`, there is a single :sidskey:`DataArray_t` entity; this narrows the specification to a single Dirichlet condition.
This lone entity has the identifier :sidskey:`Temperature`, which by the :ref:`data-name identifier conventions <dataname>` is the identifier for static temperature.
The data contained in :sidskey:`Temperature` is a floating-point scalar with a value of 273.
The qualifiers :sidsref:`DataClass` and :sidsref:`DimensionalUnits` specify that the temperature is dimensional with units of Kelvin.

Since :sidskey:`BCWallViscousIsothermal` is a simple boundary-condition type, the appropriate data set contains a :sidskey:`BCTypeSimple` entity whose value is :sidskey:`BCWallViscousIsothermal`.
For this example, only a single data set is provided, and this data set has the correct boundary-condition type.
This is an example of a trivial data-set match.

Apart from velocity and temperature, additional "numerical" boundary conditions are typically required by Navier-Stokes flow solvers, but none are given here; therefore, a code is free to implement other additional boundary conditions as desired.

Although the boundary-condition data is global, we include in this example structure parameters that are the lengths of potential local-data arrays.
Comments are added to the example with the "!" notation to document the structure parameters.
The :sidsref:`BC_t` structure function :sidskey:`ListLength` is evaluated based on :sidskey:`PointRange`.
Since :sidskey:`GridLocation` is not specified in :sidskey:`BC2`, any local data is at vertices by default.
The entity :sidskey:`Temperature` contains global data, so the value of :sidskey:`ListLength` is unused in :sidskey:`DirichletData`.

This example raises the question of whether unused structure parameters are required in structure entities.
The answer is no. We included them here for completeness. The purpose of structure parameters is to mimic the need to define elements of a entity based on information contained elsewhere (at a higher level) in the CGNS database.
When this need is not present in a given instance of a structure entity, the structure parameters are superfluous.
In some of the following examples, structure parameters that are superfluous or otherwise not needed are denoted by ":sidskey:`?`".

Example - Subsonic Inflow
~~~~~~~~~~~~~~~~~~~~~~~~~

Subsonic inflow for a 2-D structured zone: The BC patch is on the *i*-min face and includes :math:`j \in [2, 7]`.
As prescribed by the boundary-condition type, three quantities must be specified.
Uniform entropy and stagnation enthalpy are specified with values of 0.94 and 2.85, respectively.
A velocity profile is specified at face midpoints, given by the array :code:`v_inflow(j)`.
No dimensional or nondimensional information is provided.

.. code-block:: sids

  !  CellDimension = 2, IndexDimension = 2
  BC_t<2,2,?> BC3 =
    {{
    BCType_t BCType = BCInflowSubsonic ;

    GridLocation_t GridLocation = FaceCenter ;

    IndexRange_t<2> PointRange =
      {{
      int[2] Begin = [1,2] ;
      int[2] End   = [1,6] ;
      }} ;

    !  ListLength = 5
    BCDataSet_t<5> BCDataSet1 =
      {{
      BCTypeSimple_t BCTypeSimple = BCInflowSubsonic ;

      !  Data array length = ListLength = 5
      BCData_t<5> DirichletData =
        {{
        DataArray_t<real, 1, 1> EntropyApprox =
          {{
          Data(real, 1, 1) = 0.94 ;
          }} ;

        DataArray_t<real, 1, 1> EnthalpyStagnation =
          {{
          Data(real, 1, 1) = 2.85 ;
          }} ;

        DataArray_t<real, 1, 5> VelocityY =
          {{
          Data(real, 1, 5) = (v_inflow(j), j=3,7) ;
          }} ;
        }} ;
      }} ;
    }} ;

This is another example of a :ref:`simple boundary-condition type <BCTypeSimple>`.
The primary additional complexity included in this example is multiple Dirichlet conditions with one containing local data.
:sidskey:`DirichletData` contains three :sidskey:`DataArray_t` entities named :sidskey:`EntropyApprox`, :sidskey:`EnthalpyStagnation` and :sidskey:`VelocityY`.
This specifies three Dirichlet boundary conditions to be enforced, and the names identify the solution quantities to set.
Since both :sidskey:`EntropyApprox` and :sidskey:`EnthalpyStagnation` have an array-length structure parameter of one, they identify global data, and the values are provided.
:sidskey:`VelocityY` is an array of data values and contains the values in :code:`v_inflow()`.
The length of the array is given by :sidskey:`ListLength`, which represents the number of cell faces because :sidskey:`BC3` is specified using the value of :sidskey:`FaceCenter` for :sidskey:`GridLocation`.
Note that the beginning and ending indices on the array :code:`v_inflow()` are unimportant (they are user inputs); there just needs to be five values provided.

Example - Outflow
~~~~~~~~~~~~~~~~~

Outflow boundary condition with unspecified normal Mach number for an *i*-max face of a 3-D structured zone: For subsonic outflow, a uniform pressure is specified; for supersonic outflow, no boundary-condition equations are specified.

.. code-block:: sids

  !  CellDimension = 3, IndexDimension = 3
  BC_t<3,3,3> BC4 =
    {{
    BCType_t BCType = BCOutflow ;

    IndexRange_t<3> PointRange = {{ }} ;

    BCDataSet_t<?> BCDataSetSubsonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCOutflowSubsonic ;

      BCData_t<?> DirichletData =
        {{
        DataArray_t<real, 1, 1> Pressure = {{ }} ;
        }} ;
      }} ;

    BCDataSet_t<?> BCDataSetSupersonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCOutflowSupersonic ;
      }} ;
    }} ;

This is an example of a :ref:`complex boundary-condition type <BCTypeCompound>`; the equation set to be enforced depends on the local flow conditions, namely the Mach number normal to the boundary.
Two data sets are provided, :sidskey:`BCDataSetSubsonic` and :sidskey:`BCDataSetSupersonic`; recall the names are unimportant and are user defined.
The first data set has a boundary-condition type of :sidskey:`BCOutflowSubsonic` and prescribes a global Dirichlet condition on static pressure.
Any additional boundary conditions needed may be applied by a flow solver. The second data set has a boundary-condition type of :sidskey:`BCOutflowSupersonic` with no additional boundary-condition equation specification.
Typically, all solution quantities are extrapolated from the interior for supersonic outflow.
From the boundary-condition type association table, :sidskey:`BCOutflow` requires two data sets with boundary-condition types :sidskey:`BCOutflowSubsonic` and :sidskey:`BCOutflowSupersonic`.
The accompanying usage rule states that the data set for :sidskey:`BCOutflowSubsonic` should be used for a subsonic normal Mach number; otherwise, the data set for :sidskey:`BCOutflowSupersonic` should be enforced.

Any additional data sets with boundary-condition types other than :sidskey:`BCOutflowSubsonic` or :sidskey:`BCOutflowSupersonic` could be provided (the definition of :sidsref:`BC_t` allows an arbitrary list of :sidskey:`BCDataSet_t` entities); however, they should be ignored by any code processing the boundary-condition information.
Another caveat is that providing two data sets with the same simple boundary-condition type would cause indeterminate results - which one is the correct data set to apply?

The actual global data value for static pressure is not provided; an abbreviated form of the :sidskey:`Pressure` entity is shown.
This example also uses the ":sidskey:`?`" notation for unused data-array-length structure parameters.

Example - Farfield
~~~~~~~~~~~~~~~~~~

Farfield boundary condition with arbitrary flow conditions for a *j*-max face of a 2-D structured zone: If subsonic inflow, specify entropy, vorticity and incoming acoustic characteristics; if supersonic inflow specify entire flow state; if subsonic outflow, specify incoming acoustic characteristic; and if supersonic outflow, extrapolate all flow quantities.
None of the extrapolated quantities for the different boundary condition possibilities need be stated.

.. code-block:: sids

  !  CellDimension = 2, IndexDimension = 2
  BC_t<2,2,2> BC5 =
    {{
    BCType_t BCType = BCFarfield ;

    IndexRange_t<2> PointRange = {{ }} ;

    int[2] InwardNormalIndex = [0,-1] ;

    BCDataSet_t<?> BCDataSetInflowSupersonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCInflowSupersonic ;
      }} ;

    BCDataSet_t<?> BCDataSetInflowSubsonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCInflowSubsonic ;

      BCData<?> DirichletData =
        {{
        DataArray_t<real, 1, 1> CharacteristicEntropy      = {{ }} ;
        DataArray_t<real, 1, 1> CharacteristicVorticity1   = {{ }} ;
        DataArray_t<real, 1, 1> CharacteristicAcousticPlus = {{ }} ;
        }} ;
      }} ;

    BCDataSet_t<?> BCDataSetOutflowSupersonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCOutflowSupersonic ;
      }} ;

    BCDataSet_t<?> BCDataSetOutflowSubsonic =
      {{
      BCTypeSimple_t BCTypeSimple = BCOutflowSubsonic ;

      BCData<?> DirichletData =
        {{
        DataArray_t<real, 1, 1> CharacteristicAcousticMinus = {{ }} ;
        }} ;
      }} ;
    }} ;


The farfield boundary-condition type is the most complex of the :ref:`compound boundary-condition types <BCTypeCompound>`.
:sidskey:`BCFarfield` requires four data sets; these data sets must contain the :ref:`simple boundary-condition types <BCTypeSimple>` :sidskey:`BCInflowSupersonic`, :sidskey:`BCInflowSubsonic`, :sidskey:`BCOutflowSupersonic` and :sidskey:`BCOutflowSubsonic`.
This example provides four appropriate data sets. The :ref:`usage rule <BCType-assoc>` given for :sidskey:`BCFarfield` states which set of boundary-condition equations to be enforced based on the normal velocity and normal Mach number.

The data set for supersonic-inflow provides no information other than the :ref:`boundary-condition type <BCType>`.
A flow solver is free to apply any conditions that are appropriate; typically all solution quantities are set to freestream reference state values.
The data set for subsonic-inflow states that three Dirichlet conditions should be enforced; the three data identifiers provided are from the :ref:`standard data-name identifier conventions <dataname>`.
The data set for supersonic-outflow only provides the boundary-condition type, and the data set for subsonic-outflow provides one Dirichlet condition on the incoming acoustic characteristic, :sidskey:`CharacteristicAcousticMinus`.

Also provided in the example is the inward-pointing computational-coordinate normal; the normal points in the :math:`-j` direction, meaning the BC patch is a *j*-max face.
This information could also be obtained from the BC patch description given in :sidskey:`IndexRange`.

Note that this example shows only the overall layout of the boundary-condition entity.
:sidskey:`IndexRange` and all :sidskey:`DataArray_t` entities are abbreviated, and all unused structure functions are not evaluated.

Example - Viscous Solid Wall II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are circumstances when a user may wish to define a BC patch using vertices (under :sidsref:`BC_t`), but store the BC data at face centers (under :sidsref:`BCDataSet_t`).
The following example is similar to the :ref:`Viscous Solid Wall <ex-bc6>` example given previously, with the exception that the Dirichlet data for temperature is stored at face centers rather than at vertices.

As before, the example is a viscous solid wall in a 3-D structured zone, where a Dirichlet condition is enforced for temperature; the wall temperature for the entire wall is specified to be 273 K.
The BC patch is on the *j*-min face and is bounded by the indices (1,1,1) and (33,1,9).

.. code-block:: sids

  !  CellDimension = 3, IndexDimension = 3
  BC_t<3,3,3> BC2 =
    {{
    BCType_t BCType = BCWallViscousIsothermal ;

    !  Grid location is Vertex by default
    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1 ,1,1] ;
      int[3] End   = [33,1,9] ;
      }} ;

    !  ListLength = 33*9 = 297
    BCDataSet_t<297> BCDataSet1 =
      {{
      BCTypeSimple_t BCTypeSimple = BCWallViscousIsothermal ;

      GridLocation_t GridLocation = FaceCenter ;
      IndexRange_t<3> PointRange =
        {{
        int[3] Begin = [1 ,1,1] ;
        int[3] End   = [32,1,8] ;
        }} ;

      !  ListLength = 32*8 = 256
      BCData_t<256> DirichletData =
        {{
        DataArray_t<real, 1, 1> Temperature =
          {{
          Data(real, 1, 1) = 273. ;

          DataClass_t DataClass = Dimensional ;

          DimensionalUnits_t DimensionalUnits =
            {{
            MassUnits        = MassUnitsNull ;
            LengthUnits      = LengthUnitsNull ;
            TimeUnits        = TimeUnitsNull ;
            TemperatureUnits = Kelvin ;
            AngleUnits       = AngleUnitsNull ;
            }} ;
          }} ;
        }} ;
      }} ;
    }} ;

As in the previous :ref:`Viscous Solid Wall <ex-bc6>` example, although the boundary-condition data is global, we include in this example structure parameters that are the lengths of potential local-data arrays.
In :sidsref:`BC_t`, :sidskey:`GridLocation` is not specified, and thus is :sidskey:`Vertex` by default.
The structure function :sidskey:`ListLength` is 297, based on the specification of :sidskey:`PointRange`, and that value is passed to :sidskey:`BCDataSet_t`.

In this example :sidskey:`PointRange` is specified in :sidskey:`BCDataSet_t`, so the :sidskey:`ListLength` passed into it from :sidskey:`BC_t` is not used.
In :sidskey:`BCDataSet_t`, :sidskey:`GridLocation` is specified as :sidskey:`FaceCenter`, and :sidskey:`PointRange` is set accordingly.
The corresponding value of :sidskey:`ListLength` is 256, which is passed into :sidsref:`BCData_t`.

As before, in :sidskey:`BCData_t` the entity :sidskey:`Temperature` contains global data, so the value of :sidskey:`ListLength` is unused.

.. last line
