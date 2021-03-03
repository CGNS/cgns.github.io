.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIOErrorHandling:
   
Error Handling Routines
=======================

cgio_error_message
------------------
:C Signature:
  .. c:function:: int cgio_error_message(char *error_msg)

:Fortran Signature:
  .. f:subroutine:: cgio_error_message_f(error_msg,  ier)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`error_msg`
      - OUT: Error message from CGIO or the underlying database manager.

:Returns:    :code:`ier` - Error status
  
:Modes:  `- - -`

:Description:
  Gets the error message for the last error encountered, and returns it in :code:`error_msg`, Maximum length of the error message is :code:`CGIO_MAX_ERROR_LENGTH` (80). In C, :code:`error_msg` should be dimensioned at least 81 in the calling routine to allow for the terminating :code:`'0'`. The function returns the error code corresponding to the error message.


cgio_error_code
---------------
:C Signature:
  .. c:function:: void cgio_error_code(int *errcode, int *file_type)

:Fortran Signature:
  .. f:subroutine:: cgio_error_code_f(errcode, file_type)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`errcode`
      - OUT: The last error code from CGIO or the underlying database manager.
    * - :code:`file_type`
      - OUT: Where the last error was encountered. :code:`CGIO_FILE_NONE` for an error coming from CGIO, else the type of database.
  
:Modes:  `- - -`

:Description:
  Returns the last error code in :code:`errcode` and where is was generated in :code:`file_type`.
  If the error code is < 0, then the error is from the CGIO library, and :code:`file_type` will be :code:`CGIO_FILE_NONE`, otherwise :code:`file_type` will be the type of database.
 

cgio_error_exit
---------------
:C Signature:
  .. c:function:: void cgio_error_exit(const char *msg)

:Fortran Signature:
  .. f:subroutine:: cgio_error_exit_f(msg)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`msg`
      - IN: An additional message to print, which prefixes the error message before exiting. This may be :code:`NULL` or an empty string, in which case it is not printed.
  
:Modes:  `- - -`

:Description:
  Prints :code:`msg` and any error message to :code:`stderr` and exits.
  The exit code will be :code:`abort_flag` if it is set, else −1.
  If :code:`msg` is :code:`NULL` or an empty string, then it is not printed.

cgio_error_abort
----------------
:C Signature:
  .. c:function:: void cgio_error_abort(int abort_flag)

:Fortran Signature:
  .. f:subroutine:: cgio_error_abort_f(abort_flag)

:Parameters:
  .. list-table::
    :widths: 15 85
    
    * - :code:`abort_flag`
      - IN: Abort on error flag.
  
:Modes:  `- - -`

:Description:
  Sets the flag to abort (exit) when an error is encountered.
  If :code:`abort_flag` is non-zero, then an error in the CGIO routines or database managers will cause :c:func:`cgio_error_exit` to be called. The exceptions are :c:func:`cgio_is_supported`, :c:func:`cgio_check_file`, and :c:func:`cgio_is_link`.
  These routines will not cause an abort on an error.



Error Messages
--------------
This is a list of the possible return codes from the CGIO routines along with the error messages.

.. table::

  =======   ============================================
   Code     Error Message
  =======   ============================================
     0      no error
    −1      invalid cgio index
    −2      malloc/realloc failed
    −3      unknown file open mode
    −4      invalid file type
    −5      filename is NULL or empty
    −6      character string is too small
    −7      file was not found
    −8      pathname is NULL or empty
    −9      no match for pathname
    −10     error opening file for reading
    −11     file opened in read-only mode
    −12     NULL or empty string
    −13     invalid configure option
    −14     rename of tempfile file failed
    −15     too many open files
    −16     dimensions exceed that for a 32-bit integer
  =======   ============================================

Error codes from the ADF and HDF5 database managers.

