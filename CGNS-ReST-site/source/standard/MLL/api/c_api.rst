.. _cgns_api_c-ref:

###################################################
CGNS/MLL API Overview for C and Fortran applications
###################################################

These are all the types and functions available in the CGNS C API.

.. note::
  For details and conventions regarding the equivalent Fortran APIs,
  please refer to :ref:`MLLGeneralRemarks-ref`.

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

CGNS Base Information
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="../../FMM/nodes.html#cgnsbase-t"><code>CGNSBase_t</code></a>
             (<a href="../../SIDS/hierarchy.html#cgns-entry-level-structure-definition-cgnsbase-t">SIDS</a>)</p>

.. doxygengroup:: CGNSBaseInformation
    :content-only:

------

.. _CGNSZoneInformation-ref: 

CGNS Zone Information
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.Zone_t"><code>Zone_t</code></a>
             (<a href="../../SIDS/hierarchy.html#zone-structure-definition-zone-t">SIDS</a>))</p>

.. <a href="../../FMM/nodes.html#Zone">File Mapping</a>)</p>

.. doxygengroup:: CGNSZoneInformation
    :content-only:

------

.. _SimulationType-ref: 

Simulation Type
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.SimulationType_t"><code>SimulationType_t</code></a>

.. doxygengroup:: SimulationType
    :content-only:

------

**********************
Descriptors
**********************

.. _DescriptiveText-ref:

Descriptive Text
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>Descriptor_t</code>

.. doxygengroup:: DescriptiveText
    :content-only:

------

.. _OrdinalValue-ref:

Ordinal Value
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>Ordinal_t</code>

.. doxygengroup:: OrdinalValue
    :content-only:

------

**********************
Physical Data
**********************

.. _DataArrays-ref:

Data Arrays
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DataArray_t</code>

.. doxygengroup:: DataArrays
    :content-only:

------

.. _DataClass-ref:

Data Class (DataClass_t)
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.DataClass_t"><code>DataClass_t</code></a>

.. doxygengroup:: DataClass
    :content-only:

------

.. _DataConversionFactors-ref:

Data Conversion Factors
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DataConversion_t</code>

.. doxygengroup:: DataConversionFactors
    :content-only:

------

.. _DimensionalUnits-ref:

Dimensional Units
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>DimensionalUnits_t</code>

.. doxygengroup::  DimensionalUnits
    :content-only:

------

.. _DimensionalExponents-ref:

Dimensional Exponents
_________________________________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DimensionalExponents_t</code>

.. doxygengroup::  DimensionalExponents
    :content-only:

------

**********************
Location and Position
**********************

.. _GridLocation-ref:

Grid Location
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.GridLocation_t"><code>GridLocation_t</code></a>
             (<a href="../../SIDS/block.html#GridLocation">SIDS</a>,
              <a href="../../FMM/nodes.html#GridLocation">File Mapping</a>)</p>

.. doxygengroup:: GridLocation
    :content-only:

------

.. _PointSets-ref:

Point Sets
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>IndexArray_t</code>,
             <code>IndexRange_t</code>
             (<a href="../../SIDS/block.html#IndexArray">SIDS</a>,
              <a href="../../FMM/nodes.html#IndexRange">File Mapping</a>)</p>

.. doxygengroup:: PointSets
    :content-only:

------

.. _RindLayers-ref:

Rind Layers
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>Rind_t</code>
             (<a href="../../SIDS/block.html#Rind">SIDS</a>,
              <a href="../../FMM/nodes.html#Rind">File Mapping</a>)</p>

.. doxygengroup:: RindLayers
    :content-only:

------

**********************
Auxiliary Data
**********************

.. _ReferenceState-ref:

Reference State
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>ReferenceState_t</code>

.. doxygengroup:: ReferenceState
    :content-only:

------

.. _Gravity-ref:

Gravity
______________________

.. raw:: html

   <p><i>Node</i>:  <code>Gravity_t</code>

.. doxygengroup:: Gravity
    :content-only:

------

.. _ConvergenceHistory-ref:

Convergence History
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>ConvergenceHistory_t</code>

.. doxygengroup:: ConvergenceHistory
    :content-only:

------

.. _IntegralData-ref:

Integral Data
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>IntegralData_t</code>

.. doxygengroup:: IntegralData
    :content-only:

------

.. _UserDefinedData-ref:

User-Defined Data
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>UserDefinedData_t</code>

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

Zone Grid Coordinates
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>GridCoordinates_t</code>

.. doxygengroup:: ZoneGridCoordinates
    :content-only:

------

.. _ElementConnectivity-ref:

Element Connectivity
____________________________________________

