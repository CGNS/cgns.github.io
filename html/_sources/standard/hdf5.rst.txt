.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _HDF5Implementation:
   
CGNS/HDF5 - An HPC implementation
=================================

This section specifies the exact manner in which, under CGNS conventions,
data structures (the SIDS) are to be stored in, i.e., mapped onto, the file structure provided by the HDF database manager.
Adherence to the mapping conventions guarantees uniform meaning and location of CFD data within HDF files, and thereby allows the construction of universal software to read and write the data.

Implementation Summary
----------------------

The purpose of the current document is to describe the way in which CFD data is to be represented in an HDF5 data tree. To do this, it is necessary to first describe the HDF5 data structure itself in some detail. Therefore, a conceptual summary of HDF5 is given here in order to make the current document relatively independent, and to allow the reader to focus on those aspects of HDF5 which are essential to understanding the file mapping.

Any HDF5 file with a conformant mapping is *CGNS/HDF5* compliant. The mapping has been made using a per-node basis. Instead of having a new mapping dedicated to HDF5, we have made a mapping from the ADF nodes to a set of HDF5 groups. While this is not an optimal mapping, the use of such an HDF5 node allows us to re-use the ADF API without change.

The `HDF5 documentation <https://portal.hdfgroup.org/display/HDF5/HDF5>`_ should be used as the authoritative references to resolve any issues not covered by this summary.

General Description of HDF5
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The HDF5 library provides CGNS with a low level storage system.
This library is developed and maintained by the `National Center for Supercomputing Applications <http://www.ncsa.illinois.edu/>`_  at the University of Illinois at Urbana-Champaign.
It offers a free storage system, with support for a very large number of platforms used in the scientific world. This system is in charge of all physical features such as storage, compression, virtual access to data and many other services also useful for the CGNS users.

HDF5 allows a fine tuning of the physical devices, however, the SLL use of HDF5 forces all *property lists* to `DEFAULT` values.

Refer to the `HDF5 web site <https://www.hdfgroup.org/solutions/hdf5/>`_ for further information about HDF5.

Dedicated HDF5 Structures
^^^^^^^^^^^^^^^^^^^^^^^^^
The *CGNS node* is an HDF5 group. It contains attributes, an optional dataset and optional child groups. This structure is required and can be extended by other implementors as long as the following requirements are fullfilled.

In a CGNS tree, most of the nodes are *normal* nodes. These nodes can optionally contain data and have other nodes as children.

There are special nodes, such as the root node and the nodes managing the links. These special link structures use the HDF5 mount system. It is not necessary for either the MLL or SLL users to understand the HDF5 mount system, but it should be understood by SLL implementors.

The CGNS Node Mapping
~~~~~~~~~~~~~~~~~~~~~
The *CGNS node* uses *groups* and *attributes* elements of HDF5.
A basic CGNS node is composed of elements listed in the following table.
The attribute names have been enclosed in square brackets, because the SLL uses private attributes with a leading *space* character.
These brackets are not part of the names.

.. table:: **Basic Node**
  :align: center

  +--------------------+-----------+----------------+
  | GROUP                                           |
  +====================+===========+================+
  | REQUIRED ATTRIBUTE |  [name]   |   U8LE[33]     |
  +--------------------+-----------+----------------+
  | REQUIRED ATTRIBUTE |  [label]  |   U8LE[33]     |
  +--------------------+-----------+----------------+
  | REQUIRED ATTRIBUTE |  [type]   |  U8LE[3]       |
  +--------------------+-----------+----------------+
  | REQUIRED ATTRIBUTE |  [ order] | H5T_NATIVE_INT |
  +--------------------+-----------+----------------+
  | OPTIONAL DATASET   |  [ data]  |                |
  +--------------------+-----------+----------------+

All the children groups of a node are understood as SLL children nodes of this node, unless the group name starts with a *space* character. The *dataset* contains the actual data of a node.
In the case of a node without data (i.e. :code:`MT` type), the dataset does not exist.

In addition to the attributes of a *normal* node, special attribute names are reserved for the root node, shown in the following table.
The name of the root node is ``[HDF5 MotherNode]``, its label is ``[Root Node of HDF5 File]``, type is ``MT``.

.. table:: **Root Node**
  :align: center

  +---------------------+------------+-------------+
  | GROUP               |  [/]                     |
  +=====================+============+=============+
  | REQUIRED ATTRIBUTE  | [ version] |   U8LE[33]  |
  +---------------------+------------+-------------+
  | REQUIRED ATTRIBUTE  | [ format]  |   U8LE[33]  |
  +---------------------+------------+-------------+

