.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GridCoordinatesFigure:

GridCoordinates Figure
======================

.. container:: fighead
     
   **GridCoordinates Node**
   
   (See :ref:`Zone_t figure <ZoneFigure>` )
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  Data-name identifier or user defined     
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`  or :sidskey:`R8`      
      * -  Dimensions:    
        -  :sidskey:`IndexDimension`      
      * -  Dimension Values:     
        -  :sidskey:`DataSize[]`      
      * -  Data:    
        -  Grid coordinate values     
      * -  Cardinality:    
        -  0, *N*      
      * -  Parameters:    
        -  :sidskey:`DataType` , :sidskey:`IndexDimension` , :sidskey:`DataSize`      
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`Rind`      
      * -  Label:    
        -  :sidsref:`Rind_t`      
      * -  Data-Type:    
        -  :sidskey:`I4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`2*IndexDimension`      
      * -  Data:    
        -  :sidskey:`RindPlanes`      
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
        -  :sidskey:`DataClass`      
      * -  Label:     
        -  :sidsref:`DataClass_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DimensionalUnits`      
      * -  Label:     
        -  :sidsref:`DimensionalUnits_t`      
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

    The data labeled :sidskey:`RindPlanes` under :sidskey:`Rind_t` refers to number of rind planes for structured grids, and number of rind points for unstructured grids.


.. last line
