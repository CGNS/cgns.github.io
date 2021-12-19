.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources



.. default-domain:: sids


.. role:: sidskey(code)


.. role:: sidsref(code)





.. _FMMNodeDescriptions:

Detailed CGNS Node Descriptions
===============================



This section, together with the :ref:`CGNS File Mapping Figures <StandardFMMFigures>` , constitutes a complete description of the CGNS database structure, together with detailed descriptions of the contents of each attribute of each node. It is intended to be suitable as a reference for anyone implementing CGNS within their own database manager or using the :ref:`CGIO Core Routines <CGIOCoreRoutines>`. It should also be of interest to those wishing to understand exactly where information is stored within a CGNS database.



Note that it is the advertised purpose of the :ref:`CGNS Mid-Level Library <StandardMLL>`  to store and retrieve information in conformity with the mapping herein described. Therefore, anyone accessing a CGNS database through the CGNS routines alone does not need a detailed understanding of the file mapping per se. However, this document should still prove useful in ascertaining the meaning of some of the arguments which must be supplied to the Library routines. Further, it will be necessary to consult the :ref:`SIDS <CGNS-SIDS>` themselves to determine some of the naming conventions.



The node descriptions in this section are closely coupled to and cross-referenced with the :ref:`CGNS File Mapping Figures <StandardFMMFigures>`, which show all the nodes defined in the SIDS that have child nodes. In the current section, the "**Children:**" entry in the list of  *Node Attributes*  is a link to the figure showing that node with its children. The "**Label:**" entry (or, in some cases, the "**Name:**" entry) is a link to the definition of the node's data structure in the SIDS.



The nodal hierarchy of the CGNS database directly reflects that of the :ref:`SIDS <CGNS-SIDS>` . Certain sections of the SIDS, notably :ref:`Building-Block Structure Definitions <StandardBlockStructure>` , :ref:`Data-Array Structure Definitions <StandardDataArrayStruct>` , and :ref:`Miscellaneous Data Structures <StandardMiscDataStruct>` , describe basic data structures which appear repeatedly as children of nodes representing more complex structures. In order to simplify the presentation and avoid the introduction of undefined terms, this section has been divided into two parts.
The first defines a number of :ref:`basic types <basicnodes>` which recur often in the structure, and the second describes :ref:`higher level nodes <specializednodes>`  of more specific function built from the :ref:`basic nodes <basicnodes>`



.. _basicnodes:


Basic CGNS Nodes
----------------



In this section we describe CGNS nodes which hold fundamental  *types*  of information. Their structure and function, which are the same everywhere, are described here. However, the  *meaning*  of the data they hold at any particular point in a CGNS database depends on the context, i.e., the parent node. Therefore, where necessary, any special context-dependent meaning is elaborated in the paragraph devoted to the parent.



.. _descriptorgroup:


Descriptor Group
^^^^^^^^^^^^^^^^


These are user-assigned nodes designed to further describe the user's intent. Their data is meant for human perusal or other user-designated purposes.



.. _Descriptor:

:sidskey:`Descriptor_t`
~~~~~~~~~~~~~~~~~~~~~~~


The purpose of a node of type :sidskey:`Descriptor_t`  is to store textual data. It is not intended to be read by any system software, except to return the text for human examination.


The intent of the :sidskey:`Descriptor_t`  node is to hold comment sufficient to allow someone other than the originator to understand what the node contains. This may consist of a problem description, reference documents, personal notes, etc.


Any node may have zero to many :sidskey:`Descriptor_t`  children, with the uses differentiated by the Name field. At this time, there are  *no*  conventions for these names or for the form of the associated text. It is expected that a standard set such as :sidskey:`README` , :sidskey:`TimeStamp` , etc. will evolve as a matter of practice.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`Descriptor_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string to be stored, including any carriage control or null bytes.
   * - Data:
     - String - Since line terminators can be stored within the data, the user could conceptually store an entire document in this        area, read it into a program and then print it out. For example,        an entire PostScript document describing the problem (and maybe        results) could be stored in the Data field, read by a program and then sent to a printer.
   * - Children:
     - None
   * - Cardinality:
     - 0, *N*





.. _Ordinal:

:sidskey:`Ordinal_t`
~~~~~~~~~~~~~~~~~~~~

Because there is no notion of order among children, there is occasionally a desire to order children in a way that survives from one opening of a CGNS database to another. The current CGNS Library provides means of doing this. However, another early method was to place the node "number" in a child of type :sidskey:`Ordinal_t` .


Like :sidskey:`Descriptor_t` , the :sidskey:`Ordinal_t`  node is completely under the control of the user, who takes full responsibility for its content. Unlike :sidskey:`Descriptor_t` , CGNS conventions do not encourage the use of :sidskey:`Ordinal_t` , as it usually encodes information which is redundant with the name. It is not read or written by standard CGNS software, and so there is no assurance that sibling nodes will be differently, consecutively, or consistently numbered by :sidskey:`Ordinal_t` . Clearly, if :sidskey:`Ordinal_t`  must be used, no node should have more than one :sidskey:`Ordinal_t`  child, and no two siblings should have :sidskey:`Ordinal_t`  children containing the same data.


It is worth noting that, if consistent numbering is desired, one way of achieving it is to make the desired integer either the name or part of the name. In fact, if, for example, individual zones are left unnamed, the default convention will provide names of :sidskey:`Zone1` , :sidskey:`Zone2` , etc. Alternatively, the character strings ":sidskey:`1` ", ":sidskey:`2` ", ..., are legal names. The CGNS software, of course, will return these as strings. This may necessitate type conversion or parsing before the names can be used as integer indices.



.. list-table:: **Node Attributes**
   :stub-columns: 1



   * - Name:
     - :sidskey:`Ordinal`
   * - Label:
     - :sidsref:`Ordinal_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - The user-defined ordinal number (an integer).
   * - Children:
     - None
   * - Cardinality:
     - 0,1





.. _physicalgroup:

Physical Data Group
^^^^^^^^^^^^^^^^^^^


.. _DataClass:

:sidskey:`DataClass_t`
~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`DataClass_t`  node specifies the dimensional nature of the data in and below its parent. It overrides any :sidskey:`DataClass_t`  information higher up in the tree. There are six recognized string values. It is necessary to consult the SIDS to determine the precise meaning.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:

     - :sidskey:`DataClass`
   * - Label:

     - :sidskey:`DataClass_t`
   * - DataType:

     - :sidskey:`C1`
   * - Dimension:

     - 1
   * - Dimension Values:

     - The length of the string
   * - Data:

     - One of: :sidskey:`DataClassNull` , :sidskey:`DataClassUserDefined` ,       :sidskey:`Dimensional` , :sidskey:`NormalizedByDimensional` ,       :sidskey:`NormalizedByUnknownDimensional` , :sidskey:`NondimensionalParameter` , or :sidskey:`DimensionlessConstant`
   * - Children:

     - None
   * - Cardinality:

     - 0,1





.. _DimensionalUnits:

:sidskey:`DimensionalUnits_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`DimensionalUnits_t`  node specifies dimensional units which apply to data in and below its parent.  It overrides any :sidskey:`DimensionalUnits_t`  information higher up in the tree. There are five strings to specify, corresponding, respectively, to units for mass, length, time, temperature, and angular measure. The number of recognized string values varies with the physical property.


Units for three additional types of data are specified in a child node, :ref:`AdditionalUnits_t <AdditionalUnits>` .


.. list-table:: **Node Attributes**
   :stub-columns: 1



   * - Name:
     - :sidskey:`DimensionalUnits`
   * - Label:
     - :sidsref:`DimensionalUnits_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 2
   * - Dimension Values:
     - (32,5)
   * - Data:
     - .. list-table::

         * - For mass, one of:
           - :sidskey:`MassUnitsNull` , :sidskey:`MassUnitsUserDefined` , :sidskey:`Kilogram` , :sidskey:`Gram` , :sidskey:`Slug` , :sidskey:`Pound-Mass`
         * - For length, one of:
           - :sidskey:`LengthUnitsNull` , :sidskey:`LengthUnitsUserDefined` ,               :sidskey:`Meter` , :sidskey:`Centimeter` , :sidskey:`Millimeter` ,               :sidskey:`Foot` , :sidskey:`Inch`
         * - For time, one of:
           - :sidskey:`TimeUnitsNull` , :sidskey:`TimeUnitsUserDefined` ,               :sidskey:`Second`
         * - For temperature, one of:
           - :sidskey:`TemperatureUnitsNull` ,               :sidskey:`TemperatureUnitsUserDefined` , :sidskey:`Kelvin` ,               :sidskey:`Celsius` , :sidskey:`Rankine` , :sidskey:`Fahrenheit`
         * - For angles, one of:
           - :sidskey:`AngleUnitsNull` , :sidskey:`AngleUnitsUserDefined` ,               :sidskey:`Degree` , :sidskey:`Radian`
   * - Children:
     - See :ref:`DimensionalUnits_t figure <DimensionalUnitsFigure>`
   * - Cardinality:
     - 0,1



