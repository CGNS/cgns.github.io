.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLGeneral:
   
General Remarks
---------------

The CGNS Mid-Level Library may be downloaded from the `CGNS site <https://github.com/CGNS/CGNS>`_.

Organization of the MLL documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The sections that follow describe the Mid-Level Library functions in detail.
The first three sections cover some basic file operations (i.e., opening and closing a CGNS file, and some configuration options), accessing a specific node in a CGNS database, and error handling.
The remaining sections describe the functions used to read, write, and modify nodes and data in a CGNS database. These sections basically follow the organization used in the "Detailed CGNS Node Descriptions" section of the SIDS File Mapping manual.

At the start of each sub-section is a Node line, listing the the applicable CGNS node label, with links to that node's description in the :ref:`SIDS<CGNS-SIDS>` and :ref:`SIDS File Mapping <StandardFMM>` manuals.

Syntax
^^^^^^

Next is a table illustrating the syntax for the Mid-Level Library functions.
The C functions are shown in the top half of the table, followed by the corresponding Fortran routines in the bottom half of the table.
Fortran subroutines identified in green indicates APIs which do not have explicit interfaces.
Input variables are shown in an :in:`upright blue` font, and output variables are shown in a :out:`slanted red` font.
For each function, the right-hand column lists the modes (read, write, and/or modify) applicable to that function.

The input and output variables are then listed and defined.

Language
^^^^^^^^

The CGNS Mid-Level Library is written in C, but each function has a Fortran counterpart.
All function names start with ``"cg_"``.
The Fortran functions have the same name as their C counterpart with the addition of the suffix ``"_f"``.

Character Strings
^^^^^^^^^^^^^^^^^
All data structure names and labels in CGNS are limited to 32 characters.
When reading a file, it is advised to pre-allocate the character string variables to 32 characters in Fortran, and 33 in C (to include the string terminator).
Other character strings, such as the CGNS file name or descriptor text, are unlimited in length.
The space for unlimited length character strings will be created by the Mid-Level Library; it is then the responsibility of the application to release this space by a call to :c:func:`cg_free`.

Error Status
^^^^^^^^^^^^
All C functions return an integer value representing the error status.
All Fortran functions have an additional parameter, :code:`ier`, which contains the value of the error status.
An error status different from zero implies that an error occured. The error message can be printed using the error handling functions of the CGNS library.
The error codes are coded in the C and Fortran include files *cgnslib.h* and *cgnslib_f.h*. 


Typedefs
^^^^^^^^

Several types of variables are defined using typedefs in the *cgnslib.h* file.
These are intended to facilitate the implementation of CGNS in C.
These variable types are defined as an enumeration of key words admissible for any variable of these types.
The file *cgnslib.h* must be included in any C application programs which use these data types.

.. warning::

  The :code:`cgsize_t` typedef  will be either a 32-bit or 64-bit integer depending on how the library was built.
  Many of the C functions in the MLL use :code:`cgsize_t` instead of :code:`int` in the arguments to cope with 32/64-bit support.
  These functions include any that may exceed the 2Gb limit of an int, e.g. zone dimensions, element data, boundary conditions, and connectivity.
  The :code:`cglong_t` typedef is always a 64-bit integer.

The list of enumerated values (key words) for each of these variable types (typedefs) are:

