
.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)



Particle Data
-------------

This section defines structure types for describing the particle data.

Particle Zone Structure Definition: :sidskey:`ParticleZone_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidskey:`ParticleZone_t` structure contains all information pertinent to an individual set of particles.

.. code-block:: sids

 ParticleZone_t< PhysicalDimension > :=
   {

   int ParticleSize ;                                                 (r)

   List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

   List( ParticleCoordinate<ParticleSize>
         ParticleCoordinates MovedParticles1 ... MovedParticlesN ) ;  (o)

   FamilyName_t FamilyName ;                                          (o)

   List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ; (o)

   List( ParticleSolution_t<ParticleSize>
         ParticleSolution1 ... ParticleSolutionN ) ;                  (o)

   List( IntegralData_t IntegralData1 ... IntegralDataN ) ;           (o)

   ParticleIterativeData_t<NumberOfSteps> ParticleIterativeData ;     (o)

   ReferenceState_t ReferenceState ;                                  (o)

   DataClass_t DataClass ;                                            (o)

   DimensionalUnits_t DimensionalUnits ;                              (o)

   ParticleEquationSet_t ParticleEquationSet ;                        (o)

   List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
   } ;


.. note::

   1. Default names for the :sidskey:`Descriptor_t`, :sidskey:`ParticleCoordinates_t`, :sidskey:`ParticleSolution_t`, :sidskey:`IntegralData_t`, and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleZone_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FamilyName`, :sidskey:`FlowEquationSet`, :sidskey:`ParticleCoordinates`, :sidskey:`ParticleSolution`, :sidskey:`ParticleIterativeData`, and :sidskey:`ReferenceState`.
   2. The original particle coordinates should have the name :sidskey:`ParticleCoordinates`. Default names for the remaining entities in the :sidskey:`ParticleCoordinates_t` list are as shown; users may choose other legitimate names, subject to, the restrictions listed in the previous note.
   3. There may be multiple :sidskey:`ParticleZone_t` per base. This allows users to create different groups of particles. :sidskey:`FamilyName_t` and :sidskey:`AdditionalFamilyName_t` nodes can be used to discern each :sidskey:`ParticleZone_t` node.
   4. :sidskey:`ParticleSize` is the only required field within the :sidskey:`ParticleZone_t` structure.

:sidskey:`ParticleZone_t` requires the parameter :sidskey:`PhysicalDimension`. :sidskey:`ParticleSize` corresponds to the number of particles in the :sidskey:`ParticleZone_t`. :sidskey:`ParticleSize` identifies the size of the particle-size arrays and is passed on to the particle coordinates and particle solution.

The :sidskey:`ParticleCoordinates_t` structure contains the physical coordinates of the center of each particle in the :sidskey:`ParticleZone_t`. The original particle coordinates are contained in :sidskey:`ParticleCoordinates`. Additional :sidskey:`ParticleCoordinates_t` data structures are allowed, to store particles at multiple time steps or iterations.

:sidskey:`FamilyName` identifies to which family particles belongs. Where multiple families are desired, :sidskey:`AdditionalFamilyName` nodes may be used to specify them. Both :sidskey:`FamilyName` and :sidskey:`AdditionalFamilyName` should refer to a :sidskey:`CGNSBase_t` level :sidskey:`Family_t`, in the parent base of the :sidskey:`ParticleZone_t` or in another sibling base (see :ref:`Base Level Families`).

Particle-solution quantities are contained in the list of :sidskey:`ParticleSolution_t` structures.
Multiple :sidskey:`ParticleSolution_t` structures can be provided to store
particle-solution data at multiple time steps or iterations.

Miscellaneous :sidsref:`ParticleZone_t`-specific global data is contained
in the list of :sidsref:`IntegralData_t` structures.

The particle-based :sidsref:`DataArray_t` vectors in :sidsref:`ParticleSolution_t` can correspond to a subset of particles defined in :sidsref:`ParticleCoordinates_t` through the use of a :sidsref:`PointRange` or :sidsref:`PointList`. Unless a :sidsref:`PointList` is defined, particle-based :sidsref:`DataArray_t` vectors in :sidsref:`ParticleSolution_t` must use the same ordering as those defined in :sidsref:`ParticleCoordinates_t`.