.. _AdditionalUnits:

:sidskey:`AdditionalUnits_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`AdditionalUnits_t`  node specifies dimensional units for additional types of data. To maintain compatibility with earlier CGNS versions, this is an optional child node of :ref:`DimensionalUnits_t <DimensionalUnits>` . The specified units apply to data in and below the parent of the corresponding :sidskey:`DimensionalUnits_t`  node, and override any :sidskey:`AdditionalUnits_t`  information higher up in the tree. There are three strings to specify, corresponding, respectively, to units for electric current, substance amount, and luminous intensity. The number of recognized string values varies with the physical property.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`AdditionalUnits`
   * - Label:
     - :sidsref:`AdditionalUnits_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 2
   * - Dimension Values:
     - (32,3)
   * - Data:
     - .. list-table::

         * - For electric current, one of:
           - :sidskey:`ElectricCurrentUnitsNull`, :sidskey:`ElectricCurrentUnitsUserDefined` , :sidskey:`Ampere` ,               :sidskey:`Abampere` , :sidskey:`Statampere` , :sidskey:`Edison` ,               :sidskey:`auCurrent`
         * - For substance amount, one of:
           - :sidskey:`SubstanceAmountUnitsNull`, :sidskey:`SubstanceAmountUnitsUserDefined` , :sidskey:`Mole` ,               :sidskey:`Entities` , :sidskey:`StandardCubicFoot` ,               :sidskey:`StandardCubicMeter`
         * - For luminous intensity, one of:
           - :sidskey:`LuminousIntensityUnitsNull`, :sidskey:`LuminousIntensityUnitsUserDefined` , :sidskey:`Candela` ,               :sidskey:`Candle` , :sidskey:`Carcel` , :sidskey:`Hefner` ,               :sidskey:`Violle`
   * - Children:
     - None
   * - Cardinality:
     - 0,1


.. _DataConversion:

:sidskey:`DataConversion_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`DataConversion_t`  node specifies a non-homogeneous linear function which converts non-dimensional data in its parent to raw dimensional data. Although in principle it overrides any :sidskey:`DataConversion_t`  information higher up in the tree, it is generally not meaningful for it to apply to more than one kind of physical data. Therefore, CGNS specifies its use only as a child of a node which actually contains a single type of real data.


There are two values to specify, corresponding to the scale factor and offset. The SIDS contain the exact conversion formula.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`DataConversion`
   * - Label:
     - :sidsref:`DataConversion_t`
   * - DataType:
     - :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 2
   * - Data:
     - :sidskey:`ConversionScale` , :sidskey:`ConversionOffset`
   * - Children:
     - None
   * - Cardinality:
     - 0,1


.. _DimensionalExponents:

:sidskey:`DimensionalExponents_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`DimensionalExponents_t`  node specifies the powers of mass, length, time, temperature, and angular measure which characterize dimensional data in its parent. Although in principle it overrides any :sidskey:`DimensionalExponents_t`  information higher up in the tree, it is generally not meaningful for it to apply to more than one kind of physical data. Therefore, CGNS specifies its use only as a child of a node which actually contains a single type of real data. There are five values to specify, corresponding to the five types of units specified using :ref:`DimensionalUnits_t <DimensionalUnits>` . The data type is real, not integer.

Exponents for three additional types of data are specified in a child node, :ref:`AdditionalExponents_t <AdditionalExponents>` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`DimensionalExponents`
   * - Label:
     - :sidsref:`DimensionalExponents_t`
   * - DataType:
     - :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 5
   * - Data:
     - :sidskey:`MassExponent` , :sidskey:`LengthExponent` , :sidskey:`TimeExponent` ,       :sidskey:`TemperatureExponent` , :sidskey:`AngleExponent`
   * - Children:
     - See :ref:`DimensionalExponents_t figure <DimensionalExponentsFigure>`
   * - Cardinality:
     - 0,1


.. _AdditionalExponents:

:sidskey:`AdditionalExponents_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`AdditionalExponents_t`  node specifies the powers of the units for additional types of data, which characterize the corresponding dimensional data. There are three values to specify, corresponding to the three types of units specified using :ref:`AdditionalUnits_t <AdditionalUnits>` . The data type is real, not integer.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`AdditionalExponents`
   * - Label:
     - :sidsref:`AdditionalExponents_t`
   * - DataType:
     - :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 3
   * - Data:
     - :sidskey:`ElectricCurrentExponent`, :sidskey:`SubstanceAmountExponent`, :sidskey:`LuminousIntensityExponent`
   * - Children:
     - None
   * - Cardinality:
     - 0,1



.. _DataArray:

:sidskey:`DataArray_t`
~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`DataArray_t`  node is a very general type of node meant to hold large arrays of data, such as grids and flowfields. Often, some of the attributes of a :sidskey:`DataArray_t`  node depend on the context in which the node is found; that is, they are structure parameters.


For example, the SIDS specify that the Data Type of :sidskey:`DataArray_t`  is a structure parameter, ":sidskey:`DataType`", which may assume any of the values ":sidskey:`In`", ":sidskey:`Rn`", or ":sidskey:`Cn`".


The other two attributes of :sidskey:`DataArray_t` , :sidskey:`Dimensions`  and :sidskey:`DataSize` , also depend on the context where they are being used. :sidskey:`Dimensions`  is a function of the underlying dimensionality of the data being described (often :sidskey:`IndexDimension` , defined in the :sidskey:`CGNSBase_t`  node), and the :sidskey:`DataSize`  may be inferred from detailed descriptions of the grid.


A node may have any number of :sidskey:`DataArray_t`  children. The meaning of their contents is differentiated by Name, often according to conventions specified by the SIDS. SIDS names are usually precise and descriptive, such as :sidskey:`CoordinateTheta`  or :sidskey:`EnergyInternal` . (See the SIDS for a :ref:`current list of sanctioned names <dataname>` .) Conversely, quantities not specified by the SIDS can be stored in :sidskey:`DataArray_t`  nodes, but should be given names other than those specified in the SIDS. In other words, to comply with the SIDS requires that one give a quantity the SIDS-defined name  *if and only if*  it is one of the SIDS-defined quantities.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - Context dependent
   * - Label:
     - :sidsref:`DataArray_t`
   * - DataType:
     - Context dependent
   * - Dimension:
     - Context dependent
   * - Dimension Values:
     - Context dependent
   * - Data:
     - The array of data values
   * - Children:
     - See :ref:`DataArray_t figure <DataArrayFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`DataType`, dimension of the data, size of the data



Integer Arrays
~~~~~~~~~~~~~~

Integer array nodes perform the same function as nodes of type :sidskey:`DataArray_t` , but store integer instead of real arrays. They are always of type :sidskey:`int[]`  or :sidskey:`cgsize_t[]` , with the dimensions and values given either explicitly in the appropriate fields, or as parameters or functions. The :sidskey:`cgsize_t`  data type is used wherever there is the potential of exceeding the size limit for a 32-bit integer (:sidskey:`I4` ), such as :sidskey:`PointList` , :sidskey:`PointRange` , and :sidskey:`ElementRange` .




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - Context dependent
   * - Label:
     - :sidsref:`int` , :sidskey:`int[IndexDimension]` , :sidskey:`int[2*IndexDimension]` ,       or :sidskey:`int[1 + ... + IndexDimension]`
   * - DataType:
     - :sidskey:`I4`  or :sidskey:`cgsize_t`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1, :sidskey:`IndexDimension` , :sidskey:`2*IndexDimension` , or       :sidskey:`(1 + ... + IndexDimension)`
   * - Data:
     - The array of integer values
   * - Cardinality:
     - 0,1
   * - Children:
     - None
   * - Parameters:
     - :sidskey:`IndexDimension`  or none (context dependent)



.. _locationgroup:

Location and Position Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. _GridLocation:

:sidskey:`GridLocation_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`GridLocation_t`  node specifies the physical location, with respect to the underlying grid, with which the field data below its parent is associated. The value (data field) is a character string of enumeration type, i.e., it must take one of a number of predefined values. These values are: :sidskey:`Vertex` , :sidskey:`CellCenter` , :sidskey:`FaceCenter` , :sidskey:`IFaceCenter` , :sidskey:`JFaceCenter` , :sidskey:`KFaceCenter` , or :sidskey:`EdgeCenter` . The strings are case sensitive, and an exact match is required. The :sidskey:`GridLocation_t`  node is optional, and the default is :sidskey:`Vertex` .




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GridLocation`
   * - Label:
     - :sidsref:`GridLocation_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of the string value
   * - Data:
     - :sidskey:`Vertex` , :sidskey:`CellCenter` , :sidskey:`FaceCenter` , :sidskey:`IFaceCenter` ,       :sidskey:`JFaceCenter` , :sidskey:`KFaceCenter` , or :sidskey:`EdgeCenter`
   * - Children:
     - None
   * - Cardinality:
     - 0,1




.. _Rind:

:sidskey:`Rind_t`
~~~~~~~~~~~~~~~~~

The presence of a :sidskey:`Rind_t`  node indicates that field data stored below its parent includes values associated with a spatial extent beyond that of the basic underlying grid. Such data often arise from the use of ghost cells, or from the copying of information from adjacent zones.


Within a single zone, the size of the basic grid is found in the :ref:`data field of the Zone_t node <Zone>` . The data field of a :sidskey:`Rind_t`  node contains integers specifying the number of planes (for structured grids) or number of rind points or elements (for unstructured grids) of included extra data. The planes for structured grids correspond to the low and high values in the  *i* -direction, low and high values in the  *j* -direction, and low and high values in the  *k* -direction (if needed), in that order. Note that the actual size of the field data, which is stored in a :sidskey:`DataArray_t`  sibling node, is a :sidskey:`DataSize`  structure parameter which depends on the basic grid size, the :sidskey:`GridLocation` , and the :sidskey:`Rind` .



The :sidskey:`Rind_t`  node is optional, and the default is no rind.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Rind`
   * - Label:
     - :sidsref:`Rind_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - :sidskey:`2*IndexDimension`
   * - Data:
     - Number of planes of extra data in low  *i* , high  *i* ,        low  *j* , high  *j* , etc., (for structured grids) or        number of points or elements of extra data (for unstructured        grids)
   * - Children:
     - None
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`IndexDimension`



.. _IndexRange:

:sidskey:`IndexRange_t`
~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`IndexRange_t`  node describes a subregion of a zone. This may be, for example, a sub-block or a portion of a face of a zone. It may be used to describe the locations of boundary condition patches and holes for overset grids.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`PointRange` , :sidskey:`PointRangeDonor` , :sidskey:`ElementRange` ,       or user defined
   * - Label:
     - :sidsref:`IndexRange_t`
   * - DataType:
     - :sidskey:`cgsize_t`
   * - Dimension:
     - 2
   * - Dimension Values:
     - :sidskey:`IndexDimension` , 2
   * - Data:
     - First indices, last indices
   * - Children:
     - None
   * - Cardinality:
     - Context dependent
   * - Parameters:
     - :sidskey:`IndexDimension`





.. _IndexArray:

:sidskey:`IndexArray_t`
~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`IndexArray_t`  node describes a general subregion of a zone. Unlike :sidskey:`IndexRange_t` , it lists all the elements of the subregion, rather then only the first and last ones. Its use is similar to :sidskey:`IndexRange_t` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`PointList` , :sidskey:`PointListDonor` , :sidskey:`CellListDonor` ,       or :sidskey:`InwardNormalList`
   * - Label:
     - :sidsref:`IndexArray_t`
   * - DataType:
     - :sidskey:`cgsize_t` , or (for :sidskey:`InwardNormalList` ) :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 2
   * - Dimension Values:
     - :sidskey:`IndexDimension` , number of items in the list;       or (for :sidskey:`InwardNormalList` ) :sidskey:`PhysicalDimension` , number       of items in the list
   * - Data:
     - Index coordinates of each point or element in the list, or       (for :sidskey:`InwardNormalList` ) physical-space normal vectors       at each point or element in the list
   * - Children:
     - None
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`IndexDimension` , either :sidskey:`PointListSize`  or       :sidskey:`ListLength` , and :sidskey:`DataType` ;       or (for :sidskey:`InwardNormalList` )       :sidskey:`PhysicalDimension` , :sidskey:`ListLength` , and :sidskey:`DataType`




.. _auxiliarygroup:

Auxiliary Data Group
^^^^^^^^^^^^^^^^^^^^


.. _ReferenceState:

:sidskey:`ReferenceState_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The appearance of a :sidskey:`ReferenceState_t`  node is optional. It is used to specify the values of flow quantities at reference conditions, e.g., at freestream or stagnation. This is typically done for the whole database, in which case the :sidskey:`ReferenceState_t`  node is a child of the :sidskey:`CGNSBase_t`  node.

:sidskey:`ReferenceState_t`  nodes follow the usual convention that information specified lower in the tree overrides higher level specifications. Such overrides are therefore specified if a :sidskey:`ReferenceState_t`  node appears as a child of a :sidskey:`Zone_t` , :sidskey:`ZoneBC_t` , or :sidskey:`BCDataSet_t`  node.

The actual values are stored in one or more :sidskey:`DataArray_t`  children whose names identify the quantities being stored. If present, the units specified in the :sidskey:`DimensionalUnits_t`  child apply to all :sidskey:`DataArray_t`  children, subject to the usual override convention. ( I.e., if one of the :sidskey:`DataArray_t`  children itself has a :sidskey:`DimensionalUnits_t`  child, it takes precedence over the higher level specification.)


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ReferenceState`
   * - Label:
     - :sidsref:`ReferenceState_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`ReferenceState_t figure <ReferenceStateFigure>`
   * - Cardinality:
     - 0,1







.. _ConvergenceHistory:

:sidskey:`ConvergenceHistory_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`ConvergenceHistory_t`  nodes are intended for the storage of lists of quantities accumulated during calculations associated with either the entire CGNS database or with a single zone.

In the former case, they are called Global convergence histories, and appear as children of the :sidskey:`CGNSBase_t`  node. In the latter, they are called Local and stored below, with the zones to which they correspond.

Each :sidskey:`ConvergenceHistory_t`  node is a parent of a collection of one-dimensional :sidskey:`DataArray_t`  nodes, each of which contains a list of values of a quantity defined by the user. These quantities are differentiated by their user-assigned Names. User definitions of the names are recorded in a :sidskey:`Descriptor_t`  child node with Name :sidskey:`NormDefinitions` . Children of types :sidskey:`DataClass_t`  and :sidskey:`DimensionalUnits_t`  modify the meaning of the :sidskey:`DataArray_t`  children in the usual manner.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GlobalConvergenceHistory`  if under a :sidskey:`CGNSBase_t`  node;       :sidskey:`ZoneConvergenceHistory`  if under a :sidskey:`Zone_t`  node
   * - Label:
     - :sidsref:`ConvergenceHistory_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - Number of iterations
   * - Children:
     - See :ref:`ConvergenceHistory_t figure <ConvergenceHistoryFigure>`
   * - Cardinality:
     - 0,1



.. _IntegralData:

:sidskey:`IntegralData_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`IntegralData_t`  nodes are intended for the storage of integrated flow quantities such as mass flows, forces and moments. These are kept in :sidskey:`DataArray_t`  children just as in the :sidskey:`ConvergenceHistory_t`  nodes, except that these nodes hold only one real number each.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`IntegralData_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`IntegralData_t figure <IntegralDataFigure>`
   * - Cardinality:
     - 0, *N*



.. _UserDefinedData:

:sidskey:`UserDefinedData_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`UserDefinedData_t`  nodes are intended as a means of storing arbitrary user-defined data in :sidskey:`Descriptor_t`  and :sidskey:`DataArray_t`  children without the restrictions or implicit meanings imposed on these node types at other node locations.

Multiple :sidskey:`Descriptor_t`  and :sidskey:`DataArray_t`  children may be stored below a :sidskey:`UserDefinedData_t`  node, and the :sidskey:`DataArray_t`  children may be of any dimension and size.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`UserDefinedData_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`UserDefinedData_t figure <UserDefinedDataFigure>`
   * - Cardinality:
     - 0, *N*





.. _Gravity:

:sidskey:`Gravity_t`
~~~~~~~~~~~~~~~~~~~~

An optional :sidskey:`Gravity_t`  node may be used to define the gravitational vector.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Gravity`
   * - Label:
     - :sidsref:`Gravity_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`Gravity_t figure <GravityFigure>`
   * - Cardinality:
     - 0,1



.. _specializednodes:

Specialized Nodes
-----------------

In this section we describe nodes whose use is specialized to certain types of CFD-related data. Although these nodes may appear in multiple places in a CGNS DataBase, they play a single role in the description of the data.


.. _gridspecification:

Grid Specification
^^^^^^^^^^^^^^^^^^

CGNS recognizes the notion of a collection of subdomains called zones, within each of which there is a single structured or unstructured grid. Mathematically, the grid is an assignment of a location in physical space to each element in a discrete computational space. An essential feature of the grid is the connection structure it inherits from the underlying computational space.

It is possible, given a grid, to create others from it, by translation to cell centers, for example. However, CGNS views these as new field structures associated with the original grid, and the File Mapping specifies that they be stored as :ref:`FlowSolution_t or DiscreteData_t nodes <fieldspecification>` .


.. _GridCoordinates:

:sidskey:`GridCoordinates_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`GridCoordinates_t`  node describes a grid associated with a single zone. For a structured zone, the connection structure of the underlying computational space is that of a rectangular array, and its dimension is the :sidskey:`IndexDimension` , that is, the number of integers required to identify a point in the grid. The physical dimension is the number of real coordinates assigned at each grid point and need not be the same. Thus CGNS can store a grid, for example, with :sidskey:`IndexDimension`  equal to two and a physical dimension of three, that is, a structured grid on a curved surface.

