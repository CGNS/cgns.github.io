.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardMiscDataStruct:

Miscellaneous Data Structures
=============================

This section contains miscellaneous structure types for describing reference states, convergence history, discrete field data, integral or global data, families, and user-defined data.

Reference State Structure Definition: ``ReferenceState_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ReferenceState_t` describes a reference state, which is a list of geometric or flow-state quantities defined at a common location or condition. Examples of typical reference states associated with CFD calculations are freestream, plenum, stagnation, inlet and exit. Note that providing a :sidskey:`ReferenceState` description is particularly important if items elsewhere in the CGNS database are :ref:`NormalizedByUnknownDimensional <normbyunkdim>`.

.. code-block:: sids

  ReferenceState_t :=
    {
    Descriptor_t ReferenceStateDescription ;                           (o)
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidskey:`Descriptor_t`, :sidskey:`DataArray_t`, and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ReferenceState_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, or :sidskey:`ReferenceStateDescription`. 

Data-name identifiers associated with :sidskey:`ReferenceState` are shown in the table below.

.. table:: **Data-Name Identifiers for Reference State**

  +----------------------------------------+----------------------------------------------+------------------+
  | Data-Name Identifier                   | Description                                  |  Units           |
  +========================================+==============================================+==================+
  |:sidskey:`Mach`                         | Mach number, :math:`M = q/c`                 |  :math:`-`       |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Mach_Velocity`                | Velocity scale, :math:`q`                    |  :math:`L/T`     |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Mach_VelocitySound`           | Speed of sound scale, :math:`c`              |  :math:`L/T`     |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Reynolds`                     | Reynolds number, :math:`Re = V L_{R} / \nu`  |  :math:`-`       |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Reynolds_Velocity`            | Velocity scale, :math:`V`                    |  :math:`L/T`     |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Reynolds_Length`              | Length scale, :math:`L_{R}`                  |  :math:`L`       |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`Reynolds_ViscosityKinematic`  | Kinematic viscosity scale, :math:`\nu`       |  :math:`L^{2}/T` |
  +----------------------------------------+----------------------------------------------+------------------+
  |:sidskey:`LengthReference`              | Reference length, :math:`L`                  |  :math:`L`       |
  +----------------------------------------+----------------------------------------------+------------------+


In addition, any flowfield quantities (such as :sidskey:`Density`, :sidskey:`Pressure`, etc.) can be included in the :sidskey:`ReferenceState`.

The reference length :math:`L` (:sidskey:`LengthReference`) may be necessary for :ref:`NormalizedByUnknownDimensional <normbyunkdim>` databases, to define the length scale used for nondimensionalizations.
It may be the same or different from the :sidskey:`Reynolds_Length` used to define the Reynolds number.

Because of different definitions for angle of attack and angle of yaw, these quantities are not explicitly defined in the SIDS. Instead, the user can unambigouosly denote the freestream velocity vector direction by giving :sidskey:`VelocityX`, :sidskey:`VelocityY`, and :sidskey:`VelocityZ` in :sidskey:`ReferenceState`, (with the reference state denoting the freestream).

Care should be taken when defining the reference state quantities to ensure consistency. (See the discussion in the section on :ref:`Nondimensional Data Normalized by Unknown Dimensional Quantities <normbyunkdim>`.) For example, if velocity, length, and time are all defined, then the velocity stored should be length/time.
If consistency is not followed, different applications could interpret the resulting data in different ways.

:sidskey:`DataClass` defines the default for the class of data contained in the reference state.
If any reference state quantities are dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

We recommend using the :sidskey:`ReferenceStateDescription` entity to document the flow conditions. The format of the documentation is currently unregulated. 

Reference State Example
^^^^^^^^^^^^^^^^^^^^^^^

An example is presented in this section of a reference state entity that contains dimensional data. An additional example of a nondimensional reference state is provided in the :ref:`Structured Two-Zone Flat Plate Example <twozone>`.

