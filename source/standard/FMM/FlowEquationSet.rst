.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _FlowEquationSetFigure:

FlowEquationSet Figure
======================



.. container:: fighead2
  
   **FlowEquationSet Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>` and :ref:`Zone_t <ZoneFigure>` figures)
   
     

.. container:: columns


  .. container:: left

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GoverningEquations`                    
          * -  Label:           
            -  :sidsref:`GoverningEquations_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`GoverningEquationsType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`CellDimension`                    
          * -  Child Nodes:           
            -  :ref:`GoverningEquations_t                figure <GoverningEquationsFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`GasModel`                    
          * -  Label:           
            -  :sidsref:`GasModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`GasModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`GasModel_t figure <GasModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ViscosityModel`                    
          * -  Label:           
            -  :sidsref:`ViscosityModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ViscosityModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ViscosityModel_t                figure <ViscosityModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ThermalRelaxationModel`                    
          * -  Label:           
            -  :sidsref:`ThermalRelaxationModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ThermalRelaxationModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ThermalRelaxationModel_t                figure <ThermalRelaxationModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`ChemicalKineticsModel`                    
          * -  Label:           
            -  :sidsref:`ChemicalKineticsModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ChemicalKineticsModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ChemicalKineticsModel_t                figure <ChemicalKineticsModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`EMMagneticFieldModel`                    
          * -  Label:           
            -  :sidsref:`EMMagneticFieldModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`EMMagneticFieldModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`EMMagneticFieldModel_t                figure <EMMagneticFieldModelFigure>`         
    
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

  .. container:: right

    
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidsref:`EquationDimension`                    
          * -  Label:           
            -  ":sidskey:`int` "                   
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
            -  :sidskey:`ThermalConductivityModel`                    
          * -  Label:           
            -  :sidsref:`ThermalConductivityModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`ThermalConductivityModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`ThermalConductivityModel_t                figure <ThermalConductivityModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`TurbulenceModel`                    
          * -  Label:           
            -  :sidsref:`TurbulenceModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`TurbulenceModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Parameters:           
            -  :sidskey:`CellDimension`                    
          * -  Child Nodes:           
            -  :ref:`TurbulenceModel_t                figure <TurbulenceModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`TurbulenceClosure`                    
          * -  Label:           
            -  :sidsref:`TurbulenceClosure_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`TurbulenceClosureType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`TurbulenceClosure_t                figure <TurbulenceClosureFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`EMElectricFieldModel`                    
          * -  Label:           
            -  :sidsref:`EMElectricFieldModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`EMElectricFieldModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`EMElectricFieldModel_t                figure <EMElectricFieldModelFigure>`         
    
    .. container:: figelem2
            
       .. list-table::
          :class:  figtable
          :stub-columns: 1
          :widths: 38 62
                       
          * -  Name:           
            -  :sidskey:`EMConductivityModel`                    
          * -  Label:           
            -  :sidsref:`EMConductivityModel_t`                    
          * -  Data-Type:           
            -  :sidskey:`C1`                    
          * -  Dimensions:           
            -  1                   
          * -  Dimension Values:            
            -  Length of string                   
          * -  Data:           
            -  :sidskey:`EMConductivityModelType`  value                   
          * -  Cardinality:           
            -  0,1                   
          * -  Child Nodes:           
            -  :ref:`EMConductivityModel_t                figure <EMConductivityModelFigure>`         
    
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
            -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`         


.. last line