:sidskey:`IndexDimension`  is a zone dependent parameter. For an unstructured grid, it always equals one, meaning that a unique index is required to specified a node location. For a structured grid, :sidskey:`IndexDimension`  varries with the :sidskey:`CellDimension`  of the mesh. For a mesh composed of 3D cells, :sidskey:`IndexDimension`  equals 3, while for a mesh composed of surface or shell elements, :sidskey:`IndexDimension`  equals 2. The values of the physical coordinates of the grid points are stored in :sidskey:`DataArray_t`  children of :sidskey:`GridCoordinates_t` . The names of the coordinates are stored in the Name field of the corresponding :sidskey:`DataArray_t`  node. For common coordinate systems, i.e., Cartesian, polar, cylindrical, and spherical, the names are specified by the SIDS.


Unlike :ref:`FlowSolution_t and DiscreteData_t nodes <fieldspecification>` , :sidskey:`GridCoordinates_t`  nodes are not permitted to have :sidskey:`GridLocation_t`  children, because all grid points are at vertices by definition.


Coordinate arrays may also contain rind data. If they do, the :sidskey:`GridCoordinates_t`  node must have a :sidskey:`Rind_t`  child node describing the amount of rind. All :sidskey:`DataArray_t`  nodes under :sidskey:`GridCoordinates_t`  must have the same size. Because the number of field quantities to be stored depends on the number of rind, the actual dimension values are functions, specified in this document by the generic term :sidskey:`DataSize[]` .



Under each node of type :sidskey:`Zone_t` , the original grid is contained in a node named :sidskey:`GridCoordinates` .  Additional :sidskey:`GridCoordinates_t`  data structures are allowed, with user-defined names, to store the grid at multiple time steps or iterations.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GridCoordinates`  or user defined
   * - Label:
     - :sidsref:`GridCoordinates_t`
   * - DataType:
     - :sidskey:`MT`  or :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 2
   * - Dimension Values:
     - :sidskey:`PhysicalDimension` , 2
   * - Data:
     - :sidskey:`BoundingBox`  values
   * - Children:
     - See :ref:`GridCoordinates_t figure <GridCoordinatesFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`VertexSize` , :sidskey:`PhysicalDimension`
   * - Functions:
     - :sidskey:`DataSize`



.. _Elements:

:sidskey:`Elements_t`
~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`Elements_t`  data structure is required for unstructured zones, and contains the element connectivity data, the element type, the element range, the parent elements data, and the number of boundary elements.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`Elements_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 2
   * - Data:
     - :sidskey:`ElementType`  value, :sidskey:`ElementSizeBoundary`
   * - Children:
     - See :ref:`Elements_t figure <ElementsFigure>`
   * - Cardinality:
     - 0, *N*


.. _Axisymmetry:

:sidskey:`Axisymmetry_t`
~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`Axisymmetry_t`  data structure may be included as a child of the :sidskey:`CGNSBase_t`  node to record the axis of rotation and the angle of rotation around this axis for an axisymmetric database.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Axisymmetry`
   * - Label:
     - :sidsref:`Axisymmetry_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`Axisymmetry_t figure <AxisymmetryFigure>`
   * - Cardinality:
     - 0,1


.. _RotatingCoordinates:

:sidskey:`RotatingCoordinates_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`RotatingCoordinates_t`  data structure may be included as a child of either the :sidskey:`CGNSBase_t`  node or a :sidskey:`Zone_t`  node to record the center of rotation and the rotation rate vector for a rotating coordinate system.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`RotatingCoordinates`
   * - Label:
     - :sidsref:`RotatingCoordinates_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`RotatingCoordinates_t figure <RotatingCoordinatesFigure>`
   * - Cardinality:
     - 0,1



.. _fieldspecification:

Field Specification
^^^^^^^^^^^^^^^^^^^

The object of computational field physics is to compute fields of physical data associated with points in space.



.. _FlowSolution:

:sidskey:`FlowSolution_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`FlowSolution_t`  node describes a field of physical data associated with the grid for a single zone. It is intended for the storage of computed flowfield data such as densities and pressures. There is no convention as to how many or what kind of quantities must or may be stored. In particular, it is not specified that the quantities need in any sense be either complete or non-redundant.

The data are stored in :sidskey:`DataArray_t`  children of :sidskey:`FlowSolution_t` . These :sidskey:`DataArray_t`  nodes are dimensioned by the same underlying :sidskey:`IndexDimension`  parameter as the grid, and the order of storage within the :sidskey:`DataArray_t`  nodes is presumed the same as it is for the grid. The names of the physical quantities are stored in the Name field of the corresponding :sidskey:`DataArray_t`  node. For common fluid dynamic quantities the :ref:`names are specified by the SIDS <dataname>` .

The relationship between the locations of the field quantities and the vertices of the grid is specified by a :sidskey:`GridLocation_t`  child node. If this node is absent, the field quantities are assumed to be associated with the grid vertices. Field arrays may also contain rind data. If they do, the :sidskey:`FlowSolution_t`  node must have a :sidskey:`Rind_t`  child node describing the amount of rind. All :sidskey:`DataArray_t`  nodes under a single :sidskey:`FlowSolution_t`  must have the same size. Field arrays containing different numbers of rind must be stored under different :sidskey:`FlowSolution_t`  nodes. There may be any number of nodes of type :sidskey:`FlowSolution_t`  under a :sidskey:`Zone_t` .



Because the number of field quantities to be stored depends on the number of rind and on the location with respect to the grid, the actual dimension values are functions, specified in this document by the generic term :sidskey:`DataSize[]` .



The meaning of the field arrays is modified in the usual way by any :sidskey:`DataClass_t`  or :sidskey:`DimensionalUnits_t`  children of the :sidskey:`FlowSolution_t`  node.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`FlowSolution_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`FlowSolution_t figure <FlowSolutionFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`VertexSize` , :sidskey:`CellSize`
   * - Functions:
     - :sidskey:`DataSize`





.. _DiscreteData:

:sidskey:`DiscreteData_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`DiscreteData_t`  nodes are identical to :sidskey:`FlowSolution_t`  nodes, but are intended for the storage of fields of real data not usually identified as part of the field solution, such as cell-centered grids.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`DiscreteData_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`FlowSolution_t figure <FlowSolutionFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`VertexSize` , :sidskey:`CellSize`
   * - Functions:
     - :sidskey:`DataSize`





.. _ZoneSubRegion:

:sidskey:`ZoneSubRegion_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`ZoneSubRegion_t`  node allows for the ability to give flowfield or other information over a subset of the entire zone in a CGNS file. This subset may be over a portion of a boundary, or it may be over a portion of the entire field.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`ZoneSubRegion_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - RegionCellDimension
   * - Children:
     - See :ref:`ZoneSubRegion_t figure <ZoneSubRegionFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`VertexSize` , :sidskey:`CellSize`
   * - Functions:
     - :sidskey:`DataSize`



.. _connectivitygroup:

Connectivity Group
^^^^^^^^^^^^^^^^^^



:sidskey:`Transform`  Node
~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`Transform`  node is a node of type :sidskey:`int[]`  which is identified by its name rather than its label. Thus the name must be ":sidskey:`Transform` ". It appears only as a child of a node of type :sidskey:`GridConnectivity1to1_t` .

