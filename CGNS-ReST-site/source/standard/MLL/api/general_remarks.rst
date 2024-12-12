.. _MLLGeneralRemarks-ref:

#################
General Remarks
#################

********************************************
   Acquiring the Software and Documentation
********************************************

.. _Acquiring-ref:

The CGNS Mid-Level Library may be downloaded from the `CGNS site <https://github.com/CGNS/CGNS>`_. The manual,
as well as the other CGNS documentation is available from the `CGNS documentation website <https://cgns.org>`_.

****************************************
    Organization of This Manual
****************************************

The sections that follow describe the Mid-Level Library functions in detail. The first three sections cover
`basic file operations <../../MLL/api/c_api.html#file-and-library-operations>`_ (i.e., opening and
closing a CGNS file, and CGNS internal configuration options),
`accessing a specific node in a CGNS database <../../MLL/api/c_api.html#accessing-a-node>`_,
and `error handling <../../MLL/api/c_api.html#error-handling>`_. The remaining sections describe the functions
used to read, write, and modify nodes and data in a CGNS database. These sections basically follow the
organization used in the Section :ref:`Detailed CGNS Node Descriptions <FMMNodeDescriptions>`.

****************************************
    Syntax
****************************************

The API descriptions are structured as follows. First, a brief overview is provided, followed by an optional,
more detailed explanation. Next, the argument parameters are listed, accompanied by descriptions of each variable.
Finally, there is a summary of the return value. Note, as of CGNS-3.1.0, some of the arguments to the Mid-Level Library
have changed from *int* to *cgsize_t* to support 64-bit data. Changed APIs can quickly be identified by
searching for *cgsize_t*.

.. MLL_Language-ref:

****************************************
    Language
****************************************

The CGNS Mid-Level Library is written in C, but each function has a Fortran counterpart.
All function names start with "*cg_*". The Fortran functions have the same name as 
their C counterpart with the addition of the suffix "*_f*".

****************************************
    Character Strings
****************************************

All data structure names and labels in CGNS are limited to 32 characters. 
When reading a file, it is advised to pre-allocate the character string
variables to 32 characters in Fortran, and 33 in C (to include the string terminator).
Other character strings, such as the CGNS file name or descriptor text, are unlimited in length. 
The Mid-Level Library will create the space for unlimited-length character strings; it is 
then the application's responsibility to release this space by a call to cg_free.

****************************************
    Error Status
****************************************
All C functions return an integer value representing the error status. All Fortran functions have an
additional parameter, *ier*, which contains the error status value. An error status different
from zero implies that an error occurred. The error message can be printed using the
:ref:`error handling functions<errorhandling-ref>` of the CGNS library. The error codes are
coded in the C and Fortran include files *cgnslib.h* and the CGNS module (or *cgnslib_f.h*).

.. _Typedefs-ref:

****************************************
    Typedefs
****************************************

Beginning with CGNS-3.1.0, two new typedef variables have been introduced to support 64-bit mode. The *cglong_t* typedef
is always a 64-bit integer, and ``cgsize_t`` will be either a 32-bit or 64-bit integer, depending on how the library was built.
Many of the C functions in the MLL have been changed to use ``cgsize_t`` instead of *int* in the arguments. These functions
include any that may exceed the 2Gb limit of an int, e.g., zone dimensions, element data, boundary conditions, and connectivity.
In Fortran, all integer data is taken to be *INTEGER\*4* for 32-bit and *INTEGER\*8* for 64-bit builds. 

..
 TODO:MSB: I'm not entirely sure that the last sentence is accurate or what specific data it refers to.

Several types of variables are defined using typedefs in the *cgnslib.h* file. These are intended to facilitate
the implementation of CGNS in C. These variable types are defined as an enumeration of keywords admissible for
any variable of these types. The file *cgnslib.h* must be included in any C application programs that use these
data types.

Fortran defines the same keywords as integer parameters in the *CGNS* module (previously *cgnslib_f.h*).
Such variables should be declared as *integer* in Fortran applications. The *CGNS* module (previously *cgnslib_f.h*)
must be included in any Fortran application using these keywords.

.. note::
         The first two enumerated values in these lists, xxxNull and xxxUserDefined, are only
         available in the C interface, and are provided in the advent that your C compiler does
         strict type checking. In Fortran, these values are replaced by the numerically
         equivalent *CG_Null* and *CG_UserDefined*. These values are also defined in the C interface. Thus,
         either form may be used. The function prototypes for the MLL use *CG_Null*
         and *CG_UserDefined*, rather than the more specific values.

.. toctree::

   enums

****************************************
    Character Names for Typedefs
****************************************

The CGNS library defines character arrays that map the typedefs above to character strings.
These are global arrays dimensioned to the size of each list of typedefs. To retrieve a character 
string representation of a typedef, use the typedef value as an index to the appropriate character array. 
For example, to retrieve the string "*Meter*" for the ``LengthUnits_t`` Meter typedef, use ``LengthUnitsName[Meter]``. 
Functions are available to retrieve these names without the need for direct global data access. These functions 
also do bounds checking on the input, and if out of range, will return the string "<invalid>". An additional 
benefit is that these will work from within a Windows DLL, and are thus the recommended access technique. 
The routines have the same name as the global data arrays, but with a "*cg_*" prepended. 
For the example above, use ``cg_LengthUnitsName(Meter)``.