.. raw:: html

   <p><i>Node</i>: <a href="./enums.html#c.ElementType_t"><code>Elements_t</code></a>
             (<a href="../../SIDS/grid.html#Elements">SIDS</a>,
              <a href="../../FMM/nodes.html#Elements">File Mapping</a>)</p>

.. doxygengroup:: ElementConnectivity
    :content-only:

------

.. _Axisymmetry-ref:

Axisymmetry
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>Axisymmetry_t</code>

.. doxygengroup:: Axisymmetry
    :content-only:

------

.. _Rotating-ref:

Rotating Coordinates
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>RotatingCoordinates_t</code>

.. doxygengroup:: RotatingCoordinates
    :content-only:

------

**********************
Solution Data
**********************

.. _FlowSolution-ref:

Flow Solution
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>FlowSolution_t</code>

.. doxygengroup:: FlowSolution
    :content-only:

------

.. _DiscreteData-ref:

Discrete Data
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DiscreteData_t</code>

.. doxygengroup:: DiscreteData
    :content-only:

------

.. _ZoneSubregions-ref:

Zone Subregions
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>ZoneSubRegion_t</code>

.. doxygengroup:: ZoneSubregions
    :content-only:

------

**********************
Grid Connectivity
**********************

.. _OneToOneConnectivity-ref:

One-to-One Connectivity
_________________________________________________________________

.. raw:: html

   <p><i>Node</i>: <code>GridConnectivity1to1_t</code>

.. doxygengroup:: OneToOneConnectivity
    :content-only:

------

.. _GeneralizedConnectivity-ref:

Generalized Connectivity
_________________________________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>GridConnectivity_t</code>

.. doxygengroup:: GeneralizedConnectivity
    :content-only:

------

.. _SpecialGridConnectivityProperty-ref:

Special Grid Connectivity Properties
_________________________________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>GridConnectivityProperty_t</code>

.. doxygengroup:: SpecialGridConnectivityProperty
    :content-only:

------

.. _OversetHoles-ref:

Overset Holes
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>OversetHoles_t</code>

.. doxygengroup:: OversetHoles
    :content-only:

------

**********************
Boundary Conditions
**********************

.. _BoundaryConditionType-ref:

Boundary Condition Type and Location
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>BC_t</code>

.. doxygengroup:: BoundaryConditionType
    :content-only:

------

.. _BoundaryConditionDatasets-ref:

Boundary Condition Datasets
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>BCDataSet_t</code>

.. doxygengroup:: BoundaryConditionDatasets
    :content-only:

------

.. _BCData-ref:

Boundary Condition Data
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>BCData_t</code>

.. doxygengroup:: BCData
    :content-only:

------

.. _SpecialBoundaryConditionProperty-ref:

Special Boundary Condition Properties
_________________________________________________________________

.. raw:: html

   <p><i>Node</i>: <code>BCProperty_t</code>

.. doxygengroup:: SpecialBoundaryConditionProperty
    :content-only:

------

**********************
Equation Specification
**********************

.. _FlowEquationSet-ref:

Flow Equation Set
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>FlowEquationSet_t</code>

.. doxygengroup:: FlowEquationSet
    :content-only:

------

.. _ParticleEquationSet-ref:

Particle Equation Set
________________________________________________

.. raw:: html

   <p><i>Node</i>: <a href="./enums.html#c.ParticleEquationSet_t"><code>ParticleEquationSet_t</code></a>
              (<a href="../../SIDS/particles.html#ParticleEquationSet">SIDS</a>,
               <a href="../../FMM/nodes.html#ParticleEquationSet">File Mapping</a>)</p>

.. doxygengroup:: ParticleEquationSet
    :content-only:

------

.. _GoverningEquations-ref:

Governing Equations
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>GoverningEquations_t</code>

.. doxygengroup:: GoverningEquations
    :content-only:

------

.. _ParticleGoverningEquations-ref:

Particle Governing Equations
________________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.ParticleGoverningEquationsType_t"><code>ParticleGoverningEquationsType_t</code></a>


.. doxygengroup:: ParticleGoverningEquations
    :content-only:

------

.. _AuxiliaryModel-ref:

Auxiliary Model
____________________________________________
.. doxygengroup:: AuxiliaryModel
    :content-only:

------

.. _ParticleModel-ref:

Particle Model
________________________________________________

.. raw:: html

   <p><i>Node</i>:  <a href="./enums.html#c.ParticleModelType_t"><code>ParticleModelType_t</code></a>


.. doxygengroup:: ParticleModel
    :content-only:

------

**********************
Families
**********************

