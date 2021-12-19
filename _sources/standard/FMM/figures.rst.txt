.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

   
.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)


.. _StandardFMMFigures:

CGNS File Mapping Figures
=========================

This section contains figures illustrating the nodal structure of a CGNS database.
An example file hierarchy is shown below, but without any internal detail of the individual nodes.
Just below the :sidskey:`Root Node` is a :sidsref:`CGNSLibraryVersion_t` node, and one or more :sidsref:`CGNSBase_t` nodes.
Each :sidskey:`CGNSBase_t` node represents the root node of a CGNS database.

.. _example-hierarchy:

.. figure:: ../../../images/filemap/cgns_figure1.gif
   :width: 600px
   :align: center
   :alt: Example file hierarchy


The remaining figures present all the nodes defined in the :ref:`SIDS <CGNS-SIDS>` that have child nodes.
An example illustrating the general layout of these figures is shown below.

.. figure:: ../../../images/filemap/example_node.gif
   :width: 540px
   :align: center
   :alt: Example node


At the top of each figure is a single parent node (with a tan background), and below it are boxes (with gray backgrounds) containing descriptions of the various child nodes.

In the parent's box are links to the figures corresponding to its parents in turn.
Each child's "**Label:**" entry is a link to the definition of that data structure in the :ref:`SIDS <CGNS-SIDS>`.
If a child node has children of its own, the "**Child Nodes:**" entry is a link to the figure showing that node as a parent, with its children.
To save space, nodes that were shown in a previous figure are abbreviated, with a link to that figure in the "**See:**" entry.

.. note::

  In some of the figures the data type is specified as :sidskey:`cgsize_t`.
  This data type has been introduced with the advent of CGNS library version 3.1.3, and is the natural size of a word for a given compilation of the library.
  For a 32-bit compilation, :sidskey:`cgsize_t` will be a 32-bit integer (:sidskey:`I4`), and for a 64-bit compilation it will be a 64-bit integer (:sidskey:`I8`).
  Regardless of how the file is written, the data is returned to an application as :sidskey:`cgsize_t`.
  When reading :sidskey:`I8` values in a 32-bit application, an error will be generated if the size of the data exceeds the 32-bit integer limitation.


The following list contains links to the remaining figures. 

.. toctree::

  ArbitraryGridMotion
  Area
  AverageInterface
  Axisymmetry
  BaseIterativeData
  BC
  BCData
  BCDataSet
  BCProperty
  CGNSBase
  ChemicalKineticsModel
  ConvergenceHistory
  DataArray
  DimensionalExponents
  DimensionalUnits
  Elements
  EMConductivityModel
  EMElectricFieldModel
  EMMagneticFieldModel
  Family
  FamilyBC
  FamilyBCDataSet
  FlowEquationSet
  FlowSolution
  GasModel
  GeometryReference
  GoverningEquations
  Gravity
  GridConnectivity
  GridConnectivity1to1
  GridConnectivityProperty
  GridCoordinates
  IntegralData
  OversetHoles
  Periodic
  ReferenceState
  RigidGridMotion
  RotatingCoordinates
  ThermalConductivityModel
  ThermalRelaxationModel
  TurbulenceClosure
  TurbulenceModel
  UserDefinedData
  ViscosityModel
  WallFunction
  Zone
  ZoneBC
  ZoneGridConnectivity
  ZoneIterativeData
  ZoneSubRegion

.. last line