=============================
Typedef Name Access Functions 
=============================

.. doxygenfunction:: cg_MassUnitsName
.. doxygenfunction:: cg_LengthUnitsName
.. doxygenfunction:: cg_TimeUnitsName
.. doxygenfunction:: cg_TemperatureUnitsName
.. doxygenfunction:: cg_ElectricCurrentUnitsName
.. doxygenfunction:: cg_SubstanceAmountUnitsName
.. doxygenfunction:: cg_LuminousIntensityUnitsName
.. doxygenfunction:: cg_DataClassName
.. doxygenfunction:: cg_GridLocationName
.. doxygenfunction:: cg_BCDataTypeName
.. doxygenfunction:: cg_GridConnectivityTypeName
.. doxygenfunction:: cg_PointSetTypeName
.. doxygenfunction:: cg_GoverningEquationsTypeName
.. doxygenfunction:: cg_ModelTypeName
.. doxygenfunction:: cg_BCTypeName
.. doxygenfunction:: cg_DataTypeName
.. doxygenfunction:: cg_ElementTypeName
.. doxygenfunction:: cg_ZoneTypeName
.. doxygenfunction:: cg_RigidGridMotionTypeName
.. doxygenfunction:: cg_ArbitraryGridMotionTypeName
.. doxygenfunction:: cg_SimulationTypeName
.. doxygenfunction:: cg_WallFunctionTypeName
.. doxygenfunction:: cg_AreaTypeName
.. doxygenfunction:: cg_AverageInterfaceTypeName

****************************************
    64-bit C Portability and Issues
****************************************
If you use the ``cgsize_t`` data type in new code, it will work in both 32 and 64-bit compilation modes.
In order to support CGNS versions prior to 3.1, you may also want to add something like this to your code:

.. code-block:: C

  #if CGNS_VERSION < 3100
  #define cgsize_t int
  #endif

Existing code that uses *int* will not work with a CGNS 3.1 library compiled in 64-bit mode. You may want
to add something like this to your code:

.. code-block:: C

  #if CGNS_VERSION >= 3100 && CG_BUILD_64BIT
  #error does not work in 64 bit mode
  #endif

or modify your code to use ``cgsize_t``.

.. _CallingCGNSFortran-ref:

****************************************
    Calling CGNS from Fortran
****************************************

Starting with CGNS-3.3.0, a new CGNS module was added to the library. Fortran programs can 
use the new module by adding ``USE CGNS``. The use of ``include 'cgnslib_f.h'`` is deprecated as of CGNS-3.3.0.

.. note::

  **Fortran Helper Functions**

  .. code-block:: Fortran

     FUNCTION cg_get_type(buf)

  Returns the data type of ``buf``, where ``buf`` is a scalar. This is a useful function
  for automatically passing the correct data type of a buffer.

  For example:

  .. code-block:: Fortran

     CALL cg_coord_read_f(cg,base,zone,coordname,cg_get_type(mydata(1)),rmin,DataSize,mydata,ier) 

.. _CGNSFortranPort-ref:

****************************************
    64-bit Fortran Portability 
****************************************

Starting with CGNS-3.3.0, the Fortran APIs have the following specifications (recommended for portability):

    * Fortran arguments should be declared as the default ``INTEGER`` if the corresponding argument in the C API is declared as an ``int``.
    * Fortran arguments should be declared as ``INTEGER(cgsize_t)`` if the corresponding argument in the C API is declared as ``cgsize_t``.
    * Fortran arguments should be declared as type ``INTEGER(cgenum_t)`` if the corresponding argument in the C API is declared as :ref:`enumerated values (enums)<Typedefs-ref>`. 

An integer parameter,`` CG_BUILD_64BIT``, can be used to tell the size of ``cgsize_t``, which will be set to 1 in 64-bit mode and 0 otherwise. You may use this parameter to check at run time if the CGNS library has been compiled in 64-bit mode or not, as in:

.. code-block:: Fortran

  IF (CG_BUILD_64BIT .NE. 0) THEN
      PRINT *,'will not work in 64-bit mode'
      STOP
  ENDIF

If you are using a CGNS library prior to version 3.1, this parameter will not be defined, and you will need to
rely on your compiler initializing all undefined values to 0 (not always the case) for this test to work.

.. warning::

   **The following practice is not recommended!**

   If you have explicitly defined your default integers, which are passed to the CGNS library as ``INTEGER*8``, or used 
   a compiler option to promote implicit integers to ``INTEGER*8``, then you MUST compile the CGNS library with the same 
   compiler option to promote implicit integers to ``INTEGER*8``. If you really must promote all integers 
   to ``INTEGER*8`` in your code, and you are not able to compile the CGNS library with the same compiler options, then 
   it is recommended that all arguments in the CGNS Fortran APIs should be declared as ``INTEGER(C_INT)`` if the 
   corresponding argument in the C API is declared as an ``int``.
