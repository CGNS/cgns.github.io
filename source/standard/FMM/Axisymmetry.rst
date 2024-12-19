.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _AxisymmetryFigure:

Axisymmetry Figure
==================



.. container:: fighead2
  
   **Axisymmetry Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>`  figure)

  
.. container:: columns

  .. container:: left    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`AxisymmetryReferencePoint`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  2                   
          * -  Data:           
            -  Origin for defining rotation axis                   
          * -  Cardinality:           
            -  1                   
          * -  Child Nodes:           
            -  :ref:`DataArray_t figure <DataArrayFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`AxisymmetryAngle`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  Circumferential extent                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`DataArray_t figure <DataArrayFigure>`         
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`AxisymmetryAxisVector`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  2                   
          * -  Data:           
            -  Direction cosines of rotation axis                   
          * -  Cardinality:           
            -  1                   
          * -  Child Nodes:           
            -  :ref:`DataArray_t figure <DataArrayFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`CoordinateNames`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  32,2                   
          * -  Data:           
            -  Dataname identifiers for coordinates                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`DataArray_t figure <DataArrayFigure>`         
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
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