The node hosting the link entries is a special node named ``[ mount]`` without attributes nor data.
This group should be a child of the root node, its absolute path is ``[/ mount]``.
The group ``[ mount]`` contains one group for each mounted file refered to by a link.
Each entry has the attributes described in the table below.
The link node itself is a group with the special name ``[ link]``.
This implementation is discussed further in the section describing the :ref:`link mechanism <link-mechanism>`.


.. table:: **Link Node**
  :align: center

  +---------------------+------------+-----------------+
  | GROUP               | **[/ mount/ *]**             |
  +=====================+============+=================+
  | REQUIRED ATTRIBUTE  | [ refcnt]  | H5T_NATIVE_INT  |
  +---------------------+------------+-----------------+
  | REQUIRED ATTRIBUTE  | [ file]    | H5T_NATIVE_CHAR |
  +---------------------+------------+-----------------+

The Node ID
~~~~~~~~~~~
The node ID is a unique identifier assigned to each existing node by HDF5 when the file containing it is opened,
and to new nodes as they are created. SLL inquiries generally return node IDs as a result and accept node IDs as input.
By building a table of IDs, calling software can subsequently access specific nodes without further search.
The Node ID is real and is not under user control, its lifetime is ended by the closing of the HDF5 file.

The Node Name
~~~~~~~~~~~~~
The node Name is a 32-byte character field which is user controllable.
Its general use is to distinguish among the children of a given node; consequently, no two children of the same parent may have the same Name.
Constraints related to the node name are detailed in the *General CGNS SLL Mapping Concepts* section, under :ref:`Node Name<HDF5NodeName>`.

The Label
~~~~~~~~~
The Label is a 32-byte character field which is user controllable. SLL assigns no formal role to the Label, but the intent was to identify the structure of the included data. It is common for the various children of a single parent to store different instances of the same structure. Therefore, there is no prohibition against more than one child of the same parent having the same Label.

The Data Type
~~~~~~~~~~~~~
The Data Type is a 32-byte character field which specifies the type and precision of any data which is stored in the data field. Types provided by HDF5 are:

.. table:: **Data Types**

  +---------------------+----------+-------------------+
  | Data Type           | Notation | HDF5 Type         |
  +=====================+==========+===================+
  | No Data             | MT       |       -           |
  +---------------------+----------+-------------------+
  | Integer 32          | I4       | H5T_NATIVE_INT32  |
  +---------------------+----------+-------------------+
  | Integer 64          | I8       | H5T_NATIVE_INT64  |
  +---------------------+----------+-------------------+
  | Unsigned Integer 32 | U4       | H5T_NATIVE_UINT32 |
  +---------------------+----------+-------------------+
  | Unsigned Integer 64 | U8       | H5T_NATIVE_UINT64 |
  +---------------------+----------+-------------------+
  | Real 32             | R4       | H5T_NATIVE_FLOAT  |
  +---------------------+----------+-------------------+
  | Real 64             | R8       | H5T_NATIVE_DOUBLE |
  +---------------------+----------+-------------------+
  | Complex 64          | X4       | H5T_COMPOUND [1]_ |
  +---------------------+----------+-------------------+
  | Complex 128         | X8       | H5T_COMPOUND [1]_ |
  +---------------------+----------+-------------------+
  | Character           | C1       | H5T_NATIVE_CHAR   |
  +---------------------+----------+-------------------+
  | Byte                | B1       | H5T_NATIVE_UCHAR  |
  +---------------------+----------+-------------------+
  | Link                | LK       |        -          |
  +---------------------+----------+-------------------+
  
There is no mapping to HDF5 MT and LK types, because there is no actual data space associated with the nodes. The type information itself is stored in the node as the strings "MT" and "LK".

.. note::
  .. [1] The types X4 and X8 are not true types in HDF5. They are mapped to H5T_COMPOUND structures to combine the real and imaginary parts. This support is experimental.

The data storage format is translated as described below.

.. table:: **Native Formats**

  +-----------------+------------------+
  | Native Format   |  HDF5 Type       |
  +=================+==================+
  | H5T_IEEE_F32BE  |  IEEE_BIG_32     |
  +-----------------+------------------+
  | H5T_IEEE_F32LE  |  IEEE_LITTLE_32  |
  +-----------------+------------------+
  | H5T_IEEE_F64BE  |  IEEE_BIG_64     |
  +-----------------+------------------+
  | H5T_IEEE_F64LE  |  IEEE_LITTLE_64  |
  +-----------------+------------------+