This node stores the transformation matrix relating the indices of two adjacent zones. Its data field contains a list of :sidskey:`IndexDimension`  signed integers, each within the range :sidskey:`[-IndexDimension, ..., +IndexDimension]` , and no two of which have the same absolute value. Thus in 3-D allowed components are :math:`0`, :math:`\pm 1`, :math:`\pm 2`, and :math:`\pm 3`.
Each component of the array shows the image in the adjacent zone of a positive index increment in the current zone. The SIDS contain complete details.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Transform`
   * - Label:
     - ":sidskey:`int[IndexDimension]` "
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - :sidskey:`IndexDimension`
   * - Data:
     - Transformation matrix (shorthand)
   * - Children:
     - None
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`IndexDimension`





.. _GridConnectivityType:

:sidskey:`GridConnectivityType_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this node is to describe the type of zone-to-zone connectivity specified by its parent, which is always a :sidskey:`GridConnectivity_t`  node. The connectivity type is given in the data field as a character string which may take one of three specific values: :sidskey:`Abutting` , :sidskey:`Abutting1to1` , or :sidskey:`Overset` .

There is a shorthand form of the :sidskey:`GridConnectivity_t`  node, namely, :sidskey:`GridConnectivity1to1_t` , which incorporates the assumption that the connection is :sidskey:`Abutting1to1` . Nodes of type :sidskey:`GridConnectivity1to1_t`  do not have :sidskey:`GridConnectivityType_t`  subnodes. However, :sidskey:`GridConnectivity1to1_t`  nodes can only be used to specify zone-to-zone connections on rectangular subregions between two structured zones. So the use of :sidskey:`GridConnectivityType_t`  subnodes to specify :sidskey:`Abutting1to1`  is required if the connecting regions are not rectangular, or if the connectivity involves a least one unstructured zone.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GridConnectivityType`
   * - Label:
     - :sidsref:`GridConnectivityType_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`Abutting` , :sidskey:`Abutting1to1` , or :sidskey:`Overset`
   * - Children:
     - None
   * - Cardinality:
     - 0,1



.. _GridConnectivity1to1:

:sidskey:`GridConnectivity1to1_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This node is a shorthand format of :sidskey:`GridConnectivity_t`  capable of describing only :sidskey:`Abutting1to1`  connections between two structured zones. The underlying subregion must have rectangular data structure.

Each :sidskey:`GridConnectivity1to1_t`  node describes a subregion of a face of a zone whose vertices are coincident in a 1-to-1 fashion with those of a corresponding subregion of a face of another zone. Each :sidskey:`ZoneGridConnectivity_t`  node may have as many :sidskey:`GridConnectivity1to1_t`  (or :sidskey:`GridConnectivity_t` ) children as are required to describe the connection structure.

The location of the connected subregion of a face of the current zone is given in a single child of type :sidskey:`IndexRange_t` , whose name is specified by the mapping as ":sidskey:`PointRange` ". The location of the corresponding subregion on a face of the other zone is given in a single child of type :sidskey:`IndexRange_t` , whose name is specified by the mapping as ":sidskey:`PointRangeDonor` ". The first (i.e., beginning) points in these :sidskey:`IndexRange_t`  nodes are presumed to be coincident. The specification of the correspondence is completed by the inclusion of a :sidskey:`Transform`  child node which describes the relative orientation of the two systems of indices. The second (i.e., end) point of the :sidskey:`PointRange`  subnode specifies the extant of the connection.

In general, the File Mapping seeks to avoid the storage of redundant data. However, there are two redundancies associated with :sidskey:`GridConnectivity1to1_t` . First, for the sake of symmetry, the information recorded here is duplicated (in reverse) in a corresponding node under the donor zone. It is expected that these two specifications will agree.

Second, the end point of the :sidskey:`PointRangeDonor`  can be calculated from the other three points specified, along with the transform. However, the transform cannot be inferred from the four points. Therefore, the end point of the :sidskey:`PointRangeDonor`  is considered to be redundant, and the three points and the transform are designated as the primary specification.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`GridConnectivity1to1_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ZoneDonorName`
   * - Children:
     - See :ref:`GridConnectivity1to1_t figure <GridConnectivity1to1Figure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension`





.. _GridConnectivity:

:sidskey:`GridConnectivity_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`GridConnectivity_t`  node is the most general format for describing grid connectivity. It can describe one-to-one, mismatched, and overset connectivity, and the underlying subregions of the connecting zones need not be rectangular.

Each :sidskey:`GridConnectivity_t`  node describes a subregion of a zone which corresponds to a subregion of another zone. Each :sidskey:`ZoneGridConnectivity_t`  node may have as many :sidskey:`GridConnectivity_t`  (or :sidskey:`GridConnectivity1to1_t` ) children as are required to describe the connection structure.

The location of the connected subregion of the current zone is given in a single child of type either :sidskey:`IndexRange_t`  or :sidskey:`IndexArray_t` , whose name is specified by the mapping as ":sidskey:`PointRange` " or ":sidskey:`PointList` ", respectively.

If the grid connectivity is one-to-one, the corresponding subregion is defined with a single child of type :sidskey:`IndexArray_t` , whose name is specified by the mapping as ":sidskey:`PointListDonor` ".  Otherwise, the corresponding subregion is defined by two child nodes, one defining the cells and the other the interpolation factors within the cells. See the SIDS for the complete description.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`GridConnectivity_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ZoneDonorName`
   * - Children:
     - See :ref:`GridConnectivity_t figure <GridConnectivityFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`CellDimension`
   * - Functions:
     - :sidskey:`PointListSize`





.. _GridConnectivityProperty:

:sidskey:`GridConnectivityProperty_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An optional :sidskey:`GridConnectivityProperty_t`  node may be used to record special properties associated with particular connectivity patches.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GridConnectivityProperty`
   * - Label:
     - :sidsref:`GridConnectivityProperty_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`GridConnectivityProperty_t figure <GridConnectivityPropertyFigure>`
   * - Cardinality:
     - 0,1



.. _Periodic:

:sidskey:`Periodic_t`
~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`Periodic_t`  node may be used as a child of :sidskey:`GridConnectivityProperty_t`  to record data associated with a periodic interface.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Periodic`
   * - Label:
     - :sidsref:`Periodic_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`Periodic_t figure <PeriodicFigure>`
   * - Cardinality:
     - 0,1







.. _AverageInterface:

:sidskey:`AverageInterface_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`AverageInterface_t`  node is used as a child of :sidskey:`GridConnectivityProperty_t`  when data at the current connectivity interface is to be averaged in some way prior to passing it to a neighboring interface.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`AverageInterface`
   * - Label:
     - :sidsref:`AverageInterface_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`AverageInterface_t figure <AverageInterfaceFigure>`
   * - Cardinality:
     - 0,1


.. _OversetHoles:

:sidskey:`OversetHoles_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`OversetHoles_t`  describes a region in a grid in which solution values are to be ignored because the data in the region is to be represented by values associated with other "overlapping" zones (equivalent to that specified by :sidskey:`IBLANK`  = 0 in the PLOT3D format). Each :sidskey:`ZoneGridConnectivity_t`  node may have as many :sidskey:`OversetHoles_t`  children as are required to describe the affected region.

Each hole is described either by a single child of type :sidskey:`IndexArray_t`  or by any number of children of type :sidskey:`IndexRange_t` . The latter is provided as a means of specifying holes which are unions of small numbers of logically rectangular subregions. However, if the region is irregular, the intent is that it should be specified by a single child of type :sidskey:`IndexArray_t`  which lists the points.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`OversetHoles_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`OversetHoles_t figure <OversetHolesFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension`





.. _ZoneGridConnectivity:

:sidskey:`ZoneGridConnectivity_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each :sidskey:`Zone_t`  node may have zero or more children of type :sidskey:`ZoneGridConnectivity_t` . It holds no data, but serves as the point below which all connectivity data associated with the zone can be found. Multiple :sidskey:`ZoneGridConnectivity_t`  nodes may be used to specify time-dependent changes in the connectivity information.



.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ZoneGridConnectivity or user defined`
   * - Label:
     - :sidsref:`ZoneGridConnectivity_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`ZoneGridConnectivity_t figure <ZoneGridConnectivityFigure>`
   * - Cardinality:
     - 0,N
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`CellDimension`



.. _bcgroup:

Boundary Condition Group
^^^^^^^^^^^^^^^^^^^^^^^^

Nodes in this group are used to specify the physical boundary conditions. Each boundary condition is associated with a subregion of a zone. For brevity below, we use the word "domain" to refer to the region on which a boundary condition is to be enforced.



The domain is usually, but not necessarily, a subregion of a face of the zone. The mapping is sufficiently general to permit the description of internal boundary conditions and boundary conditions which do not lie on a constant coordinate plane.



Mathematical boundary conditions are generally applied on subregions of physical dimension one less than the corresponding field problem. This condition, however, is neither defined nor enforced by the File Mapping.



A large number of standard boundary condition types`  are named by the SIDS. In addition, it is possible to define new types as collections of Dirichlet and Neumann conditions. It is not possible to describe the entire array of possibilities within this document, and the reader should consult the SIDS for a full description.



