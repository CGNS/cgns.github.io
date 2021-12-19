.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLGridConnectivity:
   
Grid Connectivity
-----------------



.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `One-to-One Connectivity`_
   * - ``cg_n1to1_global``
     - Get total number of 1-to-1 interfaces in a database
   * - ``cg_1to1_read_global``
     - Read data for all 1-to-1 interfaces in a database
   * - ``cg_1to1_write``
     - Write 1-to-1 connectivity data for a zone
   * - ``cg_n1to1``
     - Get number of 1-to-1 interfaces in a zone
   * - ``cg_1to1_read``
     - Read 1-to-1 connectivity data for a zone 

       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Generalized Connectivity`_
     
   * - ``cg_conn_write``
     - Write generalized connectivity data
   * - ``cg_conn_write_short``
     - Write generalized connectivity data without donor information
   * - ``cg_nconns``
     - Get number of generalized connectivity interfaces in a zone
   * - ``cg_conn_info``
     - Get info about a generalized connectivity interface
   
.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Special Grid Connectivity Properties`_
   * - ``cg_conn_periodic_write``
     - Write data for periodic interface
   * - ``cg_conn_average_write``
     - Write data for averaging interface
   * - ``cg_conn_periodic_read``
     - Read data for periodic interface
   * - ``cg_conn_average_read``
     - Read data for averaging interface 

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Overset Holes`_
   * - ``cg_hole_write``
     - Write overset hole data
   * - ``cg_nholes``
     - Get number of overset holes in a zone
   * - ``cg_hole_info``
     - Get info about an overset hole
   * - ``cg_hole_read``
     - Read overset hole data 

   

One-to-One Connectivity
^^^^^^^^^^^^^^^^^^^^^^^

Generalized Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^

Special Grid Connectivity Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overset Holes
^^^^^^^^^^^^^

 
.. last line
