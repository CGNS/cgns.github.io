.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GridConnectivity1to1Figure:

GridConnectivity1to1 Figure 
===========================

.. container:: fighead
     
   **GridConnectivity1to1 Node**
   
   (See :ref:`ZoneGridConnectivity_t figure <ZoneGridConnectivityFigure>` )


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidsref:`Transform`      
      * -  Label:     
        -  ":sidskey:`int[IndexDimension]` "     
      * -  Data-Type:    
        -  :sidskey:`I4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`IndexDimension`      
      * -  Data:    
        -  Transformation matrix (shorthand)     
      * -  Cardinality:    
        -  0,1     
      * -  Parameters:    
        -  :sidskey:`IndexDimension`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointRange`      
      * -  Label:    
        -  :sidsref:`IndexRange_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  2     
      * -  Dimension Values:     
        -  :sidskey:`IndexDimension` ,2     
      * -  Data:    
        -  :sidskey:`Begin[]` , :sidskey:`End[]`      
      * -  Cardinality:    
        -  1     
      * -  Parameters:    
        -  :sidskey:`IndexDimension`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointRangeDonor`      
      * -  Label:    
        -  :sidsref:`IndexRange_t`      
      * -  Data-Type:    
        -  :sidskey:`cgsize_t`      
      * -  Dimensions:    
        -  2     
      * -  Dimension Values:     
        -  :sidskey:`IndexDimension` ,2     
      * -  Data:    
        -  :sidskey:`Begin[]` , :sidskey:`End[]`      
      * -  Cardinality:    
        -  1     
      * -  Parameters:    
        -  :sidskey:`IndexDimension`  

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
        -  :sidskey:`Ordinal`      
      * -  Label:     
        -  :sidsref:`Ordinal_t`      
      * -  See:    
        -  :ref:`Zone_t figure <ZoneFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`GridConnectivityProperty`      
      * -  Label:    
        -  :sidsref:`GridConnectivityProperty_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`GridConnectivityProperty_t 	figure <GridConnectivityPropertyFigure>`  

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

  #. :sidskey:`GridConnectivity1to1` is only applicable to structured-to-structured 1-to-1 mesh connectivity.
  #. :sidskey:`cgsize_t` is determined by the application from which the node is written. For a 32-bit application, :sidskey:`cgsize_t` will be :sidskey:`I4`, and :sidskey:`I8` for a 64-bit application. 

.. last line