The Number of Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~
The Data portion of a node is designed to store multi-dimensional arrays of data, each element of which is presumed to be of the Data Type specified. The Number of Dimensions specifies the number of integers required to reference a single datum within the array.

The Dimension Values
~~~~~~~~~~~~~~~~~~~~
The Dimension Values are a list of integers expressing the actual sizes of the stored array in each of the dimensions specified. These dimensions are stored by the *dataspace* associated with the *dataset*; no other attributes contains these values.

The Data
~~~~~~~~
In an HDF5 node, the portion of the node holding the actual stored data array is a *dataset*.

The Child Table
~~~~~~~~~~~~~~~
All groups of the current group are said to be the children of this group, except the groups with a name starting with a space character. Each of these children groups is a *normal* node (i.e. group).

Children may be identified by their names and labels, and, thence, by their node IDs once these have been determined.
HDF5 provides no notion of order among children, but the SLL layer adds a creation order stored in the ``[ order]`` attribute. This order is guaranteed to be the same from call to call, even after the file has been closed and re-opened.

Note that there is no *parent* table; that is, a node has no direct knowledge of its parent.
Since calling software must open the file from the root, it presumably cannot access a child without having first accessed the parent.
It is the responsibility of the calling software to record the node ID of the parent if this information will be required.

.. _link-mechanism:

The link mechanism
~~~~~~~~~~~~~~~~~~
A ``LK`` typed node is a link. Such a node refers to another node elsewhere.
In other words, the *link* has no child or contents, but is a name of a node somewhere in the current file or in another file.
The ``LK`` typed node is said to be the *source* node, while the node elsewhere is said to be the *destination* node.
It is the role of the SLL layer to insure consistency [in particular in order to avoid an acyclic graph]
and transparency of the link mechanism, so that any normal node request to the *link* node is performed as if it is performed on the destination node.
A *link* destination can be in the same file as the link source or in another file.
In both cases, the link is made using an HDF5 soft link from source to destination.
In the case of a destination in another file, the destination file is mounted in the ``[/ mount]`` [absolute path] group and the soft link is made from the source to the destination now present in this mounted file. Each time a file is mounted, the ``[/ refcnt]`` [absolute path] attribute is incremented.
The file is unmounted if there is no reference to itself.


General HDF5 Mapping Concepts 
-----------------------------
This section describes the general philosophy underlying the use of the HDF5 tree structure by CGNS. The section :ref:`Detailed CGNS Node Descriptions <StandardFMMNodeDescription>` describes the exact conventions for each type of data.

We first describe the :ref:`roles of the various HDF5 elements<HDFElements>` (i.e. groups or attributes) as they are specifically applied within CGNS, followed by a description of :ref:`the overall layout<internal>` of the tree structure itself.

.. _HDFElements:

Use of HDF5 Elements in CGNS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We previously described the general role of each of the HDF5 elements without reference to CFD. Here we note any additional information regarding their use within CGNS.

We first describe attributes recognized by both HDF5 and CGNS. We then describe certain elements which are derived from context, i.e., which the node possesses by virtue of its location within a CGNS database. These notions, namely, :ref:`Cardinality<HDF5Cardinality>`, :ref:`Parameters<HDF5Parameters>`, and :ref:`Functions<HDF5Functions>`, are unique to CGNS.

The Node ID
~~~~~~~~~~~
The Node ID is completely controlled by HDF5, and thus its role is exactly the same for CGNS as it is for HDF5. CGNS software accesses the Node ID only through calls to HDF5. HDF5 itself guarantees that Node IDs are unique and constant within any HDF5 file (or collection of files) while the file(s) are open.

.. _HDF5NodeName:

The Node Name
~~~~~~~~~~~~~
In CGNS, the Name may be left to the choice of the user, or it may be specified by the :ref:`SIDS<CGNS-SIDS>`.
At the levels of the tree nearest the root, the (end-)user is free to set the Name to distinguish among like objects in the case at hand.
For example, in a multizone problem, nodes associated with different zones might be named ``"UnderLeftWing"`` or ``"AboveForwardFuselage"``.
At this level, it is generally not possible to identify a collection of names which are likely to recur. This means that the naming of high level objects does not require standardization, and the SIDS are silent regarding the naming convention.