Example - Reference State with Dimensional Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A freestream reference state where all data quantities are dimensional. Standard atmospheric conditions at sea level are assumed for static quantities, and all stagnation variables are obtained using the isentropic relations.
The flow velocity is 200 m/s aligned with the *x*-axis. Dimensional units of kilograms, meters, and seconds are used. The data class and system of units are specified at the :sidskey:`ReferenceState_t` level rather than attaching this information directly to the :sidskey:`DataArray_t` entities for each reference quantity.
Data-name identifiers are provided in the section :ref:`Conventions for Data-Name Identifiers <dataname>`.

.. code-block:: sids

  ReferenceState_t ReferenceState = 
    {{
    Descriptor_t ReferenceStateDescription = 
      {{
      Data(char, 1, 45) = "Freestream at standard atmospheric conditions" ;
      }} ;
    
    DataClass_t DataClass = Dimensional ;

    DimensionalUnits_t DimensionalUnits = 
      {{
      MassUnits        = Kilogram ;
      LengthUnits      = Meter ;
      TimeUnits        = Second ;
      TemperatureUnits = Kelvin ;
      AngleUnits       = Radian ;
      }} ;

    DataArray_t<real, 1, 1> VelocityX = 
      {{
      Data(real, 1, 1) = 200. ;
      }} ;
    DataArray_t<real, 1, 1> VelocityY               = {{ 0. }} ;
    DataArray_t<real, 1, 1> VelocityZ               = {{ 0. }} ;

    DataArray_t<real, 1, 1> Pressure                = {{ 1.0132E+05 }} ;
    DataArray_t<real, 1, 1> Density                 = {{ 1.226 }} ;
    DataArray_t<real, 1, 1> Temperature             = {{ 288.15 }} ;
    DataArray_t<real, 1, 1> VelocitySound           = {{ 340. }} ;
    DataArray_t<real, 1, 1> ViscosityMolecular      = {{ 1.780E-05 }} ;

    DataArray_t<real, 1, 1> PressureStagnation      = {{ 1.2806E+05 }} ;
    DataArray_t<real, 1, 1> DensityStagnation       = {{ 1.449 }} ;
    DataArray_t<real, 1, 1> TemperatureStagnation   = {{ 308.09 }} ;
    DataArray_t<real, 1, 1> VelocitySoundStagnation = {{ 351.6 }} ;

    DataArray_t<real, 1, 1> PressureDynamic         = {{ 0.2542E+05 }} ;
    }} ;                        

Note that all :sidsref:`DataArray_t` entities except :sidskey:`VelocityX` have been abbreviated. 



Convergence History Structure Definition: ``ConvergenceHistory_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Flow solver convergence history information is described by the :sidskey:`ConvergenceHistory_t` structure.
This structure contains the number of iterations and a list of data arrays containing convergence information at each iteration.