.. list-table::
  :widths: 20 80

  * - ZoneType_t
    - ZoneTypeNull, ZoneTypeUserDefined, Structured, Unstructured
  * - ElementType_t
    - ElementTypeNull, ElementTypeUserDefined, NODE, BAR_2, BAR_3, TRI_3, TRI_6, QUAD_4, QUAD_8, QUAD_9, TETRA_4, TETRA_10, PYRA_5, PYRA_14, PENTA_6, PENTA_15, PENTA_18, HEXA_8, HEXA_20, HEXA_27, MIXED, PYRA_13, NGON_n, NFACE_n, BAR_4, TRI_9, TRI_10, QUAD_12, QUAD_16, TETRA_16, TETRA_20, PYRA_21, PYRA_29, PYRA_30, PENTA_24, PENTA_38, PENTA_40, HEXA_32, HEXA_56, HEXA_64, BAR_5, TRI_12, TRI_15, QUAD_P4_16, QUAD_25, TETRA_22, TETRA_34, TETRA_35, PYRA_P4_29, PYRA_50, PYRA_55, PENTA_33, PENTA_66, PENTA_75, HEXA_44, HEXA_98, HEXA_125
  * - DataType_t
    - DataTypeNull, DataTypeUserDefined, Integer, RealSingle, RealDouble, Character, LongInteger
  * - DataClass_t
    - DataClassNull, DataClassUserDefined, Dimensional, NormalizedByDimensional, NormalizedByUnknownDimensional, NondimensionalParameter, DimensionlessConstant
  * - MassUnits_t
    - MassUnitsNull, MassUnitsNullUserDefined, Kilogram, Gram, Slug, PoundMass
  * - LengthUnits_t
    - LengthUnitsNull, LengthUnitsUserDefined, Meter, Centimeter, Millimeter, Foot, Inch
  * - TimeUnits_t
    - TimeUnitsNull, TimeUnitsUserDefined, Second
  * - TemperatureUnits_t
    - TemperatureUnitsNull, TemperatureUnitsUserDefined, Kelvin, Celsius, Rankine, Fahrenheit
  * - AngleUnits_t
    - AngleUnitsNull, AngleUnitsUserDefined, Degree, Radian
  * - ElectricCurrentUnits_t
    - ElectricCurrentUnitsNull, ElectricCurrentUnitsUserDefined, Ampere, Abampere, Statampere, Edison, auCurrent
  * - SubstanceAmountUnits_t
    - SubstanceAmountUnitsNull, SubstanceAmountUnitsUserDefined, Mole, Entities, StandardCubicFoot, StandardCubicMeter
  * - LuminousIntensityUnits_t
    - LuminousIntensityUnitsNull, LuminousIntensityUnitsUserDefined, Candela, Candle, Carcel, Hefner, Violle
  * - GoverningEquationsType_t
    - GoverningEquationsTypeNull, GoverningEquationsTypeUserDefined, FullPotential, Euler, NSLaminar, NSTurbulent, NSLaminarIncompressible, NSTurbulentIncompressible
  * - ModelType_t
    - ModelTypeNull, ModelTypeUserDefined, Ideal, VanderWaals, Constant, PowerLaw, SutherlandLaw, ConstantPrandtl, EddyViscosity, ReynoldsStress, ReynoldsStressAlgebraic, Algebraic_BaldwinLomax, Algebraic_CebeciSmith, HalfEquation_JohnsonKing, OneEquation_BaldwinBarth, OneEquation_SpalartAllmaras, TwoEquation_JonesLaunder, TwoEquation_MenterSST, TwoEquation_Wilcox, CaloricallyPerfect, ThermallyPerfect, ConstantDensity, RedlichKwong, Frozen, ThermalEquilib, ThermalNonequilib, ChemicalEquilibCurveFit, ChemicalEquilibMinimization, ChemicalNonequilib, EMElectricField, EMMagneticField, EMConductivity, Voltage, Interpolated, Equilibrium_LinRessler, Chemistry_LinRessler
  * - GridLocation_t
    - GridLocationNull, GridLocationUserDefined, Vertex, CellCenter, FaceCenter, IFaceCenter, JFaceCenter, KFaceCenter, EdgeCenter
  * - GridConnectivityType_t
    - GridConnectivityTypeNull, GridConnectivityTypeUserDefined, Overset, Abutting, Abutting1to1
  * - PointSetType_t
    - PointSetTypeNull, PointSetTypeUserDefined, PointList, PointRange, PointListDonor, PointRangeDonor, ElementList, ElementRange, CellListDonor
  * - BCType_t
    - BCTypeNull, BCTypeUserDefined, BCAxisymmetricWedge, BCDegenerateLine, BCExtrapolate, BCDegeneratePoint, BCDirichlet, BCFarfield, BCNeumann, BCGeneral, BCInflow, BCOutflow, BCInflowSubsonic, BCOutflowSubsonic, BCInflowSupersonic, BCOutflowSupersonic, BCSymmetryPlane, BCTunnelInflow, BCSymmetryPolar, BCTunnelOutflow, BCWallViscous, BCWall, BCWallViscousHeatFlux, BCWallInviscid, BCWallViscousIsothermal, FamilySpecified
  * - BCDataType_t
    - BCDataTypeNull, BCDataTypeUserDefined, Dirichlet, Neumann
  * - RigidGridMotionType_t
    - RigidGridMotionTypeNull, RigidGridMotionTypeUserDefined, ConstantRate, VariableRate
  * - ArbitraryGridMotionType_t
    - ArbitraryGridMotionTypeNull, ArbitraryGridMotionTypeUserDefined, NonDeformingGrid, DeformingGrid
  * - SimulationType_t
    - SimulationTypeNull, SimulationTypeUserDefined, TimeAccurate, NonTimeAccurate
  * - WallFunctionType_t
    - WallFunctionTypeNull, WallFunctionTypeUserDefined, Generic
  * - AreaType_t
    - AreaTypeNull, AreaTypeUserDefined, BleedArea, CaptureArea
  * - AverageInterfaceType_t
    - AverageInterfaceTypeNull, AverageInterfaceTypeUserDefined, AverageAll, AverageCircumferential, AverageRadial, AverageI, AverageJ, AverageK