Because every HDF5 node must be given a name when it is opened, default names, based on the node Label, are provided by convention.
The :ref:`CGNS Midlevel Library<MLLIntroduction>` will record the default names if none is provided by the user.
The precise formula is given in the Label section below.

At levels of the tree farther from the root, the SIDS often specify the name.
There is, for example, a commonly encountered collection of flow variables whose general meaning is widely understood.
In this case, standardizing the name conveys precise information. Thus the SIDS specify, for instance, that a node containing static internal energy per unit mass should have the Name "``EnergyInternal``".
Adherence to these :ref:`naming conventions<dataname>` guarantees uniform meaning of the data from site to site and user to user.
Of course, there may be a desire to store quantities for which no naming convention is specified.
In this case any suitable name can be used, but there is no guarantee of proper interpretation by anyone unaware of the choice.

By extension, a node name is a series of names separated by a *slash* "/" (like the POSIX file system names), moreover "/" is the root name of the CGNS tree.

A CGNS Name can contain any printable ASCII character except the *slash* "/" and the *dot* "." when this dot is the first character of the name.

The Label
~~~~~~~~~
Within CGNS, nearly all labels reflect C-style type definitions ("typedefs") specified by the SIDS, and end in the characters ``"_t"``.
Some "Leaf" nodes (i.e. nodes that have no children) do not represent higher level CGNS structures and therefore have labels that do not follow the ``"_t"`` convention.
At this writing, all such nodes have the type ``int[]``, i.e., integer array, a type already recognized in C, for which a separate type definition would be artificial.
Such nodes are generally located by the software through their names, which are specified by the SIDS, rather than through their labels.

The Label generally indicates the role of the data at and below the node in the context of CFD. Nodes which are entry points to data for a particular zone, for example, have the Label ``"Zone_t"``.

Parent nodes often have a number of children each containing data for different instances of the same structure. Multiple children of the same parent therefore often have the same Label. It is customary for software to conduct searches which depend on the Label, e.g., to determine the number of zones in a problem. The software will fail if the conventions regarding Labels are not observed.

Labels are also used to build default node Names. These are derived from the Label by dropping the characters ``"_t"`` and substituting the smallest positive integer resulting in a unique name among children of the same parent.
For example, the first default Name for a node of type ``Zone_t`` will be ``"Zone1"``; the second will be ``"Zone2"``; and so on.

The Data Type
~~~~~~~~~~~~~
Data Types are completely specified by the file mapping.
Although HDF5 provides a number of types, in CGNS the only types used are :code:`MT` (No Data), :code:`I4` (Integer), :code:`R4` and :code:`R8` (Real), :code:`X4` and :code:`X8` (Complex), :code:`C1` (Character), and :code:`LK` (Link).

The specification of data types within the File Mapping allows for the probability that files written under different circumstances may differ in precision. The issue is complicated by the ability of HDF5 to sense the capabilities of the platform on which it is running and interpret or record data accordingly.
The general rule is that, although the user of HDF5 can specify the precision in which it is desired to read or write the data, HDF5 knows both the precision available at the source and the precision acceptable to the destination and will mitigate accordingly.
Thus to specify the precison of real data as :code:`R4`, for example, has no meaning unless both :code:`R4` and :code:`R8` are available.
Therefore, the generic specification ``"DataType"`` is used to allow for all possibilities.

For all integer data specified by the SIDS, :code:`I4` provides sufficient precision.

The Number of Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~
Whenever data is stored at a node, it is in the form of a single array of elements of a single date type. Insofar as possible, the dimension specified by CGNS is the natural underlying dimension; for example, a rectangular array of pressures is stored with dimension equal to the physical dimension of the problem.

There are situations in which this representation is not feasible. For instance, a list of points which do not form a rectangular array in physical space may be compacted into a one-dimensional array in HDF5.

Frequently the data is of type :code:`C1` (character data).
In some cases, the data holds additional information in the form of a name specified by the SIDS, and in some cases holds user comment. All such data is generally represented as a one-dimensional array (or list) of characters.

The Dimension Values
~~~~~~~~~~~~~~~~~~~~
These are used exactly as specified by HDF5. In the case of rectangular arrays of physical data, the dimension values are set to the actual sizes in physical space. Note that these sizes often depend on whether the values are associated with grid nodes, cell centers or other physical locations with respect to the grid. In any event, they refer to the amount of data actually stored, not to any larger array from which it may have been extracted.

