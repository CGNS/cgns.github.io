.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _RotatingCoordinatesFigure:

RotatingCoordinates Figure
==========================

.. container:: fighead
     
   **RotatingCoordinates Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>`  and :ref:`Family_t <FamilyFigure>`  figures)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`RotationCenter`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`PhysicalDimension`      
      * -  Data:    
        -  Coordinates of center of rotation     
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
        -  :sidskey:`RotationRateVector`      
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  :sidskey:`PhysicalDimension`      
      * -  Data:    
        -  Angular velocity components     
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

.. last line
