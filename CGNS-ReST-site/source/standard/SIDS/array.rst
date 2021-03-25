.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _StandardDataArrayStruct:

Data-Array Structure Definitions
++++++++++++++++++++++++++++++++

This section defines the structure type :sidskey:`DataArray_t` for describing data arrays.
This general-purpose structure is used to declare data arrays and scalars throughout the CGNS hierarchy.
It is used to describe grid coordinates, flow-solution data, governing flow parameters, boundary-condition data, and other information.
For most of these different types of CFD data, we have also established a :ref:`list of standardized identifiers<dataname>` for entities of type :sidskey:`DataArray_t`.
For example, :sidskey:`Density` is used for data arrays containing static density.

We address five classes of data with the :sidskey:`DataArray_t` structure type:

#. dimensional data (e.g., velocity in units of m/s);
#. nondimensional data normalized by dimensional reference quantities;
#. nondimensional data with associated nondimensional reference quantities;
#. nondimensional parameters (e.g., Reynolds number, pressure coefficient);
#. pure constants (e.g., :math:`π`, :math:`e`). 

The first two of these classes often occur within the same test case, where each piece of data is either dimensional itself or normalized by a dimensional quantity.
The third data class is typical of a completely nondimensional test case, where all field data and reference quantities are nondimensional.
The fourth class, nondimensional parameters, are universal in CFD, although not always consistently defined.
The individual components of nondimensional parameters may be data from any of the first three classes.

Each of the five classes of data requires different information to describe dimensional units or normalization associated with the data.
These requirements are reflected in the structure definition for :sidskey:`DataArray_t`.

The remainder of this section is as follows: The structure type :sidskey:`DataArray_t` is first defined.
Then the class identification and data manipulation is discussed for each of the five data classes. Finally, examples of :sidskey:`DataArray_t` entities are presented.

Definition ``DataArray_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`DataArray_t` describes a multi-dimensional data array of given type, dimensionality and size in each dimension. The data may be dimensional, nondimensional or pure constants. Qualifiers are provided to describe dimensional units or normalization information associated with the data.

.. code-block:: sids

  DataArray_t< DataType, int Dimension, int[Dimension] DimensionValues > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    Data( DataType, Dimension, DimensionValues ) ;                     (r)

    DataClass_t DataClass ;                                            (o)
    
    DimensionalUnits_t DimensionalUnits ;                              (o)

    DimensionalExponents_t DimensionalExponents ;                      (o)
    
    DataConversion_t DataConversion ;                                  (o)
    } ;

.. note::
   
   #. Default names for the :sidsref:`Descriptor_t` list are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`DataArray_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents`, or :sidskey:`DataConversion`.
   #. :sidskey:`Data()` is the only required field for :sidskey:`DataArray_t`. 

:sidskey:`DataArray_t` requires three structure parameters: :sidskey:`Dimension` is the dimensionality of the data array; :sidskey:`DimensionValues` is an array of length :sidskey:`Dimension` that contains the size of the data arrays in each dimension; and :sidskey:`DataType` is the data type of the data stored. :sidskey:`DataType` will usually be real, but other data types are permissible.

