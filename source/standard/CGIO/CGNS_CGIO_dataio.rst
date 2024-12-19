.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIODataIO:
   
Data I/O Routines
=================

cgio_read_data_type
-------------------
:C Signature:
  .. c:function:: int cgio_read_data_type(int cgio_num, double id, const cgsize_t *s_start, const cgsize_t *s_end, const cgsize_t *s_stride, const char *m_data_type,      int m_num_dims, const cgsize_t *m_dims, const cgsize_t *m_start, const cgsize_t *m_end, const cgsize_t *m_stride, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_read_data_type_f(cgio_num, id, s_start, s_end, s_stride, m_data_type, m_num_dims, m_dims, m_start, m_end, m_stride, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`s_start`
      - Starting indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_end`
      - Ending indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_stride`
      - Step increment for data in the database.
    * - :code:`m_num_dims`
      - Number of dimensions for data in memory.
    * - :code:`m_dims`
      - Dimension values for data in memory.
    * - :code:`m_start`
      - Starting indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_end`
      - Ending indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_stride`
      - Step increment for data in memory.
    * - :code:`m_data_type`
      - Type of data being used for data in memory. One of "I4", "I8", "U4", "U8", "R4", "R8", "C1", or "B1".
    * - :code:`data`
      - Array of data to be read.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  This routine provides general purpose read capabilities from the node identified by :code:`id` in the database given by :code:`cgio_num`. It allows for a general specification of the starting location within the data as well as fixed step lengths (strides) through the data from the initial position.
  This capability works for both the data on disk and the data being stored in memory. One set of vectors (:code:`s_start`, :code:`s_end` and :code:`s_stride`) are used to describe the mapping of the data within the node, and a second set of vectors (:code:`m_start`, :code:`m_end` and :code:`m_stride`) are used to describe the mapping of the desired data within memory.
  
  The memory dimensions are given by :code:`m_num_dims` and :code:`m_dims`. There is no requirement that the node dimensions and memory dimensions match, only that the total number of values to be read are the same for the node and memory specifications.
  
  The data are stored in both memory and on disk in "Fortran ordering". That is, the first index varies the fastest, and indexing starts at 1. Negative indexing is not allowed.

  Be careful when writing data using :c:func:`cgio_write_all_data` and then using :c:func:`cgio_read_data_type` to randomly access the data. :c:func:`cgio_write_all_data_type` takes a starting address in memory and writes N words to disk, making no assumption as to the order of the data. :c:func:`cgio_read_data_type` assumes that the data have Fortran-like ordering to navigate through the data in memory and on disk. It assumes that the first dimension varies the fastest.
  It would be easy for a C program to use the default array ordering (last dimension varying fastest) and write the data out using :c:func:`cgio_write_all_data_type`. Then another program might use :c:func:`cgio_read_data_type` to access a subsection of the data, and the routine would not return what was expected.

  There can be a significant performance penalty for using :c:func:`cgio_read_data_type` when compared with :c:func:`cgio_read_all_data_type`. If performance is a major consideration, it is best to organize data to take advantage of the speed of :c:func:`cgio_read_all_data_type`.

  The function returns 0 on success, else an error code.


cgio_read_all_data_type
-----------------------
:C Signature:
  .. c:function:: int cgio_read_all_data_type(int cgio_num, double id, const char *m_data_type, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_read_all_data_type_f(cgio_num, id, m_data_type, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`m_data_type`
      - Type of data being used for data in memory. One of "I4", "I8", "U4", "U8", "R4", "R8", "C1", or "B1".
    * - :code:`data`
      - Array of data to be read.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Reads all the data from the node identified by :code:`id` in the database given by :code:`cgio_num`. On success, the function returns 0 and the data in :code:`data`, else an error code is returned. Note: Data is returned in Fortran indexing order. 


cgio_read_block_data_type
-------------------------
:C Signature:
  .. c:function:: int cgio_read_block_data_type(int cgio_num, double id, cgsize_t b_start, cgsize_t b_end, const char *m_data_type, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_read_block_data_type_f(cgio_num, id, b_start, b_end, m_data_type, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`b_start`
      - Starting offset (index) for the data in the database. Fortran indexing is used (starting at 1).
    * - :code:`b_end`
      - Ending offset (index) for the data in the database. Fortran indexing is used (starting at 1).
    * - :code:`m_data_type`
      - Type of data being used for data in memory. One of "I4", "I8", "U4", "U8", "R4", "R8", "C1", or "B1".
    * - :code:`data`
      - Array of data to be read.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Reads a contiguous block of data from the node identified by :code:`id` in the database given by :code:`cgio_num`.
  On success, the function returns 0 and the data in :code:`data`, else an error code is returned. The starting index is given by :code:`b_start` and the end by :code:`b_end`.
  Note: Fortran indexing order for multi-dimensional data is used when computing the starting and ending locations.

cgio_write_data
---------------
:C Signature:
  .. c:function:: int cgio_write_data(int cgio_num, double id, const cgsize_t *s_start, const cgsize_t *s_end, const cgsize_t *s_stride, int m_num_dims, const cgsize_t *m_dims, const cgsize_t *m_start, const cgsize_t *m_end, const cgsize_t *m_stride, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_write_data_f(cgio_num, id, s_start, s_end, s_stride, m_num_dims, m_dims, m_start, m_end, m_stride, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`s_start`
      - Starting indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_end`
      - Ending indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_stride`
      - Step increment for data in the database.
    * - :code:`m_num_dims`
      - Number of dimensions for data in memory.
    * - :code:`m_dims`
      - Dimension values for data in memory.
    * - :code:`m_start`
      - Starting indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_end`
      - Ending indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_stride`
      - Step increment for data in memory.
    * - :code:`data`
      - Array of data to be read or written.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  This function is similar to :c:func:`cgio_read_data_type`, but writes the data from memory to the node.


cgio_write_data_type
--------------------
:C Signature:
  .. c:function:: int cgio_write_data_type(int cgio_num, double id, const cgsize_t *s_start, const cgsize_t *s_end, const cgsize_t *s_stride, const char *m_data_type, int m_num_dims, const cgsize_t *m_dims, const cgsize_t *m_start, const cgsize_t *m_end, const cgsize_t *m_stride, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_write_data_type_f(cgio_num, id, s_start, s_end, s_stride, m_data_type, m_num_dims, m_dims, m_start, m_end, m_stride, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`s_start`
      - Starting indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_end`
      - Ending indices for data in the database. Fortran indexing is used (starting at 1).
    * - :code:`s_stride`
      - Step increment for data in the database.
    * - :code:`m_num_dims`
      - Number of dimensions for data in memory.
    * - :code:`m_dims`
      - Dimension values for data in memory.
    * - :code:`m_start`
      - Starting indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_end`
      - Ending indices for data in memory. Fortran indexing is used (starting at 1).
    * - :code:`m_stride`
      - Step increment for data in memory.
    * - :code:`m_data_type`
      - Type of data being used for data in memory. One of "I4", "I8", "U4", "U8", "R4", "R8", "C1", or "B1".
    * - :code:`data`
      - Array of data to be read or written.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  This function is similar to :c:func:`cgio_read_data_type`, but writes the data from memory to the node.



cgio_write_all_data
-------------------
:C Signature:
  .. c:function:: int cgio_write_all_data(int cgio_num, double id, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_write_all_data_f(cgio_num, id, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`data`
      - Array of data to be written.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  This function is similar to :c:func:`cgio_read_all_data_type`, but writes the data from memory to the node.


cgio_write_all_data_type
------------------------
:C Signature:
  .. c:function:: int cgio_write_all_data_type(int cgio_num, double id, const char *m_data_type, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_write_all_data_type_f(cgio_num, id, m_data_type, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`m_data_type`
      - Type of data being used for data in memory. One of "I4", "I8", "U4", "U8", "R4", "R8", "C1", or "B1".
    * - :code:`data`
      - Array of data to be written.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  This function is similar to :c:func:`cgio_read_all_data_type`, but writes the data from memory to the node.



cgio_write_block_data
---------------------
:C Signature:
  .. c:function:: int cgio_write_block_data(int cgio_num, double id, cgsize_t b_start, cgsize_t b_end, void *data)

:Fortran Signature:
  .. f:subroutine:: cgio_write_block_data_f(cgio_num, id, b_start, b_end, data, ier)

:Parameters:
  .. list-table::
    :widths: 15 85

    * - :code:`cgio_num`
      - Database identifier.
    * - :code:`id`
      - Node identifier.
    * - :code:`b_start`
      - Starting offset (index) for the data in the database. Fortran indexing is used (starting at 1).
    * - :code:`b_end`
      - Ending offset (index) for the data in the database. Fortran indexing is used (starting at 1).
    * - :code:`data`
      - Array of data to be written.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  This function is similar to :c:func:`cgio_read_block_data_type`, but writes the data from memory to the node.


.. last line
