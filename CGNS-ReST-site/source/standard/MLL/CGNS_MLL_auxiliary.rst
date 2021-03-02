.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLAuxiliaryData:
   
Auxiliary Data
--------------


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


Reference State
^^^^^^^^^^^^^^^

Gravity
^^^^^^^

Convergence History
^^^^^^^^^^^^^^^^^^^

Integral Data
^^^^^^^^^^^^^

User-Defined Data
^^^^^^^^^^^^^^^^^

Freeing Memory
^^^^^^^^^^^^^^



.. last line