.. note::
   The first two enumerated values in these lists, xxxNull and xxxUserDefined, are only available in the C interface, and are provided in the advent that your C compiler does strict type checking.
   In Fortran, these values are replaced by the numerically equivalent :code:`CG_Null` and :code:`CG_UserDefined`.
   These values are also defined in the C interface, thus either form may be used.
   The function prototypes for the MLL use :code:`CG_Null` and :code:`CG_UserDefined`, rather than the more specific values.
  


Character Name of Typedefs
^^^^^^^^^^^^^^^^^^^^^^^^^^
The CGNS library defines character arrays which map the typedefs above to character strings.
These are global arrays dimensioned to the size of each list of typedefs.
To retrieve a character string representation of a typedef, use the typedef value as an index to the appropiate character array.
For example, to retrieve the string ``"Meter"`` for the ``LengthUnits_t Meter`` typedef, use ``LengthUnitsName[Meter]``.
Functions are available to retrieve these names without the need for direct global data access.
These functions also do bounds checking on the input, and if out of range, will return the string ``"<invalid>"``.
An additional benefit is that these will work from within a Windows DLL, and are thus the **recommended access technique**.
The routines have the same name as the global data arrays, but with a ``"cg_"`` prepended.
For the example above, use ``"cg_LengthUnitsName(Meter)"``.


  .. table::
   
    +--------------------------------------------------------------------------------------------------------------------------------+
    | Typedef Name Access Functions                                                                                                  |
    +================================================================================================================================+
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_MassUnitsName`` (:in:`MassUnits_t type`);                                                       |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_LengthUnitsName`` (:in:`LengthUnits_t type`);                                                   |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_TimeUnitsName`` (:in:`TimeUnits_t type`);                                                       |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_TemperatureUnitsName`` (:in:`TemperatureUnits_t type`);                                         |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_ElectricCurrentUnitsName`` (:in:`ElectricCurrentUnits_t type`);                                 |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_SubstanceAmountUnitsName`` (:in:`SubstanceAmountUnits_t type`);                                 |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_LuminousIntensityUnitsName`` (:in:`LuminousIntensityUnits_t type`);                             |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_DataClassName`` (:in:`DataClass_t type`);                                                       |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_GridLocationName`` (:in:`GridLocation_t type`);                                                 |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_BCDataTypeName`` (:in:`BCDataType_t type`);                                                     |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_GridConnectivityTypeName`` (:in:`GridConnectivityType_t type`);                                 |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_PointSetTypeName`` (:in:`PointSetType_t type`);                                                 |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_GoverningEquationsTypeName`` (:in:`GoverningEquationsType_t type`);                             |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_ModelTypeName`` (:in:`ModelType_t type`);                                                       |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_BCTypeName`` (:in:`BCType_t type`);                                                             |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_DataTypeName`` (:in:`DataType_t type`);                                                         |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_ElementTypeName`` (:in:`ElementType_t type`);                                                   |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_ZoneTypeName`` (:in:`ZoneType_t type`);                                                         |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_RigidGridMotionTypeName`` (:in:`RigidGridMotionType_t type`);                                   |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_ArbitraryGridMotionTypeName`` (:in:`ArbitraryGridMotionType_t type`);                           |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_SimulationTypeName`` (:in:`SimulationType_t type`);                                             |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_WallFunctionTypeName`` (:in:`WallFunctionType_t type`);                                         |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_AreaTypeName`` (:in:`AreaType_t type`);                                                         |
    |                                                                                                                                |
    | :out:`const char *name` = ``cg_AverageInterfaceTypeName`` (:in:`AverageInterfaceType_t type`);                                 |
    |                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------+


