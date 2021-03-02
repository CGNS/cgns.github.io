.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLFileOperations:
   
File Operations
---------------

These functions usually are found the the preamble or the epilog of your
application code using the :term:`CGNS/MLL`.


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Opening and closing a File`_
   * - ``cg_open`` 
     - Open a CGNS file
   * - ``cg_version``
     - Get CGNS file version
   * - ``cg_precision`` 
     - Get CGNS file precision
   * - ``cg_close``
     - Close a CGNS file
   * - ``cg_is_cgns``
     - Check for a valid CGNS file
   * - ``cg_save_as``
     - Save the open CGNS file
   * - ``cg_set_file_type`` 
     - Set default file type
   * - ``cg_get_file_type``
     - Get file type for open CGNS file

       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Configuring CGNS internals`_
   * - ``cg_configure`` 
     - Configure CGNS internals
   * - ``cg_error_handler`` 
     - Set CGNS error handler
   * - ``cg_set_compress`` 
     - Set CGNS compression mode
   * - ``cg_get_compress`` 
     - Get CGNS compression mode
   * - ``cg_set_path`` 
     - Set the CGNS link search path
   * - ``cg_add_path`` 
     - Add to the CGNS link search path

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Interfacing with CGIO`_
   * - ``cg_get_cgio`` 
     - get the CGIO index number
   * - ``cg_root_id`` 
     - get the root node ID


Opening and closing a File
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`ier` = :sig-name:`cg_open` (:in:`char *filename`, :in:`int mode`, :out:`int *fn`);                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_version` (:in:`int fn`, :out:`float *version`);                                                     | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_precision` (:in:`int fn`, :out:`int *precision`);                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_close` (:in:`int fn`);                                                                              | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_is_cgns` (:in:`const char *filename`, :out:`int *file_type`);                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_save_as` (:in:`int fn`, :in:`const char *filename`, :in:`int file_type`, :in:`int follow_links`);   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_set_file_type` (:in:`int file_type`);                                                               | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_get_file_type` (:in:`int fn`, :out:`int *file_type`);                                               | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call ``cg_open_f`` (:in:`filename`, :in:`mode`, :out:`fn`, :out:`ier`)                                                         | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_version_f`` (:in:`fn`, :out:`version`, :out:`ier`)                                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_precision_f`` (:in:`fn`, :out:`precision`, :out:`ier`)                                                               | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_close_f`` (:in:`fn`)                                                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_is_cgns_f`` (:in:`filename`, :out:`file_type`)                                                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_save_as_f`` (:in:`fn`, :in:`filename`, :in:`file_type`, :in:`follow_links`)                                          | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_set_file_type_f`` (:in:`file_type`)                                                                                  | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_get_file_type_f`` (:in:`fn`, :out:`file_type`)                                                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
:filename:	   	Name of the CGNS file, including path name if necessary. There is no limit on the length of this character variable.
:mode:		Mode used for opening the file. The modes currently supported are :code:`CG_MODE_READ`, :code:`CG_MODE_WRITE`, and :code:`CG_MODE_MODIFY`.
:fn:		CGNS file index number.
:version:		CGNS version number.
:precision:		Precision used to write the CGNS file. The return value will be one of 32 (32-bit), 64 (64-bit), or 0 if not known.
:file_type:		Type of CGNS file. This will typically be either :code:`CG_FILE_ADF` or :code:`CG_FILE_HDF5` depending on the underlying file format. However, note that when built in 32-bit, there is also an option to create a Version 2.5 CGNS file by setting the file type to :code:`CG_FILE_ADF2`.
:follow_links:	This flag determines whether links are left intact when saving a CGNS file. If non-zero, then the links will be removed and the data associated with the linked files copied to the new file.
:ier:		Error status. 

The function :code:`cg_open` must always be the first one called. It opens a CGNS file for reading and/or writing and returns an index number :code:`fn`. The index number serves to identify the CGNS file in subsequent function calls. Several CGNS files can be opened simultaneously. The current limit on the number of files opened at once depends on the platform.

The file can be opened in one of the following modes:

.. list-table::

  * - **CG_MODE_READ**
    - Read only mode.
  * - **CG_MODE_WRITE**
    - Write only mode.
  * - **CG_MODE_MODIFY**
    - Reading and/or writing is allowed.


The function :code:`cg_close` must always be the last one called.
It closes the CGNS file designated by the index number :code:`fn` and frees the memory where the CGNS data was kept.
When a file is opened for writing, :code:`cg_close` writes all the CGNS data in memory onto disk prior to closing the file.
Consequently, if is omitted, the CGNS file is not written properly.

In order to reduce memory usage and improve execution speed, large arrays such as grid coordinates or flow solutions are not actually stored in memory.
Instead, only basic information about the node is kept, while reads and writes of the data is directly to and from the application's memory.
An attempt is also made to do the same with unstructured mesh element data.