.. _CGNSFamilyDefinition-ref:

Family Definition
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>Family_t</code>

.. doxygengroup:: CGNSFamilyDefinition
    :content-only:

------

.. _CGNSGeometry-ref:

Geometry Reference
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>GeometryReference_t</code>

.. doxygengroup:: CGNSGeometryReference
    :content-only:

------

.. _CGNSFamilyBoundaryCondition-ref:

Family Boundary Condition
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>FamilyBC_t</code>

.. doxygengroup:: CGNSFamilyBoundaryCondition
    :content-only:

------

.. _FamilyName-ref:

Family Name
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>FamilyName_t</code>

.. doxygengroup:: FamilyName
    :content-only:

------

**********************
Time-Dependent Data
**********************

.. _BaseIterativeData-ref:

Base Iterative Data
____________________________________________

.. raw:: html

   <i>Node</i>: <a href="./enums.html#c.BaseIterativeData_t"><code>BaseIterativeData_t</code></a>
             (<a href="../../SIDS/time.html#BaseIterativeData">SIDS</a>,
              <a href="../../FMM/nodes.html#BaseIterativeData">File Mapping</a>)

.. doxygengroup:: BaseIterativeData
    :content-only:

------

.. _ZoneIterativeData-ref:

Zone Iterative Data
____________________________________________

.. raw:: html

   <i>Node</i>:  <a href="./enums.html#c.ZoneIterativeData_t"><code>ZoneIterativeData_t</code></a>
              (<a href="../../SIDS/time.html#ZoneIterativeData">SIDS</a>,
               <a href="../../FMM/nodes.html#ZoneIterativeData">File Mapping</a>)

.. doxygengroup:: ZoneIterativeData
    :content-only:

------

.. _ParticleIterativeData-ref:

Particle Iterative Data
____________________________________________

.. raw:: html

   <i>Node</i>: <a href="./enums.html#c.ParticleIterativeData_t"><code>ParticleIterativeData_t</code></a>
             (<a href="../../SIDS/time.html#ParticleIterativeData">SIDS</a>,
              <a href="../../FMM/nodes.html#ParticleIterativeData">File Mapping</a>)

.. doxygengroup:: ParticleIterativeData
    :content-only:

------


.. _RigidGridMotion-ref:

Rigid Grid Motion
____________________________________________

.. raw:: html

   <p><i>Node</i>: <code>RigidGridMotion_t</code>
             (<a href="../../SIDS/time.html#RigidGridMotion">SIDS</a>,
              <a href="../../FMM/nodes.html#RigidGridMotion">File Mapping</a>)</p>

.. doxygengroup:: RigidGridMotion
    :content-only:

------

.. _ArbitraryGridMotion-ref:

Arbitrary Grid Motion
________________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>ArbitraryGridMotion_t</code>
             (<a href="../../SIDS/time.html#ArbitraryGridMotion">SIDS</a>,
              <a href="../../FMM/filemap/nodes.html#ArbitraryGridMotion">File Mapping</a>)</p>

.. doxygengroup:: ArbitraryGridMotion
    :content-only:

------

.. _ZoneGridConnectivity-ref:

Zone Grid Connectivity
________________________________________________

.. raw:: html

   <p><i>Node</i>: <code>ZoneGridConnectivity_t</code>
             (<a href="../../SIDS/time.html#ZoneGridConnectivity">SIDS</a>,
              <a href="../../FMM/filemap/nodes.html#ZoneGridConnectivity">File Mapping</a>)</p>

.. doxygengroup:: ZoneGridConnectivity
    :content-only:

------

**********************
Links
**********************

.. _Links-ref:

.. doxygengroup:: Links
    :content-only:


**********************
Particle Specification
**********************

.. _ParticleZoneInformation-ref:


Particle Zone Information
________________________________________________

.. note::
   When a CGNS file is opened via the cg_open() MLL function, the particle zones are sorted
   alphanumerically by name (the creation order is ignored/discarded). It is considered good
   standard practice to always choose particle names to be alphabetically increasing.
   For example, Particle0001, Particle0002, etc. is appropriate for up to 9999 particles.

.. doxygengroup:: ParticleZoneInformation
    :content-only:

------

.. _ParticleCoordinates-ref:

Particle Coordinates
________________________________________________

.. doxygengroup:: ParticleCoordinates
    :content-only:

------

.. _ParticleSolution-ref:

Particle Solution
________________________________________________

.. doxygengroup:: ParticleSolution
    :content-only:

------

.. _ParticleSolutionData-ref:

Particle Solution Data
________________________________________________

.. doxygengroup:: ParticleSolutionData
    :content-only:



