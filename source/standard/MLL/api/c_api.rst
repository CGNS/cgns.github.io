.. _cgns_api_c-ref:

#####################################################
CGNS/MLL API Overview for C and Fortran applications
#####################################################

These are all the types and functions available in the CGNS C API.

.. note::
   Please refer to :ref:`MLLGeneralRemarks-ref` for details and conventions regarding
   the equivalent Fortran APIs, paying special attention to :ref:`CGNSFortranPort-ref`.

******************************************
File and Library Operations
******************************************

.. cgns-group-function-summary:: CGNSFile Opening and Closing a CGNS File

..
  Because of the way internals is split into two groups, this summary of functions is done manually.  CGNSInternals_FNC_CG_CONFIG has no matching reference.  The manual implementation merges the output of the following:
..
  cgns-group-function-summary:: CGNSInternals_FNC_CG_CONFIG Configuring CGNS Internals
..
  cgns-group-function-summary:: CGNSInternals Configuring CGNS Internals

* :ref:`Configuring CGNS Internals<CGNSInternals-ref>`

  * :cpp:func:`cg_configure<cg_configure>` - Configure CGNS library internal options.
  * :cpp:func:`cg_error_handler<cg_error_handler>` - Set CGNS error handler
  * :cpp:func:`cg_set_compress<cg_set_compress>` - Set CGNS compression mode.
  * :cpp:func:`cg_get_compress<cg_get_compress>` - Get CGNS compression mode.
  * :cpp:func:`cg_set_path<cg_set_path>` - Set the CGNS link search path.
  * :cpp:func:`cg_add_path<cg_add_path>` - Add to the CGNS link search path.

.. cgns-group-function-summary:: CGNSInterfaceCGIO Interfacing with CGIO

.. _CGNSFile-ref:

CGNS File Operations
____________________________________________

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

.. cgns-group-function-summary:: AccessingANode
.. cgns-group-function-summary:: DeletingANode

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

.. cgns-group-function-summary:: ErrorHandling

.. doxygengroup:: ErrorHandling
    :content-only:

------

**********************
Structural Nodes
**********************

.. cgns-group-function-summary:: CGNSBaseInformation CGNS Base Information
.. cgns-group-function-summary:: CGNSZoneInformation CGNS Zone Information
.. cgns-group-function-summary:: SimulationType

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
             (<a href="../../SIDS/hierarchy.html#zone-structure-definition-zone-t">SIDS</a>)</p>

.. <a href="../../FMM/nodes.html#Zone">File Mapping</a>)</p>

.. note::
   When a CGNS file is opened via the cg_open() MLL function, the zones are sorted alphanumerically by name (the creation order is ignored/discarded).
   This mechanism is provided to enable ordinal zone indexing.
   Therefore, if ordinal zone indexing is desired, it is considered good standard practice to always choose zone names to be alphabetically increasing.
   For example, Zone0001, Zone0002, etc. is appropriate for up to 9999 zones.

.. warning::
   Because the cgnsview tool uses the low-level cgio API, it does not sort the zones by name and zone order presented may not match that of the MLL API. Generally, cgnsview presents the zones in creation order for both ADF and HDF5 formats. One exception is CGNS files that are either created or opened using the HDF5 v1.6 library (or older) will always be presented alphabetically (creation order tracking was added to HDF5 in v1.8).

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

.. cgns-group-function-summary:: DescriptiveText
.. cgns-group-function-summary:: OrdinalValue

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

.. cgns-group-function-summary:: DataArrays
.. cgns-group-function-summary:: DataClass
.. cgns-group-function-summary:: DataConversionFactors
.. cgns-group-function-summary:: DimensionalUnits
.. cgns-group-function-summary:: DimensionalExponents

.. _DataArrays-ref:

Data Arrays
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DataArray_t</code>

.. doxygengroup:: DataArrays
    :content-only:

------

.. _DataClass-ref:

Data Class
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

.. cgns-group-function-summary:: GridLocation
.. cgns-group-function-summary:: PointSets
.. cgns-group-function-summary:: RindLayers

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

.. cgns-group-function-summary:: ReferenceState
.. cgns-group-function-summary:: Gravity
.. cgns-group-function-summary:: ConvergenceHistory
.. cgns-group-function-summary:: IntegralData
.. cgns-group-function-summary:: UserDefinedData
.. cgns-group-function-summary:: FreeingMemory

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

