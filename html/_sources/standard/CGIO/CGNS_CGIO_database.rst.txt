.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIODatabase:
   
Database-Level Routines
=======================

cgio_is_supported
-----------------
  :C Signature:
    .. c:function:: int cgio_is_supported(int file_type)

  :Fortran Signature:
    .. f:subroutine:: cgio_is_supported_f(file_type, ier)
  
  :Parameters:
      - :code:`int file_type`
         IN: Type of database file. acceptable values are :code:`CGIO_FILE_NONE`, :code:`CGIO_FILE_ADF`, :code:`CGIO_FILE_HDF5` and :code:`CGIO_FILE_ADF2`.

  :Returns:         ier - Error status
  
  :Modes:  `- - -`

  :Description:
    Determines if the database type given by :code:`file_type` is supported by the library. Returns 0 if supported, else :code:`CGIO_ERR_FILE_TYPE` if not. :code:`CGIO_FILE_ADF` is always supported; :code:`CGIO_FILE_HDF5` is supported if the library was built with HDF5; and :code:`CGIO_FILE_ADF2` is supported when built in 32-bit mode.

cgio_check_file
-----------------
  :C Signature:
    .. c:function:: int cgio_check_file(const char *filename, int *file_type)

  :Fortran Signature:
    .. f:subroutine:: cgio_check_file_f(filename, file_type, ier)
  
  :Parameters:
      - :code:`const char *filename`
          IN: Name of the database file, including path name if necessary. There is no limit on the length of this character variable.

      - :code:`int *file_type`
          OUT: Type of database file. acceptable values are :code:`CGIO_FILE_NONE`, :code:`CGIO_FILE_ADF`, :code:`CGIO_FILE_HDF5` and :code:`CGIO_FILE_ADF2`.
   

  :Returns:         ier - Error status
  
  :Modes:  `- - -`

  :Description:
    Checks the file filename to determine if it is a valid database. If so, returns 0 and the type of database in file_type, otherwise returns an error code and file_type will be set to CGIO_FILE_NONE.

cgio_open_file
--------------
  :C Signature:
    .. c:function:: int cgio_open_file(const char *filename, int file_mode, int file_type, int *cgio_num)

  :Fortran Signature:
    .. f:subroutine:: cgio_open_file_f(filename, file_mode, file_type, cgio_num, ier)
  
  :Parameters:
     - :code:`char* filename`
        IN: Name of the database file, including path name if necessary. There is no limit on the length of this character variable. 
     - :code:`int file_type`
        IN: Type of database file. acceptable values are :code:`CGIO_FILE_NONE`, :code:`CGIO_FILE_ADF`, :code:`CGIO_FILE_HDF5` and :code:`CGIO_FILE_ADF2`.
     - :code:`int file_mode`
        IN: Mode used for opening the file. The supported modes are. CGIO_MODE_READ, CGIO_MODE_WRITE, and CGIO_MODE_MODIFY.
     - :code:`int* cgio_num`
        OUT: Indentifier for the open database file.

  :Returns:         ier - Error status
  
  :Modes:  `r w m`

  :Description:
    Opens a database file of the specified type and mode. If successfull, returns 0, and the database identifier in cgio_num, otherwise returns an error code. The database identifier is used to access the database in subsequent function calls.

    The mode in which the database is opened is given by file_mode, which may take the value CGIO_MODE_READ, CGIO_MODE_WRITE, or CGIO_MODE_MODIFY. New databases should be opened with CGIO_MODE_WRITE, while existing databases are opened with either CGIO_MODE_READ (for read-only access) or CGIO_MODE_MODIFY (for read/write access).

    A specific database type may be specified by file_type, which may be one of CGIO_FILE_NONE, CGIO_FILE_ADF, CGIO_FILE_HDF5, or CGIO_FILE_ADF2. When opening a database in write mode, CGIO_FILE_NONE indicates that the default database type should be used, otherwise the specified database type will be opened. When opening in read or modify mode, CGIO_FILE_NONE indicates that any database type is acceptable, otherwise if the database type does not match that given by file_type an error will be retuned.


cgio_close_file
---------------
  :C Signature:
    .. c:function:: int cgio_close_file(int cgio_num)

  :Fortran Signature:
    .. f:subroutine:: cgio_close_file_f(cgio_num, ier)
  
  :Parameters:
     - :code:`int cgio_num`
        OUT: Indentifier for the open database file. 

  :Returns:         ier - Error status
  
  :Modes:  `r w m`

  :Description:
    Closes the database given by cgio_num. Returns 0 for success, else an error code. 

cgio_get_file_type
------------------
  :C Signature:
    .. c:function:: int cgio_get_file_type(int cgio_num, int *file_type)

  :Fortran Signature:
    .. f:subroutine:: cgio_get_file_type_f(cgio_num, file_type, ier)
  
  :Parameters:
     - :code:`int cgio_num`
        IN: Indentifier for the open database file.
     - :code:`int *file_type`
        OUT: Type of database file. acceptable values are :code:`CGIO_FILE_NONE`, :code:`CGIO_FILE_ADF`, :code:`CGIO_FILE_HDF5` and :code:`CGIO_FILE_ADF2`.

  :Returns:         ier - Error status
  
  :Modes:  `r w m`

  :Description:
    Gets the type of the database given by cgio_num. Returns 0 and the type in file_type if successfull, else an error code. 


cgio_get_root_id
----------------
  :C Signature:
    .. c:function:: int cgio_get_root_id(int cgio_num, double *rootid)

  :Fortran Signature:
    .. f:subroutine:: cgio_get_root_id_f(cgio_num, rootid, ier)
  
  :Parameters:
     - :code:`int cgio_num`
        IN: Indentifier for the open database file.
     - :code:`double *rootid`
        OUT: Node identifier for the root node of the database.

  :Returns:         ier - Error status
  
  :Modes:  `r w m`

  :Description:
    Gets the unique node identifier for the root node in the database given by :code:`cgio_num`. Returns 0 and the identifier in :code:`rootid` if successfull, else an error code.



.. last line
