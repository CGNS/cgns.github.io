.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ParticleEquationSetFigure:

ParticleEquationSet Figure
==========================



.. container:: fighead2
  
   **ParticleEquationSet Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>` and :ref:`Zone_t <ParticleZoneFigure>` figures)
   
     

.. container:: columns


  .. container:: left

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleGoverningEquations`                    
          * -  Label:           
            -  :sidsref:`ParticleGoverningEquations_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticleGoverningEquationsType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`CellDimension`                    
          * -  Child Nodes:           
            -  :ref:`ParticleGoverningEquations_t figure <ParticleGoverningEquationsFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleBreakupModel`                    
          * -  Label:           
            -  :sidsref:`ParticleBreakupModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticleBreakupModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ParticleBreakupModel_t figure <ParticleBreakupModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleCollisionModel`                    
          * -  Label:           
            -  :sidsref:`ParticleCollisionModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticleCollisionModel`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ParticleCollisionModel_t figure <ViscosityModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleForceModel`                    
          * -  Label:           
            -  :sidsref:`ParticleForceModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticleForceModel`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ParticleForceModel_t  figure <ParticleForceModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticlePhaseChangeModel`                    
          * -  Label:           
            -  :sidsref:`ParticlePhaseChangeModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticlePhaseChangeModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ParticlePhaseChangeModel_t figure <ParticlePhaseChangeModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleWallInteractionModel`                    
          * -  Label:           
            -  :sidsref:`ParticleWallInteractionModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ParticleWallInteractionModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ParticleWallInteractionModel_t figure <ParticleWallInteractionModelFigure>`         
    
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
            -  :ref:`DimensionalUnits_t figure <DimensionalUnitsFigure>`         

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidsref:`EquationDimension`                    
          * -  Label:           
            -  :sidskey:`int`                   
          * -  Data-Type:           
            -  :sidskey:`I4`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  1                   
          * -  Data:           
            -  :sidskey:`EquationDimension`  value                   
          * -  Cardinality:           
            -  0,1        
    
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
            -  :ref:`UserDefinedData_t figure <UserDefinedDataFigure>`         


.. last line
