.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _ParticleZoneFigure:

ParticleZone Figure
===================



.. container:: fighead2
  
   **ParticleZone Node**
   
   (See :ref:`CGNSBase_t figure <CGNSBaseFigure>` )



.. container:: columns

  .. container:: left
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleCoordinates`  (original particles); User defined                (additional particless)                   
          * -  Label:           
            -  :sidsref:`ParticleCoordinates_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`ParticleSize`                                    
          * -  Child Nodes:            
            -  :ref:`ParticleCoordinates_t                figure <ParticleCoordinatesFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`ParticleIterativeData_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`NumberOfSteps`                    
          * -  Child Nodes:            
            -  :ref:`ParticleIterativeData_t                figure <ParticleIterativeDataFigure>`            
    
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
            -  :ref:`ReferenceState_t figure <ReferenceStateFigure>`         
    
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
            -  :ref:`IntegralData_t figure <IntegralDataFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  User defined                   
          * -  Label:           
            -  :sidsref:`ParticleSolution_t`                    
          * -  Data-Type:           
            -  :sidskey:`MT`                    
          * -  Cardinality:           
            -  0, *N*                    
          * -  Parameters:           
            -  :sidskey:`ParticleSize`                    
          * -  Functions:           
            -  :sidsref:`DataSize`                    
          * -  Child Nodes:            
            -  :ref:`ParticleSolution_t figure <ParticleSolutionFigure>`

  .. container:: right    
    
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
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  
    
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
            -  :ref:`DimensionalUnits_t figure <DimensionalUnitsFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ParticleEquationSet`                    
          * -  Label:            
            -  :sidsref:`ParticleEquationSet_t`                    
          * -  See:           
            -  :ref:`ParticleEquationSet_t figure <ParticleEquationSetFigure>`         
    
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
