.. _cgns_api_c-ref:

###############
CGNS C API
###############

These are all the types and functions available in the CGNS C API.

.. _CGNSFile-ref:

******************************************
File and Library Operations
******************************************

.. doxygengroup:: CGNSFile
    :content-only:

------

.. _CGNSInternals-ref:

Configuring CGNS Internals
________________________________________________

.. doxygengroup:: CGNSInternals_FNC_CG_CONFIG
    :content-only:
..
  Keep the reference order to be after CGNSInternals_FNC_CG_CONFIG
..

List of Valid CGNS Configuration Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. doxygengroup:: CGNSInternals_CG_CONFIG
    :content-only:

.. doxygengroup:: CGNSInternals
    :content-only:

.. _CGNSInterfaceCGIO-ref:

Interfacing with CGIO
____________________________________________
.. doxygengroup:: CGNSInterfaceCGIO
    :content-only:

------

**********************
Navigating a CGNS File
**********************

.. _AccessingANode-ref:

Accessing a Node
____________________________________________
.. doxygengroup:: AccessingANode
    :content-only:

.. doxygenpage:: CGNS_Navigation_Ill
    :content-only:

------

.. _DeletingANode-ref:

Deleting a Node
____________________________________________
.. doxygengroup:: DeletingANode
    :content-only:

------

.. _errorhandling-ref:

**********************
Error Handling
**********************

.. doxygengroup:: ErrorHandling
    :content-only:

------

**********************
Structural Nodes
**********************

.. _CGNSBaseInformation-ref: 

CGNS Base Information (CGNSBase_t)
____________________________________________
.. doxygengroup:: CGNSBaseInformation
    :content-only:

------

.. _CGNSZoneInformation-ref: 

CGNS Zone Information (Zone_t)
____________________________________________
.. doxygengroup:: CGNSZoneInformation
    :content-only:

------

.. _SimulationType-ref: 

Simulation Type (SimulationType_t)
____________________________________________
.. doxygengroup:: SimulationType
    :content-only:

------

**********************
Descriptors
**********************

.. _DescriptiveText-ref:

Descriptive Text (Descriptor_t)
____________________________________________
.. doxygengroup:: DescriptiveText
    :content-only:

------

.. _OrdinalValue-ref:

Ordinal Value (Ordinal_t)
____________________________________________
.. doxygengroup:: OrdinalValue
    :content-only:

------

**********************
Physical Data
**********************

.. _DataArrays-ref:

Data Arrays (DataArray_t)
____________________________________________
.. doxygengroup:: DataArrays
    :content-only:

------

.. _DataClass-ref:

Data Class (DataClass_t)
____________________________________________
.. doxygengroup:: DataClass
    :content-only:

------

.. _DataConversionFactors-ref:

Data Conversion Factors (DataConversion_t)
____________________________________________
.. doxygengroup:: DataConversionFactors
    :content-only:

------

.. _DimensionalUnits-ref:

Dimensional Units (DimensionalUnits_t)
____________________________________________
.. doxygengroup::  DimensionalUnits
    :content-only:

------

.. _DimensionalExponents-ref:

Dimensional Exponents (DimensionalExponents_t)
_________________________________________________________________
.. doxygengroup::  DimensionalExponents
    :content-only:

------

**********************
Location and Position
**********************

.. _GridLocation-ref:

Grid Location (GridLocation_t)
____________________________________________
.. doxygengroup:: GridLocation
    :content-only:

------

.. _PointSets-ref:

Point Sets (IndexArray_t, IndexRange_t)
____________________________________________
.. doxygengroup:: PointSets
    :content-only:

------

.. _RindLayers-ref:

Rind Layers (Rind_t)
____________________________________________
.. doxygengroup:: RindLayers
    :content-only:

------

**********************
Auxiliary Data
**********************

.. _ReferenceState-ref:

Reference State (ReferenceState_t)
____________________________________________
.. doxygengroup:: ReferenceState
    :content-only:

------

.. _Gravity-ref:

Gravity (Gravity_t)
______________________
.. doxygengroup:: Gravity
    :content-only:

------

.. _ConvergenceHistory-ref:

Convergence History (ConvergenceHistory_t)
____________________________________________
.. doxygengroup:: ConvergenceHistory
    :content-only:

------

.. _IntegralData-ref:

Integral Data (IntegralData_t)
____________________________________________
.. doxygengroup:: IntegralData
    :content-only:

------

.. _UserDefinedData-ref:

User-Defined Data (UserDefinedData_t)
____________________________________________
.. doxygengroup:: UserDefinedData
    :content-only:

------

.. _FreeingMemory-ref:

Freeing Memory
____________________________________________
.. doxygengroup:: FreeingMemory
    :content-only:

------

**********************
Grid Specification
**********************

.. _ZoneGridCoordinates-ref:

Zone Grid Coordinates (GridCoordinates_t)
____________________________________________
.. doxygengroup:: ZoneGridCoordinates
    :content-only:

------

.. _ElementConnectivity-ref:

Element Connectivity (Elements_t)
____________________________________________
.. doxygengroup:: ElementConnectivity
    :content-only:

------

.. _Axisymmetry-ref:

Axisymmetry (Axisymmetry_t)
____________________________________________
.. doxygengroup:: Axisymmetry
    :content-only:

------

.. _Rotating-ref:

Rotating Coordinates (RotatingCoordinates_t)
____________________________________________
.. doxygengroup:: RotatingCoordinates
    :content-only:

------

**********************
Solution Data
**********************

.. _FlowSolution-ref:

Flow Solution (FlowSolution_t)
____________________________________________
.. doxygengroup:: FlowSolution
    :content-only:

------

.. _DiscreteData-ref:

Discrete Data (DiscreteData_t)
____________________________________________
.. doxygengroup:: DiscreteData
    :content-only:

------

.. _ZoneSubregions-ref:

Zone Subregions (ZoneSubRegion_t)
____________________________________________
.. doxygengroup:: ZoneSubregions
    :content-only:

------

**********************
Grid Connectivity
**********************

.. _OneToOneConnectivity-ref:

One-to-One Connectivity (GridConnectivity1to1_t)
_________________________________________________________________
.. doxygengroup:: OneToOneConnectivity
    :content-only:

------

.. _GeneralizedConnectivity-ref:

Generalized Connectivity (GridConnectivity_t)
_________________________________________________________________
.. doxygengroup:: GeneralizedConnectivity
    :content-only:

------

.. _SpecialGridConnectivityProperty-ref:

Special Grid Connectivity Properties (GridConnectivityProperty_t)
_________________________________________________________________
.. doxygengroup:: SpecialGridConnectivityProperty
    :content-only:

------

.. _OversetHoles-ref:

Overset Holes (OversetHoles_t)
____________________________________________
.. doxygengroup:: OversetHoles
    :content-only:

------

**********************
Boundary Conditions
**********************

.. _BoundaryConditionType-ref:

Boundary Condition Type and Location (BC_t)
____________________________________________
.. doxygengroup:: BoundaryConditionType
    :content-only:

------

.. _BoundaryConditionDatasets-ref:

Boundary Condition Datasets (BCDataSet_t)
____________________________________________
.. doxygengroup:: BoundaryConditionDatasets
    :content-only:

------

.. _BCData-ref:

Boundary Condition Data (BCData_t)
____________________________________________
.. doxygengroup:: BCData
    :content-only:

------

.. _SpecialBoundaryConditionProperty-ref:

Special Boundary Condition Properties (BCProperty_t)
_________________________________________________________________
.. doxygengroup:: SpecialBoundaryConditionProperty
    :content-only:

------

**********************
Equation Specification
**********************

.. _FlowEquationSet-ref:

Flow Equation Set (FlowEquationSet_t)
____________________________________________
.. doxygengroup:: FlowEquationSet
    :content-only:

------

.. _GoverningEquations-ref:

Governing Equations (GoverningEquations_t)
____________________________________________
.. doxygengroup:: GoverningEquations
    :content-only:

------

.. _AuxiliaryModel-ref:

Auxiliary Model
____________________________________________
.. doxygengroup:: AuxiliaryModel
    :content-only:

------

**********************
Families
**********************

.. _CGNSFamilyDefinition-ref:

Family Definition (Family_t)
____________________________________________
.. doxygengroup:: CGNSFamilyDefinition
    :content-only:

------

.. _CGNSGeometry-ref:

Geometry Reference (GeometryReference_t)
____________________________________________
.. doxygengroup:: CGNSGeometryReference
    :content-only:

------

.. _CGNSFamilyBoundaryCondition-ref:

Family Boundary Condition (FamilyBC_t)
____________________________________________
.. doxygengroup:: CGNSFamilyBoundaryCondition
    :content-only:

------

.. _FamilyName-ref:

Family Name (FamilyName_t)
____________________________________________
.. doxygengroup:: FamilyName
    :content-only:

------

**********************
Time-Dependent Data
**********************

.. _BaseIterativeData-ref:

Base Iterative Data (BaseIterativeData_t)
____________________________________________
.. doxygengroup:: BaseIterativeData
    :content-only:

------

.. _ZoneIterativeData-ref:

Zone Iterative Data (ZoneIterativeData_t)
____________________________________________
.. doxygengroup:: ZoneIterativeData
    :content-only:

------

.. _RigidGridMotion-ref:

Rigid Grid Motion (RigidGridMotion_t)
____________________________________________
.. doxygengroup:: RigidGridMotion
    :content-only:

------

.. _ArbitraryGridMotion-ref:

Arbitrary Grid Motion (ArbitraryGridMotion_t)
________________________________________________
.. doxygengroup:: ArbitraryGridMotion
    :content-only:

------

.. _ZoneGridConnectivity-ref:

Zone Grid Connectivity (ZoneGridConnectivity_t)
________________________________________________
.. doxygengroup:: ZoneGridConnectivity
    :content-only:

------

**********************
Links
**********************

.. _Links-ref:

.. doxygengroup:: Links
    :content-only:
