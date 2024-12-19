.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ZoneGridConnectivityFigure:

ZoneGridConnectivity Figure
===========================

.. container:: fighead
     
   **ZoneGridConnectivity Node**
   
   (See :ref:`Zone_t  <ZoneFigure>` )
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`GridConnectivity1to1_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  :sidskey:`ZoneDonorName`      
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`IndexDimension`      
      * -  Functions:    
        -  None     
      * -  Child Nodes:    
        -  :ref:`GridConnectivity1to1_t figure <GridConnectivity1to1Figure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`GridConnectivity_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  :sidskey:`ZoneDonorName`      
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`IndexDimension` , :sidskey:`CellDimension`      
      * -  Functions:    
        -  :sidsref:`PointListSize`      
      * -  Child Nodes:    
        -  :ref:`GridConnectivity_t figure <GridConnectivityFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:    
        -  :sidsref:`OversetHoles_t`      
      * -  Data-Type:    
        -  :sidskey:`MT`      
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`IndexDimension`      
      * -  Child Nodes:     
        -  :ref:`OversetHoles_t figure <OversetHolesFigure>`  

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
        -  :ref:`CGNSBase_t  <CGNSBaseFigure>`  

.. note::

  :sidskey:`GridConnectivity1to1` is only applicable to structured-to-structured 1-to-1 mesh connectivity.


.. last line