64-bit Portability and Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is recommended to use :code:`cgsize_t` data type with MLL API as it will work in both 32 and 64-bit compilation modes.

CGNS and Fortran
^^^^^^^^^^^^^^^^
Starting with CGNS-3.3.0, a new CGNS module was added to the library.
Fortran programs can use the new module by adding :code:`USE CGNS`.
The use of include *'cgnslib_f.h'* is **deprecated** as of CGNS-3.3.0.

  .. table::
    :widths: 110 15
   
    +--------------------------------------------------------------------------------------------------------------------------------+-------+
    | Fortran Helper functions                                                                                                       | Modes |
    +================================================================================================================================+=======+
    | **FUNCTION** ``cg_get_type`` (:in:`buf`)                                                                                       |       |
    |                                                                                                                                |       |
    | Returns the data type of *buf*, where *buf* is a scalar. This is a useful function for automatically                           |       |
    | passing the correct data type of a buffer.                                                                                     |       |
    |                                                                                                                                |       |
    | For example:                                                                                                                   |       |
    |                                                                                                                                |       |
    | CALL ``cg_coord_read_f`` (cg, base, zone, coordname, **cg_get_type(data(1))**, rmin, DataSize, data, ier)                      |       |
    |                                                                                                                                |       |
    +--------------------------------------------------------------------------------------------------------------------------------+-------+

Fortran APIs which can accept a null character or an empty string are encouraged to pass :code:`C_NULL_CHAR` as opposed to :code:`"\0"` or ``""``. 

The Fortran APIs have the following specifications (recommended for portability):

- Fortran arguments should be declared as the default :code:`INTEGER` if the corresponding argument in the C API is declared as an :code:`int`.
- Fortran arguments should be declared as :code:`INTEGER(cgsize_t)` if the corresponding argument in the C API is declared as :code:`cgsize_t`.
- Fortran arguments should be declared as type :code:`INTEGER(cgenum_t)` if the corresponding argument in the C API is declared as enumerated values (:code:`enums` ). 

An integer parameter, :code:`CG_BUILD_64BIT`, can be used to tell the size of :code:`cgsize_t`, which will be set to 1 in 64-bit mode and 0 otherwise.
You may use this parameter to check at run time if the CGNS library has been compiled in 64-bit mode or not, as in:

.. code-block::

  if (CG_BUILD_64BIT .ne. 0) then
      print *,'will not work in 64-bit mode'
      stop
  endif


.. last line
