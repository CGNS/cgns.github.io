.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _CGNSBaseFigure:

CGNSBase Figure
===============

.. container:: fighead2
  
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * - Name:    
        -  User defined     
      * -  Label:    
        -  :sidskey:`CGNSBase_t`      
      * -  Data-Type:    
        -  :sidskey:`I4`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  2     
      * -  Data:    
        -  :sidskey:`CellDimension` , :sidskey:`PhysicalDimension`      
      * -  Cardinality:    
        -  0, *N*    

.. container:: columns

  .. container:: left    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`Zone_t`                    
          * -  Data-Type:           
            -  :sidskey:`cgsize_t`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  :sidskey:`IndexDimension` ,3                   
          * -  Data:           
            -  :sidskey:`VertexSize[IndexDimension]`, :sidskey:`CellSize[IndexDimension]`, :sidskey:`VertexSizeBoundary[IndexDimension]`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`CellDimension`, :sidskey:`PhysicalDimension`                    
          * -  Child Nodes:           
            -  :ref:`Zone_t figure <ZoneFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`SimulationType`                    
          * -  Label:           
            -  :sidsref:`SimulationType_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:     
            -  Length of string
          * -  Data:           
            -  :sidskey:`SimulationType`  value                   
          * -  Cardinality:           
            -  0,1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`BaseIterativeData_t`                    
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  :sidskey:`NumberOfSteps`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`BaseIterativeData_t                figure <BaseIterativeDataFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ReferenceState`                    
          * -  Label:           
            -  :sidsref:`ReferenceState_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`ReferenceState_t                figure <ReferenceStateFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`Axisymmetry`                    
          * -  Label:           
            -  :sidsref:`Axisymmetry_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`Axisymmetry_t figure <AxisymmetryFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`RotatingCoordinates`                    
          * -  Label:           
            -  :sidsref:`RotatingCoordinates_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`RotatingCoordinates_t figure <RotatingCoordinatesFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`Gravity`                    
          * -  Label:           
            -  :sidsref:`Gravity_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`Gravity_t figure <GravityFigure>`         

  .. container:: right  
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`IntegralData_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Child Nodes:            
            -  :ref:`IntegralData_t                figure <IntegralDataFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GlobalConvergenceHistory`                    
          * -  Label:           
            -  :sidsref:`ConvergenceHistory_t`                    
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  Number of iterations                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ConvergenceHistory_t figure <ConvergenceHistoryFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`Family_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Child Nodes:            
            -  :ref:`Family_t figure <FamilyFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`FlowEquationSet`                    
          * -  Label:           
            -  :sidsref:`FlowEquationSet_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`CellDimension`                    
          * -  Child Nodes:            
            -  :ref:`FlowEquationSet_t figure <FlowEquationSetFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`DataClass`                    
          * -  Label:           
            -  :sidsref:`DataClass_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`DataClass`  value                   
          * -  Cardinality:           
            -  0,1        
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`DimensionalUnits`                    
          * -  Label:           
            -  :sidsref:`DimensionalUnits_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  2                   
          * -  Dimension Values:            
            -  (32,5)                   
          * -  Data:           
            -  :sidskey:`DimensionalUnits`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:            
            -  :ref:`DimensionalUnits_t figure <DimensionalUnitsFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`Descriptor_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  Description string                   
          * -  Cardinality:           
            -  0, *N*         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`UserDefinedData_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Child Nodes:            
            -  :ref:`UserDefinedData_t figure <UserDefinedDataFigure>`         

.. note::

   :sidskey:`cgsize_t` is determined by the application from which the node is written. For a 32-bit application, :sidskey:`cgsize_t` will be :sidskey:`I4`, and :sidskey:`I8` for a 64-bit application.


.. last line
