.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLPhysicalData:
   
Physical Data
-------------

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Data Arrays`_
   * - ``cg_array_write``
     - Write data array
   * - ``cg_array_general_write``
     - Write shaped array to a subset of data array
   * - ``cg_narrays``
     - Get number of data arrays under current node
   * - ``cg_array_info``
     - Get data array info
   * - ``cg_array_read``
     - Read data array
   * - ``cg_array_read_as``
     - Read data array as a certain type
   * - ``cg_array_general_read``
     - Read subset of data array to a shaped array


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Data Class`_   
   * - ``cg_dataclass_write``
     - Write data class
   * - ``cg_dataclass_read`` 
     - Read data class 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Data Conversion Factors`_
   * - ``cg_conversion_write``
     - Write conversion factors
   * - ``cg_conversion_info``
     - Get conversion factors data type
   * - ``cg_conversion_read``
     - Read conversion factors 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Dimensional Units`_
   * - ``cg_units_write``
     - Write first five dimensional units
   * - ``cg_unitsfull_write``
     - Write all eight dimensional units
   * - ``cg_nunits``
     - Get number of dimensional units
   * - ``cg_units_read``
     - Read first five dimensional units
   * - ``cg_unitsfull_read``
     - Read all eight dimensional units 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Dimensional Exponents`_
   * - ``cg_exponents_write``
     - Write first five dimensional exponents
   * - ``cg_expfull_write``
     - Write all eight dimensional exponents
   * - ``cg_nexponents``
     - Get number of dimensional exponents
   * - ``cg_exponents_info``
     - Get exponent data type
   * - ``cg_exponents_read``
     - Read first five dimensional exponents
   * - ``cg_expfull_read``
     - Read all eight dimensional exponents 



Data Arrays
^^^^^^^^^^^
Node: DataArray_t (SIDS, File Mapping) 

.. table::
   :widths: 110 15
   
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | C Functions                                                                                                                                                   | Modes   |
   +===============================================================================================================================================================+=========+
   | :out:`ier` = :sig-name:`cg_array_write` (:in:`char *arrayname`, :in:`DataType_t datatype`, :in:`int rank`, :in:`cgsize_t *dimensions`, :in:`void *data`);     | `- w m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_array_general_write` (:in:`char *arrayname`, :in:`DataType_t datatype`, :in:`int rank`, :in:`cgsize_t *dimensions`,                | `- w m` |
   | :in:`cgsize_t *range_min`, :in:`cgsize_t *range_max`, :in:`DataType_t mem_datatype`, :in:`int mem_rank`, :in:`cgsize_t *mem_dimensions`,                      |         |
   | :in:`cgsize_t *mem_range_min`, :in:`cgsize_t *mem_range_max`, :in:`void *data`);                                                                              |         |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_narrays` (:out:`int *narrays`);                                                                                                    | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_array_info` (:in:`int A`, :out:`char *arrayname`, :out:`DataType_t *datatype`, :out:`int *rank`, :out:`cgsize_t *dimensions`);     | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_array_read` (:in:`int A`, :out:`void *data`);                                                                                      | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_array_read_as` (:in:`int A`, :in:`DataType_t datatype`, :out:`void *data`);                                                        | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | :out:`ier` = :sig-name:`cg_array_general_read` (:in:`int A`, :in:`cgsize_t *range_min`, :in:`cgsize_t *range_max`, :in:`DataType_t mem_datatype`,             | `r - m` |
   | :in:`int mem_rank`, :in:`cgsize_t *mem_dimensions`, :in:`cgsize_t *mem_range_min`, :in:`cgsize_t *mem_range_max`, :out:`void *data`);                         |         |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
.. table::
   :widths: 110 15
   
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | Fortran interfaces                                                                                                                                            | Modes   |
   +===============================================================================================================================================================+=========+
   | call ``cg_array_write_f`` (:in:`arrayname`, :in:`datatype`, :in:`rank`, :in:`dimensions`, :in:`data`, :out:`ier`)                                             | `- w m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_array_general_write_f`` (:in:`arrayname`, :in:`datatype`, :in:`rank`, :in:`dimensions`,                                                             | `- w m` |
   | :in:`range_min`, :in:`range_max`, :in:`mem_datatype`, :in:`mem_rank`, :in:`mem_dimensions`,                                                                   |         |
   | :in:`mem_range_min`, :in:`mem_range_max`, :in:`data`, :out:`ier`)                                                                                             |         |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_narrays_f`` (:out:`narrays`, :out:`ier`)                                                                                                            | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_array_info_f`` (:in:`A`, :out:`arrayname`, :out:`datatype`, :out:`rank`, :out:`dimensions`, :out:`ier`)                                             | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_array_read_f`` (:in:`A`, :out:`data`, :out:`ier`)                                                                                                   | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_array_read_as_f`` (:in:`A`, :in:`datatype`, :out:`data`, :out:`ier`)                                                                                | `r - m` |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
   | call ``cg_array_general_read_f`` (:in:`A`, :in:`range_min`, :in:`range_max`, :in:`mem_datatype`,                                                              | `r - m` |
   | :in:`mem_rank`, :in:`mem_dimensions`, :in:`mem_range_min`, :in:`mem_range_max`, :out:`data`, :out:`ier`)                                                      |         |
   +---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:narrays:	   	Number of DataArray_t nodes under the current node.