The optional entities :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents` and :sidsref:`DataConversion` provide information on dimensional units and normalization associated with the data. The function of these qualifiers is provided in the next section.

This structure type is formulated to describe an array of scalars.
Therefore, for vector quantities (e.g., the position vector or the velocity vector), separate structure entities are required for each component of the vector.
For example, the Cartesian coordinates of a 3-D grid are described by three separate :sidskey:`DataArray_t` entities: one for x, one for y and one for z (see the example for :ref:`Cartesian Coordinates for a 2-D Structured Grid<ex_grid1>`).

Definition ``DataConversion_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`DataConversion_t` contains conversion factors for recovering raw dimensional data from given nondimensional data. These conversion factors are typically associated with nondimensional data that is normalized by dimensional reference quantities.

.. code-block:: sids

  DataConversion_t :=
    {
    real ConversionScale ;                                             (r)
    
    real ConversionOffset ;                                            (r)
    } ;

Given a nondimensional piece of data, :sidskey:`Data(nondimensional)`, the conversion to "raw" dimensional form is:

.. code-block:: sids

  Data(raw) = Data(nondimensional)*ConversionScale + ConversionOffset

These conversion factors are further described in the section :ref:`Nondimensional Data Normalized by Dimensional Quantities<normbydim>`.

Data Manipulation
^^^^^^^^^^^^^^^^^

The optional entities of :sidskey:`DataArray_t` provide information for manipulating the data, including changing units or normalization.
This section describes the rules under which these optional entities operate and the specific manipulations that can be performed on the data.

Within a given instance of :sidskey:`DataArray_t`, the class of data and all information required for manipulations may be completely and precisely specified by the entities :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents` and :sidskey:`DataConversion`.
:sidskey:`DataClass` identifies the class of data and governs the manipulations that can be performed.
Each of the five data classes is treated separately in the subsequent sections.

The entities :sidskey:`DataClass` and :sidskey:`DimensionalUnits` serve special functions in the CGNS hierarchy.
If :sidskey:`DataClass` is absent from a given instance of :sidskey:`DataArray_t`, then its value is determined from "global" data.
This global data may be set at any level of the CGNS hierarchy with the data set at the lowest level taking precedence.
:sidskey:`DimensionalUnits` may be similarly set by global data.
The rules for determining the appropriate set of global data to apply is further detailed in the section :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`.

This alternate functionality provides a measure of economy in describing dimensional units or normalization within the hierarchy.
Examples that make use of global data are available for both :ref:`grid coordinates<grid_example>` and :ref:`flow solutions<flow_example>`.
A complete :ref:`two-zone example<twozone>` case also depicts this alternate functionality.

.. _dimensional:

Dimensional Data
~~~~~~~~~~~~~~~~

If :sidskey:`DataClass` = :sidskey:`Dimensional`, the data is dimensional.
The optional qualifiers :sidskey:`DimensionalUnits` and :sidskey:`DimensionalExponents` describe dimensional units associated with the data.
These qualifiers are provided to specify the system of dimensional units and the dimensional exponents, respectively.
For example, if the data is the x-component of velocity, then :sidskey:`DimensionalUnits` will state that the pertinent dimensional units are, say, :sidskey:`Meter` and :sidskey:`Second`; :sidskey:`DimensionalExponents` will specify that the pertinent dimensional exponents are :sidskey:`LengthExponent = 1` and :sidskey:`TimeExponent = -1`.
Combining the information gives the units m/s. Examples showing the use of these two qualifiers are provided.

If :sidskey:`DimensionalUnits` is absent, then the appropriate set of dimensional units is obtained from "global" data.
The rules for determining this appropriate set of global dimensional units are presented in the section :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`.

If :sidskey:`DimensionalExponents` is absent, then the appropriate dimensional exponents can be determined by convention if the specific instance of :sidskey:`DataArray_t` corresponds to one of the :ref:`standardized data-name identifiers <dataname>`.
Otherwise, the exponents are unspecified. We strongly recommend inclusion of the :sidskey:`DimensionalExponents` qualifier whenever the data is dimensional and the instance of :sidskey:`DataArray_t` is not among the list of standardized identifiers.

.. _normbydim:

Nondimensional Data Normalized by Dimensional Quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If :sidskey:`DataClass` = :sidskey:`NormalizedByDimensional`, the data is nondimensional and is normalized by dimensional reference quantities.
All optional entities in :sidskey:`DataArray_t` are used. :sidskey:`DataConversion` contains factors to convert the nondimensional data to "raw" dimensional data; these factors are :sidskey:`ConversionScale` and :sidskey:`ConversionOffset`.
The conversion process is as follows:

.. code-block:: sids

  Data(raw) = Data(nondimensional)*ConversionScale + ConversionOffset