When a CGNS file is newly created using :code:`CG_MODE_WRITE`, the default type of database manager used is determined at compile time.
If the CGNS library was built with HDF5 version 1.8 or later support, the file type will be :code:`CG_FILE_HDF5`, otherwise :code:`CG_FILE_ADF` is used.
This may be changed either by setting an environment variable, :code:`CGNS_FILETYPE`, to one of adf, hdf5, or adf2, or by calling the routine :code:`cg_set_file_type` prior to the :code:`cg_open` call.
Calling :code:`cg_set_file_type` with the argument :code:`CG_FILE_NONE` will reset the library to use the default file type.

.. note::
  If the environment variable :code:`CGNS_FILETYPE` is set, it takes precedence.

For existing files, the function :code:`cg_is_cgns` may be used to determine if a file is a CGNS file or not, and the type of file (:code:`CG_FILE_ADF` or :code:`CG_FILE_HDF5`).
If the file is a CGNS file, :code:`cg_is_cgns` returns :code:`CG_OK`,
otherwise :code:`CG_ERROR` is returned and :code:`file_type` is set to :code:`CG_FILE_NONE`.

The CGNS file identified by :code:`fn` may be saved to a different filename and type using :code:`cg_save_as`. In order to save as an HDF5 file, the library must have been built with HDF5 support. ADF support is always built. The function :code:`cg_set_file_type` sets the default file type for newly created CGNS files. The function :code:`cg_get_file_type` returns the file type for the CGNS file identified by :code:`fn`. If the CGNS library is built as 32-bit, the additional file type, :code:`CG_FILE_ADF2`, is available. This allows creation of a 2.5 compatible CGNS file.