In the case of list data, the dimension value is the length of the list. Lists of characters may contain termination bytes such as ``"\n"``; by this means an entire document can be stored in the data field.

The Data
~~~~~~~~
CGNS imposes no conventions on the data itself beyond those specified by HDF5.
Note that it is a responsibility of the CGNS software to ensure that the amount and type of stored data agrees with the specification of the data type, number of dimensions, and dimension values.

The Child Table
~~~~~~~~~~~~~~~
The Child Table is completely controlled by HDF5, and thus its role is exactly the same for CGNS as it is for HDF5. CGNS software accesses and modifies the child table only through calls to HDF5.

In addition to the meaning of attributes of individual HDF5 nodes, the File Mapping specifies the relations between nodes in a CGNS database. Consequently, the File Mapping determines what kinds of nodes will lie in the child table.

It is important to reemphasize that HDF5 provides no notion of order among children. This means children can be identified only by their names, labels and system-provided node IDs. In particular, the order of a list of children returned by HDF5 has nothing to do with the order in which they were inserted in the file. However, the order returned is consistent from call to call provided the file has not been closed and the node structure has not been modifed.

.. _HDF5Cardinality:

Cardinality
~~~~~~~~~~~
The *cardinality* of a CGNS node is the number of nodes of the same label permitted at one point in the tree, i.e., as children of the same parent. It consists of both lower and upper limits.

Since the notion of a CGNS database allows for work in progress, the lower limit is generally zero (although the database may be of little use until certain nodes are filled). The upper limit is usually either one or many (N).

.. _HDF5Parameters:

Parameters
~~~~~~~~~~
CGNS relies on the fact that SLL nodes cannot be found except by following the pointers from their parents. This means that software accessing a node has had an opportunity to note all the data above that node in the tree. Therefore, nodes do not repeat within themselves information which is necessary for their interpretation but which is available at a higher level.

A datum which is necessary for the proper interpretation of a node but which is derived from its ancestors is referred to as a *structure parameter*.

.. _HDF5Functions:

Functions
~~~~~~~~~
Occasionally the proper interpretation of a node depends on an implicitly understood *function* of its structure parameters.
Usually these relate to the actual amount of data stored.
Several of these functions are defined in the :ref:`SIDS<CGNS-SIDS>` and referenced in this document.

CGNS Databases
^^^^^^^^^^^^^^
Definition of a CGNS Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By definition, a CGNS database is created when, within an HDF5 file, a node is created which conforms to the :ref:`specifications given below<HDF5BaseNode>` for a node of type ":sidskey:`CGNSBase_t`".
This node is conceptually the root of the CGNS database.
Because it is created and controlled by the user, it cannot be the root of the HDF5 file.
Current CGNS conventions require that it be located directly below the HDF5 root node.

Further, by the mechanism of links, a CGNS database may span multiple files.
Thus there is no notion of a CGNS *file*, only of a CGNS *database* implemented within one or more *HDF5 files*.

By virtue of its intended use, a CGNS database is dynamic in that its content at any time reflects the current state of a CFD problem of interest.
For example, after the completion of a grid generation procedure, a CGNS file may contain a grid but no boundary conditions.
Therefore, beyond the occurrence of a :sidskey:`CGNSBase_t` node, there is no minimum content required in a CGNS database.

Conversely, there is no proscription against the inclusion, anywhere within an HDF5 file containing a CGNS database, of nodes of any form whatsoever, provided only that their naming and labelling does not mimic CGNS conventions. Such "non-CGNS" nodes, and those below them in the HDF5 tree, are not regarded as part of the CGNS database. CGNS software will not detect the existence of non-CGNS nodes.

We may therefore take the following as a definition of a CGNS database:

  A CGNS database is a subtree of an HDF5 file or files which is rooted at a node with label ":sidskey:`CGNSBase_t`" and which conforms to the :ref:`SIDS data model<CGNS-SIDS>` as implemented by the :ref:`SIDS File Mapping<StandardFMM>`.

Location of CGNS Databases within HDF5 Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An HDF5 file may contain more than one :sidskey:`CGNSBase_t` node; i.e., there may be more than one CGNS database rooted within the same HDF5 file.
CGNS software accepts the name of the desired database as an argument, and will locate the correct :sidskey:`CGNSBase_t` node within the specified HDF5 file. 
Obviously, each :sidskey:`CGNSBase_t` node in a single HDF5 file must have a unique name.

