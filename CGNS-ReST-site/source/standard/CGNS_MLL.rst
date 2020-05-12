.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardMLL:

.. index::
   single: standard; API; CGNS/MLL;
   
.. _MLLIntroduction:

An API for C and Fortran applications
=====================================

The **Mid-Level Library** (aka MLL) is an example implementation of the
:term:`CGNS/HDF5` file mapping providing both a C and a Fortran API.

The :term:`CGNS/MLL` :term:`API` set of function:

 - :ref:`File Operations <MLLFileOperations>`
 - :ref:`File Operations <MLLFileOperations>`
 - :ref:`File Operations <MLLFileOperations>`
 - :ref:`File Operations <MLLFileOperations>`

.. _MLLFileOperations:
   
File Operations
---------------

These functions usually are found the the preamble or the epilog of your
application code using the :term:`CGNS/MLL`.

.. list-table::
   :header-rows: 1
   :widths: 2 8
   :width: 100%	    

   * -
     - Opening and closing a file
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
   :width: 100%	    
	   
   * - 
     - Configuring CGNS internals
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
   :width: 100%	    

   * - 
     - Interfacing with CGIO
   * - ``cg_get_cgio`` 
     - get the CGIO index number
   * - ``cg_root_id`` 
     - get the root node ID


.. last line
