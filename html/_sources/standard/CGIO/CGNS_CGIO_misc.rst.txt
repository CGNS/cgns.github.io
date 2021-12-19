.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIOMiscellaneous:
   
Miscellaneous Routines
======================

cgio_flush_to_disk
------------------
:C Signature:
  .. c:function:: int cgio_flush_to_disk(int cgio_num)

:Fortran Signature:
  .. f:subroutine:: cgio_flush_to_disk_f(cgio_num, ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`cgio_num`
      - IN: Database identifier.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- w m`

:Description:
  Forces any buffered data in the database manager to be written to disk. Returns 0 if successfull, else an error code.

cgio_library_version
--------------------

:C Signature:
  .. c:function:: int cgio_library_version(int cgio_num, char *version)

:Fortran Signature:
  .. f:subroutine:: cgio_library_version_f(cgio_num, version, ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`version`
      - OUT: 32-byte character string containing the database library version.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the current library version for the database given by :code:`cgio_num`.
  The version is returned in version which is of maximum length :code:`CGIO_MAX_VERSION_LENGTH` (32).
  In C, version should be dimensioned at least 33 in the calling routine to allow for the terminating :code:`'0'`. The function returns 0 if successfull, else an error code. 
 

cgio_file_version
-----------------
:C Signature:
  .. c:function:: int cgio_file_version(int cgio_num, char *file_version, char *creation_date, char *modified_date)

:Fortran Signature:
  .. f:subroutine:: cgio_file_version_f(cgio_num, file_version, creation_date, modified_date, ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`cgio_num`
      - IN: Database identifier.
    * - :code:`file_version`
      - OUT: 32-byte character string containing the database file version.
    * - :code:`creation_date`
      - OUT: 32-byte character string containing the database file creation date.
    * - :code:`modified_date`
      - OUT: 32-byte character string containing the last modification date for the database file.

:Returns:    :code:`ier` - Error status
  
:Modes:  `r w m`

:Description:
  Gets the version, creation and last modified dates, for the database file given by :code:`cgio_num`.
  The version is returned in :code:`file_version`, which is of maximum length :code:`CGIO_MAX_VERSION_LENGTH` (32).
  The creation date is returned in :code:`creation_date`, and the last modified date in :code:`modified_date`,
  which are of maximum length :code:`CGIO_MAX_DATE_LENGTH` (32).
  In C, these should be dimensioned at least 33 in the calling routine to allow for the terminating :code:`'0'`.
  The function returns 0 if successfull, else an error code.


.. last line
