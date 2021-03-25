.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

Time-Dependent Flow
===================

This section describes structure types intended primarily for time-dependent flows. Data structures are presented for storing time-dependent or iterative data, and for recording rigid and arbitary grid motion. The section concludes with several examples. 

Iterative Data Structure Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to keep a record of time dependent or iterative data, the data structures BaseIterativeData_t and ZoneIterativeData_t are used.

Base Iterative Data Structure Definition: ``BaseIterativeData_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`BaseIterativeData_t` data structure is located directly under the :sidsref:`CGNSBase_t` node.
It contains information about the number of time steps or iterations being recorded, and the time and/or iteration values at each step.
In addition, it may include the list of zones and families for each step of the simulation, if these vary throughout the simulation.

The :sidskey:`BaseIterativeData_t` data structure is defined as follows:

.. code-block:: sids

  BaseIterativeData_t :=
    {
    int NumberOfSteps                                                  (r)

    DataArray_t<real, 1, NumberOfSteps> TimeValues ;                   (o/r)
    DataArray_t<int,  1, NumberOfSteps> IterationValues ;              (r/o)

    DataArray_t<int,  1, NumberOfSteps> NumberOfZones ;                (o)
    DataArray_t<int,  1, NumberOfSteps> NumberOfFamilies ;             (o)
    DataArray_t<char, 3, [65, MaxNumberOfZones, NumberOfSteps]>
       ZonePointers ;                                                  (o)
    DataArray_t<char, 3, [65, MaxNumberOfFamilies, NumberOfSteps]>
       FamilyPointers ;                                                (o)

    List( DataArray_t<> DataArray1 ... DataArrayN ) ;                  (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    }

.. note::

    #. Default names for the :sidsref:`DataArray_t`, :sidsref:`Descriptor_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`BaseIterativeData_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FamilyPointers`, :sidskey:`IterationValues`, :sidskey:`NumberOfFamilies`, :sidskey:`NumberOfZones`, :sidskey:`TimeValues`, or :sidskey:`ZonePointers`.
    
    #. :sidskey:`NumberOfSteps` is a required element of the :sidskey:`BaseIterativeData_t` data structure. It holds either the number of time steps or the number of iterations being recorded.
    
    #. :sidskey:`TimeValues` or :sidskey:`IterationValues` must be defined. If both are used, there must be a one-to-one correspondence between them. 

:sidskey:`TimeValues` and :sidskey:`IterationValues` are data-name identifiers corresponding to the time and iteration values stored in the file. When :sidskey:`IterationValues` are used, the iterative data stored in the database correspond to **values at the end of the associated iteration**.

The data-name identifiers :sidskey:`NumberOfZones` and :sidskey:`ZonePointers` are only used if different zone data structures apply to different steps of the simulation. (See the :ref:`Adapted Unstructured Mesh example <ex_adaptedunstructuredmesh>`.)

Similarly, if the geometry varies with time or iteration, then the data-name identifiers :sidskey:`NumberOfFamilies` and :sidskey:`FamilyPointers` are used to record which :sidsref:`Family_t` data structure(s) correspond(s) to which step.

The :sidskey:`DataArray_t` nodes for :sidskey:`ZonePointers` and :sidskey:`FamilyPointers` are defined as three-dimensional arrays. For each recorded step, the names of all zones and families being used for the step may be recorded. Note that the names are limited to 65 characters; this is the maximum size of a name of a zone from another base: 32 chars + '/' + 32 chars. Only one '/' character is allowed, then the first token before the '/' is the CGNSBase name and the second token is the Zone or Family name. If no '/' is found, the name is a Zone or a Family name of the current CGNS Base. The variables :sidskey:`MaxNumberOfZones` and :sidskey:`MaxNumberOfFamilies` represent the maximum number of zones and families that apply to one step. So if :sidskey:`NumberOfSteps` = 5 and :sidskey:`NumberOfZones` = {2,2,3,4,3}, then :sidskey:`MaxNumberOfZones` equals 4.

When :sidskey:`NumberOfZones` and :sidskey:`NumberOfFamilies` vary for different stored time steps, the name :sidskey:`Null` is used in :sidskey:`ZonePointers` and :sidskey:`FamilyPointers` as appropriate for steps in which the :sidskey:`NumberOfZones` or :sidskey:`NumberOfFamilies` is less than the :sidskey:`MaxNumberOfZones` or :sidskey:`MaxNumberOfFamilies`.

Any number of extra :sidskey:`DataArray_t` nodes are allowed. These should be used to record data not covered by this specification. 

Zone Iterative Data Structure Definition: ``ZoneIterativeData_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`ZoneIterativeData_t` data structure is located under the :sidskey:`Zone_t` node. It may be used to record pointers to zonal data for each recorded step of the simulation, and is defined as follows:

.. code-block:: sids

  ZoneIterativeData_t< int NumberOfSteps > :=
    {
    DataArray_t<char, 2, [32, NumberOfSteps]>
       RigidGridMotionPointers ;                                       (o)
    DataArray_t<char, 2, [32, NumberOfSteps]>
       ArbitraryGridMotionPointers ;                                   (o)
    DataArray_t<char, 2, [32, NumberOfSteps]>
       GridCoordinatesPointers ;                                       (o)
    DataArray_t<char, 2, [32, NumberOfSteps]>
       FlowSolutionPointers ;                                          (o)
    DataArray_t<char, 2, [32, NumberOfSteps]>
       ZoneGridConnectivityPointers ;                                  (o)
    DataArray_t<char, 2, [32, NumberOfSteps]>
       ZoneSubRegionPointers ;                                         (o)

    List( DataArray_t<> DataArray1 ... DataArrayN ) ;                  (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    }

.. note::

    Default names for the :sidsref:`DataArray_t`, :sidsref:`Descriptor_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ZoneIterativeData_t` and shall not include the names :sidskey:`ArbitraryGridMotionPointers`, :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FlowSolutionPointers`, :sidskey:`GridCoordinatesPointers`, :sidskey:`RigidGridMotionPointers`, :sidskey:`ZoneGridConnectivityPointers`, or :sidskey:`ZoneSubRegionPointers`.
    
The data arrays with data-name identifiers :sidskey:`xxxPointers` contain lists of associated data structures for each recorded time value or iteration. These data structures contain data at the associated time value, or at the end of the associated iteration. There is an implied one-to-one correspondence between each pointer (from 1, 2, ..., :sidskey:`NumberOfSteps`) and the associated :sidskey:`TimeValues` and/or :sidskey:`IterationValues` under :sidskey:`BaseIterativeData_t`. They refer by name to data structures within the current zone. The name :sidskey:`Null` is used when a particular time or iteration does not have a corresponding data structure to point to.

Any number of extra :sidskey:`DataArray_t` nodes are allowed. These should be used to record data not covered by this specification.

The :sidskey:`ZoneIterativeData_t` data structure may not exist without the :sidskey:`BaseIterativeData_t` under the :sidskey:`CGNSBase_t` node. However :sidskey:`BaseIterativeData_t` may exist without :sidskey:`ZoneIterativeData_t`. 


Rigid Grid Motion Structure Definition: ``RigidGridMotion_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding rigid grid motion information to the CGNS file enables an application code to determine the mesh location without the need to alter the original mesh definition recorded under :sidsref:`GridCoordinates_t`. A data structure named :sidskey:`RigidGridMotion_t` is used to record the necessary data defining a rigid translation and/or rotation of the grid coordinates.

The rigid grid motion is recorded independently for each zone of the CGNS base. Therefore the :sidskey:`RigidGridMotion_t` data structure is located under the zone data structure (:sidsref:`Zone_t`). There may be zero to several :sidskey:`RigidGridMotion_t` nodes under a :sidskey:`Zone_t` node. The multiple rigid grid motion definitions may be associated with different iterations or time steps in the computation. This association is recorded under the :sidsref:`ZoneIterativeData_t` data structure.

.. code-block:: sids

  RigidGridMotion_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    RigidGridMotionType_t RigidGridMotionType ;                        (r)

    DataArray_t<real, 2, [PhysicalDimension, 2]> OriginLocation ;      (r)
    DataArray_t<real, 1,  PhysicalDimension>     RigidRotationAngle ;  (o/d)
    DataArray_t<real, 1,  PhysicalDimension>     RigidVelocity ;       (o)
    DataArray_t<real, 1,  PhysicalDimension>     RigidRotationRate ;   (o)

    List( DataArray_t DataArray1 ... DataArrayN ) ;                    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`RigidGridMotion_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`OriginLocation`, :sidskey:`RigidGridMotionType`, :sidskey:`RigidRotationAngle`, :sidskey:`RigidRotationRate`, or :sidskey:`RigidVelocity`.
    
    #. :sidskey:`RigidGridMotionType` and :sidskey:`OriginLocation` are the only required elements under :sidskey:`RigidGridMotion_t`. All other elements are optional. 

:sidskey:`RigidGridMotionType_t` is an enumeration type that describes the type of rigid grid motion.

.. code-block:: sids

  RigidGridMotionType_t := Enumeration(
    RigidGridMotionTypeNull,
    RigidGridMotionTypeUserDefined,
    ConstantRate,
    VariableRate ) ;

The characteristics of the grid motion are defined by the following data-name identifiers: 

.. table:: **Data-Name Identifiers for Rigid Grid Motion**
  :align: center

  +---------------------------------+-----------------------------------------------------------------------------------------+------------------+
  | Data-Name Identifier            | Description                                                                             | Units            |
  +=================================+=========================================================================================+==================+
  | :sidskey:`OriginLocation`       | Physical coordinates of the origin before and after the rigid grid motion               | :math:`L`        |
  +---------------------------------+-----------------------------------------------------------------------------------------+------------------+
  | :sidskey:`RigidRotationAngle`   | Rotation angles about each axis of the translated coordinate system.                    | :math:`\alpha`   |
  |                                 | If rotating about more than one axis, the rotation is performed first about the x-axis, |                  |
  |                                 | then the y-axis, then the z-axis. If not specified, :sidskey:`RigidRotationAngle`       |                  |
  |                                 | is set to zero.                                                                         |                  |
  +---------------------------------+-----------------------------------------------------------------------------------------+------------------+
  | :sidskey:`RigidVelocity`        | Grid velocity vector of the origin translation                                          | :math:`L/T`      |
  +---------------------------------+-----------------------------------------------------------------------------------------+------------------+
  | :sidskey:`RigidRotationRate`    | Rotation rate vector about the axis of the translated coordinate system                 | :math:`\alpha/T` |
  +---------------------------------+-----------------------------------------------------------------------------------------+------------------+

Any number of :sidskey:`DataArray_t` nodes are allowed. These may be used to record data not covered by this specification.

"Rigid grid motion" implies relative motion of grid zones. However, no attempt is made in the :sidskey:`RigidGridMotion_t` data structure to require that the :sidskey:`ZoneGridConnectivity_t` information be updated to be consistent with the new grid locations.
Whether the :sidskey:`ZoneGridConnectivity_t` information refers to the original connectivity (of :sidskey:`GridCoordinates`) or the latest connectivity (of the moved or deformed grid) is currently left up to the user.


Arbitrary Grid Motion Structure Definition: ``ArbitraryGridMotion_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a grid is in motion, it is often necessary to account for the position of each grid point as the grid deforms.
When all grid points move at the same velocity, the grid keeps its original shape. This particular case of grid motion may be recorded under the :sidsref:`RigidGridMotion_t` data structure.
On the other hand, if the grid points have different velocity, the grid is deforming. The :sidskey:`ArbitraryGridMotion_t` data structure allows the CGNS file to contain information about arbitrary grid deformations.
If not present, the grid is assumed to be rigid.

Note that multiple :sidsref:`GridCoordinates_t` nodes may be stored under a :sidsref:`Zone_t`.
This allows the storage of the instantaneous grid locations at different time steps or iterations.

The arbitrary grid motion is recorded independently for each zone of the CGNS base.
Therefore the :sidskey:`ArbitraryGridMotion_t` data structure is located under the zone data structure (:sidsref:`Zone_t`).
There may be zero to several :sidskey:`ArbitraryGridMotion_t` nodes under a single :sidskey:`Zone_t` node.
The multiple arbitrary grid motion definitions may be associated with different iterations or time steps in the computation.
This association is recorded under the :sidsref:`ZoneIterativeData_t` data structure.

.. code-block:: sids

  ArbitraryGridMotion_t< int IndexDimension, int VertexSize[IndexDimension], 
                         int CellSize[IndexDimension] > :=
    {
    ArbitraryGridMotionType_t ArbitraryGridMotionType ;                (r)

    List(DataArray_t<real, IndexDimension, DataSize[]>
       GridVelocityX GridVelocityY ... ) ;                             (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridLocation_t GridLocation ;                                      (o/d)

    Rind_t<IndexDimension> Rind ;                                      (o/d)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    }

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ArbitraryGridMotion_t` and shall not include the names :sidskey:`ArbitraryGridMotionType`, :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`GridLocation`, or :sidskey:`Rind`.
    
    #. The only required element of the :sidskey:`ArbitraryGridMotion_t` data structure is the :sidskey:`ArbitraryGridMotionType`. Thus, even if a deforming grid application does not require the storage of grid velocity data, the :sidskey:`ArbitraryGridMotion_t` node must exist (with :sidskey:`ArbitraryGridMotionType = DeformingGrid`) to indicate that deformed grid points (:sidsref:`GridCoordinates_t`) exist for this zone.
    
    #. :sidsref:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points or elements (for unstructured grids) included in the grid velocity data.
    
    #. The :sidsref:`GridLocation` specifies the location of the velocity data with respect to the grid; if absent, the data is assumed to coincide with grid vertices (i.e., GridLocation = Vertex). 

:sidskey:`ArbitraryGridMotion_t` requires three structure parameters; :sidskey:`IndexDimension` identifies the dimensionality of the grid-size arrays, and :sidskey:`VertexSize` and :sidskey:`CellSize` are the number of core vertices and cells, respectively, in each index direction, excluding rind points.
For structured zones, core vertices and cells begin at :code:`[1,1,1]` (in 3-D) and end at :sidskey:`VertexSize` and :sidskey:`CellSize`, respectively.
For unstructured zones, :sidskey:`IndexDimension` is always 1.

:sidskey:`ArbitraryGridMotionType_t` is an enumeration type that describes the type of arbitrary grid motion.

.. code-block:: sids

  ArbitraryGridMotionType_t := Enumeration(
    ArbitraryGridMotionTypeNull,
    ArbitraryGridMotionTypeUserDefined,
    NonDeformingGrid,
    DeformingGrid ) ;

The :sidskey:`DataArray_t` nodes are used to store the components of the grid velocity vector.
The table below lists the data-name identifiers used to record these vectors in Cartesian, cylindrical, and spherical coordinate systems.

  
.. table:: **Data-Name Identifiers for Grid Velocity**

  +-------------------------------+--------------------------------------------+-------------------+
  | Data-Name Identifier          | Description	                               | Units             |
  +===============================+============================================+===================+
  | :sidskey:`GridVelocityX`      | :math:`x`-component of grid velocity       | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityY`      | :math:`y`-component of grid velocity       | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityZ`      | :math:`z`-component of grid velocity       | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityR`      | :math:`r`-component of grid velocity       | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityTheta`  | :math:`\theta`-component of grid velocity  | :math:`\alpha/T`  |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityPhi`    | :math:`\phi`-component of grid velocity    | :math:`\alpha/T`  |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityXi`     | :math:`\xi`-component of grid velocity     | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityEta`    | :math:`\eta`-component of grid velocity    | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+
  | :sidskey:`GridVelocityZeta`   | :math:`\zeta`-component of grid velocity   | :math:`L/T`       |
  +-------------------------------+--------------------------------------------+-------------------+

The field :sidsref:`GridLocation` specifies the location of the grid velocities with respect to the grid; if absent, the grid velocities are assumed to coincide with grid vertices (i.e., GridLocation = Vertex). All grid velocities within a given instance of :sidskey:`ArbitraryGridMotion_t` must reside at the same grid location.

:sidsref:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points or elements (for unstructured grids) included in the data. Its purpose and function are identical to those described for the :sidsref:`GridCoordinates_t` structure.
Note, however, that the Rind in this structure is independent of the :sidskey:`Rind` contained in :sidsref:`GridCoordinates_t` or :sidsref:`FlowSolution_t`.
They are not required to contain the same number of rind planes or elements. Also, the location of any rind points is assumed to be consistent with the location of the core data points (e.g., if :sidskey:`GridLocation = CellCenter`, rind points are assumed to be located at fictitious cell centers).

:sidsref:`DataClass` defines the default for the class of data contained in the :sidsref:`DataArray_t` entities. For dimensional grid velocities, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Point-by-point grid velocity implies a deformation (or potentially only motion) of the grid points relative to each other. Because the original grid coordinates definition remains unchanged with the name :sidsref:`GridCoordinates`, any deformed coordinates must be written with a different name (e.g., :sidskey:`MovedGrid#1` or another used-defined name) and are pointed to using :sidskey:`GridCoordinatesPointers` in the data structure :sidsref:`ZoneIterativeData_t`.

Point-by-point grid velocity may also lead to relative motion of grid zones, or movement of grid along abutting interfaces.
However, no attempt is made here to require that the :sidsref:`ZoneGridConnectivity_t` information be updated to be consistent with the new grid locations.
Whether the :sidskey:`ZoneGridConnectivity_t` information refers to the original connectivity (of :sidsref:`GridCoordinates`) or the latest connectivity (of the moved or deformed grid) is currently left up to the user.

.. c:function:: FUNCTION DataSize()

   :return value: one-dimensional ``int`` array of length :sidskey:`IndexDimension`
   :dependencies: :sidskey:`IndexDimension`, :sidskey:`VertexSize[]`, :sidskey:`CellSize[]`, :sidskey:`GridLocation`, :sidskey:`Rind`

   The function :sidskey:`DataSize[]` is the size of the DataArrays containing the grid velocity components. It is identical to the function :sidskey:`DataSize[]` defined for :sidsref:`FlowSolution_t`.

Zone Grid Connectivities
^^^^^^^^^^^^^^^^^^^^^^^^

Multiple :sidsref:`ZoneGridConnectivity_t` nodes may be used to specify time-dependent changes in the connectivity information associated with the zone.
The time variation is the recorded in the :sidsref:`ZoneIterativeData_t` node as :sidskey:`ZoneGridConnectivityPointers`.

Examples for Time-Dependent Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example - Rigid Grid Motion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, the whole mesh moves rigidly, so the only time-dependent data are the grid coordinates and flow solutions.
However, since the mesh moves rigidly, the grid coordinates need not be recorded at each time step.
Instead, a :sidsref:`RigidGridMotion_t` data structure is recorded for each step of the computation.

The number of steps and time values for each step are recorded under :sidsref:`BaseIterativeData_t`.

.. code-block:: sids

  CGNSBase_t {
    BaseIterativeData_t {
      NumberOfSteps = N ;
      TimeValues = time1, time2, ..., timeN ;
    } ;
  } ;

The multiple rigid grid motion and flow solution data structures are recorded under the zone. :sidskey:`RigidGridMotionPointers` and :sidskey:`FlowSolutionPointers` keep the lists of which :sidsref:`RigidGridMotion_t` and :sidsref:`FlowSolution_t` nodes correspond to each time step.

.. code-block:: sids

  Zone_t Zone {

    --- Time independent data
    GridCoordinates_t GridCoordinates
    ZoneBC_t ZoneBC
    ZoneGridConnectivity_t ZoneGridConnectivity

    --- Time dependent data
    RigidGridMotion_t RigidGridMotion#1
    RigidGridMotion_t RigidGridMotion#2
    ...
    RigidGridMotion_t RigidGridmotion#N

    FlowSolution_t Solution#0
    FlowSolution_t Solution#1
    FlowSolution_t Solution#2
    ...
    FlowSolution_t Solution#N

    ZoneIterativeData_t {
      RigidGridMotionPointers = {"RigidGridMotion#1", "RigidGridMotion#2", ...,
         "RigidGridMotion#N"}
      FlowSolutionPointers = {"Solution#1", "Solution#2", ..., "Solution#N"}
    }
  }

Note that there may be more solutions under a zone than those pointed to by :sidskey:`FlowSolutionPointers`. In this example, :sidskey:`Solution#0` could correspond to a restart solution.

Example - Deforming Grid Motion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, velocity vectors are node dependent allowing for mesh deformation. In such a case, it is difficult or even impossible to recompute the mesh at each time step.
Therefore the grid coordinates are recorded for each step.

Multiple :sidsref:`GridCoordinates_t` and :sidskey:`FlowSolution_t` data structures are recorded under the zone.
In addition, the data structure :sidsref:`ArbitraryGridMotion_t` is recorded for each step.
:sidskey:`GridCoordinatesPointers`, :sidskey:`FlowSolutionPointers`, and :sidskey:`ArbitraryGridMotionPointers_t` keep the list of which grid coordinates definition, flow solution, and arbitrary grid motion definition correspond to each time step.

.. code-block:: sids

  Zone_t Zone {

    --- Time independent data
    ZoneBC_t ZoneBC
    ZoneGridConnectivity_t ZoneGridConnectivity

    --- Time dependent data
    List ( GridCoordinates_t GridCoordinates MovedGrid#1 MovedGrid#2 ...
           MovedGrid#N )
    List ( FlowSolution_t Solution#0 Solution#1 Solution#2 ... Solution#N )
    List ( ArbitraryGridMotion_t ArbitraryGridMotion#1 
           ArbitraryGridMotion#2 ... ArbitraryGridMotion#N )
    ZoneIterativeData_t {
      GridCoordinatesPointers = {"MovedGrid#1", "MovedGrid#2", ...,
         "MovedGrid#N"}
      FlowSolutionPointers = {"Solution#1", "Solution#2", ..., "Solution#N"}
      ArbitraryGridMotionPointers = {"ArbitraryGridMotion#1",
         "ArbitraryGridMotion#2", ..., "ArbitraryGridMotion#N"}
    }
  }


Example - Adapted Unstructured Mesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, the mesh size varies at each remeshing, therefore new zones must be created. :sidskey:`ZonePointers` is used to keep a record of the zone definition corresponding to each recorded step.
Let's assume that the solution is recorded every 50 iterations, and the grid is adapted every 100 iterations.

The number of steps, iteration values for each step, number of zones for each step, and name of these zones are recorded under :sidsref:`BaseIterativeData_t`.

.. code-block:: sids

  CGNSBase_t {
    BaseIterativeData_t {
      NumberOfSteps = 4
      IterationValues = {50, 100, 150, 200}
      NumberOfZones = {1, 1, 1, 1}
      ZonePointers = {"Zone1", "Zone1", "Zone2", "Zone2"}
    }
  }

Each zone holds 2 solutions recorded at 50 iterations apart. Therefore the :sidsref:`ZoneIterativeData_t` data structure must be included to keep track of the :sidskey:`FlowSolutionPointers`.

.. code-block:: sids

  Zone_t Zone1 {

    --- Constant data
    GridCoordinates_t GridCoordinates
    Elements_t Elements
    ZoneBC_t ZoneBC

    --- Variable data
    List ( FlowSolution_t InitialSolution Solution50 Solution100 )
    ZoneIterativeData_t {
      FlowSolutionPointers = {"Solution50", "Solution100", "Null", "Null"}
    }
  }

  Zone_t Zone2 {

    --- Constant data
    GridCoordinates_t GridCoordinates
    Elements_t Elements
    ZoneBC_t ZoneBC

    --- Variable data
    List ( FlowSolution_t RestartSolution Solution150 Solution200 )
    ZoneIterativeData_t {
      FlowSolutionPointers = {"Null", "Null", "Solution150", "Solution200"}
    }
  }

.. note::

    #. If the solution was recorded every 100 iterations instead of every 50 iterations, then each zone would have only one :sidsref:`FlowSolution_t` node and the data structure :sidsref:`ZoneIterativeData_t` would not be required.

    #. Note that :sidskey:`FlowSolutionPointers` is always an array of size :sidskey:`NumberOfSteps` even if some of the steps are defined in another zone. 

Example - Combination of Grid Motion and Time-Accuracy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following is an example demonstrating the use of the rigid grid motion, arbitrary grid motion, and time-accurate data nodes in CGNS. The example is a 3-zone case. Zone 1 is rigidly rotating about the x-axis at a constant rate, with no translation. Zone 2 is a deforming zone. Zone 3 is a fixed zone. This is a time-accurate simulation with two solutions saved at times 15.5 and 31.0, corresponding to iteration numbers 1000 and 2000.

No units are given in this example, but a real case would establish them. Also, a real case would include connectivity, boundary conditions, and possibly other information as well. Each indentation represents a level down (a child) from the parent node.

.. code-block:: sids

  Base (CGNSBase_t)
    SimulationType (SimulationType_t) Data=TimeAccurate
    BaseIterativeData (BaseIterativeData_t) Data=NumberOfSteps=2
      TimeValues (DataArray_t) Data=(15.5, 31.0)
      IterationValues (DataArray_t) Data=(1000, 2000)
    Zone#1 (Zone_t)
      GridCoordinates (GridCoordinates_t)
        CoordinateX (DataArray_t)
        CoordinateY (DataArray_t)
      RigidGridMotion#1(RigidGridMotion_t) Data=RigidGridMotionType=ConstantRate
        OriginLocation (DataArray_t) Data=(0,0,0), (0,0,0)
        RigidRotationAngle (DataArray_t) Data=(5., 0., 0.)
      RigidGridMotion#2(RigidGridMotion_t) Data=RigidGridMotionType=ConstantRate
        OriginLocation (DataArray_t) Data=(0,0,0), (0,0,0)
        RigidRotationAngle (DataArray_t) Data=(10., 0., 0.)
      ZoneIterativeData (ZoneIterativeData_t)
        RigidGridMotionPointers (DataArray_t) Data=(RigidGridMotion#1,
                                                    RigidGridMotion#2)
        FlowSolutionPointers (DataArray_t) Data=(Soln#1, Soln#2)
      Soln#1 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)
      Soln#2 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)
    Zone#2 (Zone_t)
      GridCoordinates (GridCoordinates_t)
        CoordinateX (DataArray_t)
        CoordinateY (DataArray_t)
      MovedGrid#1 (GridCoordinates_t)
        CoordinateX (DataArray_t)
        CoordinateY (DataArray_t)
      MovedGrid#2 (GridCoordinates_t)
        CoordinateX (DataArray_t)
        CoordinateY (DataArray_t)
      ArbitraryGridMotion#1 (ArbitraryGridMotion_t)
                             Data=ArbitraryGridMotionType=DeformingGrid
      ArbitraryGridMotion#2 (ArbitraryGridMotion_t)
                             Data=ArbitraryGridMotionType=DeformingGrid
        GridVelocityX (DataArray_t)
        GridVelocityY (DataArray_t)
      ZoneIterativeData (ZoneIterativeData_t)
        ArbitraryGridMotionPointers (DataArray_t) Data=("ArbitraryGridMotion#1",
                                                        "ArbitraryGridMotion#2")
        GridCoordinatesPointers (DataArray_t) Data=("MovedGrid#1",
                                                    "MovedGrid#2")
        FlowSolutionPointers (DataArray_t) Data=("Soln#1", "Soln#2")
      Soln#1 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)
      Soln#2 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)
    Zone#3 (Zone_t)
      GridCoordinates (GridCoordinates_t)
        CoordinateX (DataArray_t)
        CoordinateY (DataArray_t)
      ZoneIterativeData (ZoneIterativeData_t)
        FlowSolutionPointers (DataArray_t) Data=("Soln#1", "Soln#2")
      Soln#1 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)
      Soln#2 (FlowSolution_t)
        Density (DataArray_t)
        VelocityX (DataArray_t)

.. note::

    #. Under :sidsref:`BaseIterativeData_t`, one can give either :sidskey:`TimeValues`, or :sidskey:`IterationValues`, or both. In the example, both have been given.
    #. The nodes :sidskey:`NumberOfZones` and :sidskey:`ZonePointers` are not required under the :sidsref:`BaseIterativeData_t` node in this example because all existing zones are used for each time step.
    #. Under :sidsref:`ArbitraryGridMotion`, the :sidskey:`GridVelocity` data is optional. In the example, it was put under one of the nodes but not under the other. Hence, ":sidskey:`ArbitraryGridMotion#1`" in the example has no children nodes, while ":sidskey:`ArbitraryGridMotion#2`" does.
    #. The pointers under :sidsref:`ZoneIterativeData_t` point to names of nodes within the same zone. Thus, for example, :sidskey:`Soln#1` refers to the flow solution named :sidskey:`Soln#1` in the same zone, even though there are flow solution nodes in other zones with the same name.
    #. The name :sidskey:`GridCoordinates` always refers to the original grid. Thus, when a grid is deforming, the deformed values must be put in :sidsref:`GridCoordinates_t` nodes of a different name. In the example, the deformed grids (for :sidskey:`Zone#2`) at the two times of interest were put into ":sidskey:`MovedGrid#1`" and ":sidskey:`MovedGrid#2`".
    #. Because the node ":sidskey:`ArbitraryGridMotion#1`" doesn't really add any information in the current example (since it was decided not to store :sidskey:`GridVelocity` data under it), one has the option of not including this node in the CGNS file. If it is removed, then under :sidskey:`Zone#2`'s :sidsref:`ZoneIterativeData`, the :sidskey:`ArbitraryGridMotionPointers` data would be replaced by:
     
       .. code-block:: sids
        
         Data = (Null, ArbitraryGridMotion#2)

.. last line