The :sidsref:`ParticleIterativeData_t` data structure may be used to record pointers to particle data at multiple time steps or iterations.

Reference-state data specific to an individual zone is contained in the :sidsref:`ReferenceState` structure.

:sidsref:`DataClass` defines the particle default for the class of data contained in the :sidsref:`ParticleZone_t` and its substructures. If a :sidsref:`ParticleZone_t` contains dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. :sidsref:`ReferenceState`, and :sidsref:`ParticleEquationSet` have special function in the hierarchy. They are applicable throughout a given particle zone, but their precedence may be superseded by local entities contained in the particle zone's substructures. If any of these entities are present within a given instance of :sidsref:`ParticleZone_t`, they take precedence over the corresponding global entities contained in database's :sidsref:`CGNSBase_t` entity. These precedence rules are further discussed in the section on :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`.

:sidsref:`DataClass` and :sidsref:`DimensionalUnits` have special function in the hierarchy. They are applicable throughout a given :sidsref:`ParticleZone_t`, but their precedence may be superseded by local entities contained in the :sidsref:`ParticleZone_t`'s substructures. If any of these entities are present within a given instance of :sidsref:`ParticleZone_t`, they take precedence over the corresponding global entities contained in the database's :sidsref:`ParticleZone_t` or :sidsref:`CGNSBase_t` entity. These precedence rules are further discussed in the section on :ref:`Precedence Rules and Scope Within the Hierarchy<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidsref:`Descriptor_t` and :sidsref:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Particle Coordinates Structure Definition: :sidskey:`ParticleCoordinates_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The physical coordinates of the particle centers are described by the
:sidsref:`ParticleCoordinates_t` structure. This structure contains a list for the data arrays of the individual components of the position vector.

.. code-block:: sids

  ParticleCoordinates_t< int ParticleSize, int PhysicalDimension> :=
    {
    DataArray_t<DataType,PhysicalDimension, 2> BoundingBox ;           (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( DataArray_t<DataType, ParticleSize>
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;


.. note::

   1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleCoordinates_t` and shall not include the names :sidskey:`DataClass`, or :sidskey:`DimensionalUnits`.
   2. There are no required fields for :sidsref:`ParticleCoordinates_t`.
   3. The structure parameter :sidsref:`DataType` must be consistent with the data stored in the :sidsref:`DataArray_t` substructures.

:sidskey:`ParticleCoordinates_t` requires one structure parameters:  :sidskey:`ParticleSize`, which is the number of particles in the :sidsref:`ParticleZone_t` node.

The particle coordinates data is stored in the list of :sidsref:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity may contain a single component of the position vector (e.g., three separate :sidskey:`DataArray_t` entities are used for x, y, and z).