Configuring CGNS Internals
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. table:: Configuring CGNS Internals
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`ier` = :sig-name:`cg_configure` (:in:`int option`, :in:`void *value`);                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_error_handler` (:in:`void (*)(int, char *)`);                                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_set_compress` (:in:`int compress`);                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_get_compress` (:out:`int *compress`);                                                               | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_set_path` (:in:`const char *path`);                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_add_path` (:in:`const char *path`);                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call ``cg_exit_on_errors_f`` (:in:`flag`)                                                                                      | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_set_compress_f`` (:in:`compress`, :out:`ier`)                                                                        | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_get_compress_f`` (:out:`compress`, :out:`ier`)                                                                       | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_set_path_f`` (:in:`path`, :out:`ier`)                                                                                | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_add_path_f`` (:in:`path`, :out:`ier`)                                                                                | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
  :option:	   	The option to configure, currently one of :code:`CG_CONFIG_ERROR`, :code:`CG_CONFIG_COMPRESS`, :code:`CG_CONFIG_SET_PATH`, :code:`CG_CONFIG_ADD_PATH`,  :code:`CG_CONFIG_FILE_TYPE`, :code:`CG_CONFIG_RIND_INDEX`, :code:`CG_CONFIG_HDF5_COMPRESS`, or :code:`CG_CONFIG_HDF5_MPI_COMM` as defined in ``cgnslib.h``.
  :value:		The value to set, type cast as :code:`void *`.
  :compress:	CGNS compress (rewrite) setting.
  :path:		Pathname to search for linked to files when opening a file with external links.
  :flag:		Fortran flag to set automatic exit in the case of error.
  :ier:         Error status. 

The function :code:`cg_configure` allows certain CGNS library internal options to be configured. The currently supported options and expected values are:

:CG_CONFIG_ERROR:        This allows an error call-back function to be defined by the user. The value should be a pointer to a function to receive the error. The function is defined as :code:`void err_callback(int is_error, char *errmsg)`, and will be called for errors and warnings. The first argument, is_error, will be 0 for warning messages, 1 for error messages, and −1 if the program is going to terminate (i.e., a call to :code:`cg_error_exit()`). The second argument is the error or warning message. If this is defined, warning and error messages will go to the function, rather than the terminal. A value of :code:`NULL` will remove the call-back function.
 
:CG_CONFIG_COMPRESS:	 This is the rewrite-upon-close setting.     

  .. note::
    Prior versions of the library would automatically rewrite the CGNS file when it was closed after being opened in modify mode if there was unused space. This is no longer done, due to possible conflicts when using parallel I/O. The previous behavior may be recovered by setting value to a positive integer. In this case the file will be rewritten if the number of node deletions or modifications are equal to or exceed this number. Setting value to a negative number will force the rewrite when the file is closed. The default value is 0 (no rewrite).
 
:CG_CONFIG_SET_PATH:		Sets the search path for locating linked-to files. The argument value should be a character string containing one or more directories, formatted the same as for the :code:`PATH` environment variable. This will replace any current settings. Setting value to :code:`NULL` will remove all paths.
 
:CG_CONFIG_ADD_PATH:		Adds a directory, or list of directories, to the linked-to file search path. This is the same as :code:`CG_CONFIG_SET_PATH`, but adds to the path instead of replacing it.
 
:CG_CONFIG_FILE_TYPE:		Sets the default file type for newly created CGNS files. The argument, value should be set to one of :code:`CG_FILE_NONE`, :code:`CG_FILE_ADF`, :code:`CG_FILE_HDF5`, or :code:`CG_FILE_ADF2`. See the discussion above for :code:`cg_set_file_type`.
 
:CG_CONFIG_RIND_INDEX:		This option affects index bounds on structured arrays with rind planes.
                            By default (`CG_CONFIG_RIND_CORE`), the core array locations always begin at index 1. Lower rind planes, if present, would have an index less than 1.
                            For backward compatibility, `CG_CONFIG_RIND_ZERO` is provided and the index 1 will then locate the start of the array and not necessarily the start the core array.

                            .. note::
                                 Use of this option does not change the cgns file in any way; it only modifies the API to the library.
                                 The API changed for versions of the Mid-Level Library greater than 3.4. Before, it did not produce this behavior.
                                 Index 1 always represented the start of an array: in an array with no rind planes, the core location would have index 1; in an array with 1 rind plane, the core location would have index 2. In version 3.4 of the Mid-Level Library, the behavior of the API was fixed to match that specified in the SIDS: core array locations always begin at index 1. This option allows for configuring the library to pre-3.4 indexing behavior (set value to :code:`CG_CONFIG_RIND_ZERO`) or the new default behavior (set value to :code:`CG_CONFIG_RIND_CORE`). Note that using :code:`CG_CONFIG_RIND_ZERO` is considered obsolete, but is provided for backwards compatability.
                                 Most users should not set this option and use the default.
                                 Values used for this option do not need to be explicitly cast as :code:`void*`.
   
 
:CG_CONFIG_HDF5_COMPRESS:		Sets the compression level for data written from HDF5. The default is no compression. Setting value to -1, will use the default compression level of 6. The acceptable values are 0 to 9, corresponding to gzip compression levels.
 
:CG_CONFIG_HDF5_MPI_COMM:		Sets the MPI communicator for parallel I/O. The default is :code:`MPI_COMM_WORLD`. The new communicator is given by typecasting it to a :code:`void *`. This is generally used internally - see :ref:`cgp_mpi_comm` instead.

The routines :code:`cg_error_handler`, :code:`cg_set_compress`, :code:`cg_set_path`, :code:`cg_add_path`, and :code:`cg_set_file_type` are convenience functions built on top of :code:`cg_configure`.

There is no Fortran counterpart to function :code:`cg_configure` or :code:`cg_error_handler`. The Fortran function :code:`cg_exit_on_error_f` routine be be used in place of :code:`cg_error_handler`. If flag is non-zero, then when an error is encountered, the library will print the error message and exit with an code of 1. Setting flag to zero (the default) prevents this and the error is returned to the user code.

.. note::
  The HDF5 implementation does not support search paths for linked files. The links need to be either absolute or relative pathnames. As a result, it is recommended that the search path options not be used as they may be removed in future versions.

Interfacing with CGIO
^^^^^^^^^^^^^^^^^^^^^

.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | C Functions                                                                                                                    | Modes |
   +================================================================================================================================+=======+
   | :out:`ier` = :sig-name:`cg_get_cgio` (:in:`int fn`, :out:`int *cgio_num`);                                                     | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | :out:`ier` = :sig-name:`cg_root_id` (:in:`int fn`, :out:`double *rootid`);                                                     | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   
.. table::
   :widths: 110 15
   
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | Fortran interfaces                                                                                                             | Modes |
   +================================================================================================================================+=======+
   | call ``cg_get_cgio_f`` (:in:`fn`, :out:`cgio_num`, :out:`ier`)                                                                 | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+
   | call ``cg_root_id_f``  (:in:`fn`, :out:`rootid`, :out:`ier`)                                                                   | r w m |
   +--------------------------------------------------------------------------------------------------------------------------------+-------+

:in:`Input` / :out:`Ouput`
~~~~~~~~~~~~~~~~~~~~~~~~~~
  :fn:        CGNS file index number.
  :cgio_num:  CGIO indentifier for the CGNS file.
  :rootid:    Root node identifier for the CGNS file.
  :ier:       Error status.

These allow for the use of the :ref:`low-level CGIO functions` in conjunction with the Mid Level Library. The function :code:`cg_get_cgio`
returns the CGIO database identifier for the specified CGNS file, which is used in the CGIO routines. The root node identifier for the CGNS file is returned by :code:`cg_root_id`.
 

.. last line
