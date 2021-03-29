.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _GridConnectivityFigure:

GridConnectivity Figure
=======================



.. container:: fighead2
  
   **GridConnectivity Node**
   
   (See :ref:`ZoneGridConnectivity_t figure <ZoneGridConnectivityFigure>` )
   
     

.. container:: columns


  .. container:: left

    
    
    .. container:: figelem2
            
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
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GridLocation`                    
          * -  Label:            
            -  :sidsref:`GridLocation_t`                    
          * -  See:           
            -  :ref:`FlowSolution_t                figure <FlowSolutionFigure>`         
    
    .. container:: figelem2
            
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
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`CellListDonor`  or :sidskey:`PointListDonor`                    
          * -  Label:           
            -  :sidsref:`IndexArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`cgsize_t`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension`  of donor, :sidskey:`PointListSize[]`                    
          * -  Data:           
            -  Cells or nodes on adjoining patch                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`PointListSize[]`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GridConnectivityProperty`                    
          * -  Label:            
            -  :sidsref:`GridConnectivityProperty_t`                    
          * -  See:           
            -  :ref:`GridConnectivity1to1_t figure <GridConnectivity1to1Figure>`         

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`PointList`                    
          * -  Label:           
            -  :sidsref:`IndexArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`cgsize_t`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension` , :sidskey:`PointListSize[]`                    
          * -  Data:           
            -  Vector of nodes on current patch                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`PointListSize`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GridConnectivityType`                    
          * -  Label:           
            -  :sidsref:`GridConnectivityType_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`GridConnectivityType`  value                   
          * -  Cardinality:           
            -  0,1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`InterpolantsDonor`                    
          * -  Label:           
            -  :sidsref:`DataArray_t`                    
          * -  Data-Type:           
            -  :sidskey:`R4`  or :sidskey:`R8`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`CellDimension` , :sidskey:`PointListSize[]`                    
          * -  Data:           
            -  Interpolants for each node                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`CellDimension` , :sidskey:`PointListSize[]`         
    
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


.. note::

  #. The nodes :sidskey:`PointRange` and :sidskey:`PointList` are mutually exclusive.
  #. For mismatched interfaces, the combination of :sidskey:`CellListDonor` and :sidskey:`InterpolantsDonor` is used to define the position of each receiver point in the donor zone.
  #. :sidskey:`cgsize_t` is determined by the application from which the node is written. For a 32-bit application, :sidskey:`cgsize_t` will be :sidskey:`I4`, and :sidskey:`I8` for a 64-bit application. 


.. last line