Standardized data-name identifiers for the particle coordinates are
described in :ref:`Conventions for Data-Name Identifiers<convention>`.

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional grid coordinates, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules<precedence>`. An example that uses these particle-coordinate defaults is shown under :ref:`Particle Coordinates Examples<particleCoordinatesExample>`.


.. _ParticleCoordinatesexample:

Example - Particle Coordinates for a 3-D Case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example show how to set the particle coordinates in the case where :sidskey:`ParticleSize` is 15.

.. code-block:: sids

  !  ParticleSize = 15
  ParticleCoordinates_t<15> ParticleCoordinates =
    {{

    ! DataType = real
    ! ParticleSize = 15
    DataArray_t<real, 1, 15> CoordinateX =
      {{
      Data(real, 1, 15) = (x(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> CoordinateY =
      {{
      Data(real, 1, 15) = (y(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> CoordinateZ =
      {{
      Data(real, 1, 15) = (z(i), i=1,15) ;
      }} ;
    }} ;


.. _ParticleSolution:

Particle Solution Structure Definition: :sidskey:`ParticleSolution_t` 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The solution on each particle within a given :sidskey:`ParticleZone_t` is described by the
:sidskey:`ParticleSolution_t` structure.
This structure contains a list for the data arrays of the individual
solution variables. Particle solutions are implicitly defined at particle centers,
and correspond to the solution for the entire particle.

.. code-block:: sids

  ParticleSolution_t< int ParticleSize> :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    IndexRange PointRange ;                                            (o)
    IndexArray<DataSize[], int> PointList ;                            (o)

    List( DataArray_t<DataType, DataSize[]>
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleSolution_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`PointList` or :sidskey:`PointRange`.
   2. There are no required fields for :sidskey:`ParticleSolution_t`.
   3. Both of the fields :sidskey:`PointList` and :sidskey:`PointRange` are optional. Only one of these two fields may be specified.
   4. The structure parameter :sidskey:`DataType` must be consistent with the data stored in the :sidsref:`DataArray_t` structure entities; :sidskey:`DataType` is :sidskey:`real` for all particle-solution identifiers defined in the section :ref:`Conventions for Data-Name Identifiers<dataname>`.
   5. Indexing of data within the :sidsref:`DataArray_t` structure must be consistent with coordinates defined in the :sidsref:`ParticleCoordinates_t`.

The particle solution data is stored in the list of :sidsref:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity may contain a single component of the solution vector. Standardized data-name identifiers for the particle-solution quantities are described in the section :ref:`Conventions for Data-Name Identifiers<dataname>`.

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional particle solution data, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. _DataSizeParticle:

.. c:function:: FUNCTION DataSize()

   :return value: ``int``
   :dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`ParticleSolution_t` requires the structure function :sidskey:`DataSize`, which is used to specify the number of entities corresponding to a given :sidskey:`PointRange` or :sidskey:`PointList`. This will therefore be the size of the :sidskey:`ParticleSolution` data arrays. If :sidskey:`PointRange` is specified, then :sidskey:`DataSize` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`. If :sidskey:`PointList` is specified, then :sidskey:`DataSize` is the number of indices in the list of points. In this situation, :sidskey:`DataSize` becomes a user input along with the indices of the list :sidskey:`PointList`. By "user", we mean the application code that is generating the CGNS database.

.. _ParticleSolutionExample:

Example - Particle Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sids

  ParticleSolution_t<15> ParticleSolution =
    {{

    ! DataType = real
    ! ParticleSize = 15

    DataArray_t<real, 1, 15> Radius =
      {{
      Data(real, 1, 15) = (r(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> Temperature =
      {{
      Data(real, 1, 15) = (T(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> VelocityX =
      {{
      Data(real, 1, 15) = (u(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> VelocityY =
      {{
      Data(real, 1, 15) = (v(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> VelocityZ =
      {{
      Data(real, 1, 15) = (z(i), i=1,15) ;
      }} ;
    }} ;


.. _ParticleEquationSet:

Particle Equation Set Structure Definition: :sidskey:`ParticleEquationSet_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ParticleEquationSet_t` is a general description of the governing particle equations. It includes the dimensionality of the governing equations, and the collection of specific equation-set descriptions covered in subsequent sections. It can be a child node of :sidsref:`CGNSBase_t` or :sidsref:`ParticleZone_t` (or both).

.. code-block:: sids

  ParticleEquationSet_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    int EquationDimension ;                                            (o)

    ParticleGoverningEquations_t; ParticleGoverningEquations ;         (o)

    ParticleCollisionModel_t ParticleCollisionModel ;                  (o)

    ParticleBreakupModel_t ParticleBreakupModel ;                      (o)

    ParticleForceModel_t ParticleForceModel ;                          (o)

    ParticleWallInteractionModel_t ParticleWallInteractionModel ;      (o)

    ParticlePhaseChangeModel_t ParticlePhaseChangeModel ;              (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   1. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleEquationSet_t` and shall not include the names :sidskey:`ParticleGoverningEquations`, :sidskey:`ParticleCollisionModel`, :sidskey:`ParticleBreakupModel`, :sidskey:`ParticleForceModel`, :sidskey:`ParticleWallInteractionModel_t`, :sidskey:`ParticlePhaseChangeModel`, :sidskey:`DataClass`, or :sidskey:`DimensionalUnits`.
   2. There are no required elements for :sidskey:`ParticleEquationSet_t`.

:sidskey:`EquationDimension` is the dimensionality of the governing equations; it is the number of spatial variables describing the flow.

:sidsref:`DataClass` defines the default for the class of data contained in the flow-equation set. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. _ParticleGoverningEquations:

Governing Equations Structure Definition: :sidskey:`ParticleGoverningEquations_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleGoverningEquations_t` describes the class of governing equations associated with particles.


.. code-block:: sids

  ParticleGoverningEquationsType_t := Enumeration(
    ParticleGovEqTypeNull,
    ParticleGovEqTypeUserDefined,
    DEM,
    DSMC,
    SPH) ;

  ParticleGoverningEquations_t; :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ParticleGoverningEquationsType_t ParticleGoverningEquationsType ;  (r)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   1. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleGoverningEquations_t`.
   2. :sidskey:`ParticleGoverningEquationsType` is the only required element.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. _ParticleModelType:

Particle Model Type Structure Definition: :sidskey:`ParticleModelType_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleModelType_t` is a complete list of all models covered in subsequent sections. A specific model will contain a subset of this enumeration.

.. code-block:: sids

  ParticleModelType_t := Enumeration(
    Linear, NonLinear, HardSphere, SoftSphere, LinearSpringDashpot,
    Pair, BaiGosman, HertzMindlin, HertzKuwabaraKono, Kuhnke, ORourke, Wruck,
    Stochastic, NonStochastic, NTC, KelvinHelmholtz,
    KelvinHelmholtzACT, RayleighTaylor,
    KelvinHelmholtzRayleighTaylor,
    ReitzKHRT,
    TAB, ETAB, LISA, SHF, PilchErdman, ReitzDiwakar,
    Sphere, NonShpere, Tracer, BeetstraVanDerHoefKuipers,
    Ergun, CliftGrace, Gidaspow, HaiderLevenspiel, PlessisMasliyah,
    SyamlalOBrien, SaffmanMei, TennetiGargSubramaniam,
    Tomiyama, Stokes, StokesCunningham, WenYu,
    Boil, Condense, Flash, Nucleate, Chiang, Frossling, FuchsKnudsen) ;

.. _ParticleCollisionModel:

Particle Collision Model Structure Definition: :sidskey:`ParticleCollisionModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleCollisionModel_t` describes the collision model used for particle-particle interactions. The enumerated values for :sidskey:`ParticleCollisionModelType_t` are a subset of the :sidskey:`ParticleModelType_t` enumeration.

.. code-block:: sids

  ParticleCollisionModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Linear,
    NonLinear,
    HardSphere,
    SoftSphere,
    LinearSpringDashpot,
    Pair,
    HertzMindlin,
    HertzKuwabaraKono,
    ORourke,
    Stochastic,
    NonStochastic,
    NTC) ;

  ParticleCollisionModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ParticleCollisionModelType_t ParticleCollisionModelType ;          (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  1. Default names for the ":sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleCollisionModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  2. :sidskey:`ParticleCollisionModelType` is the only required element.

For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`ParticleCollisionModelType` names currently listed correspond to the following particular references.

.. table::

   ============================== =========================================================================================================================================================================================================
   :sidskey:`ORourke`             O’Rourke, P. J ., "Collective Drop Effects on Vaporizing Liquid Sprays," Ph.D. Thesis, Princeton University, Princeton, N J , United States, 1981.
   :sidskey:`NTC`                 Schmidt, D.P. and Rutland, C. J ., "A New Droplet Collision Algorithm," Journal of Computational Physics , 164 ( 1 ), 62 - 80 , 2000. DOI: 10.1006/jcph.2000.6568
   :sidskey:`HertzKuwabaraKono`   Goro Kuwabara and Kimitoshi Kono 1987 Jpn. J. Appl. Phys. 26 1230
   :sidskey:`HertzMindlin`        Tsuji Y.  et al. (1992) Lagrangian numerical simulation of plug flow of cohesionless particles in a horizontal pipe. Powder Technology, 71(3): p. 239-250. http://dx.doi.org/10.1016/0032-5910(92)88030-L
   ============================== =========================================================================================================================================================================================================

.. _ParticleBreakupModel:

Particle Breakup Model Structure Definition: :sidskey:`ParticleBreakupModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleBreakupModel_t` describes the model used for particle breakup. The enumerated values for :sidskey:`ParticleBreakupModelType_t` are a subset of the :sidskey:`ParticleModelType_t` enumeration.

.. code-block:: sids

  ParticleBreakupModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    KelvinHelmholtz,
    KelvinHelmholtzACT,
    RayleighTaylor,
    KelvinHelmholtzRayleighTaylor,
    ReitzKHRT,
    TAB,
    ETAB,
    LISA,
    SHF,
    PilchErdman,
    ReitzDiwakar) ;

  ParticleBreakupModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ParticleBreakupModelType_t ParticleBreakupModelType ;              (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleBreakupModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  2. :sidskey:`ParticleBreakupModelType` is the only required element.

For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`ParticleBreakupModelType` names currently listed correspond to the following particular references.


.. table::

   ============================== ==============================================================================================================================================================================================================================================================================================================
   :sidskey:`KelvinHelmholtz`     Reitz, R.D. and Bracco, F.V., "Mechanisms of Breakup of Round Liquid Jets," Encyclopedia of Fluid Mechanics, Gulf Publishing Company, 1986.
   .. codespell:ignore Som
   :sidskey:`KelvinHelmholtzACT`  Som, S. and Aggarwal, S.K., "Effects of Primary Breakup Modeling on Spray and Combustion Characteristics of Compression Ignition Engines", Combustion and Flame, 157(6), 1179-1193, 2010. DOI: 10.1016/j.combustflame.2010.02.018
   .. codespell:ignore Som
   :sidsref:`RayleighTaylor`      Senecal, P.K., Richards, K.J., Pomraning, E., Yang, T., Dai, M.Z., McDavid, R.M., Patterson, M.A., Hou, S., and Shethaji, T., "A New Parallel Cut-Cell Cartesian CFD Code for Rapid Grid Generation Applied to In-Cylinder Diesel Engine Simulations," SAE Paper 2007-01-0159, 2007. DOI: 10.4271/2007-01-0159
   :sidsref:`TAB`                 O’Rourke, P.J. and Amsden, A.A., "The TAB Method for Numerical Calculation of Spray Droplet Breakup," SAE Paper 872089, 1987. DOI: 10.4271/872089.
   :sidskey:`ETAB`                F.X. Tanner "Liquid Jet Atomization and Droplet Breakup Modeling of Non-Evaporating Diesel Fuel Sprays" SAE 970050, SAE Transactions: Journal of Engines, Vol 106, Sec 3 pp 127-140
   :sidskey:`LISA`                Senecal, P.K., Schmidt, D.P., Nouar, I., Rutland, C.J., Reitz, R.D., and Corradini, M.L., "Modeling High-Speed Viscous Liquid Sheet Atomization," International Journal of Multiphase Flow, 25(6-7), 1073-1097, 1999. DOI: 10.1016/S0301-9322(99)00057-9
   :sidskey:`SHF`                 R. Schmehl, G. Maier, S. Witting "CFD Analysis of Fuel Atomization, Secondary Droplet Breakup and Spray Dispersion in the Premix Duct of a LPP Combustor". Eight International Conference on Liquid Atomization and Spray Systems, 2000
   :sidskey:`PilchErdman`         Pilch, M., & Erdman, C. A. (1987). Use of breakup time data and velocity history data to predict the maximum size of stable fragments for acceleration-induced breakup of a liquid drop. International journal of multiphase flow, 13(6), 741-757. DOI:10.1016/0301-9322(87)90063-2
   :sidskey:`ReitzDiwakar`        Reitz, R.D. and Diwakar, R. "Effect of drop breakup on fuel sprays" SAE Tech. paper series, 860469 (1986)
   ============================== ==============================================================================================================================================================================================================================================================================================================

.. _ParticleForceModel: 

Particle Force Model Structure Definition: :sidskey:`ParticleForceModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleForceModel_t` describes the model used for for forces, typically lift and drag, applied on particle. The enumerated values for :sidskey:`ParticleForceModelType_t` are a subset of the :sidskey:`ParticleModelType_t` enumeration.

.. code-block:: sids

  ParticleForceModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Sphere,
    NonSphere,
    Tracer,
    BeetstraVanDerHoefKuipers,
    Ergun,
    CliftGrace,
    Gidaspow,
    HaiderLevenspiel,
    PlessisMasliyah,
    SyamlalOBrien,
    SaffmanMei,
    TennetiGargSubramaniam,
    Tomiyama,
    Stokes,
    StokesCunningham,
    WenYu) ;

  ParticleForceModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ParticleForceModelType_t ParticleForceModelType ;                  (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance      of :sidskey:`ParticleForceModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  2. :sidskey:`ParticleForceModelType` is the only required element.

For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`ParticleForceModelType` names currently listed correspond to the following particular references.

.. table::

   =========================== ========================================================================================================================================================================================================================================
   :sidskey:`Ergun`            Gidaspow, D. (1994). Multiphase flow and fluidization: continuum and kinetic theory descriptions. Academic press.
   :sidskey:`PlessisMasliyah`  Du Plessis, J. P. (1994). Analytical quantification of coefficients in the Ergun equation for fluid friction in a packed bed. Transport in porous media, 16(2), 189-207. DOI:10.1007/BF00617551
   :sidskey:`WenYu`            Wen, C. Y., & Yu, Y. H., (1966). Mechanics of fluidization. Chemical Engineering Progress Symposium Series. 62, 100-111.
   :sidskey:`CliftGrace`       Clift, R., Grace, J.R., and Weber, M.E., Bubbles, Drops,  and Particles, Academic Press, NewYork, 1978.
   :sidskey:`HaiderLevenspiel` Haider, A. and Levenspiel, O., "Drag Coefficient and Terminal Velocity of Spherical and Non-Spherical Particles," Powder Technology 58(1), 63-70, 1989.
   :sidskey:`SaffmanMei`       Koohandaz, A., Khavasi, E., Eyvazian, A., and Yousefi, H., "Prediction of particles deposition in a dilute quasi-steady gravity current by Lagrangian markers: Effect of shear-induced lift force," Scientific Reports, 10, 16673, 2020.
   =========================== ========================================================================================================================================================================================================================================

.. _ParticleWallInteractionModel:

Particle Wall Interaction Model Structure Definition: :sidskey:`ParticleWallInteractionModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticleWallInteractionModel_t` describes the model used for particle-wall interactions, including splash models. The enumerated values for :sidskey:`ParticleWallInteractionModelType_t` are a subset of the :sidskey:`ParticleModelType_t` enumeration.

.. code-block:: sids

  ParticleWallInteractionModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Linear,
    NonLinear,
    HardSphere,
    SoftSphere,
    LinearSpringDashpot,
    BaiGosman,
    HertzMindlin,
    HertzKuwabaraKono,
    Kuhnke,
    ORourke,
    Wruck,
    NTC) ;

  ParticleWallInteractionModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                    (o)

    ParticleWallInteractionModelType_t ParticleWallInteractionModelType ; (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;       (o)

    DataClass_t DataClass ;                                               (o)

    DimensionalUnits_t DimensionalUnits ;                                 (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;     (o)
    } ;

.. note::

  1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleWallInteractionModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  2. :sidskey:`ParticleWallInteractionModelType` is the only required element.

For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`ParticleWallInteractionModelType` names currently listed correspond to the following particular references.

.. table::

   ============================= =========================================================================================================================================================================================================
   :sidskey:`ORourke`            O’Rourke, P. J ., "Collective Drop Effects on Vaporizing Liquid Sprays," Ph.D. Thesis, Princeton University, Princeton, N J , United States, 1981.
   :sidskey:`Kuhnke`             Kuhnke, D., "Spray/Wall-interaction Modelling by Dimensionless Data Analysis," Ph.D. Thesis, Shaker Verlag, 2004, ISBN 3-8322-3539.
   :sidskey:`NTC`                Schmidt, D.P. and Rutland, C. J ., "A New Droplet Collision Algorithm," Journal of Computational Physics , 164 ( 1 ), 62 - 80 , 2000. DOI: 10.1006/jcph.2000.6568
   :sidskey:`BaiGosman`          Bai, C. and Gosman, A. "Development of Methodology for Spray Impingement Simulation," SAE Paper 950283, 1995. DOI: 10.4271/950283
   :sidskey:`HertzKuwabaraKono`  Goro Kuwabara and Kimitoshi Kono 1987 Jpn. J. Appl. Phys. 26 1230
   :sidskey:`HertzMindlin`       Tsuji Y.  et al. (1992) Lagrangian numerical simulation of plug flow of cohesionless particles in a horizontal pipe. Powder Technology, 71(3): p. 239-250. http://dx.doi.org/10.1016/0032-5910(92)88030-L
   :sidskey:`Wruck`              Wruck, N.M. and Renz, U., "Transient Phase-Change of Droplets Impacting on a Hot Wall,"Wiley-VCH Verlag GmbH, ISBN 978-3-527-27149-8.
   ============================= =========================================================================================================================================================================================================

.. _ParticlePhaseChangeModel:

Particle Phase Change Model Structure Definition: :sidskey:`ParticlePhaseChangeModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ParticlePhaseChangeModel_t` describes the model used for particle phase change, typically evaporation and condensation. The enumerated values for :sidskey:`ParticlePhaseChangeModelType_t` are a subset of the :sidskey:`ParticleModelType_t` enumeration.

.. code-block:: sids

  ParticlePhaseChangeModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Boil,
    Condense,
    Flash,
    Nucleate,
    Chiang,
    Frossling,
    FuchsKnudsen) ;

  ParticlePhaseChangeModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ParticlePhaseChangeModelType_t ParticlePhaseChangeModelType ;      (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticlePhaseChangeModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  2. :sidskey:`ParticlePhaseChangeModelType` is the only required element.

For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`ParticlePhaseChangeModelType` names currently listed correspond to the following particular references. 


.. table::

   ==================== ==================================================================================================================================================================================================================================================
   :sidskey:`Frossling` Amsden, A.A., O’Rourke, P.J ., and Butler, T.D., "KIVA-II: A Computer Program for Chemically Reactive Flows with Sprays," Los Alamos National Laboratory Technical Report LA-11560-MS, 1989.
   :sidskey:`Chiang`    Chiang, C.H., Raju, M.S., and Sirignano, W.A., "Numerical Analysis of a Convecting, Vaporizing Fuel Droplet with Variable Properties," International Journal of Heat and Mass Transfer, 35( 5), 1307-1324, 1992. DOI: 10.1016/0017-9310(92)90186-V
   :sidskey:`Flash`     Price, C., Hamzehloo, A., Aleiferis, P., and Richardson, R., "An Approach to Modeling Flash-Boiling Fuel Sprays for Direct-Injection Spark-Ignition Engines," Atomization and Sprays, 26(12), 1197-1239, 2016. DOI: 10.1615/AtomizSpr.2016015807
   :sidskey:`Condense`  Kryukov, A.P., Levashov, V.Yu., and Sazhin, S.S., "Evaporation of diesel fuel droplets: kinetic versus hydrodynamic models," International Journal of Heat and Mass Transfer 47, 2541-2549, 2004.
   :sidskey:`Nucleate`  Liu, X. and Cheng, P., "Dropwise condensation theory revisited Part II: Droplet nucleation density and condensation heat flux," International Journal of Heat and Mass Transfer, 83, 842-849, 2015.
   ==================== ==================================================================================================================================================================================================================================================

