.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _UserDefinedDataFigure:

UserDefinedData Figure
======================

.. container:: fighead
     
   **UserDefinedData Node**
   
   (See :ref:`CGNSBase_t <CGNSBaseFigure>` ,      :ref:`Zone_t <ZoneFigure>` ,      :ref:`GridCoordinates_t <GridCoordinatesFigure>` ,      :ref:`Elements_t <ElementsFigure>` ,      :ref:`Axisymmetry_t <AxisymmetryFigure>` ,      :ref:`RotatingCoordinates_t <RotatingCoordinatesFigure>` ,      :ref:`FlowSolution_t <FlowSolutionFigure>` ,      :ref:`ZoneGridConnectivity_t <ZoneGridConnectivityFigure>` ,      :ref:`GridConnectivity1to1_t <GridConnectivity1to1Figure>` ,      :ref:`GridConnectivity_t <GridConnectivityFigure>` ,      :ref:`GridConnectivityProperty_t <GridConnectivityPropertyFigure>` ,      :ref:`Periodic_t <PeriodicFigure>` ,      :ref:`AverageInterface_t <AverageInterfaceFigure>` ,      :ref:`OversetHoles_t <OversetHolesFigure>` ,      :ref:`ZoneBC_t <ZoneBCFigure>` ,      :ref:`BC_t <BCFigure>` ,      :ref:`BCDataSet_t <BCDataSetFigure>` ,      :ref:`BCData_t <BCDataFigure>` ,      :ref:`BCProperty_t <BCPropertyFigure>` ,      :ref:`WallFunction_t <WallFunctionFigure>` ,      :ref:`Area_t <AreaFigure>` ,      :ref:`FlowEquationSet_t <FlowEquationSetFigure>` ,      :ref:`GoverningEquations_t <GoverningEquationsFigure>` ,      :ref:`GasModel_t <GasModelFigure>` ,      :ref:`ViscosityModel_t <ViscosityModelFigure>` ,      :ref:`ThermalConductivityModel_t <ThermalConductivityModelFigure>` ,      :ref:`TurbulenceClosure_t <TurbulenceClosureFigure>` ,      :ref:`TurbulenceModel_t <TurbulenceModelFigure>` ,      :ref:`ThermalRelaxationModel_t <ThermalRelaxationModelFigure>` ,      :ref:`ChemicalKineticsModel_t <ChemicalKineticsModelFigure>` ,      :ref:`EMElectricFieldModel_t <EMElectricFieldModelFigure>` ,      :ref:`EMMagneticFieldModel_t <EMMagneticFieldModelFigure>` ,      :ref:`EMConductivityModel_t <EMConductivityModelFigure>` ,      :ref:`ConvergenceHistory_t <ConvergenceHistoryFigure>` ,      :ref:`IntegralData_t <IntegralDataFigure>` ,      :ref:`ReferenceState_t <ReferenceStateFigure>` ,      :ref:`Family_t <FamilyFigure>` ,      :ref:`BaseIterativeData_t <BaseIterativeDataFigure>` ,      :ref:`ZoneIterativeData_t <ZoneIterativeDataFigure>` ,      :ref:`RigidGridMotion_t <RigidGridMotionFigure>` ,      :ref:`ArbitraryGridMotion_t <ArbitraryGridMotionFigure>` ,  and :ref:`Gravity_t <GravityFigure>`  figures)
   
     


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
        -  :sidskey:`GridLocation`      
      * -  Label:     
        -  :sidsref:`GridLocation_t`      
      * -  See:    
        -  :ref:`FlowSolution_t figure <FlowSolutionFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointRange`      
      * -  Label:     
        -  :sidsref:`IndexRange_t`      
      * -  See:    
        -  :ref:`BC_t figure <BCFigure>`  

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  :sidskey:`PointList`      
      * -  Label:     
        -  :sidsref:`IndexArray_t`      
      * -  See:    
        -  :ref:`BC_t figure <BCFigure>`  

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
        -  :sidskey:`DataArray#`  or user defined     
      * -  Label:    
        -  :sidsref:`DataArray_t`      
      * -  Data-Type:    
        -  :sidskey:`I4` , :sidskey:`I8` , :sidskey:`R4` , :sidskey:`R8` , or :sidskey:`C1`      
      * -  Dimensions:    
        -  User defined     
      * -  Dimension Values:     
        -  User defined     
      * -  Data:    
        -  Data quantity     
      * -  Cardinality:    
        -  0, *N*      
      * -  Child Nodes:    
        -  :ref:`DataArray_t figure <DataArrayFigure>`  

.. container:: figelem
 
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

.. container:: figelem
 
   .. list-table::
      :class:  figtable
      :stub-columns: 1
      :widths: 38 62
     
      * -  Name:    
        -  User defined     
      * -  Label:     
        -  :sidsref:`AdditionalFamilyName_t`      
      * -  See:    
        -  :ref:`BC_t figure <BCFigure>`  

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

.. container:: figelem
 
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

.. last line