.. table::

    =======   =============================================================================
     Code     Error Message
    =======   =============================================================================
       1        Integer number is less than a given minimum value
       2        Integer value is greater than given maximum value
       3        String length of zero of blank string detected
       4        String length longer than maximum allowable length
       5        String length is not an ASCII-Hex string
       6        Too many ADF files opened
       7        ADF file status was not recognized
       8        ADF file open error
       9        ADF file not currently opened
      10        ADF file index out of legal range
      11        Block/offset out of legal range
      12        A string pointer is null
      13        FSEEK error
      14        FWRITE error
      15        FREAD error
      16        Internal error: Memory boundary tag bad
      17        Internal error: Disk boundary tag bad
      18        File Open Error: NEW - File already exists (see Note [1]_)
      19        ADF file format was not recognized
      20        Attempt to free the RootNode disk information
      21        Attempt to free the FreeChunkTable disk information
      22        File Open Error: OLD - File does not exist (see Note [2]_)
      23        Entered area of unimplemented code
      24        Subnode entries are bad
      25        Memory allocation failed
      26        Duplicate child name under a parent node
      27        Node has no dimensions
      28        Node's number of dimensions is not in legal range
      29        Specified child is not a child of the specified parent
      30        Data-Type is too long
      31        Invalid Data-Type
      32        A pointer is null
      33        Node had no data associated with it
      34        Error zeroing out of memory
      35        Requested data exceeds actual data available
      36        Bad end value
      37        Bad stride values
      38        Minimum value is greater than maximum value
      39        The format of this machine does not match a known signature (see Note [3]_)
      40        Cannot convert to or from an unknown native format
      41        The two conversion formats are equal; no conversion done
      42        The data format is not supported on a particular machine
      43        File close error
      44        Numeric overflow/underflow in data conversion
      45        Bad start value
      46        A value of zero is not allowable
      47        Bad dimension value
      48        Error state must be either a 0 (zero) or a 1 (one)
      49        Dimensional specifications for disk and memory are unequal
      50        Too many link levels are used; may be caused by a recursive link
      51        The node is not a link. It was expected to be a link.
      52        The linked-to node does not exist
      53        The ADF file of a linked node is not accessible
      54        A node ID of 0.0 is not valid
      55        Incomplete data when reading multiple data blocks
      56        Node name contains invalid characters
      57        ADF file version incompatible with this library version
      58        Nodes are not from the same file
      59        Priority stack error
      60        Machine format and file format are incomplete
      61        Flush error
      62        The node ID pointer is NULL
      63        The maximum size for a file exceeded
      64        Dimensions exceed that for a 32-bit integer
      70        H5Glink:soft link creation failed
      71        Node attribute doesn't exist
      72        H5Aopen:open of node attribute failed
      73        H5Iget_name:failed to get node path from ID
      74        H5Gmove:moving a node group failed
      75        H5Gunlink:node group deletion failed
      76        H5Gopen:open of a node group failed
      77        H5Dget_space:couldn't get node dataspace
      78        H5Dopen:open of the node data failed
      79        H5Dextend:couldn't extend the node dataspace
      80        H5Dcreate:node data creation failed
      81        H5Screate_simple:dataspace creation failed
      82        H5Acreate:node attribute creation failed
      83        H5Gcreate:node group creation failed
      84        H5Dwrite:write to node data failed
      85        H5Dread:read of node data failed
      86        H5Awrite:write to node attribute failed
      87        H5Aread:read of node attribute failed
      88        H5Fmount:file mount failed
      89        Can't move a linked-to node
      90        Can't change the data for a linked-to node
      91        Parent of node is a link
      92        Can't delete a linked-to node
      93        File does not exist or is not a HDF5 file
      94        unlink (delete) of file failed
      95        couldn't get file index from node ID
      96        H5Tcopy:copy of existing datatype failed
      97        H5Aget_type:couldn't get attribute datatype
      98        H5Tset_size:couldn't set datatype size
      99        routine not implemented
      100       H5L: Link target is not an HDF5 external link
      101       HDF5: No external link feature available
      102       HDF5: Internal problem with objinfo
      103       HDF5: No value for external link
      104       HDF5: Cannot unpack external link
      106       HDF5: Root descriptor is NULL
      107       dimensions need transposed - open in modify mode
      108       invalid configuration option
    =======   =============================================================================
           
.. note::

  .. [1] The user is trying to create a new file and give it a name. The system has responded that the name has already been used.

  .. [2] The user wants to open an existing file that supposedly has the given name. The system has responded that no file by that name exists.

  .. [3] When ADF wakes up, it tries to figure out what data format the machine it is running on uses (e.g., IEEE big endian, IEEE little endian, Cray). If it doesn't recognize the format, it can't convert files created on other platforms to the current one, so it issues this error message and punts. 


.. last line
