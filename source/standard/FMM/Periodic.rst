.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _PeriodicFigure:

Periodic Figure
===============



.. container:: fighead2
  
   **Periodic Node**
   
   (See :ref:`GridConnectivityProperty_t <GridConnectivityPropertyFigure>`  figure)
   
     

.. container:: columns


  .. container:: left

    
    
    .. container:: figelem2
            
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
            -  Coordinates of rotation center                   
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
            -  :sidskey:`RotationAngle`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  :sidskey:`PhysicalDimension`                    
          * -  Data:           
            -  Rotation angle                   
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
            -  :sidskey:`Translation`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  :sidskey:`PhysicalDimension`                    
          * -  Data:           
            -  Translation values                   
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
