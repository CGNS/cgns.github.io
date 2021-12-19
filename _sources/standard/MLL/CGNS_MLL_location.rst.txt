.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLLocationAndPosition:
   
Location and Position
---------------------

These functions usually are found the the preamble or the epilog of your
application code using the :term:`CGNS/MLL`.


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Grid Location`_
   * - ``cg_gridlocation_write``
     - Write grid location
   * - ``cg_gridlocation_read``
     - Read grid location
       
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Point Sets`_
   * - ``cg_ptset_write``
     - Write point set data
   * - ``cg_ptset_info``
     - Get point set information
   * - ``cg_ptset_read``
     - Read point set data

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Rind Layers`_
   * - ``cg_rind_write``
     - Write number of rind layers
   * - ``cg_rind_read``
     - Read number of rind layers 


Grid Location
^^^^^^^^^^^^^
Node: GridLocation_t (SIDS, File Mapping) 

Point Sets
^^^^^^^^^^
Node: IndexArray_t, IndexRange_t (SIDS, File Mapping) 

Rind Layers
^^^^^^^^^^^
Node: Rind_t (SIDS, File Mapping)

 
.. last line
