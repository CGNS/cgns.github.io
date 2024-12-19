.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _AreaFigure:

Area Figure
===========

.. container:: fighead
     
   **Area Node**
   
   (See :ref:`BCProperty_t <BCPropertyFigure>`  figure)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`AreaType`      
      * -  Label:    
        -  :sidsref:`AreaType_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  Length of string     
      * -  Data:    
        -  Description string     
      * -  Cardinality:    
        -  1 

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`SurfaceArea`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  1     
      * -  Data:    
        -  Size of area     
      * -  Cardinality:    
        -  1     
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`RegionName`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`C1`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  32     
      * -  Data:    
        -  Name of region     
      * -  Cardinality:    
        -  1     
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

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

.. last line