where :sidskey:`Data(nondimensional)` is the original nondimensional data, and :sidskey:`Data(raw)` is the converted raw data.
This converted raw data is dimensional, and the optional qualifiers :sidskey:`DimensionalUnits` and :sidskey:`DimensionalExponents` describe the appropriate dimensional units and exponents.
Note that :sidskey:`DimensionalUnits` and :sidskey:`DimensionalExponents` also describe the units for :sidskey:`ConversionScale` and :sidskey:`ConversionOffset`.

If :sidskey:`DataConversion` is absent, the equivalent defaults are :sidskey:`ConversionScale = 1` and :sidskey:`ConversionOffset = 0`.
If either :sidskey:`DimensionalUnits` or :sidskey:`DimensionalExponents` is absent, follow the rules described in the previous section.

Note that functionally there is little difference between these first two data classes (:sidskey:`DataClass` = :ref:`Dimensional <dimensional>` and :sidskey:`NormalizedByDimensional`).
In the first case the data is dimensional, and in the second, the converted raw data is dimensional.
Also, the equivalent defaults for :sidskey:`DataConversion` produce no changes in the data; hence, it is almost the same as stating the original data is dimensional.

Nondimensional Data Normalized by Unknown Dimensional Quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If :sidskey:`DataClass` = :sidskey:`NormalizedByUnknownDimensional`, the data is nondimensional and is normalized by some unspecified dimensional quantities.
This type of data is typical of a completely nondimensional test case, where all field data and all reference quantities are nondimensional.

Only the :sidskey:`DimensionalExponents` qualifier is used in this case, although it is expected that this qualifier will be seldom utilized in practice.
For entities of :sidskey:`DataArray_t` that are not among the list of standardized data-name identifiers, the qualifier could provide useful information by defining the exponents of the dimensional form of the nondimensional data.

Rather than providing qualifiers to describe the normalization of the data, we instead dictate that all data of type :sidskey:`NormalizedByUnknownDimensional` in a given database be nondimensionalized consistently.
This is done by picking one set of mass, length, time and temperature scales and normalizing all appropriate data by these scales.
We describe this process in detail in the following. A complete :ref:`two-zone example case <twozone>` is also available that uses a completely nondimensional database with consistent normalization used throughout.

The practice of nondimensionalization within flow solvers and other application codes is quite popular.
The problem with this practice is that to manipulate the data from a given code, one must often know the particulars of the nondimensionalization used.
This largely results from what we call inconsistent normalization - more than the minimum required scales are used to normalize data within the code.
For example, in the *OVERFLOW* flow solver, the following nondimensionalization is used:

.. table::
  
  ======================== ============================= =================================
   :math:`x' = x / L`       :math:`u' = u / (L/T)`        :math:`\rho' = \rho / (M/L^{3})`
   :math:`y' = y / L`       :math:`v' = v / (L/T)`        :math:`p' = p / (M/(LT^{2}))`
   :math:`z' = z / L`       :math:`w' = w / (L/T)`        :math:`\mu' = \mu / (M/(LT))`
  ======================== ============================= =================================

where primed quantities are nondimensional and all others are dimensional. 

Consider an existing database where all field data and all reference data is nondimensional and normalized as shown. Assume the database has a single reference state given by, 

.. table::
  
  ================================ ========================================= =================================================
   :math:`x'_{ref} = x_{ref}  / L`  :math:`u'_{ref} = u_{ref}  / (L/T)`       :math:`\rho'_{ref}  = \rho_{ref}  / (M/L^{3})`
   :math:`y'_{ref} = y_{ref}  / L`  :math:`v'_{ref} = v_{ref}  / (L/T)`       :math:`p'_{ref}  = p_{ref}  / (M/(LT^{2}))`
   :math:`z'_{ref} = z_{ref}  / L`  :math:`w'_{ref} = w_{ref}  / (L/T)`       :math:`\mu'_{ref}  = \mu_{ref}  / (M/(LT))`
  ================================ ========================================= =================================================