.. cgns-group-function-summary:: ZoneGridCoordinates
.. cgns-group-function-summary:: ElementConnectivity
.. cgns-group-function-summary:: Axisymmetry
.. cgns-group-function-summary:: RotatingCoordinates

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

.. _RotatingCoordinates-ref:

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

.. cgns-group-function-summary:: FlowSolution
.. cgns-group-function-summary:: FlowSolutionData
.. cgns-group-function-summary:: DiscreteData
.. cgns-group-function-summary:: ZoneSubregions

.. _FlowSolution-ref:

Flow Solution
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>FlowSolution_t</code>

.. doxygengroup:: FlowSolution
    :content-only:

------

.. _FlowSolutionData-ref:

Flow Solution Data
____________________________________________

.. doxygengroup:: FlowSolutionData
    :content-only:

------

.. _DiscreteData-ref:

Discrete Data
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>DiscreteData_t</code>

.. note::
   :code:`DiscreteData_t` nodes are intended for the storage of fields of data not usually identified as part of the flow solution, such as fluxes or equation residuals.
   The description for these functions is similar to the :ref:`FlowSolution_t<FlowSolution-ref>` node as described above.
   To read and write the discrete data, use :cpp:func:`cg_goto` to access the :code:`DiscreteData_t` node, then :cpp:func:`cg_array_read` and :cpp:func:`cg_array_write`.
   The dimensions provided to the array-write family of functions must match the dimensions specified by the :code:`Zone_t` and :code:`DiscreteData_t` nodes.
   Use :cpp:func:`cg_gridlocation_write` and :cpp:func:`cg_rind_write` under the :code:`DiscreteData_t` node, as required.

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

.. cgns-group-function-summary:: OneToOneConnectivity One-to-One Connectivity
.. cgns-group-function-summary:: GeneralizedConnectivity
.. cgns-group-function-summary:: SpecialGridConnectivityProperty
.. cgns-group-function-summary:: OversetHoles

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

.. cgns-group-function-summary:: BoundaryConditionType Boundary Condition Type and Location
.. cgns-group-function-summary:: BoundaryConditionDatasets
.. cgns-group-function-summary:: BCData Boundary Condition Data
.. cgns-group-function-summary:: SpecialBoundaryConditionProperty Special Boundary Condition Properties

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

.. cgns-group-function-summary:: FlowEquationSet
.. cgns-group-function-summary:: ParticleEquationSet
.. cgns-group-function-summary:: GoverningEquations
.. cgns-group-function-summary:: ParticleGoverningEquations
.. cgns-group-function-summary:: AuxiliaryModel
.. cgns-group-function-summary:: ParticleModel

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

.. cgns-group-function-summary:: CGNSFamilyDefinition Family Definition
.. cgns-group-function-summary:: CGNSFamilyHierarchyTreeDefinition Family Hierarchy Tree
.. cgns-group-function-summary:: CGNSGeometryReference Geometry Reference
.. cgns-group-function-summary:: CGNSFamilyBoundaryCondition Family Boundary Condition
.. cgns-group-function-summary:: FamilyName

.. _CGNSFamilyDefinition-ref:

Family Definition
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>Family_t</code>

.. doxygengroup:: CGNSFamilyDefinition
    :content-only:

------

.. _CGNSFamilyHierarchyTreeDefinition-ref:

Family Hierarchy Tree
____________________________________________

.. raw:: html

   <p><i>Node</i>:  <code>Family_t</code>

.. doxygengroup:: CGNSFamilyHierarchyTreeDefinition
    :content-only:

------

.. _CGNSGeometryReference-ref:

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

.. cgns-group-function-summary:: BaseIterativeData
.. cgns-group-function-summary:: ZoneIterativeData
.. cgns-group-function-summary:: ParticleIterativeData
.. cgns-group-function-summary:: RigidGridMotion
.. cgns-group-function-summary:: ArbitraryGridMotion
.. cgns-group-function-summary:: ZoneGridConnectivity

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

.. cgns-group-function-summary:: Links

.. _Links-ref:

.. doxygengroup:: Links
    :content-only:


**********************
Particle Specification
**********************

.. cgns-group-function-summary:: ParticleZoneInformation
.. cgns-group-function-summary:: ParticleCoordinates
.. cgns-group-function-summary:: ParticleSolution
.. cgns-group-function-summary:: ParticleSolutionData

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