.. code-block:: sids

  ConvergenceHistory_t :=
    {
    Descriptor_t NormDefinitions ;                                     (o)
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    int Iterations ;                                                   (r)

    List( DataArray_t<DataType, 1, Iterations> 
      DataArray1 ... DataArrayN ) ;                                    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ConvergenceHistory_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, or :sidskey:`NormDefinitions`.
  #. :sidskey:`Iterations` is the only required field for :sidskey:`ConvergenceHistory_t`. 

:sidskey:`Iterations` identifies the number of iterations for which convergence information is recorded.
This value is also passed into each of the :sidskey:`DataArray_t` entities, defining the length of the data arrays.

:sidskey:`DataClass` defines the default for the class of data contained in the convergence history.
If any convergence-history data is dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard precedence rules.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Measures used to record convergence vary greatly among current flow-solver implementations.
Convergence information typically includes global forces, norms of equation residuals, and norms of solution changes.
Attempts to systematically define a set of convergence measures within the CGNS project have been futile.
For global parameters, such as forces and moments, a set of :ref:`standardized data-array identifiers <dataname>` is used.
For equations residuals and solution changes, no such standard list exists. It is suggested that data-array identifiers for norms of equations residuals begin with :sidskey:`RSD`, and those for solution changes begin with :sidskey:`CHG`.
For example, :sidskey:`RSDMassRMS` could be used for the :math:`L_2`-norm (RMS) of mass conservation residuals.
It is also strongly recommended that :sidskey:`NormDefinitions` be utilized to describe the convergence information recorded in the data arrays.
The format used to describe the convergence norms in :sidskey:`NormDefinitions` is currently unregulated.


Discrete Data Structure Definition: ``DiscreteData_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`DiscreteData_t` provides a description of generic discrete data (i.e., data defined on a computational grid); it is identical to :sidsref:`FlowSolution_t` except for its type name.
This structure can be used to store field data, such as fluxes or equation residuals, that is not typically considered part of the flow solution.
:sidskey:`DiscreteData_t` contains a list for data arrays, identification of grid location, and a mechanism for identifying rind-point data included in the data arrays.
All data contained within this structure must be defined at the same grid location and have the same amount of rind-point data.

.. code-block:: sids

  DiscreteData_t< int CellDimension, int IndexDimension,
                  int VertexSize[IndexDimension],
                  int CellSize[IndexDimension] > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridLocation_t GridLocation ;                                      (o/d)

    IndexRange<IndexDimension> PointRange ;                            (o)
    IndexArray<IndexDimension, ListLength[], int> PointList ;          (o)

    Rind_t<IndexDimension> Rind ;                                      (o/d)

    List( DataArray_t<DataType, IndexDimension, DataSize[]> 
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)
    
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`DiscreteData_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`GridLocation`, :sidskey:`PointList`, :sidskey:`PointRange`, or :sidskey:`Rind`.
  #. There are no required fields for :sidskey:`DiscreteData_t`. :sidskey:`GridLocation` has a default of :sidskey:`Vertex` if absent. :sidskey:`Rind` also has a default if absent; the default is equivalent to having an instance of :sidskey:`Rind` whose :sidskey:`RindPlanes` array contains all zeros.
  #. Both of the fields :sidskey:`PointRange` and :sidskey:`PointList` are optional. Only one of these two fields may be specified.
  #. The structure parameter :sidskey:`DataType` must be consistent with the data stored in the :sidskey:`DataArray_t` entities.
  #. For unstructured zones :sidskey:`GridLocation` options are limited to :sidskey:`Vertex` or :sidskey:`CellCenter`, unless one of :sidskey:`PointRange` or :sidskey:`PointList` is present.
  #. Indexing of data within the :sidskey:`DataArray_t` structures, must be consistent with the associated numbering of vertices or elements. 

:sidskey:`DiscreteData_t` requires four structure parameters; :sidskey:`CellDimension` identifies the dimensionality of cells or elements, :sidskey:`IndexDimension` identifies the dimensionality of the grid size arrays, and :sidskey:`VertexSize` and :sidskey:`CellSize` are the number of core vertices and cells, respectively, in each index direction, excluding rind points. For structured zones, core vertices and cells begin at [1,1,1] (in 3-D) and end at :sidskey:`VertexSize` and :sidskey:`CellSize`, respectively. For unstructured zones, :sidskey:`IndexDimension` is always 1.

The arrays of discrete data are stored in the list of :sidskey:`DataArray_t` entities. The field :sidskey:`GridLocation` specifies the location of the data with respect to the grid; if absent, the data is assumed to coincide with grid vertices (i.e., :sidskey:`GridLocation = Vertex`). All data within a given instance of :sidskey:`DiscreteData_t` must reside at the same grid location.

For structured grids, the value of :sidskey:`GridLocation` alone specifies the location and indexing of the discrete. Vertices are explicity indexed. Cell centers and face centers are indexed using the minimum of the connecting vertex indices, as described in the section :ref:`Structured Grid Notation and Indexing Conventions <structgrid>`.

For unstructured grids, the value of :sidskey:`GridLocation` alone specifies location and indexing of discrete data only for vertex and cell-centered data. The reason for this is that element-based grid connectivity provided in the :sidskey:`Elements_t` data structures explicitly indexes only vertices and cells.
For data stored at alternate grid locations (e.g., edges), additional connectivity information is needed. This is provided by the optional fields :sidskey:`PointRange` and :sidskey:`PointList`; these refer to vertices, edges, faces or cell centers, depending on the values of :sidskey:`CellDimension` and :sidskey:`GridLocation`.
The following table shows these relations.

.. table::

  +-----------------+-----------------------------------------------------------------------+
  | CellDimension   | GridLocation                                                          |
  |                 +------------+-------------+----------------+---------------------------+
  |                 | Vertex     | EdgeCenter  | \*FaceCenter   |  CellCenter               |
  +=================+============+=============+================+===========================+
  |  1              | vertices   |  `-`        |  `-`           |  cells (line elements)    |
  +-----------------+------------+-------------+----------------+---------------------------+
  |  2              | vertices   |  edges      |  `-`           |  cells (area elements)    |
  +-----------------+------------+-------------+----------------+---------------------------+
  |  3              | vertices   |  edges      |  faces         |  cells (volume elements)  |
  +-----------------+------------+-------------+----------------+---------------------------+

Note: In the table, :sidskey:`*FaceCenter` stands for the possible types: :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter`, :sidskey:`KFaceCenter`, or :sidskey:`FaceCenter`.

Although intended for edge or face-based discrete data for unstructured grids, the fields :sidskey:`PointRange/List` may also be used to (redundantly) index vertex and cell-centered data.
In all cases, indexing of flow solution data corresponds to the element numbering as defined in the :sidskey:`Elements_t` data structures.

:sidskey:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points or elements (for unstructured grids) included in the data.
Its purpose and function are identical to those described for the :sidskey:`GridCoordinates_t` structure.
Note, however, that the :sidskey:`Rind` in this structure is independent of the :sidskey:`Rind` contained in :sidskey:`GridCoordinates_t`.
They are not required to contain the same number of rind planes or elements. Also, the location of any flow-solution rind points is assumed to be consistent with the location of the core flow solution points (e.g., if :sidskey:`GridLocation = CellCenter`, rind points are assumed to be located at fictitious cell centers).

:sidskey:`DataClass` defines the default for the class of data contained in the :sidskey:`DataArray_t` entities.
For dimensional data, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard precedence rules.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. c:function:: FUNCTION ListLength()

   :return value: ``int``
   :dependencies: :sidskey:`PointList`, :sidskey:`PointRange[]`

   :sidskey:`DiscreteData_t` requires the structure function :sidskey:`ListLength`, which is used to specify the number of entities (e.g. vertices) corresponding to a given :sidskey:`PointRange` or :sidskey:`PointList`. If :sidskey:`PointRange` is specified, then :sidskey:`ListLength` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`.
   If :sidskey:`PointList` is specified, then :sidskey:`ListLength` is the number of indices in the list of points. In this situation, :sidskey:`ListLength` becomes a user input along with the indices of the list :sidskey:`PointList`.
   By user we mean the application code that is generating the CGNS database.

.. c:function:: FUNCTION DataSize()

   :return value: one-dimensional ``int`` array of length :sidskey:`IndexDimension`
   :dependencies: :sidskey:`IndexDimension`, :sidskey:`VertexSize[]`, :sidskey:`CellSize[]`, :sidskey:`GridLocation`, :sidskey:`Rind`, :sidskey:`ListLength[]`

   The function :sidskey:`DataSize[]` is the size of discrete-data arrays. It is identical to the function :sidskey:`DataSize[]` defined for :sidskey:`FlowSolution_t`.


Integral Data Structure Definition: ``IntegralData_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`IntegralData_t` provides a description of generic global or integral data that may be associated with a particular zone or an entire database. In contrast to :sidskey:`DiscreteData_t`, integral data is not associated with any specific field location.

.. code-block:: sids

  IntegralData_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
    
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`DiscreteData_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  #. There are no required fields for :sidskey:`IntegralData_t`.
  #. The structure parameter :sidskey:`DataType` must be consistent with the data stored in the :sidskey:`DataArray_t` entities. 

:sidskey:`DataClass` defines the default class for data contained in the :sidskey:`DataArray_t` entities. For dimensional data, :sidskey:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard precedence rules.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.



Family Data Structure Definition: ``Family_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Geometric associations need to be set through one layer of indirection. That is, rather than setting the geometry data for each mesh entity (nodes, edges, and faces), they are associated to intermediate objects.
The intermediate objects are in turn linked to nodal regions of the computational mesh. We define a CFD family as this intermediate object. This layer of indirection is necessary since there is rarely a 1-to-1 connection between mesh regions and geometric entities.

The :sidskey:`Family_t` data structure holds the CFD family data. Each mesh surface is linked to the geometric entities of CAD databases by a name attribute. This attribute corresponds to a family of CAD geometric entities on which the mesh face is projected. Each one of these geometric entities is described in a CAD file and is not redefined within the CGNS file.
A :sidskey:`Family_t` data structure may be included in the :sidskey:`CGNSBase_t` structure for each CFD family of the model.

A hierarchy of :sidskey:`Family_t` nodes can be build by adding a :sidskey:`Family_t` node as child of an existing :sidskey:`Family_t` node. One can mimic an existing CAD hierarchy or add another hierarchy for special application purpose.

In case of a tree of :sidskey:`Family_t`, the actual reference to a family in the tree should follow the pattern as described in :ref:`Base Level Families <BaseLevelFamilies>`.

The :sidskey:`Family_t` structure contains all information pertinent to a CFD family. This information includes the name attribute or family name, the boundary conditions applicable to these mesh regions, and the referencing to the CAD databases.

.. code-block:: sids

  Family_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    FamilyBC_t FamilyBC ;                                              (o)

    List( GeometryReference_t
          GeometryReference1 ... GeometryReferenceN ) ;                (o)

    RotatingCoordinates_t RotatingCoordinates ;                        (o)

    List( Family_t Family1 ... FamilyN ) ;                             (o)

    List( FamilyName_t FamilyName1 ... FamilyNameN ) ;                 (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;

.. note::

  #. All data structures contained in :sidskey:`Family_t` are optional.
  #. Default names for the :sidsref:`Descriptor_t`, :sidskey:`GeometryReference_t`, and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique at this level and must not include the names :sidskey:`FamilyBC`, :sidskey:`Ordinal`, or :sidskey:`RotatingCoordinates`.
  #. The CAD referencing data are written in the :sidskey:`GeometryReference_t` data structures. They identify the CAD systems and databases where the geometric definition of the family is stored.
  #. The boundary condition type pertaining to a family is contained in the data structure :sidskey:`FamilyBC_t`. If this boundary condition type is to be used, the :sidskey:`BCType` specified under :sidskey:`BC_t` must be FamilySpecified.
  #. For the purpose of defining zone properties, families are extended to a volume of cells. In such case, the :sidskey:`GeometryReference_t` structures are not used.
  #. The mesh is linked to the family by attributing a family name to a BC patch or a zone in the data structure :sidskey:`BC_t` or :sidskey:`Zone_t`, respectively.
  #. A hierarchy of families is possible through the list of :sidskey:`FamilyName_t` nodes. These nodes contain both a user defined node name and a family name. The node name :sidskey:`FamilyParent` may be used to specify the family name for the parent of the current :sidskey:`Family_t` node.
  #. :sidskey:`Ordinal` is defined in the SIDS as a user-defined integer with no restrictions on the values that it can contain. It may be used here to attribute a number to the family.
  #. A :sidskey:`Family_t` tree structure can be specified using the list of :sidskey:`Family_t` children nodes. Into each of these children nodes the note #7 can be used to have a back tracking of the node parent.

Rotation of the CFD family may be defined using the :sidskey:`RotatingCoordinates_t` data structure.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.


Geometry Reference Structure Definition: ``GeometryReference_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The standard interface data structure identifies the CAD systems used to generate the geometry, the CAD files where the geometry is stored, and the geometric entities corresponding to the family.
The :sidskey:`GeometryReference_t` structures contain all the information necessary to associate a CFD family to the CAD databases.
For each :sidskey:`GeometryReference_t` structure, the CAD format is recorded in :sidskey:`GeometryFormat`, and the CAD file in :sidskey:`GeometryFile`.
The geometry entity or entities within this CAD file that correspond to the family are recorded under the :sidskey:`GeometryEntity_t` nodes.

.. code-block:: sids

  GeometryReference_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GeometryFormat_t GeometryFormat ;                                  (r)

    GeometryFile_t GeometryFile ;                                      (r)

    List (GeometryEntity_t GeometryEntity1 ... GeometryEntityN) ;      (o/d)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

The :sidskey:`GeometryFormat` is an enumeration type that identifies the CAD system used to generate the geometry.

.. code-block:: sids

  GeometryFormat_t := Enumeration(
    GeometryFormatNull,
    GeometryFormatUserDefined,
    NASA-IGES,
    SDRC,
    STEP-AP203,
    STEP-AP242,
    Unigraphics,
    ProEngineer,
    ICEM-CFD ) ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`GeometryEntity_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique at this level and must not include the names :sidskey:`GeometryFile` or :sidskey:`GeometryFormat`.
    #. By default, there is only one :sidskey:`GeometryEntity` and its name is the family name.
    #. There is no limit to the number of CAD files or CAD systems referenced in a CGNS file. Different parts of the same model may be described with different CAD files of different CAD systems.
    #. Other CAD geometry formats may be added to this list as needed. 



Family Boundary Condition Structure Definition: ``FamilyBC_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the main advantages of the concept of a layer of indirection (called a family here) is that the mesh density and the geometric entities may be modified without altering the association between nodes and intermediate objects, or between intermediate objects and geometric entities. This is very beneficial when handling boundary conditions and properties. Instead of setting boundary conditions directly on mesh entities, or on CAD entities, they may be associated to the intermediate objects. Since these intermediate objects are stable in the sense that they are not subject to mesh or geometric variations, the boundary conditions do not need to be redefined each time the model is modified. Using the concept of indirection, the boundary conditions and property settings are made independent of operations such as geometric changes, modification of mesh topology (i.e., splitting into zones), mesh refinement and coarsening, etc.

The :sidskey:`FamilyBC_t` data structure contains the boundary condition type. It is envisioned that it will be extended to hold both material and volume properties as well.

.. code-block:: sids

  FamilyBC_t :=
    {
    BCType_t BCType;                                                   (r)

    List( FamilyBCDataSet_t<ListLength> BCDataSet1 ... BCDataSetN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidskey:`FamilyBCDataSet_t` list are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`FamilyBC_t` and shall not include the name :sidskey:`BCType`.

:sidskey:`BCType` specifies the boundary-condition type, which gives general information on the boundary-condition equations to be enforced.
Boundary conditions are to be applied at the locations specified by the :sidskey:`BC_t` structure(s) associated with the CFD family.

The :sidskey:`FamilyBC_t` structure provides for a list of boundary-condition data sets.
In general, the proper :sidskey:`FamilyBCDataSet_t` instance to impose on the CFD family is determined by the :sidskey:`BCType` :ref:`association table <BCType-assoc>`.
The mechanics of determining the proper data set to impose is described in the section :ref:`Matching Boundary Condition Data Sets <BCType-assoc>`.

For a few boundary conditions, such as a symmetry plane or polar singularity, the value of :sidskey:`BCType` completely describes the equations to impose, and no instances of :sidskey:`FamilyBCDataSet_t` are needed.
For "simple" boundary conditions, where a single set of Dirichlet and/or Neumann data is applied, a single :sidskey:`FamilyBCDataSet_t` will likely appear (although this is not a requirement).
For "compound" boundary conditions, where the equations to impose are dependent on local flow conditions, several instances of :sidskey:`FamilyBCDataSet_t` will likely appear; the procedure for choosing the proper data set is more complex as described in the section :ref:`Matching Boundary Condition Data Sets <BCType-assoc>`.


Family Boundary Condition Data Set Structure Definition: ``FamilyBCDataSet_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`FamilyBCDataSet_t` contains Dirichlet and Neumann data for a single set of boundary-condition equations. Its intended use is for simple boundary-condition types, where the equations imposed do not depend on local flow conditions.

.. code-block:: sids

  FamilyBCDataSet_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                  (o)

    BCTypeSimple_t BCTypeSimple ;                                       (r)

    BCData_t<1> DirichletData ;                                         (o)
    BCData_t<1> NeumannData ;                                           (o)

    ReferenceState_t ReferenceState ;                                   (o)

    DataClass_t DataClass ;                                             (o)

    DimensionalUnits_t DimensionalUnits ;                               (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;   (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`FamilyBCDataSet_t` and shall not include the names :sidskey:`BCTypeSimple`, :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`DirichletData`, :sidskey:`NeumannData` or :sidskey:`ReferenceState`.
  #. :sidskey:`BCTypeSimple` is the only required field. All other fields are optional.

:sidskey:`BCTypeSimple` specifies the boundary-condition type, which gives general information on the boundary-condition equations to be enforced.
:sidskey:`BCTypeSimple` is also used for matching boundary condition data sets as discussed in the section :ref:`Matching Boundary Condition Data Sets <BCType-assoc>`.

Boundary-condition data is separated by equation type into Dirichlet and Neumann conditions. Dirichlet boundary conditions impose the value of the given variables, whereas Neumann boundary conditions impose the normal derivative of the given variables. The mechanics of specifying Dirichlet and Neumann data for boundary conditions is covered in section :ref:`Boundary Condition Specification Data <BC-specdata>`.

The substructures :sidskey:`DirichletData` and :sidskey:`NeumannData` contain boundary-condition data defined as globally constant over the family.

Reference quantities applicable to the set of boundary-condition data are contained in the :sidskey:`ReferenceState` structure.
:sidskey:`DataClass` defines the default for the class of data contained in the boundary condition data.
If the boundary conditions contain dimensional data, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these three entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Note that :sidskey:`FamilyBCDataSet_t` is similar to the data structure :sidsref:`BCDataSet_t`.
The primary difference is that :sidskey:`FamilyBCDataSet_t` only allows for globally constant Dirichlet and Neumann data. 


User-Defined Data Structure Definition: ``UserDefinedData_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the needs of all CGNS users cannot be anticipated, :sidskey:`UserDefinedData_t` provides a means of storing arbitrary user-defined data in :sidsref:`Descriptor_t` and :sidsref:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. code-block:: sids

  UserDefinedData_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridLocation_t GridLocation ;                                      (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (o)
    IndexArray_t<IndexDimension, ListLength, int> PointList ;          (o)

    List( DataArray_t<> DataArray1 ... DataArrayN ) ;                  (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    FamilyName_t FamilyName ;                                          (o)

    List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ; (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;

.. note::

  #. Default names for the :sidskey:`Descriptor_t`, :sidskey:`DataArray_t`, and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`UserDefinedData_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FamilyName`, :sidskey:`GridLocation`, :sidskey:`Ordinal`, :sidskey:`PointList`, or :sidskey:`PointRange`.
  #. :sidskey:`GridLocation` may be set to :sidskey:`Vertex`, :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter`, :sidskey:`KFaceCenter`, :sidskey:`FaceCenter`, :sidskey:`CellCenter`, or :sidskey:`EdgeCenter`. If :sidskey:`GridLocation` is absent, then its default value is :sidskey:`Vertex`. When :sidskey:`GridLocation` is set to :sidskey:`Vertex`, then :sidskey:`PointList` or :sidskey:`PointRange` refer to node indices, for both structured and unstructured grids. When :sidskey:`GridLocation` is set to :sidskey:`FaceCenter`, then :sidskey:`PointList` or :sidskey:`PointRange` refer to face elements.
  #. :sidskey:`GridLocation`, :sidskey:`PointRange`, and :sidskey:`PointList` may only be used when :sidskey:`UserDefinedData_t` is located below a :sidskey:`Zone_t` structure in the database hierarchy.
  #. Only one of :sidskey:`PointRange` and :sidskey:`PointList` may be specified.
  #. Both :sidskey:`FamilyName` and :sidskey:`AdditionalFamilyName` should refer to a :sidskey:`CGNSBase_t` level :sidskey:`Family_t`, in the parent base or in another sibling base (see :ref:`Base Level Families <BaseLevelFamilies>`). 


Gravity Data Structure Definition: ``Gravity_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidskey:`Gravity_t` data structure may be used to define the gravitational vector.

.. code-block:: sids

  Gravity_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    DataArray_t<real, 1, PhysicalDimension> GravityVector ;            (r)

    DataClass_t DataClass ;                                            (o)
    
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`Gravity_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, or :sidskey:`GravityVector`. 

The only required field under the :sidskey:`Gravity_t` data structure is :sidskey:`GravityVector`, which contains the components of the gravity vector in the coordinate system being used.

:sidskey:`DataClass` defines the default class for data contained in the :sidskey:`DataArray_t` entity.
For dimensional data, :sidskey:`DimensionalUnits` may be used to describe the system of units employed.
If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.


.. last line