If a user wanted to change the nondimensionalization of grid-point pressures, the procedure is straightforward. Let the desired new normalization be given by :math:`p''_{ijk} = p_{ijk} / (\rho_{ref} c_{ref}^{2})`, where all terms on the right-hand-side are *dimensional*, and as such they are unknown to the database user.
However, the desired manipulation is possible using only nondimensional data provided in the database,

.. math::

    p''_{ijk} &\equiv p_{ijk} / (\rho_{ref} c_{ref}^{2}) \\
              &= [p_{ijk} / (M/(LT^{2})] [(M/L^{3}) / \rho_{ref}] [(L/T) / c_{ref}]^{2} \\
              &= p'_{ijk} / (\rho'_{ref} (c'_{ref})^{2})

Thus, the desired renormalization is possible using the database's nondimensional data as if it were actually dimensional. There is, in fact, a high degree of equivalence between dimensional data and consistently normalized nondimensional data. The procedure shown in this example should extend to any desired renormalization, provided the needed :ref:`reference-state quantities <ReferenceState>` are included in the database.

This example points out two stipulations that we now dictate for data in the class :sidskey:`NormalizedByUnknownDimensional`,

   #. All nondimensional data within a given database that has :sidskey:`DataClass = NormalizedByUnknownDimensional` shall be consistently normalized.
   #. Any nondimensional :ref:`reference state <ReferenceState>` appearing in a database should be sufficiently populated with reference quantities to allow for renormalization procedures.

The second of these stipulations is somewhat ambiguous, but good practice would suggest that a flow solver, for example, should output to the database enough static and/or stagnation reference quantities to sufficiently define the state.

A :ref:`two-zone example case <twozone>` is available that shows an example of a well-populated reference state.

With these two stipulations, we contend the following:

- The dimensional scales used to nondimensionalize all data are immaterial, and there is no need to identify these quantities in a CGNS database.
- The dimensional scales need not be reference-state quantities provided in the database. For example, a given database could contain freestream reference state conditions, but all the data is normalized by sonic conditions (which are not provided in the database).
- All renormalization procedures can be carried out treating the data as if it were dimensional with a consistent set of units.
- Any application code that internally uses consistent normalization can use the data provided in a CGNS database without modification or transformation to the code's internal normalization.

Before ending this section, we note that the *OVERFLOW* flow solver mentioned above (or any other application code that internally uses inconsistent normalization) could easily read and write data to a nondimensional CGNS database that conforms to the above stipulations.
On output, the code could renormalize data so it is consistently normalized.
Probably, the easiest method would be to remove the molecular viscosity scale (:math:`\mu_\infty`), and only use :math:`L`, :math:`\rho_\infty` and :math:`c_\infty` for all normalizations (recall these are dimensional scales).
The only change from the above example would be the nondimensionalization of viscosity, which would become :math:`\mu'' = \mu / (\rho_\infty c_\infty L)`.
The code could then output all field data as,

.. table::
  
  =======================================  ==========================================  =================================================================
   :math:`x'_{ijk} = x_{ijk} / L`           :math:`u'_{ijk} = u_{ijk} / c_\infty`        :math:`\rho'_{ijk}  = \rho_{ijk}  / \rho_\infty`
   :math:`y'_{ijk} = y_{ijk} / L`           :math:`v'_{ijk} = v_{ijk} / c_\infty`        :math:`p'_{ijk}  = p_{ijk}  / (\rho_\infty c_\infty^{2})`
   :math:`z'_{ijk} = z_{ijk} / L`           :math:`w'_{ijk} = w_{ijk} / c_\infty`        :math:`\mu'_{ijk}  = \mu_{ijk}  / (\rho_\infty c_\infty^{2} L)`
  =======================================  ==========================================  =================================================================

and output the freestream reference quantities,

.. table::
  
  ==============================================  ============================================================================
    :math:`u'_\infty = u_\infty / c_\infty`        :math:`\rho'_\infty = \rho_\infty / \rho_\infty = 1`
    :math:`v'_\infty = v_\infty / c_\infty`        :math:`p'_\infty = p_\infty / (\rho_\infty c_\infty^{2}) = 1 / \gamma`
    :math:`w'_\infty = w_\infty / c_\infty`        :math:`\mu''_\infty = \mu_\infty / (\rho_\infty c_\infty L) \sim O (1/Re)`
    :math:`c'_\infty = c_\infty / c_\infty = 1`    :math:`L' = L / L = 1`
  ==============================================  ============================================================================

where :math:`\gamma` is the specific heat ratio (assumes a perfect gas) and :math:`Re` is the Reynolds number.

On input, the flow solver should be able to recover its internal normalizations from the data in a nondimensional CGNS database by treating the data as if it were dimensional.

Nondimensional Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

If :sidskey:`DataClass = NondimensionalParameter`, the data is a nondimensional parameter (or array of nondimensional parameters). Examples include Mach number, Reynolds number and pressure coefficient. These parameters are prevalent in CFD, although their definitions tend to vary between different application codes. A list of :ref:`standardized data-name identifiers for nondimensional parameters <dataname_nondim>` is provided.

We distinguish nondimensional parameters from other data classes by the fact that they are *always* dimensionless. In a completely nondimensional database, they are distinct in that their normalization is not necessarily consistent with other data.

Typically, the :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents` and :sidskey:`DataConversion` qualifiers are not used for nondimensional parameters; although, there are a few situations where they may be used (these are discussed below).
Rather than rely on optional qualifiers to describe the normalization, we establish the convention that *any nondimensional parameters should be accompanied by their defining scales*; this is further discussed in the :ref:`section on standardized data-name identifiers for nondimensional parameters <dataname_nondim>`.
An example is Reynolds number defined as :math:`Re = V L_{R} / \nu`, where :math:`V`, :math:`L_R` and :math:`\nu` are velocity, length, and viscosity scales, respectively.
Note that these defining scales may be dimensional or nondimensional data.
We establish the data-name identifiers :sidskey:`Reynolds`, :sidskey:`Reynolds_Velocity`, :sidskey:`Reynolds_Length` and :sidskey:`Reynolds_ViscosityKinematic` for the Reynolds number and its defining scales.
Anywhere an instance of :sidskey:`DataArray_t` is found with the identifier :sidskey:`Reynolds`, there should also be entities for the defining scales.
An :ref:`example of this use for Reynolds number <ex_data5>` is available.

In certain situations, it may be more convenient to use the optional qualifiers of :sidskey:`DataArray_t` to describe the normalization used in nondimensional parameters.
These situations must satisfy two requirements: First, the defining scales are dimensional; and second, the nondimensional parameter is a normalization of a single "raw" data quantity and it is clear what this raw data is.
Examples that satisfy this second constraint are pressure coefficient, where the raw data is static pressure, and lift coefficient, where the raw data is the lift force.
Conversely, Reynolds number is a parameter that violates the second requirement - there are three pieces of raw data rather than one that make up *Re*.
For nondimensional parameters that satisfy these two requirements, the qualifiers :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents` and :sidskey:`DataConversion` may be used as in the section :ref:`Nondimensional Data Normalized by Dimensional Quantities <normbydim>` to recover the raw dimensional data.


Dimensionless Constants
~~~~~~~~~~~~~~~~~~~~~~~
If :sidskey:`DataClass = DimensionlessConstant`, the data is a constant (or array of constants) with no associated dimensional units. The :sidskey:`DimensionalUnits`, :sidskey:`DimensionalExponents` and :sidskey:`DataConversion` qualifiers are not used. 

Data-Array Examples
~~~~~~~~~~~~~~~~~~~

This section presents five examples of data-array entities and illustrates the use of optional information for describing dimensional and nondimensional data.

Example - One-Dimensional Data Array, Constants
"""""""""""""""""""""""""""""""""""""""""""""""

A one-dimensional array of integers; the array is the integers from 1 to 10. The data is pure constants.

.. code-block:: sids

  !  DataType = int
  !  Dimension = 1
  !  DimensionValues = 10
  DataArray_t<int, 1, 10> Data1 =
    {{
    Data(int, 1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ;
    
    DataClass_t DataClass = DimensionlessConstant ;
    }} ;

The structure parameters for :sidskey:`DataArray_t` state the data is an one-dimensional integer array of length ten. The value of :sidskey:`DataClass` indicates the data is :ref:`unitless constants <dimensionless>`.

Example - Two-Dimensional Data Array, Pressures
"""""""""""""""""""""""""""""""""""""""""""""""

A two-dimensional array of pressures with size :math:`11 \times 9` given by the array :math:`P(i,j)`.
The data is dimensional with units of :math:`N/m^{2}` (i.e., :math:`kg/(m s^{2})`).
Note that Pressure is the data-name identifier for static pressure.

.. code-block:: sids

  !  DataType = real
  !  Dimension = 2
  !  DimensionValues = [11,9]
  DataArray_t<real, 2, [11,9]> Pressure =
    {{
    Data(real, 2, [11,9]) = ((P(i,j), i=1,11), j=1,9) ;
    
    DataClass_t DataClass = Dimensional ;

    DimensionalUnits_t DimensionalUnits =
      {{
      MassUnits        = Kilogram ;
      LengthUnits      = Meter ;
      TimeUnits        = Second ;
      TemperatureUnits = TemperatureUnitsNull ;
      AngleUnits       = AngleUnitsNull ;
      }} ;
	
    DimensionalExponents_t DimensionalExponents =
      {{
      MassExponent        = +1 ;
      LengthExponent      = -1 ;
      TimeExponent        = -2 ;
      TemperatureExponent =  0 ;
      AngleExponent       =  0 ;
      }} ;
    }} ;

From the :ref:`data-name identifier conventions <dataname>`, :sidskey:`Pressure` has a floating-point data type; hence, the appropriate structure parameter for :sidskey:`DataArray_t` is :code:`real`.

The value of :sidskey:`DataClass` indicates that the data is :ref:`dimensional <dim>`, and both the dimensional units and dimensional exponents are provided.
:sidskey:`DimensionalUnits` specifies that the units are kilograms, meters, and seconds, and :sidskey:`DimensionalExponents` specifies the appropriate exponents for pressure.
Combining the information gives pressure as :math:`kg/(m s^{2})`.
:sidskey:`DimensionalExponents` could have been defaulted, since the dimensional exponents are part of the :ref:`standardized data-name identifier <dataname>` for :sidskey:`Pressure`.

Note that FORTRAN multidimensional array indexing is used to store the data; this is reflected in the FORTRAN-like implied do-loops for :math:`P(i,j)`.

Example - Three-Dimensional Data Array, Nondimensional Static Enthalpy
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

A 3-D array of size :math:`33 \times 9 \times 17` containing nondimensional static enthalpy.
The data is normalized by freestream velocity as follows:

.. math::

    h'_{ijk} = h_{ijk} / q_{ref}^{2}

where :math:`h'_{ijk}` is nondimensional static enthalpy.
The freestream velocity is dimensional with a value of 10 m/s.

.. code-block:: sids

  !  DataType = real
  !  Dimension = 3
  !  DimensionValues = [33,9,17]
  DataArray_t<real, 3, [33,9,17]> Enthalpy =
    {{
    Data(real, 3, [33,9,17]) = (((H(i,j,k), i=1,33), j=1,9), k=1,17) ;
    
    DataClass_t DataClass = NormalizedByDimensional ;
    
    DataConversion_t DataConversion =
      {{
      real ConversionScale  = 100 ;
      real ConversionOffset = 0 ;
      }} ;
      
    DimensionalUnits_t DimensionalUnits =
      {{
      MassUnits        = MassUnitsNull ;
      LengthUnits      = Meter ;
      TimeUnits        = Second ;
      TemperatureUnits = TemperatureUnitsNull ;
      AngleUnits       = AngleUnitsNull ;
      }} ;
	
    DimensionalExponents_t DimensionalExponents =
      {{
      MassExponent        =  0 ;
      LengthExponent      = +2 ;
      TimeExponent        = -2 ;
      TemperatureExponent =  0 ;
      AngleExponent       =  0 ;
      }} ;
    }} ;

From the list of :ref:`standardized data-name identifiers <dataname>`, the identifier for static enthalpy is :sidskey:`Enthalpy` and its data type is :code:`real`.

The value of :sidskey:`DataClass` indicates that the data is :ref:`nondimensional and normalized by a dimensional reference quantity <normbydim>`.
:sidskey:`DataConversion` provides the conversion factors for recovering the raw static enthalpy, which has units of :math:`m^{2}/s^{2}` as indicated by :sidskey:`DimensionalUnits` and :sidskey:`DimensionalExponents`.
Note that :sidskey:`DimensionalExponents` could have been defaulted using the conventions for the data-name identifier :sidskey:`Enthalpy`. 

Example - Three-Dimensional Data Array, Nondimensional Database
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The previous example for nondimensional enthalpy is repeated for a completely nondimensional database.

.. code-block:: sids

  !  DataType = real
  !  Dimension = 3
  !  DimensionValues = [33,9,17]
  DataArray_t<real, 3, [33,9,17]> Enthalpy =
    {{
    Data(real, 3, [33,9,17]) = (((H(i,j,k), i=1,33), j=1,9), k=1,17) ;
    
    DataClass_t DataClass = NormalizedByUnknownDimensional ;
    }} ;

The value of :sidskey:`DataClass` indicates the appropriate class. 

Example - Data Arrays for Reynolds Number
"""""""""""""""""""""""""""""""""""""""""
Reynolds number of :math:`1.554 \times 10^{6}` based on a velocity scale of :math:`10\ m/s`, a length scale of :math:`2.3\ m` and a kinematic viscosity scale of :math:`1.48 \times 10^{−5}\ m^{2}/s`.
Assume the database has globally set the dimensional units to kilograms, meters, and seconds, and the global default data class to dimensional (:sidskey:`DataClass = Dimensional`).

.. code-block:: sids

  !  DataType = real
  !  Dimension = 1
  !  DimensionValues = 1
  DataArray_t<real, 1, 1> Reynolds =
    {{
    Data(real, 1, 1) = 1.554e+06 ;
    
    DataClass_t DataClass = NondimensionalParameter ;
    }} ;

  DataArray_t<real, 1, 1> Reynolds_Velocity =
    {{
    Data(real, 1, 1) = 10. ;
    }} ;

  DataArray_t<real, 1, 1> Reynolds_Length =
    {{
    Data(real, 1, 1) = 2.3 ;
    }} ;

  DataArray_t<real, 1, 1> Reynolds_ViscosityKinematic =
    {{
    Data(real, 1, 1) = 1.48e-05 ;
    }} ;

:sidskey:`Reynolds` contains the value of the Reynolds number, and the value of its :sidskey:`DataClass` qualifier designates it as a :ref:`nondimensional parameter <nondimparam>`. By conventions for :ref:`standardized data-name identifiers for nondimensional parameters <dataname_nondim>`, the defining scales are contained in the associated entities :sidskey:`Reynolds_Velocity`, :sidskey:`Reynolds_Length`, and :sidskey:`Reynolds_ViscosityKinematic`.
Since each of these entities contain no qualifiers, global information is used to decipher that they are all dimensional with mass, length, and time units of kilograms, meters, and seconds.
The structure parameters for each :sidskey:`DataArray_t` entity state that they contain a real scalar.

If a user wanted to convey the dimensional units of the defining scales using optional qualifiers of :sidskey:`DataArray_t`, then the last three entities in this example would have a form similar to that in the :ref:`Two-Dimensional Data Array example <ex_data2>`.


.. last line
