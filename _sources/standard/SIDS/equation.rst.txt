.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)


Governing Flow Equations
========================

This section provides structure type definitions for describing the governing flow-equation set associated with the database. The description includes the general class of governing equations, the turbulent closure equations, the gas and chemistry models, the viscosity and thermal-conductivity models, and the electromagnetics models. Included with each equation description are associated constants. The structure definitions attempt to balance the opposing requirements for future growth and extensibility with initial ease of implementation. Included in the final section are examples of flow-equation sets.

The intended use of these structures initially is primarily for archival purposes and to provide additional documentation of the flow solution. If successful in this role, it is foreseeable that these flow-equation structures may eventually be also used as inputs for grid generators, flow solvers, and post-processors. 

Flow Equation Set Structure Definition: ``FlowEquationSet_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`FlowEquationSet_t` is a general description of the governing flow equations. It includes the dimensionality of the governing equations, and the collection of specific equation-set descriptions covered in subsequent sections. It can be a child node of either :sidsref:`CGNSBase_t` or :sidsref:`Zone_t` (or both).

.. code-block:: sids

  FlowEquationSet_t< int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    int EquationDimension ;                                            (o)

    GoverningEquations_t<CellDimension> GoverningEquations ;           (o)

    GasModel_t GasModel ;                                              (o)

    ViscosityModel_t ViscosityModel ;                                  (o)

    ThermalConductivityModel_t ThermalConductivityModel ;              (o)

    TurbulenceClosure_t TurbulenceClosure ;                            (o)

    TurbulenceModel_t<CellDimension> TurbulenceModel ;                 (o)

    ThermalRelaxationModel_t ThermalRelaxationModel ;                  (o)

    ChemicalKineticsModel_t ChemicalKineticsModel ;                    (o)

    EMElectricFieldModel_t EMElectricFieldModel ;                      (o)

    EMMagneticFieldModel_t EMMagneticFieldModel ;                      (o)

    EMConductivityModel_t EMConductivityModel ;                        (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   #. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`FlowEquationSet_t` and shall not include the names :sidskey:`EMConductivityModel`, :sidskey:`EMElectricFieldModel`, :sidskey:`EMMagneticFieldModel`, :sidskey:`EquationDimension`, :sidskey:`GoverningEquations`, :sidskey:`GasModel`, :sidskey:`ViscosityModel`, :sidskey:`ThermalConductivityModel`, :sidskey:`TurbulenceClosure`, :sidskey:`TurbulenceModel`, :sidskey:`ThermalRelaxationModel`, :sidskey:`ChemicalKineticsModel`, :sidskey:`DataClass`, or :sidskey:`DimensionalUnits`.

   #. There are no required elements for :sidskey:`FlowEquationSet_t`.

:sidskey:`FlowEquationSet_t` requires a single structure parameter, :sidskey:`CellDimension`, to identify the dimensionality of index arrays for structured grids. This parameter is passed onto several substructures.

:sidskey:`EquationDimension` is the dimensionality of the governing equations; it is the number of spatial variables describing the flow. :sidsref:`GoverningEquations` describes the general class of flow equations. :sidsref:`GasModel` describes the equation of state, and :sidsref:`ViscosityModel` and :sidsref:`ThermalConductivityModel` describe the auxiliary relations for molecular viscosity and the thermal conductivity coefficient. :sidsref:`TurbulenceClosure` and :sidsref:`TurbulenceModel` describe the turbulent closure for the Reynolds-averaged Navier-Stokes equations. :sidsref:`ThermalRelaxationModel` and :sidsref:`ChemicalKineticsModel` describe the equations used to model thermal relaxation and chemical kinetics. :sidskey:`EMElectricFieldModel`, :sidskey:`EMMagneticFieldModel`, and :sidskey:`EMConductivityModel` describe the equations used to model electromagnetics.

:sidsref:`DataClass` defines the default for the class of data contained in the flow-equation set. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Governing Equations Structure Definition: ``GoverningEquations_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GoverningEquations_t` describes the class of governing flow equations associated with the solution.

.. code-block:: sids

  GoverningEquationsType_t := Enumeration(
    GoverningEquationsTypeNull,
    GoverningEquationsTypeUserDefined,
    FullPotential,
    Euler,
    NSLaminar,
    NSTurbulent,
    NSLaminarIncompressible,
    NSTurbulentIncompressible ) ;

  GoverningEquations_t< int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GoverningEquationsType_t GoverningEquationsType ;                  (r)

    int[CellDimension*(CellDimension + 1)/2] DiffusionModel ;          (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`GoverningEquations_t` and shall not include the name :sidskey:`DiffusionModel`.

    #. :sidskey:`GoverningEquationsType` is the only required element.

    #. The length of the :sidsref:`DiffusionModel` array is as follows: in 1-D it is int[1]; in 2-D it is :sidskey:`int[3]`; and in 3-D it is :sidskey:`int[6]`. For unstructured zones, :sidskey:`DiffusionModel` is not supported, and should not be used. 

:sidskey:`GoverningEquations_t` requires a single structure parameter, :sidskey:`CellDimension`. It is used to define the length of the array :sidskey:`DiffusionModel`.

:sidskey:`DiffusionModel` describes the viscous diffusion terms modeled in the flow equations, and is applicable only to the Navier-Stokes equations with structured grids. Typically, thin-layer approximations include only the diffusion terms in one or two computational-coordinate directions. :sidskey:`DiffusionModel` encodes the coordinate directions that include second-derivative and cross-derivative diffusion terms. The first :sidskey:`CellDimension` elements are second-derivative terms and the remainder elements are cross-derivative terms. Allowed values for individual elements in the array :sidskey:`DiffusionModel` are 0 and 1; a value of 1 indicates the diffusion term is modeled, and 0 indicates that they are not modeled. In 3-D, the encoding of :sidskey:`DiffusionModel` is as follows:

.. table::
  :align: left

  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | Element  | Modeled Terms                                                                                                                          |
  +==========+========================================================================================================================================+
  | *n* = 1  | Diffusion terms in *i* (:math:`\partial^2 / \partial \xi^{2}`)                                                                         |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | *n* = 2  | Diffusion terms in *j* (:math:`\partial^2 / \partial \eta^{2}`)                                                                        |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | *n* = 3  | Diffusion terms in *k* (:math:`\partial^2 / \partial \zeta^{2}`)                                                                       |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | *n* = 4  | Cross-diffusion terms in *i*-*j* (:math:`\partial^2/\partial \xi \partial \eta` and :math:`\partial^2 / \partial \eta \partial \xi`)   |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | *n* = 5  | Cross-diffusion terms in *j*-*k* (:math:`\partial^2/\partial \eta \partial \zeta` and :math:`\partial^2/\partial \zeta \partial \eta`) |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+
  | *n* = 6  | Cross-diffusion terms in *k*-*i* (:math:`\partial^2/\partial \zeta \partial \xi` and :math:`\partial^2/\partial \xi \partial \zeta`)   |
  +----------+----------------------------------------------------------------------------------------------------------------------------------------+

where derivatives in the *i*, *j* and *k* computational-coordinates are :math:`\xi`, :math:`eta` and :math:`zeta`, respectively.
The full Navier-Stokes equations in 3-D are indicated by :sidskey:`DiffusionModel = [1,1,1,1,1,1]`, and the thin-layer equations including only diffusion in the *j*-direction are :code:`[0,1,0,0,0,0]`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Model Type Structure Definition: ``ModelType_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ModelType_t` is a complete list of all models covered in subsequent sections. A specific model will contain a subset of this enumeration.

.. code-block:: sids

  ModelType_t := Enumeration(
    ModelTypeNull, ModelTypeUserDefined,
    Ideal, VanderWaals, Constant, PowerLaw,
    SutherlandLaw, ConstantPrandtl, EddyViscosity,
    ReynoldsStress, ReynoldsStressAlgebraic,
    Algebraic_BaldwinLomax, Algebraic_CebeciSmith,
    HalfEquation_JohnsonKing, OneEquation_BaldwinBarth,
    OneEquation_SpalartAllmaras, TwoEquation_JonesLaunder,
    TwoEquation_MenterSST, TwoEquation_Wilcox,
    CaloricallyPerfect, ThermallyPerfect, ConstantDensity,
    RedlichKwong, Frozen, ThermalEquilib, ThermalNonequilib,
    ChemicalEquilibCurveFit, ChemicalEquilibMinimization,
    ChemicalNonequilib, EMElectricField, EMMagneticField,
    EMConductivity, Voltage, Interpolated,
    Equilibrium_LinRessler, Chemistry_LinRessler ) ;


Thermodynamic Gas Model Structure Definition: ``GasModel_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GasModel_t` describes the equation of state model used in the governing equations to relate pressure, temperature and density. The enumerated values for :sidskey:`GasModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  GasModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Ideal,
    VanderWaals,
    CaloricallyPerfect,
    ThermallyPerfect,
    ConstantDensity,
    RedlichKwong ) ;

  GasModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GasModelType_t GasModelType ;                                      (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`GasModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  #. :sidskey:`GasModelType` is the only required element.
  #. The :sidskey:`GasModelType` enumeration name :sidskey:`Ideal` implies a calorically perfect single-component gas, but the more descriptive name :sidskey:`CaloricallyPerfect` is generally preferred. 

For a perfect gas (:sidskey:`GasModelType = CaloricallyPerfect`), the pressure, temperature, and density are related by

.. math::
  
   p = \rho R T

where :math:`R` is the ideal gas constant. Related quantities are the specific heat at constant pressure (:math:`c_{p}`), specific heat at constant volume (:math:`c_{v}`) and specific heat ratio :math:`\gamma = c_{p}/c_{v}`).
The gas constant and specific heats are related by :math:`R = c_{p} − c_{v}`. Data-name identifiers associated with the perfect gas law are listed below.


.. table:: **Data-Name Identifiers for Perfect Gas**

  +-----------------------+---------------------------------------------------------+---------------------------+
  | Data-Name Identifier  | Description                                             | Units                     |
  +=======================+=========================================================+===========================+
  | IdealGasConstant      | Ideal gas constant (:math:`R`)                          | :math:`L^2/(T^2 \Theta)`  |
  +-----------------------+---------------------------------------------------------+---------------------------+
  | SpecificHeatRatio     | Ratio of specific heats (:math:`\gamma = c_{p}/c_{v}`)  | `-`                       |
  +-----------------------+---------------------------------------------------------+---------------------------+
  | SpecificHeatVolume    | Specific heat at constant volume (:math:`c_{v}`)        | :math:`L^2/(T^2 \Theta)`  |
  +-----------------------+---------------------------------------------------------+---------------------------+
  | SpecificHeatPressure  | Specific heat at constant pressure (:math:`c_{p}`)      | :math:`L^2/(T^2 \Theta)`  |
  +-----------------------+---------------------------------------------------------+---------------------------+

If it is desired to specify any of these identifiers in a CGNS database, they should be defined as :sidsref:`DataArray` under :sidskey:`GasModel_t`.

The dimensional units are defined as follows: :math:`M` is mass, :math:`L` is length, :math:`T` is time and :math:`\Theta` is temperature.
These are further described in the section on :ref:`Conventions for Data-Name Identifiers <dataname>`.

:sidsref:`DataClass` defines the default for the class of data contained in the thermodynamic gas model. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Molecular Viscosity Model Structure Definition: ``ViscosityModel_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ViscosityModel_t` describes the model for relating molecular viscosity (:math:`\mu`) to temperature. The enumerated values for :sidskey:`ViscosityModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  ViscosityModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Constant,
    PowerLaw,
    SutherlandLaw ) ;

  ViscosityModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ViscosityModelType_t ViscosityModelType ;                          (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ViscosityModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
   
   #. :sidskey:`ViscosityModelType` is the only required element. 

The molecular viscosity models are as follows: :sidskey:`Constant` states that molecular viscosity is constant throughout the field and is equal to some reference value (:math:`\mu = \mu_{ref}`); :sidskey:`PowerLaw` states that molecular viscosity follows a power-law relation,

.. math::
  
  \mu = \mu_{ref} (T/T_{ref})^{n}

and :sidsref:`SutherlandLaw` is Sutherland's Law for molecular viscosity,

.. math::
  
  \mu = \mu_{ref} (T/T_{ref})^{3/2} (T_{ref} + T_{s}) / (T + T_{s})

where :math:`T_{s}` is the Sutherland's Law constant, and :math:`\mu_{ref}` and :math:`T_{ref}` are the reference viscosity and temperature, respectively.
For air [White, F. M., *Viscous Fluid Flow*, McGraw-Hill, 1974, p. 28-29], the power-law exponent is n = 0.666, Sutherland's law constant (:math:`T_{s}`) is 110.6 K, the reference temperature (:math:`T_{ref}`) is 273.15 K, and the reference viscosity (:math:`\mu_{ref}`) is :math:`1.716 \times 10^{-5}\ kg/(m s)`.
The data-name identifiers for molecular viscosity models are defined below.

.. table:: **Data-Name Identifiers for Molecular Viscosity Models**

  +--------------------------+----------------------------------------+-----------------------------------------------+----------------+
  | ``ViscosityModelType``   | Data-Name Identifier                   | Description                                   | Units          |
  +==========================+========================================+===============================================+================+
  | :sidskey:`PowerLaw`      | :sidskey:`PowerLawExponent`            | Power-law exponent (*n*)                      | `-`            |
  +--------------------------+----------------------------------------+-----------------------------------------------+----------------+
  | :sidskey:`SutherlandLaw` | :sidskey:`SutherlandLawConstant`       | Sutherland's Law constant (:math:`T_{s}`)     | :math:`\Theta` |
  +--------------------------+----------------------------------------+-----------------------------------------------+----------------+
  | All                      | :sidskey:`TemperatureReference`        | Reference temperature (:math:`T_{ref}`)       | :math:`\Theta` |
  +--------------------------+----------------------------------------+-----------------------------------------------+----------------+
  | All                      | :sidskey:`ViscosityMolecularReference` | Reference viscosity (:math:`\mu_{ref}`)       | :math:`M/(LT)` |
  +--------------------------+----------------------------------------+-----------------------------------------------+----------------+

If it is desired to specify any of these identifiers in a CGNS database, they should be defined as :sidsref:`DataArray` under :sidskey:`ViscosityModel_t`.

:sidsref:`DataClass` defines the default for the class of data contained in the molecular viscosity model. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 

Thermal Conductivity Model Structure Definition: ``ThermalConductivityModel_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ThermalConductivityModel_t` describes the model for relating the thermal-conductivity coefficient (:math:`k`) to temperature. The enumerated values for :sidskey:`ThermalConductivityModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  ThermalConductivityModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    ConstantPrandtl,
    PowerLaw,
    SutherlandLaw ) ;

  ThermalConductivityModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ThermalConductivityModelType_t ThermalConductivityModelType ;      (r)
    
    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ThermalConductivityModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
    
    #. :sidskey:`ThermalConductivityModelType` is the only required element. 

The thermal-conductivity models parallel the molecular viscosity models. :sidskey:`ConstantPrandtl` states that the Prandtl number (:math:`Pr = \mu c_{p}/k`) is constant and equal to some reference value.
PowerLaw relates :math:`k` to temperature via a power-law relation,

.. math::

   k = k_{ref} (T/T_{ref})^{n}

and :sidskey:`SutherlandLaw` is Sutherland's Law for molecular viscosity,

.. math::

  k = k_{ref} (T/T_{ref})^{3/2} (T_{ref} + T_{s}) / (T + T_{s})

where :math:`k_{ref}` is the reference thermal conductivity, :math:`T_{ref}` is the reference temperature, and :math:`T_{s}` is the Sutherland's law constant.
For air [White, F. M., *Viscous Fluid Flow*, McGraw-Hill, 1974, p. 32-33], the Prandtl number is :math:`Pr = 0.72`, the power-law exponent is :math:`n = 0.81`, Sutherland's law constant (:math:`T_{s}`) is 194.4 K, the reference temperature (:math:`T_{ref}`) is 273.15 K, and the reference thermal conductivity (:math:`k_{ref}`) is :math:`2.414 \times 10^{-2}\ kg\ m/(s^{3} K)`. 
Data-name identifiers for thermal conductivity models are listed below.

.. table:: **Data-Name Identifiers for Thermal Conductivity Models**

  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+
  | ``ThermalConductivityModelType``  | Data-Name Identifier                    | Description                                      | Units                      |
  +===================================+=========================================+==================================================+============================+
  | :sidskey:`ConstantPrandtl`        | :sidskey:`Prandtl`                      | Prandtl number (:math:`Pr`)	                   | :math:`-`                  |
  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+
  | :sidskey:`PowerLaw`               | :sidskey:`PowerLawExponent`             | Power-law exponent (:math:`n`)                   | :math:`-`                  |
  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+
  | :sidskey:`SutherlandLaw`          | :sidskey:`SutherlandLawConstant`        | Sutherland's Law constant (:math:`T_{s}`)        | :math:`\Theta`             |
  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+
  | All                               | :sidskey:`TemperatureReference`         | Reference temperature (:math:`T_{ref}`)          | :math:`\Theta`             |
  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+
  | All                               | :sidskey:`ThermalConductivityReference` | Reference thermal conductivity (:math:`k_{ref}`) | :math:`M L/(T^{3} \Theta)` |
  +-----------------------------------+-----------------------------------------+--------------------------------------------------+----------------------------+

If it is desired to specify any of these identifiers in a CGNS database, they should be defined as DataArrays under :sidskey:`ThermalConductivityModel_t`.

:sidsref:`DataClass` defines the default for the class of data contained in the thermal conductivity model. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 

Turbulence Structure Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section presents structure definitions for describing the form of closure used in the Reynolds-averaged (or Favre-averaged) Navier-Stokes equations for determining the Reynolds stress terms. Here "turbulence closure" refers to eddy viscosity or other approximations for the Reynolds stress terms, and "turbulence model" refers to the actual algebraic or turbulence-transport equation models used. To an extent these are independent choices (e.g., using either an eddy viscosity closure or an algebraic Reynolds-stress closure with a two-equation model).

Turbulence Closure Structure Definition: ``TurbulenceClosure_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`TurbulenceClosure_t` describes the turbulence closure for the Reynolds stress terms of the Navier-Stokes equations. The enumerated values for :sidskey:`TurbulenceClosureType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  TurbulenceClosureType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    EddyViscosity,
    ReynoldsStress,                     
    ReynoldsStressAlgebraic ) ;

  TurbulenceClosure_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    TurbulenceClosureType_t TurbulenceClosureType ;                    (r)
    
    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`TurbulenceClosure_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.

    #. :sidskey:`TurbulenceClosureType` is the only required element. 

The different types of turbulent closure are as follows: :sidskey:`EddyViscosity` is the Boussinesq eddy-viscosity closure, where the Reynolds stresses are approximated as the product of an eddy viscosity (:math:`nu_{t}`) and the mean strain tensor. Using indicial notation, the relation is,

.. math::

  −(u′_{i} u′_{j})_{ave} = \nu_{t} ( \partial u_{i} / \partial x_{j} + \partial u_{j} / \partial x_{i} )

where :math:`−(u′_{i} u′_{j})_{ave}` are the Reynolds stresses; the notation is further discussed under :ref:`Flowfield Solution <dataname_flow>` in the section on :ref:`Conventions for Data-Name Identifiers <dataname>`.
:sidskey:`ReynoldsStress` is no approximation of the Reynolds stresses.
:sidskey:`ReynoldsStressAlgebraic` is an algebraic approximation for the Reynolds stresses based on some intermediate transport quantities.

Associated with the turbulent closure is a list of constants, where each constant is described by a separate :sidsref:`DataArray_t` entity. Constants associated with the eddy-viscosity closure are listed below.

.. table:: **Data-Name Identifiers for Turbulence Closure**

  +-----------------------------+-----------------------------------------------------------------+---------------+
  | Data-Name Identifier        | Description                                                     | Units         |
  +=============================+=================================================================+===============+
  | :sidskey:`PrandtlTurbulent` | Turbulent Prandtl number (:math:`\rho \nu_{t} c_{p} / k_{t}`)   |  :math:`-`    |
  +-----------------------------+-----------------------------------------------------------------+---------------+

If it is desired to specify any of these identifiers in a CGNS database, they should be defined as :sidsref:`DataArray` under :sidskey:`TurbulenceClosure_t`.

:sidsref:`DataClass` defines the default for the class of data contained in the turbulence closure. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Turbulence Model Structure Definition: ``TurbulenceModel_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`TurbulenceModel_t` describes the equation set used to model the turbulence quantities. The enumerated values for :sidskey:`TurbulenceModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  TurbulenceModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Algebraic_BaldwinLomax,
    Algebraic_CebeciSmith,
    HalfEquation_JohnsonKing,
    OneEquation_BaldwinBarth,
    OneEquation_SpalartAllmaras,
    TwoEquation_JonesLaunder,
    TwoEquation_MenterSST,
    TwoEquation_Wilcox ) ;

  TurbulenceModel_t< int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    TurbulenceModelType_t TurbulenceModelType ;                        (r)
    
    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    int[CellDimension*(CellDimension + 1)/2] DiffusionModel ;          (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`TurbulenceModel_t` and shall not include the names :sidskey:`DiffusionModel`, :sidskey:`DataClass`, or :sidskey:`DimensionalUnits`.

  #. :sidskey:`TurbulenceModelType` is the only required element.

  #. The length of the :sidskey:`DiffusionModel` array is as follows: in 1-D it is :code:`int[1]`; in 2-D it is :code:`int[3]`; and in 3-D it is :code:`int[6]`. For unstructured zones, :sidskey:`DiffusionModel` is not supported, and should not be used.

:sidskey:`TurbulenceModel_t` requires a single structure parameter, :sidskey:`CellDimension`.
It is used to define the length of the array :sidskey:`DiffusionModel`. :sidsref:`DiffusionModel` describes the viscous diffusion terms included in the turbulent transport model equations.

The :sidskey:`TurbulenceModelType` names currently listed correspond to the following particular references.

.. table::

   ======================================== =========================================================================================================================================================================================
    :sidskey:`Algebraic_BaldwinLomax`         Baldwin, B. S., and Lomax, H. (1978) "Thin Layer Approximations and Algebraic Model for Separated Turbulent Flows," AIAA Paper 78-257.
    :sidskey:`Algebraic_CebeciSmith`          Cebeci, T., and Smith, A. M. O. (1974) Analysis of Turbulent Boundary Layers, Academic Press, New York.
	:sidskey:`HalfEquation_JohnsonKing`       Johnson, D., and King, L. (1985) "A Mathematically Simple Turbulence Closure Model for Attached and Separated Turbulent Boundary Layers," AIAA Journal, Vol. 23, No. 11, pp. 1684-1692.
    :sidskey:`OneEquation_BaldwinBarth`       Baldwin, B., and Barth, T. (1990) "A One-Equation Turbulent Transport Model for High Reynolds Number Wall-Bounded Flows," NASA TM-102847.
    :sidskey:`OneEquation_SpalartAllmaras`    Spalart, P. R., and Allmaras, S. R. (1994) "A One-Equation Turbulence Model for Aerodynamic Flows," La Recherche Aerospatiale, Vol. 1, pp. 5-21.
    :sidskey:`TwoEquation_JonesLaunder`       Jones, W., and Launder, B. (1972) "The Prediction of Laminarization with a Two-Equation Model of Turbulence," International Journal of Heat and Mass Transfer, Vol. 15, pp. 301-314.
    :sidskey:`TwoEquation_MenterSST`          Menter, F. R. (1994) "Two-Equation Eddy-Viscosity Turbulence Models for Engineering Application," AIAA Journal, Vol. 32, No. 8, pp. 1598-1605.
    :sidskey:`TwoEquation_Wilcox`             Wilcox, D. C. (1994) Turbulence Modeling for CFD, First Edition, DCW Industries, La Canada, California.
   ======================================== =========================================================================================================================================================================================


There is no formal mechanism for accounting for subsequent changes to these models. (For example, Wilcox later published 1998 and 2006 versions of his k-ω model).
If it is a mere change to constant(s), then this could be described by retaining the same :sidskey:`TurbulenceModelType` name and listing each constant using a separate :sidskey:`DataArray_t` entry.
If the change is more involved, then it is recommended to employ :sidskey:`TurbulenceModelType = UserDefined` with a child :sidskey:`Descriptor_t` node giving details about it.

Associated with each choice of turbulence model may be a list of constants, where each constant is described by a separate :sidskey:`DataArray_t` entity.
If used, the Data-Name Identifier of each constant should include the turbulence model name, as well as the constant name (e.g., :sidskey:`TurbulentSACb1`, :sidskey:`TurbulentSSTCmu`, :sidskey:`TurbulentKESigmak`, etc.).
However, no attempt is made here to formalize the names for all possible turbulence models.

DataClass defines the default for the class of data contained in the turbulence model equation set.
For any data that is dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Example - Spalart-Allmaras Turbulence Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Description for the eddy-viscosity closure and Spalart-Allmaras turbulence model, including associated constants.

.. code-block:: sids

  TurbulenceClosure_t TurbulenceClosure =
    {{
    TurbulenceClosureType_t TurbulenceClosureType = EddyViscosity ;

    DataArray_t<real, 1, 1> PrandtlTurbulent = {{ 0.90 }} ;
    }} ;

  TurbulenceModel_t TurbulenceModel = 
    {{
    TurbulenceModelType_t TurbulenceModelType = OneEquation_SpalartAllmaras ;

    DataArray_t<real, 1, 1> TurbulentSACb1   = {{ 0.1355 }} ;
    DataArray_t<real, 1, 1> TurbulentSACb2   = {{ 0.622 }} ;
    DataArray_t<real, 1, 1> TurbulentSASigma = {{ 2/3 }} ;
    DataArray_t<real, 1, 1> TurbulentSAKappa = {{ 0.41 }} ;
    DataArray_t<real, 1, 1> TurbulentSACw1   = {{ 3.2391 }} ;
    DataArray_t<real, 1, 1> TurbulentSACw2   = {{ 0.3 }} ;
    DataArray_t<real, 1, 1> TurbulentSACw3   = {{ 2 }} ;
    DataArray_t<real, 1, 1> TurbulentSACv1   = {{ 7.1 }} ;
    DataArray_t<real, 1, 1> TurbulentSACt1   = {{ 1 }} ;
    DataArray_t<real, 1, 1> TurbulentSACt2   = {{ 2 }} ;
    DataArray_t<real, 1, 1> TurbulentSACt3   = {{ 1.2 }} ;
    DataArray_t<real, 1, 1> TurbulentSACt4   = {{ 0.5 }} ;
    }} ;

Note that each :sidsref:`DataArray_t` entity is abbreviated.


Thermal Relaxation Model Structure Definition: ``ThermalRelaxationModel_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ThermalRelaxationModel_t` describes the equation set used to model thermal relaxation quantities. The enumerated values for :sidskey:`ThermalRelaxationModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  ThermalRelaxationModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Frozen,
    ThermalEquilib,
    ThermalNonequilib ) ;

  ThermalRelaxationModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ThermalRelaxationModelType_t ThermalRelaxationModelType ;          (r)
    
    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ThermalRelaxationModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
    #. :sidskey:`ThermalRelaxationModelType` is the only required element. 

:sidskey:`ThermalRelaxationModelType_t` is an enumeration type describing the type of thermal relaxation model.

:sidsref:`DataArray_t` data structures may be used to store data associated with the thermal relaxation model. :sidsref:`DataClass` defines the default for the class of data being used. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

Additional information, if needed, may be stored using :sidsref:`Descriptor_t` data structures.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.


Chemical Kinetics Model Structure Definition: ``ChemicalKineticsModel_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`ChemicalKineticsModel_t` describes the equation set used to model chemical kinetics quantities. The enumerated values for :sidskey:`ChemicalKineticsModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  ChemicalKineticsModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Frozen,
    ChemicalEquilibCurveFit,
    ChemicalEquilibMinimization,
    ChemicalNonequilib ) ;

  ChemicalKineticsModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    ChemicalKineticsModelType_t ChemicalKineticsModelType ;            (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ChemicalKineticsModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
    
  #. :sidskey:`ChemicalKineticsModelType` is the only required element. 

:sidskey:`ChemicalKineticsModelType_t` is an enumeration type describing the type of chemical kinetics model.

:sidskey:`DataArray_t` data structures may be used to store data associated with the chemical kinetics model.
Recommended data-name identifiers are listed in the following table.

.. table:: **Data-Name Identifiers for Chemical Kinetics Models**

  +-------------------------------------+------------------------------------------------------+---------------------+
  | Data-Name Identifier                | Description                                          | Units               |
  +=====================================+======================================================+=====================+
  | :sidskey:`MolecularWeightSymbol`    | Molecular weight for species Symbol                  | :math:`-`           |
  +-------------------------------------+------------------------------------------------------+---------------------+
  | :sidskey:`HeatOfFormationSymbol`    | Heat of formation per unit mass for species Symbol   | :math:`L^{2}/T^{2}` |
  +-------------------------------------+------------------------------------------------------+---------------------+
  | :sidskey:`FuelAirRatio`             | Fuel/air mass ratio                                  | :math:`-`           |
  +-------------------------------------+------------------------------------------------------+---------------------+
  | :sidskey:`ReferenceTemperatureHOF`  | Reference temperature for the heat of formation      | :math:`\Theta`      |
  +-------------------------------------+------------------------------------------------------+---------------------+

The dimensional units are defined as follows: :math:`L` is length, :math:`T` is time and :math:`\Theta` is temperature.
These are further described in the section on :ref:`Conventions for Data-Name Identifiers <dataname>`.

The variable string *Symbol* in the above data-name identifiers represents the chemical symbol for the desired species.
For example, :sidskey:`H` represents hydrogen atoms, :sidskey:`O` represents oxygen atoms, :sidskey:`H2` represents hydrogen molecules, :sidskey:`H2O` represents water molecules, and :sidskey:`C3H5O3(NO2)3` represents nitroglycerin molecules.
Any symbols from the periodic table of the elements can be used. For charged molecules or particles, the word ":sidskey:`plus`" or ":sidskey:`minus`" should be spelled out in lower case. For example, a CNO+ molecule should be denoted as :sidskey:`CNOplus`.

Other commonly used mixtures that are usually not referred to by their chemical symbols, are defined in the following table. Individual users may define new names, but these may not be recognized by other CGNS applications.
For consistency, additional names should be proposed as SIDS extensions.

.. table:: **Defined Names (Symbols) for Commonly Used Mixtures**

  +--------------------+------------------------------------------+
  | Symbol             | Mixture                                  |
  +====================+==========================================+
  | :sidskey:`Air`     | Generic air model                        |
  +--------------------+------------------------------------------+
  | :sidskey:`eminus`  | Electrons                                |
  +--------------------+------------------------------------------+
  | :sidskey:`Fuel`    | Generic fuel model                       |
  +--------------------+------------------------------------------+
  | :sidskey:`FuelAir` | Generic fuel/air mixture                 |
  +--------------------+------------------------------------------+
  | :sidskey:`JP5`     | JP5 jet fuel                             |
  +--------------------+------------------------------------------+
  | :sidskey:`JP7`     | JP7 jet fuel                             |
  +--------------------+------------------------------------------+
  | :sidskey:`JP10`    | JP10 jet fuel                            |
  +--------------------+------------------------------------------+
  | :sidskey:`Product` | Generic fuel/air product of combustion   |
  +--------------------+------------------------------------------+
  | :sidskey:`RP1`     | RP1 rocket fuel                          |
  +--------------------+------------------------------------------+

:sidskey:`DataClass` defines the default for the class of data being used.
For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

Additional information, if needed, may be stored using :sidskey:`Descriptor_t` data structures.
For example, if CHEMKIN is used, it is recommended that a :sidskey:`Descriptor_t` data structure be used to indicate this.
Reaction equations could also be specified using :sidskey:`Descriptor_t` data structures.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Electromagnetics Structure Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section presents structure definitions for describing the electric field, magnetic field, and conductivity models used for electromagnetic flows.

Electromagnetics Electric Field Model Structure Definition: ``EMElectricFieldModel_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`EMElectricFieldModel_t` describes the electric field model used for electromagnetic flows. The enumerated values for :sidskey:`EMElectricFieldModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  EMElectricFieldModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Constant,
    Frozen,
    Interpolated,
    Voltage ) ;

  EMElectricFieldModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    EMElectricFieldModelType_t EMElectricFieldModelType ;              (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`EMElectricFieldModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  
  #. :sidskey:`EMElectricFieldModelType` is the only required element. 

:sidskey:`EMElectricFieldModelType_t` is an enumeration type describing the type of electric field model.

:sidsref:`DataArray_t` data structures may be used to store data associated with the electric field model. Recommended data-name identifiers are listed in the section describing the :ref:`electromagnetics conductivity model <EMConductivityModel>`.

:sidskey:`DataClass` defines the default for the class of data contained in the electric field model. For any data that is dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Electromagnetics Magnetic Field Model Structure Definition: ``EMMagneticFieldModel_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`EMMagneticFieldModel_t` describes the magnetic field model used for electromagnetic flows. The enumerated values for :sidskey:`EMMagneticFieldModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  EMMagneticFieldModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Constant,
    Frozen,
    Interpolated ) ;

  EMMagneticFieldModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    EMMagneticFieldModelType_t EMMagneticFieldModelType ;              (r)

    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`EMMagneticFieldModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.

  #. :sidskey:`EMMagneticFieldModelType` is the only required element. 

:sidskey:`EMMagneticFieldModelType_t` is an enumeration type describing the type of magnetic field model.

:sidsref:`DataArray_t` data structures may be used to store data associated with the magnetic field model. Recommended data-name identifiers are listed in the section describing the :ref:`electromagnetics conductivity model <EMConductivityModel>`.

:sidskey:`DataClass` defines the default for the class of data contained in the magnetic field model.
For any data that is dimensional, :sidskey:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in Descriptor_t and DataArray_t children without the restrictions or implicit meanings imposed on these node types at other node locations. 

Electromagnetics Conductivity Model Structure Definition: ``EMConductivityModel_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`EMConductivityModel_t` describes the conductivity model used for electromagnetic flows. The enumerated values for :sidskey:`EMConductivityModelType_t` are a subset of the :sidskey:`ModelType_t` enumeration.

.. code-block:: sids

  EMConductivityModelType_t := Enumeration(
    ModelTypeNull,
    ModelTypeUserDefined,
    Constant,
    Frozen,
    Equilibrium_LinRessler,
    Chemistry_LinRessler ) ;

  EMConductivityModel_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    EMConductivityModelType_t EMConductivityModelType ;                (r)
    
    List( DataArray_t<DataType, 1, 1> DataArray1 ... DataArrayN ) ;    (o)

    DataClass_t DataClass ;                                            (o)
                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

  #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`EMConductivityModel_t` and shall not include the names :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
  #. :sidskey:`EMConductivityModelType` is the only required element. 

:sidskey:`EMConductivityModelType_t` is an enumeration type describing the type of conductivity model.

:sidsref:`DataArray_t` data structures may be used to store data associated with the conductivity model. Recommended data-name identifiers for all three electromagnetics models are listed in the following table.

.. table:: **Data-Name Identifiers for Electromagnetics Models**

  +---------------------------------+-----------------------------------------+-----------------------+
  | Data-Name Identifier            | Description                             | Units                 |
  +=================================+=========================================+=======================+
  | :sidskey:`Voltage`              | Voltage                                 | :math:`M L^{2}/TI`    |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`ElectricFieldX`       | x-component of electric field vector    | :math:`ML/TI`         |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`ElectricFieldY`       | y-component of electric field vector    | :math:`ML/TI`         |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`ElectricFieldZ`       | z-component of electric field vector    | :math:`ML/TI`         |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`MagneticFieldX`       | x-component of magnetic field vector    | :math:`I/L`           |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`MagneticFieldY`       | y-component of magnetic field vector    | :math:`I/L`           |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`MagneticFieldZ`       | z-component of magnetic field vector    | :math:`I/L`           |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`CurrentDensityX`      | x-component of current density vector   | :math:`I/L^{2}`       |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`CurrentDensityY`      | y-component of current density vector   | :math:`I/L^{2}`       |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`CurrentDensityZ`      | z-component of current density vector   | :math:`I/L^{2}`       |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`ElectricConductivity` | Electrical conductivity                 | :math:`ML/T^{3}I^{2}` |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`LorentzForceX`        | x-component of Lorentz force vector     | :math:`ML/T^{2}`      |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`LorentzForceY`        | y-component of Lorentz force vector     | :math:`ML/T^{2}`      |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`LorentzForceZ`        | z-component of Lorentz force vector     | :math:`ML/T^{2}`      |
  +---------------------------------+-----------------------------------------+-----------------------+
  | :sidskey:`JouleHeating`         | Joule heating                           | :math:`ML^{2}/T^{2}`  |
  +---------------------------------+-----------------------------------------+-----------------------+

The dimensional units are defined as follows: :math:`M` is mass, :math:`L` is length, :math:`T` is time, and :math:`I` is electric current.
These are further described in the section on :ref:`Conventions for Data-Name Identifiers <dataname>`.

:sidsref:`DataClass` defines the default for the class of data contained in the conductivity model. For any data that is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed.
If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 


Flow Equation Examples
^^^^^^^^^^^^^^^^^^^^^^

This section presents two examples of flow-equation sets. The first is an inviscid case and the second is a turbulent case with a one-equation turbulence model. 

Example - 3-D Compressible Euler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3-D compressible Euler with a perfect gas assumption for a monatomic gas:

.. code-block:: sids

  FlowEquationSet_t<3> EulerEquations = 
    {{
    int EquationDimension = 3 ;
    
    GoverningEquations_t<3> GoverningEquations =
      {{
      GoverningEquationsType_t GoverningEquationsType = Euler ;
      }} ;
      
    GasModel_t GasModel =
      {{
      GasModelType_t GasModelType = CaloricallyPerfect ;
      
      DataArray_t<real, 1, 1> SpecificHeatRatio =
        {{
        Data(real, 1, 1) = 1.667 ;

        DataClass_t DataClass = NondimensionalParameter ;
        }} ;
      }} ;
    }} ;

Example - 3-D Compressible Navier-Stokes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3-D compressible Navier-Stokes for a structured grid, with the S-A turbulence model, a perfect gas assumption, Sutherland's law for the molecular viscosity, a constant Prandtl-number assumption, and inclusion of the full Navier-Stokes diffusion terms; all models assume air:

.. code-block:: sids

  FlowEquationSet_t<3> NSEquations = 
    {{
    int EquationDimension = 3 ;
    
    GoverningEquations_t<3> GoverningEquations =
      {{
      GoverningEquationsType_t GoverningEquationsType = NSTurbulent ;
      
      int[6] DiffusionModel = [1,1,1,1,1,1] ;
      }} ;
      
    GasModel_t GasModel =
      {{
      GasModelType_t GasModelType = CaloricallyPerfect ;
      
      DataArray_t<real, 1, 1> SpecificHeatRatio = {{ 1.4 }} ;
      }} ;

    ViscosityModel_t ViscosityModel =
      {{
      ViscosityModelType_t ViscosityModelType = SutherlandLaw ;
      
      DataArray_t<real, 1, 1> SutherlandLawConstant = 
        {{ 
        Data(real, 1, 1) = 110.6 }} ;
      
        DataClass_t DataClass = Dimensional ;
        DimensionalUnits_t DimensionalUnits = {{ TemperatureUnits = Kelvin }} ;
        }} ;
      }} ;

    ThermalConductivityModel_t ThermalConductivityModel =
      {{
      ThermalConductivityModelType_t ThermalConductivityModelType =
         ConstantPrandtl ;
      
      DataArray_t<real, 1, 1> Prandtl = {{ 0.72 }} ;
      }} ;

    TurbulenceClosure_t<3> TurbulenceClosure =
      {{
      TurbulenceClosureType_t TurbulenceClosureType = EddyViscosity ;
      
      DataArray_t<real, 1, 1> PrandtlTurbulent = {{ 0.90 }} ;
      }} ;
      
    TurbulenceModel_t<3> TurbulenceModel =
      {{
      TurbulenceModelType_t TurbulenceModelType = OneEquation_SpalartAllmaras ;
      
      int[6] DiffusionModel = [1,1,1,1,1,1] ;
      }} ;      
    }} ;

Note that all :sidsref:`DataArray_t` entities are abbreviated except :sidskey:`SutherlandLawConstant`. 

.. last line
