.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ZoneFigure:

Zone Figure
===========



.. container:: fighead2
  
   **Zone Node**
   
   (See :ref:`CGNSBase_t figure <CGNSBaseFigure>` )



.. container:: columns

  .. container:: left
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GridCoordinates`  (original grid); User defined                (additional grids)                   
          * -  Label:           
            -  :sidsref:`GridCoordinates_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`VertexSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:            
            -  :ref:`GridCoordinates_t                figure <GridCoordinatesFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`DiscreteData_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`VertexSize` ,                :sidskey:`CellSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:            
            -  :ref:`FlowSolution_t                figure <FlowSolutionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`Elements_t`                    
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  2                   
          * -  Data:           
            -  :sidskey:`ElementType` , :sidskey:`ElementSizeBoundary`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Child Nodes:           
            -  :ref:`Elements_t figure <ElementsFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ZoneBC`                    
          * -  Label:           
            -  :sidsref:`ZoneBC_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`PhysicalDimension`                    
          * -  Child Nodes:            
            -  :ref:`ZoneBC_t figure <ZoneBCFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`ZoneIterativeData_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`NumberOfSteps`                    
          * -  Child Nodes:            
            -  :ref:`ZoneIterativeData_t                figure <ZoneIterativeDataFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`RigidGridMotion_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`RigidGridMotionType`  value                   
          * -  Cardinality:           
            -  0, *N*                    
          * -  Child Nodes:           
            -  :ref:`RigidGridMotion_t                figure <RigidGridMotionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`ZoneSubRegion_t`                    
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  :sidskey:`RegionCellDimension`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`VertexSize` ,                :sidskey:`CellSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:           
            -  :ref:`ZoneSubRegion_t                figure <ZoneSubRegionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ReferenceState`                    
          * -  Label:            
            -  :sidsref:`ReferenceState_t`                    
          * -  See:           
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`         
    
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
            -  :sidsref:`IntegralData_t`                    
          * -  See:           
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`         

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`FlowSolution_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`VertexSize` ,                :sidskey:`CellSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:            
            -  :ref:`FlowSolution_t                figure <FlowSolutionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ZoneType`                    
          * -  Label:           
            -  :sidsref:`ZoneType_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`Structured`  or :sidskey:`Unstructured`                    
          * -  Cardinality:           
            -  1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`Ordinal`                    
          * -  Label:           
            -  :sidsref:`Ordinal_t`                    
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  User-defined ordinal                   
          * -  Cardinality:           
            -  0,1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ZoneGridConnectivity or user defined`                    
          * -  Label:           
            -  :sidsref:`ZoneGridConnectivity_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,N                   
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`CellDimension`                    
          * -  Child Nodes:            
            -  :ref:`ZoneGridConnectivity_t                figure <ZoneGridConnectivityFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`ArbitraryGridMotion_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ArbitraryGridMotionType`  value                   
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`IndexDimension` , :sidskey:`VertexSize` ,                :sidskey:`CellSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:           
            -  :ref:`ArbitraryGridMotion_t                figure <ArbitraryGridMotionFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`FamilyName`                    
          * -  Label:            
            -  :sidsref:`FamilyName_t`                    
          * -  See:           
            -  :ref:`BC_t figure <BCFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`User defined`                    
          * -  Label:            
            -  :sidskey:`AdditionalFamilyName_t`                    
          * -  See:           
            -  :ref:`BC_t figure <BCFigure>`         
    
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
            -  :sidskey:`FlowEquationSet`                    
          * -  Label:            
            -  :sidsref:`FlowEquationSet_t`                    
          * -  See:           
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ZoneConvergenceHistory`                    
          * -  Label:            
            -  :sidsref:`ConvergenceHistory_t`                    
          * -  See:           
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`RotatingCoordinates`                    
          * -  Label:            
            -  :sidsref:`RotatingCoordinates_t`                    
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