:sidskey:`InwardNormalIndex`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`InwardNormalIndex`  node is a node of type :sidskey:`int[IndexDimension]`  which is identified by its Name. It applies to structured grids only, and its function is to specify on which side of the domain the condition is to be enforced.



:sidskey:`InwardNormalIndex`  may have only one nonzero element, whose sign indicates the computational-coordinate direction of the boundary condition patch normal; this normal points into the interior of the zone. For example, if the domain lies on the face of a three-dimensional zone where the second index is a maximum, the inward normal index values are [0,-1,0].



The :sidskey:`InwardNormalIndex`  node must apply to the entire domain of the boundary condition.



For a boundary condition on a face of a zone, the :sidskey:`InwardNormalIndex`  can be calculated from other data and need not be specified. Its purpose is to define the normal direction for internal boundary conditions and other cases where the direction is ambiguous.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`InwardNormalIndex`
   * - Label:
     - ":sidskey:`int[IndexDimension]` "
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - :sidskey:`IndexDimension`
   * - Data:
     - Index of inward normal
   * - Children:
     - None
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`IndexDimension`



:sidskey:`InwardNormalList`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An :sidskey:`InwardNormalList`  node is a node of type :sidskey:`IndexArray_t`  identified by its Name. Its data field contains an array of physical (real) vectors which point into the region on which the boundary condition is to be applied.  It may be used for boundary conditions on complex domains for which :sidskey:`InwardNormalIndex`  is not defined, or to store vectors orthogonal to the domain of the boundary condition where these are not easily calculated from the domain itself.



.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`InwardNormalList`
   * - Label:
     - :sidsref:`IndexArray_t`
   * - DataType:
     - :sidskey:`R4`  or :sidskey:`R8`
   * - Dimension:
     - 2
   * - Dimension Values:
     - :sidskey:`PhysicalDimension` , :sidskey:`ListLength`
   * - Data:
     - Inward normal vectors
   * - Children:
     - None
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`PhysicalDimension` , :sidskey:`ListLength`





.. _BCData:

:sidskey:`BCData_t`
~~~~~~~~~~~~~~~~~~~

When global or local Dirichlet or Neumann boundary conditions are defined, a node of type :sidskey:`BCData_t`  is introduced to store the numerical data. For global data, this consists of a single quantity kept in a :sidskey:`DataArray_t`  child. For local data, e.g., a pressure profile, it is a vector of quantities stored in an order corresponding to that defining the domain and kept in a child node of type :sidskey:`DataArray_t` .



.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`DirichletData`  or :sidskey:`NeumannData`
   * - Label:
     - :sidsref:`BCData_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`BCData_t figure <BCDataFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`ListLength`



.. _BCDataSet:

:sidskey:`BCDataSet_t`
~~~~~~~~~~~~~~~~~~~~~~

The function of a :sidskey:`BCDataSet_t`  node is to specify the equations to be applied at the boundary, including any actual data values which may be required. The type of the equation is specified by the SIDS and recorded in the data field. For some types, the data is implicit or empty. For others, the data is specified in :sidskey:`BCData_t`  children.

If the locations at which the boundary conditions are to be applied are specified in :sidskey:`BCDataSet_t` , using :sidskey:`PointRange`  or :sidskey:`PointList` , the structure function :sidskey:`ListLength`  is used. Otherwise, the structure parameter :sidskey:`ListLength`  is required.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`BCDataSet_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`BCTypeSimple`  value
   * - Children:
     - See :ref:`BCDataSet_t figure <BCDataSetFigure>`
   * - Cardinality:
     - 0, *N*
   * - Functions:
     - :sidskey:`ListLength`
   * - Parameters:
     - :sidskey:`ListLength`


.. _BC:

:sidskey:`BC_t`
~~~~~~~~~~~~~~~

A :sidskey:`BC_t`  node specifies a single boundary condition to be applied on a single zone. It specifies the domain on which the condition is to be applied and the equations to be enforced. All the :sidskey:`BC_t`  nodes for a single zone are found under that zone's :sidskey:`ZoneBC_t`  node. A :sidskey:`ZoneBC_t`  node may have as many :sidskey:`BC_t`  children as are required to describe the physical boundary conditions on the corresponding zone.



The domain on which the boundary condition is to be enforced is specified by a single node of type either :sidskey:`IndexRange_t`  or :sidskey:`IndexArray_t` . The equations are specified in one or more :sidskey:`BCDataSet_t`  children.



The type of the boundary condition, which may be either simple or compound, is specified in the data field.  For a complete description, it is necessary to consult the SIDS.




.. list-table:: **Node Attributes**
   :stub-columns: 1



   * - Name:
     - User defined
   * - Label:
     - :sidsref:`BC_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`BCType`  value
   * - Children:
     - See :ref:`BC_t figure <BCFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`PhysicalDimension`





.. _ZoneBC:

:sidskey:`ZoneBC_t`
~~~~~~~~~~~~~~~~~~~

The :sidskey:`ZoneBC_t`  node occurs at most once for each zone and serves as the location under which all boundary conditions on that zone are collected.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ZoneBC`
   * - Label:
     - :sidsref:`ZoneBC_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`ZoneBC_t figure <ZoneBCFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`PhysicalDimension`





.. _BCProperty:

:sidskey:`BCProperty_t`
~~~~~~~~~~~~~~~~~~~~~~~

An optional :sidskey:`BCProperty_t`  node may be used to record special properties associated with particular boundary condition patches.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`BCProperty`
   * - Label:
     - :sidsref:`BCProperty_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`BCProperty_t figure <BCPropertyFigure>`
   * - Cardinality:
     - 0,1



.. _WallFunction:

:sidskey:`WallFunction_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`WallFunction_t`  node may be used as a child of :sidskey:`BCProperty_t`  to record data associated with the use of wall function boundary conditions.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`WallFunction`
   * - Label:
     - :sidsref:`WallFunction_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`WallFunction_t figure <WallFunctionFigure>`
   * - Cardinality:
     - 0,1







.. _Area:

:sidskey:`Area_t`
~~~~~~~~~~~~~~~~~


An :sidskey:`Area_t`  node may be used as a child of :sidskey:`BCProperty_t`  to record data associated with area-related boundary conditions such as bleed.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`Area`
   * - Label:
     - :sidsref:`Area_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`Area_t figure <AreaFigure>`
   * - Cardinality:
     - 0,1





.. _equationspecification:

Equation Specification Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Nodes in this group serve to identify the physical model associated with the data being recorded. Nearly always, the data is of enumeration type and is selected from a collection of terms defined in detail in the SIDS.  The names are largely self explanatory, and the detailed definitions will not be repeated here. Numerical values associated with the physical model depend on the type of modeling being chosen and are generally stored in child nodes of type :sidskey:`DataArray_t` .



.. _GoverningEquations:

:sidskey:`GoverningEquations_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This node names the equation set being solved, for example, :sidskey:`FullPotential`  or :sidskey:`NSTurbulent` . If Navier-Stokes, the diffusion terms retained may be specified in a :sidskey:`DiffusionModel`  subnode.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GoverningEquations`
   * - Label:
     - :sidsref:`GoverningEquations_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`GoverningEquationsType`  value
   * - Children:
     - See :ref:`GoverningEquations_t figure <GoverningEquationsFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`CellDimension`


.. _GasModel:

:sidskey:`GasModel_t`
~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`GasModel_t`  names the gas model used, for example, :sidskey:`Ideal`  or :sidskey:`VanderWaals` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GasModel`
   * - Label:
     - :sidsref:`GasModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`GasModelType`  value
   * - Children:
     - See :ref:`GasModel_t figure <GasModelFigure>`
   * - Cardinality:
     - 0,1


.. _ViscosityModel:

:sidskey:`ViscosityModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`ViscosityModel_t`  names the molecular viscosity model used to relate the viscosity to the temperature, for example, :sidskey:`PowerLaw`  or :sidskey:`SutherlandLaw` .




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ViscosityModel`
   * - Label:
     - :sidsref:`ViscosityModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ViscosityModelType`  value
   * - Children:
     - See :ref:`ViscosityModel_t figure <ViscosityModelFigure>`
   * - Cardinality:
     - 0,1



:sidskey:`EquationDimension`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node named :sidskey:`EquationDimension` , of type :sidskey:`int[]` , gives the number of dependent variables required for a complete solution description, or the number of equations being solved. For example, for :sidskey:`NSTurbulent`  with the  :math:`k`-:math:`\epsilon`  turbulence model in three dimensions, it is 7.

.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`EquationDimension`
   * - Label:
     - ":sidskey:`int` "
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - :sidskey:`EquationDimension`  value
   * - Children:
     - None
   * - Cardinality:
     - 0,1



.. _ThermalConductivityModel:

:sidskey:`ThermalConductivityModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`ThermalConductivityModel_t`  names the model used to relate the thermal conductivity to the temperature, for example, :sidskey:`ConstantPrandtl` , :sidskey:`PowerLaw` , or :sidskey:`SutherlandLaw` . These closely parallel the viscosity model.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ThermalConductivityModel`
   * - Label:
     - :sidsref:`ThermalConductivityModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ThermalConductivityModelType`  value
   * - Children:
     - See :ref:`ThermalConductivityModel_t figure <ThermalConductivityModelFigure>`
   * - Cardinality:
     - 0,1


.. _TurbulenceClosure:

:sidskey:`TurbulenceClosure_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`TurbulenceClosure_t`  names the method of closing the Reynolds stress equations when the governing equations are turbulent, for example, :sidskey:`EddyViscosity`  or :sidskey:`ReynoldsStressAlgebraic` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`TurbulenceClosure`
   * - Label:
     - :sidsref:`TurbulenceClosure_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`TurbulenceClosureType`  value
   * - Children:
     - See :ref:`TurbulenceClosure_t figure <TurbulenceClosureFigure>`
   * - Cardinality:
     - 0,1


.. _TurbulenceModel:

:sidskey:`TurbulenceModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`TurbulenceModel_t`  names the equation set used to model the turbulence quantities, for example, :sidskey:`Algebraic_BaldwinLomax`  or :sidskey:`OneEquation_SpalartAllmaras` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`TurbulenceModel`
   * - Label:
     - :sidsref:`TurbulenceModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`TurbulenceModelType`  value
   * - Children:
     - See :ref:`TurbulenceModel_t figure <TurbulenceModelFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`CellDimension`



.. _ThermalRelaxationModel:

:sidskey:`ThermalRelaxationModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`ThermalRelaxationModel_t`  names the equation set used to model the thermal relaxation quantities, for example, :sidskey:`Frozen`  or :sidskey:`ThermalEquilib` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ThermalRelaxationModel`
   * - Label:
     - :sidsref:`ThermalRelaxationModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ThermalRelaxationModelType`  value
   * - Children:
     - See :ref:`ThermalRelaxationModel_t figure <ThermalRelaxationModelFigure>`
   * - Cardinality:
     - 0,1







.. _ChemicalKineticsModel:

:sidskey:`ChemicalKineticsModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`ChemicalKineticsModel_t`  names the equation set used to model the chemical kinetics quantities, for example, :sidskey:`Frozen`  and :sidskey:`ChemicalEquilibCurveFit` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ChemicalKineticsModel`
   * - Label:
     - :sidsref:`ChemicalKineticsModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ChemicalKineticsModelType`  value
   * - Children:
     - See :ref:`ChemicalKineticsModel_t figure <ChemicalKineticsModelFigure>`
   * - Cardinality:
     - 0,1



.. _EMElectricFieldModel:

:sidskey:`EMElectricFieldModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`EMElectricFieldModel_t`  names the electric field model used for electromagnetic flows, for example, :sidskey:`Constant`  or :sidskey:`Voltage` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`EMElectricFieldModel`
   * - Label:
     - :sidsref:`EMElectricFieldModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`EMElectricFieldModelType`  value
   * - Children:
     - See :ref:`EMElectricFieldModel_t figure <EMElectricFieldModelFigure>`
   * - Cardinality:
     - 0,1


.. _EMMagneticFieldModel:

:sidskey:`EMMagneticFieldModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`EMMagneticFieldModel_t`  names the magnetic field model used for electromagnetic flows, for example, :sidskey:`Constant`  or :sidskey:`Interpolated`.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`EMMagneticFieldModel`
   * - Label:
     - :sidsref:`EMMagneticFieldModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`EMMagneticFieldModelType`  value
   * - Children:
     - See :ref:`EMMagneticFieldModel_t figure <EMMagneticFieldModelFigure>`
   * - Cardinality:
     - 0,1



.. _EMConductivityModel:

:sidskey:`EMConductivityModel_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`EMConductivityModel_t`  names the conductivity model used for electromagnetic flows, for example, :sidskey:`Constant`  or :sidskey:`Equilibrium_LinRessler` .


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`EMConductivityModel`
   * - Label:
     - :sidsref:`EMConductivityModel_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`EMConductivityModelType`  value
   * - Children:
     - See :ref:`EMConductivityModel_t figure <EMConductivityModelFigure>`
   * - Cardinality:
     - 0,1


.. _FlowEquationSet:

:sidskey:`FlowEquationSet_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node of type :sidskey:`FlowEquationSet_t`  appears either at the highest level of the tree (under :sidskey:`CGNSBase_t` ), to indicate the equation set whose solution is recorded throughout the database, or below a :sidskey:`Zone_t`  node, to indicate the set of equations solved in that zone. The usual convention applies, i.e., specifications at the local (zone) level override global specifications.



.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`FlowEquationSet`
   * - Label:
     - :sidsref:`FlowEquationSet_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`FlowEquationSet_t figure <FlowEquationSetFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`CellDimension`



.. _familygroup:

Family Group
^^^^^^^^^^^^

Because there is rarely a 1-to-1 connection between mesh regions and geometric entities, it is often desirable to set geometric associations indirectly in a CGNS file. That is, rather than setting the geometry data for each mesh entity (nodes, edges, and faces), it's useful to associate them with intermediate objects. The intermediate objects are in turn linked to nodal regions of the computational mesh. This intermediate object is defined as a  *CFD family* .

Each mesh surface may linked to the geometric entities of one or more CAD databases by a user-defined CFD family name. The CFD family corresponds to one or more CAD geometric entities on which the mesh face is projected. Each one of these geometric entities is described in a CAD file and is not redefined within the CGNS file.


.. _Family:

:sidskey:`Family_t`
~~~~~~~~~~~~~~~~~~~

This node, a child of a :sidskey:`CGNSBase_t`  node or a :sidskey:`Family_t`  node, contains the definition of a single CFD family. Multiple :sidskey:`Family_t`  nodes are allowed.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`Family_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`Family_t figure <FamilyFigure>`
   * - Cardinality:
     - 0, *N*


.. _FamilyName:

:sidskey:`FamilyName_t`
~~~~~~~~~~~~~~~~~~~~~~~

This node is used to identify a family to which a particular zone or boundary belongs. Note that the name of the family is defined by the "Name" of the :sidskey:`Family_t`  node, and is stored as data in the :sidskey:`FamilyName_t`  node.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`FamilyName or user defined`
   * - Label:
     - :sidsref:`FamilyName_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - Name of CFD family
   * - Children:
     - None
   * - Cardinality:
     - 0,1


.. _AdditionalFamilyName:

:sidskey:`AdditionalFamilyName_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This node is a supplement to the :sidskey:`FamilyName_t`  node, and is used to identify additional families to which a particular zone or boundary belongs.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`user defined`
   * - Label:
     - :sidsref:`AdditionalFamilyName_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - Name of CFD family
   * - Children:
     - None
   * - Cardinality:
     - 0,N


.. _FamilyBC:

:sidskey:`FamilyBC_t`
~~~~~~~~~~~~~~~~~~~~~

This node contains a boundary condition type for a particular CFD family.

.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`FamilyBC`
   * - Label:
     - :sidsref:`FamilyBC_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`BCType`  value
   * - Children:
     - See :ref:`FamilyBC_t figure <FamilyBCFigure>`
   * - Cardinality:
     - 0,1




.. _FamilyBCDataSet:

:sidskey:`FamilyBCDataSet_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A :sidskey:`FamilyBCDataSet_t`  node contains Dirichlet and Neumann data for a single set of boundary condition equations to be applied to a Family. It's intended use is for simple boundary condition types, where the equations imposed do not depend on local flow conditions.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`FamilyBCDataSet_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`BCTypeSimple`  value
   * - Children:
     - See :ref:`FamilyBCDataSet_t figure <FamilyBCDataSetFigure>`
   * - Cardinality:
     - 0, *N*


.. _GeometryReference:

:sidskey:`GeometryReference_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`GeometryReference_t`  nodes are used to associate a CFD family with one or more CAD databases.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`GeometryReference_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`GeometryReference_t figure <GeometryReferenceFigure>`
   * - Cardinality:
     - 0, *N*


.. _GeometryFile:

:sidskey:`GeometryFile_t`
~~~~~~~~~~~~~~~~~~~~~~~~~

This node contains the name of the CAD geometry file.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GeometryFile`
   * - Label:
     - :sidsref:`GeometryFile_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - Name of the CAD geometry file
   * - Children:
     - None
   * - Cardinality:
     - 1


.. _GeometryFormat:

:sidskey:`GeometryFormat_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This enumeration node defines the format of the CAD geometry file.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`GeometryFormat`
   * - Label:
     - :sidsref:`GeometryFormat_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - Name of the CAD geometry format
   * - Children:
     - None
   * - Cardinality:
     - 1





.. _GeometryEntity:

:sidskey:`GeometryEntity_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:sidskey:`GeometryEntity_t`  nodes define the names of the entities in CAD geometry file that make up a CFD family.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`GeometryEntity_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - None
   * - Cardinality:
     - 0, *N*



.. _timedepgroup:

Time-Dependent Group
^^^^^^^^^^^^^^^^^^^^

Nodes in this section are used for information related to time-dependent flows, and include specification of grid motion and storage of time-dependent or iterative data.


.. _BaseIterativeData:

:sidskey:`BaseIterativeData_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Located directly under the :sidskey:`CGNSBase_t`  node, the :sidskey:`BaseIterativeData_t`  node contains information about the number of time steps or iterations being recorded, and the time and/or iteration values at each step. In addition, it may include the list of zones and families for each step of the simulation, if these vary throughout the simulation.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`BaseIterativeData_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - :sidskey:`NumberOfSteps`
   * - Children:
     - See :ref:`BaseIterativeData_t figure <BaseIterativeDataFigure>`
   * - Cardinality:
     - 0,1



.. _ZoneIterativeData:

:sidskey:`ZoneIterativeData_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`ZoneIterativeData_t`  node is a child of the :sidskey:`Zone_t`  node, and is used to store pointers to zonal data for each recorded step of the simulation.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`ZoneIterativeData_t`
   * - DataType:
     - :sidskey:`MT`
   * - Children:
     - See :ref:`ZoneIterativeData_t figure <ZoneIterativeDataFigure>`
   * - Cardinality:
     - 0,1
   * - Parameters:
     - :sidskey:`NumberOfSteps`





.. _RigidGridMotion:

:sidskey:`RigidGridMotion_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~





:sidskey:`RigidGridMotion_t`  nodes are used to store data defining rigid translation and/or rotation of the grid coordinates. Multiple :sidskey:`RigidGridMotion_t`  nodes may be associated with different iterations or time steps in the computation. This association is recorded under the :sidskey:`ZoneIterativeData_t`  node.



.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`RigidGridMotion_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`RigidGridMotionType`  value
   * - Children:
     - See :ref:`RigidGridMotion_t figure <RigidGridMotionFigure>`
   * - Cardinality:
     - 0, *N*



.. _ArbitraryGridMotion:

:sidskey:`ArbitraryGridMotion_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


:sidskey:`ArbitraryGridMotion_t`  nodes are used to store grid velocities for each grid point in a zone (i.e., for deforming grids). Multiple :sidskey:`ArbitraryGridMotion_t`  nodes may be associated with different iterations or time steps in the computation. This association is recorded under the :sidskey:`ZoneIterativeData_t`  node.



Note that instantaneous grid coordinates at different iterations or time steps may be recorded using multiple :sidskey:`GridCoordinates_t`  nodes under a :sidskey:`Zone_t`  node.




.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`ArbitraryGridMotion_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`ArbitraryGridMotionType`  value
   * - Children:
     - See :ref:`ArbitraryGridMotion_t figure <ArbitraryGridMotionFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`IndexDimension` , :sidskey:`VertexSize` , :sidskey:`CellSize`
   * - Functions:
     - :sidskey:`DataSize`





.. _structuralnodes:

Structural Nodes
^^^^^^^^^^^^^^^^


In this section we describe the highest levels of the hierarchy. Nodes in this section store only quantities which refer to all the entities below them. Therir primary function is to provide organization to the data below.



.. _Zone:

:sidskey:`Zone_t`
~~~~~~~~~~~~~~~~~


Directly below the highest level node in the database, which is by definition of type :sidskey:`CGNSBase_t` , are found nodes of type :sidskey:`Zone_t`  providing entry into the data specific to each zone. There are as many :sidskey:`Zone_t`  nodes as there are zones. Their children, in turn, record grid, field, connectivity, and boundary conditions, and a variety of auxiliary data.




.. list-table:: **Node Attributes**
   :stub-columns: 1



   * - Name:
     - User defined
   * - Label:
     - :sidsref:`Zone_t`
   * - DataType:
     - :sidskey:`cgsize_t`
   * - Dimension:
     - 2
   * - Dimension Values:
     - :sidskey:`IndexDimension` , 3
   * - Data:
     - :sidskey:`VertexSize[IndexDimension]` , :sidskey:`CellSize[IndexDimension]` ,       :sidskey:`VertexSizeBoundary[IndexDimension]`
   * - Children:
     - See :ref:`Zone_t figure <ZoneFigure>`
   * - Cardinality:
     - 0, *N*
   * - Parameters:
     - :sidskey:`CellDimension` , :sidskey:`PhysicalDimension`



.. _CGNSBase:

:sidskey:`CGNSBase_t`
~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`CGNSBase_t`  node is by definition the highest level node in the database, and is located directly below the database root node. It provides entry into all other data. Multiple :sidskey:`CGNSBase_t`  nodes are allowed in a file. The particular database being accessed is determined by the name of the :sidskey:`CGNSBase_t`  node.

The only data stored in the node itself are :sidskey:`CellDimension` , the dimensionality of a cell in the mesh (i.e., 3 for a volume cell and 2 for a face cell), and :sidskey:`PhysicalDimension` , the number of indices required to specify a unique physical location in the field data being recorded. However, a variety of global information concerning the entire database may be stored in children of the :sidskey:`CGNSBase_t`  node. In particular, a :sidskey:`Descriptor_t`  node at this level can store user commentary on the entire history of the development of the database.

Other information typically stored directly below the :sidskey:`CGNSBase_t`  node includes convergence histories, reference states, dimensional units, integrated quantities, and information on the flow equations being solved.

.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - User defined
   * - Label:
     - :sidsref:`CGNSBase_t`
   * - DataType:
     - :sidskey:`I4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 2
   * - Data:
     - :sidskey:`CellDimension` , :sidskey:`PhysicalDimension`
   * - Children:
     - See :ref:`CGNSBase_t figure <CGNSBaseFigure>`
   * - Cardinality:
     - 0, *N*


.. _SimulationType:

:sidskey:`SimulationType_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This enumeration-type node is a child of the :sidskey:`CGNSBase_t`  node, and specifies whether or not the data below :sidskey:`CGNSBase_t`  is time-accurate.

.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`SimulationType`
   * - Label:
     - :sidsref:`SimulationType_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`TimeAccurate`  or :sidskey:`NonTimeAccurate`
   * - Children:
     - None
   * - Cardinality:
     - 0,1



.. _ZoneType:

:sidskey:`ZoneType_t`
~~~~~~~~~~~~~~~~~~~~~

This enumeration-type node is a required child of the :sidskey:`Zone_t`  node, and specifies whether the grid in that zone is structured or unstructured.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`ZoneType`
   * - Label:
     - :sidsref:`ZoneType_t`
   * - DataType:
     - :sidskey:`C1`
   * - Dimension:
     - 1
   * - Dimension Values:
     - Length of string
   * - Data:
     - :sidskey:`Structured`  or :sidskey:`Unstructured`
   * - Children:
     - None
   * - Cardinality:
     - 1



.. _CGNSLibraryVersion:

:sidskey:`CGNSLibraryVersion_t`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A file containing a CGNS database also contains, directly below the root node, a :sidskey:`CGNSLibraryVersion_t`  node. This node stores the version number of the CGNS standard with which the file is consistent, and is created automatically when the file is created or modified using the :ref:`CGNS Mid-Level Library <StandardMLL>` . Note that this node is not actually part of the CGNS database, since it is not located below a :sidskey:`CGNSBase_t`  node.

Note that a file may contain multiple CGNS databases, but there is only one :sidskey:`CGNSLibraryVersion_t`  node. It is assumed that the version number in the :sidskey:`CGNSLibraryVersion_t`  node is applicable to all the CGNS databases in the file.

Note also that some CGNS nodes may actually be links to CGNS nodes in other files. In this case, it is assumed that the :sidskey:`CGNSLibraryVersion_t`  node in the "top-level" file is applicable to the file(s) containing the linked nodes.


.. list-table:: **Node Attributes**
   :stub-columns: 1

   * - Name:
     - :sidskey:`CGNSLibraryVersion`
   * - Label:
     - :sidsref:`CGNSLibraryVersion_t`
   * - DataType:
     - :sidskey:`R4`
   * - Dimension:
     - 1
   * - Dimension Values:
     - 1
   * - Data:
     - CGNS version number
   * - Children:
     - None
   * - Cardinality:
     - 1


.. last line