:A:		Data array index, where 1 ≤ A ≤ narrays.
:arrayname:		Name of the DataArray_t node.
:datatype:		Type of data held in the DataArray_t node. The admissible types are Integer, LongInteger, RealSingle, RealDouble, and Character.
:rank:		Number of dimensions of array in file (max 12). See Node Management Routines in CGIO User's Guide.
:dimensions:		Dimensions of array in file.
:range_min:		Lower range index in file (eg., imin, jmin, kmin).
:range_max:		Upper range index in file (eg., imax, jmax, kmax).
:mem_datatype:		The type of data held in memory. The admissible types are Integer, LongInteger, RealSingle, RealDouble, and Character.
:mem_rank:		Number of dimensions of array in memory (max 12).
:mem_dimensions:		Dimensions of array in memory.
:mem_range_min:		Lower range index in memory (eg., imin, jmin, kmin).
:mem_range_max:		Upper range index in memory (eg., imax, jmax, kmax).
:data:		The data array in memory.
:ier:		Error status. 

The function cg_array_general_write may be used to write from a subset of the array in memory to a subset of the array in the file. When using the partial write, any existing data from range_min to range_max will be overwritten by the new values. All other values will not be affected.

The functions cg_array_general_read and cg_array_general_write allow for type conversion when both reading from and writing to the file.

When using cg_array_general_write and cg_array_general_read, the lower core elements in the file have index 1 for defining range_min and range_max; whereas for the array in memory, defined by mem_rank and mem_dimensions, the lower array elements in memory have index 1 for defining mem_range_min and mem_range_max. The actual lower and upper bounds of the array in memory can be anything. For example, to fully read a two-dimensional 6 × 6 data array with 1 rind plane on each side in the file to an 8 × 8 array in memory (mem_rank = 2 and mem_dimensions = (8,8)), set range_min and range_max to (0,0) and (7,7), and set mem_range_min and mem_range_max to (1,1) and (8,8).

Data Class
^^^^^^^^^^
Node: DataClass_t (SIDS, File Mapping) 



Data Conversion Factors
^^^^^^^^^^^^^^^^^^^^^^^
Node: DataConversion_t (SIDS, File Mapping) 

Dimensional Units
^^^^^^^^^^^^^^^^^
Nodes: DimensionalUnits_t (SIDS, File Mapping) 

Dimensional Exponents
^^^^^^^^^^^^^^^^^^^^^
Node: DimensionalExponents_t (SIDS, File Mapping)

.. last line
