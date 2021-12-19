.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ElementsFigure:

Elements Figure
===============

.. container:: fighead
     
   **Elements Node**
   
   (See :ref:`Zone_t <ZoneFigure>`  figure)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`ElementRange`      
      * -  Label:    
        -  :sidsref:`IndexRange_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  2     
      * -  Data:    
        -  Begin, end     
      * -  Cardinality:    
        -  1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`ElementConnectivity`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`ElementDataSize`      
      * -  Data:    
        -  Element connectivity table     
      * -  Cardinality:    
        -  1     
      * -  Functions:    
        -  :sidskey:`NPE` , :sidskey:`ElementSize` , :sidskey:`ElementDataSize`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`ElementStartOffset`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`ElementSize + 1`      
      * -  Data:    
        -  Element connectivity position table     
      * -  Cardinality:    
        -  0,1     
      * -  Functions:    
        -  :sidskey:`ElementDataSize`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`ParentElements`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  2     
      * -  Dimension Values:     
        -  :sidskey:`ElementSize` ,2     
      * -  Data:    
        -  :sidskey:`Parent1[ElementSize]` , :sidskey:`Parent2[ElementSize]`      
      * -  Cardinality:    
        -  0,1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`ParentElementsPosition`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  2     
      * -  Dimension Values:     
        -  :sidskey:`ElementSize` ,2     
      * -  Data:    
        -  :sidskey:`SideOfParent1[ElementSize]` ,         :sidskey:`SideOfParent2[ElementSize]`      
      * -  Cardinality:    
        -  0,1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`Rind`      
      * -  Label:     
        -  :sidsref:`Rind_t`      
      * -  See:    
        -  :ref:`GridCoordinates_t figure <GridCoordinatesFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:     
        -  :sidsref:`Descriptor_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:     
        -  :sidsref:`UserDefinedData_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  


.. note::

   :sidskey:`cgsize_t` is determined by the application from which the node is written. For a 32-bit application, :sidskey:`cgsize_t` will be :sidskey:`I4`, and :sidskey:`I8` for a 64-bit application.


.. last line
