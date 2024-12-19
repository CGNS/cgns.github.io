.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _DataArrayFigure:

DataArray Figure
================

.. container:: fighead
     
   **DataArray Node**
   
   (See :ref:`GridCoordinates_t <GridCoordinatesFigure>`, :ref:`Elements_t <ElementsFigure>` ,      :ref:`Axisymmetry_t <AxisymmetryFigure>` ,      :ref:`RotatingCoordinates_t <RotatingCoordinatesFigure>` , :ref:`FlowSolution_t <FlowSolutionFigure>` ,      :ref:`GridConnectivity_t <GridConnectivityFigure>` ,      :ref:`Periodic_t <PeriodicFigure>` ,      :ref:`BCData_t <BCDataFigure>` ,      :ref:`Area_t <AreaFigure>` ,      :ref:`GasModel_t <GasModelFigure>` ,      :ref:`ViscosityModel_t <ViscosityModelFigure>` ,      :ref:`ThermalConductivityModel_t <ThermalConductivityModelFigure>` ,      :ref:`TurbulenceClosure_t <TurbulenceClosureFigure>` ,      :ref:`TurbulenceModel_t <TurbulenceModelFigure>` ,      :ref:`ThermalRelaxationModel_t <ThermalRelaxationModelFigure>` ,      :ref:`ChemicalKineticsModel_t <ChemicalKineticsModelFigure>` ,      :ref:`EMElectricFieldModel_t <EMElectricFieldModelFigure>` ,      :ref:`EMMagneticFieldModel_t <EMMagneticFieldModelFigure>` ,      :ref:`EMConductivityModel_t <EMConductivityModelFigure>` ,      :ref:`ConvergenceHistory_t <ConvergenceHistoryFigure>` ,      :ref:`IntegralData_t <IntegralDataFigure>` ,      :ref:`ReferenceState_t <ReferenceStateFigure>` ,      :ref:`BaseIterativeData_t <BaseIterativeDataFigure>` ,      :ref:`ZoneIterativeData_t <ZoneIterativeDataFigure>` ,      :ref:`RigidGridMotion_t <RigidGridMotionFigure>` ,      :ref:`ArbitraryGridMotion_t <ArbitraryGridMotionFigure>` ,      :ref:`UserDefinedData_t <UserDefinedDataFigure>`, and :ref:`Gravity_t <GravityFigure>` figures)
   
     


.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DimensionalExponents`      
      * -  Label:    
        -  :sidsref:`DimensionalExponents_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`  or :sidskey:`R8`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  5     
      * -  Data:    
        -  :sidskey:`MassExponent` , :sidskey:`LengthExponent` , :sidskey:`TimeExponent` ,         :sidskey:`TemperatureExponent` , :sidskey:`AngleExponent`      
      * -  Cardinality:    
        -  0,1     
      * -  Child Nodes:     
        -  :ref:`DimensionalExponents_t figure <DimensionalExponentsFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`DataConversion`      
      * -  Label:    
        -  :sidsref:`DataConversion_t`      
      * -  Data-Type:    
        -  :sidskey:`R4`  or :sidskey:`R8`      
      * -  Dimensions:    
        -  1     
      * -  Dimension Values:     
        -  2     
      * -  Data:    
        -  :sidskey:`ConversionScale` , :sidskey:`ConversionOffset`      
      * -  Cardinality:    
        -  0,1 

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
        -  :sidskey:`DimensionalUnits`      
      * -  Label:     
        -  :sidsref:`DimensionalUnits_t`      
      * -  See:    
        -  :ref:`CGNSBase_t figure <CGNSBaseFigure>`  

.. last line