A CGNS database may link to CGNS nodes in the same or other HDF5 files.
Thus, for example, a CGNS database may reference the grid from another CGNS database without physically copying the the information.
In this case, the structure of the HDF5 file into which the link is made is invisible except below the node to which the link is made.

File Management
~~~~~~~~~~~~~~~
Beyond *Open* and *Close* neither HDF5 nor CGNS provides any file management facilities. The user is responsible for ensuring that:

- The HDF5 file containing the root of the required database is available and its permissions are properly set at runtime.
- If links are made to other HDF5 files, including any not under the user's direct control, these are also available at runtime.
- No file is opened for writing by more than one program at a time. 

It is possible, within CGNS, to protect files from inadvertent writing by opening them as "read only".

.. _internal:

Internal Organization of a CGNS Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _HDF5BaseNode:

The CGNSBase_t Node
~~~~~~~~~~~~~~~~~~~
At the highest level of the tree defining a CGNS database there is always a node labeled ":sidsref:`CGNSBase_t`".
The name of this node is user defined, and serves essentially as the name of the database itself. This name is used by the CGNS software to open the database.

The CGNSLibraryVersion_t Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An HDF5 file may also contain other nodes below the root node beside :sidskey:`CGNSBase_t`,
but these are *not* officially part of the CGNS database and will not be recognized by most CGNS software.
One exception to this is a node called :sidskey:`CGNSLibraryVersion_t`, which is a child of the HDF5 root node.
This node stores the version number of the CGNS standard with which the file is consistent, and is created automatically when the file is created or modified using the :ref:`CGNS Mid-Level Library<MLLIntroduction>`. Officially, the CGNS version number is not a part of the CGNS database (because it is not located below :sidskey:`CGNSBase_t`).
But because the Mid-Level Library software makes use of it, the node is included in this document.

Topological Basis of CGNS Database Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Below the root, the organization of a CGNS database reflects the problem topology. Omitting detail, the overall structure of the HDF5 file is shown in the first of the :ref:`CGNS File Mapping Figures<StandardFMMfigs>`.
Below the HDF5 root node is the :sidskey:`CGNSLibraryVersion_t` node, and one or more :sidskey:`CGNSBase_t` nodes.
Each :sidskey:`CGNSBase_t` node is the root of a CGNS database.

At the next level below a :sidskey:`CGNSBase_t` node are general specifications which apply to the problem globally, such as reference states, units, and so on.
At this level we also find a collection of nodes labeled ":sidsref:`Zone_t`". The tree below each of these holds all the data local to one of the various zones or subdomains which constitute the problem.

Beneath each :sidskey:`Zone_t` node there are nodes whose subtrees store: the grid (labeled :sidsref:`GridCoordinates_t`);
flowfields (:sidsref:`FlowSolution_t`); boundary conditions (:sidsref:`ZoneBC_t`);
information about the geometrical connection to other zones (:sidsref:`GridConnectivity_t`); and information defining time-dependent data.
Below these there may be additional nodes containing yet more geometrically local information.
For example, under the :sidskey:`ZoneBC_t` node there are nodes defining individual boundary conditions on portions of faces of the zone (:sidsref:`BC_t`).

Certain types of nodes originally specified at a high level are optionally repeated below.
For example, immediately below a :sidskey:`Zone_t` node we may find another :sidsref:`ReferenceState_t` node.
The CGNS convention is that such a node overrides (for the associated portion of the topology only) any data found at a higher level.

Topics Not Currently Covered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No specification of the kind represented by this file mapping can ever be complete. However, it is worth noting that there are certain entities common in CFD which are not currently specified by the file mapping.

Within nodes of type :sidsref:`FlowSolution_t`, the current file mapping permits the storage of fields of any number of dependent variables. In addition to those whose names are specified in the SIDS the user may add any desired quantities, naming them appropriately. Names that are not currently codified in the SIDS will not be common between practitioners without separate communication.

Obviously any sort of physical field could be stored in a :sidskey:`FlowSolution_t` node. The problem with using CGNS for such applications lies in the probable need to specify additional physical information. Standardizing this information is tantamount to extending the SIDS and File Mapping to the disciplines in question.

Similarly, if a reacting flow problem requires the specification of rate tables or catalytic wall boundary conditions, extensions to the SIDS and File mapping will be needed. 

.. last line
