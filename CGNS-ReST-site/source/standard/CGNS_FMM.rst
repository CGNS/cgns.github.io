.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)


.. _StandardFMM:
   
CGNS/FMM - Data model mapping to implementation
===============================================

The SIDS File Mapping Manual specifies the exact manner in which, under CGNS conventions, CFD data structures (the :ref:`SIDS <CGNS-SIDS>`) are to be stored in, i.e., mapped onto, the file structure provided by a database manager.
Adherence to the mapping conventions guarantees uniform meaning and location of CFD data within database files, and thereby allows the construction of universal software to read and write the data.
Physical data storage is accomplished via a general database manager, either ADF (Advanced Data Format) or HDF (Hierarchical Data Format).

This document describes the general concepts behind and structure of a CGNS Database. The implementation details of reading and writing to a storage medium are left to an underlying database manager. The :ref:`CGIO User's Guide <StandardCGIO>` provides the core routines to access the database manager at that level.

Since CGNS was originally developed based on the ADF (Advanced Data Format) as the database manager, much of this documentation parallels those concepts. With the introduction of the HDF5 (Hierarchical Data Format) database manager, the concepts in this document have been "mapped" to HDF5.

We first describe the structure of the database, and the nodes from which it is constructed, followed by a description of the overall layout of the tree structure itself.

The section :ref:`Detailed CGNS Node Descriptions <FMMNodeDescriptions>` describes the exact conventions for each type of data.

Conceptual Structure of a CGNS Database
---------------------------------------

Although the physical structure of a CGNS file in storage is (or should be) of little concern to users of CGNS, an understanding of its logical or conceptual structure is essential. This structure determines its suitability for the type of data at hand and is reflected in all of the low-level database access routines.

A CGNS file consists entirely of a collection of elements called nodes. These nodes are arranged in a tree structure which is logically similar to a UNIX file system. The nodes are said to be connected in a "child-parent" relationship according to the following simple rules:

  #. Each node may have any number of child nodes.
  #. Except for one node, called the root, each node is the child of exactly one other node, called its parent.
  #. The root node has no parent. 

Every node in a CGNS file has exactly the same internal structure. Each node contains identifying information, pointers to any children, and, optionally, data.

When a CGNS file is opened (by the appropriate database manager), information is returned to the calling program which is sufficient to access the root node. It is then the responsibility of the program to search the tree for whatever information is required, or to add to the tree any information it wishes to store.

There is a special kind of node called a link, which serves as a pointer to a node in another CGNS file, or in another part of the same CGNS file. The tree structure at and below the node to which the link points is available as if that node were present instead of the link. This allows a CGNS file to span multiple physical files, and also allows a portion of one CGNS file to be referenced by several other CGNS files.

The Structure of a Node
-----------------------

The File Mapping specifies not only the location of the node at which a particular kind of data is to be stored, but also how the internal structure of the node is to be used. Each node contains a number of fields into which data may be recorded. They are:

- `The Node Name`_
- `The Label`_
- `The Data Type`_
- `The Number of Dimensions`_
- `The Dimension Values`_
- `The Data`_

In addition, two other entities associated with the nodes are provided by the database manager itself. These are:

- `The Node ID`_
- `The Child Table`_

The Node Name
^^^^^^^^^^^^^

The node Name is a 32-byte character field which is user controllable. Its general use is to distinguish among the children of a given node; consequently, no two children of the same parent may have the same Name.

The Name may be left to the choice of the user, or it may be specified by the :ref:`SIDS <CGNS-SIDS>`. At the levels of the tree nearest the root, the (end-)user is free to set the Name to distinguish among like objects in the case at hand. For example, in a multizone problem, nodes associated with different zones might be named ":sidskey:`UnderLeftWing`" or ":sidskey:`AboveForwardFuselage`".
At this level, it is generally not possible to identify a collection of names which are likely to recur. This means that the naming of high level objects does not require standardization, and the SIDS are silent regarding the naming convention.

Because every node must be given a name when it is opened, default names, based on the node Label, are provided by convention. The :ref:`CGNS Midlevel Library <StandardMLL>` will record the default names if none is provided by the user. The precise formula is given in the Label section below.

At levels of the tree farther from the root, the SIDS often specify the name. There is, for example, a commonly encountered collection of flow variables whose general meaning is widely understood. In this case, standardizing the name conveys precise information. Thus the SIDS specify, for instance, that a node containing static internal energy per unit mass should have the Name ":sidskey:`EnergyInternal`". Adherence to these :ref:`naming conventions <dataname>` guarantees uniform meaning of the data from site to site and user to user. Of course, there may be a desire to store quantities for which no naming convention is specified. In this case any suitable name can be used, but there is no guarantee of proper interpretation by anyone unaware of the choice.

The Label
^^^^^^^^^

The Label is a 32-byte character field which is used to identify the structure of the included data. It is common for the various children of a single parent to store different instances of the same structure. Therefore, there is no prohibition against more than one child of the same parent having the same Label.

Within CGNS, nearly all labels reflect C-style type definitions ("typedefs") specified by the SIDS, and end in the characters "_t". Some "Leaf" nodes (i.e. nodes that have no children) do not represent higher level CGNS structures and therefore have labels that do not follow the ":sidskey:`_t`" convention.
At this writing, all such nodes have the type :sidskey:`int[]`, i.e., integer array, a type already recognized in C, for which a separate type definition would be artificial.
Such nodes are generally located by the software through their names, which are specified by the SIDS, rather than through their labels.

The Label generally indicates the role of the data at and below the node in the context of CFD. Nodes which are entry points to data for a particular zone, for example, have the Label ":sidskey:`Zone_t`".

Parent nodes often have a number of children each containing data for different instances of the same structure. Multiple children of the same parent therefore often have the same Label. It is customary for software to conduct searches which depend on the Label, e.g., to determine the number of zones in a problem. The software will fail if the conventions regarding Labels are not observed.

Labels are also used to build default node Names. These are derived from the Label by dropping the characters ":sidskey:`_t`" and substituting the smallest positive integer resulting in a unique name among children of the same parent. For example, the first default Name for a node of type :sidskey:`Zone_t` will be ":sidskey:`Zone1`"; the second will be ":sidskey:`Zone2`"; and so on.

The Data Type
^^^^^^^^^^^^^

The Data Type is a 2-byte character field which specifies the type and precision of any data which is stored in the data field. The data types allowed by CGNS are:

.. table::

    =====================    =============
    Data Type                Notation
    =====================    =============
    No Data                  :sidskey:`MT`
    Link                     :sidskey:`LK`
    Character                :sidskey:`C1`
    Byte                     :sidskey:`B1`
    Integer 32               :sidskey:`I4`
    Integer 64               :sidskey:`I8`
    Unsigned Integer 32      :sidskey:`U4`
    Unsigned Integer 64      :sidskey:`U8`
    Real 32                  :sidskey:`R4`
    Real 64                  :sidskey:`R8`
    Complex 64               :sidskey:`X4`
    Complex 128              :sidskey:`X8`
    =====================    =============


The :sidskey:`MT` node contains no data, thus the number of dimensions and dimension values are ignored. This node is typically used as a container for children nodes.

The :sidskey:`LK` node is a link to a node within within the current or an external database. The actual data stored with the node is a file name and node path name to the link (as :sidskey:`C1` data). This information is available only through the core link access routines. A normal read of a :sidskey:`LK` node will will return the node properties (with the exception of the Name) from the linked-to node.

The specification of data types within the File Mapping allows for the probability that files written under different circumstances, or on different platforms, may differ in precision or format. It is the responsibility of the database manager to provide any data conversions required, and to ensure precision of the data.


The Number of Dimensions
^^^^^^^^^^^^^^^^^^^^^^^^

The Data portion of a node is designed to store multi-dimensional arrays of data, each element of which is presumed to be of the Data Type specified.
The Number of Dimensions specifies the number of integers required to reference a single datum within the array. The limit for the Number of Dimensions is **12**.

Whenever data is stored at a node, it is in the form of a single array of elements of a single date type.

.. note::
    
   Fortran-indexing conventions are used within CGNS.
   For multi-dimensional data, this means that the first index of the array varies the fastest, and indexing starts at 1. This is important to understand when reading the data into multi-dimensional "C" arrays, since the indexing order is opposite to that as used by CGNS.

.. note::

   Character data (:sidskey:`C1`) is not stored with a "C" terminating ':code:`0`' character, but rather is padded out with blanks (space character) as in Fortran character data.
   The MLL, however, will add the terminating-':code:`0`' to the strings when returning this data to a "C" application.

The Dimension Values
^^^^^^^^^^^^^^^^^^^^

The Dimension Values are a list of integers expressing the actual sizes of the stored array in each of the dimensions specified. With the introduction of 64-bit capability with CGNS Version 3.1.3, these dimensions are stored internally as 64-bit integers, regardless of the compilation mode (32 or 64-bit mode). They are returned to the application, however, as :sidskey:`cgsize_t` variables.

In the case of rectangular arrays of physical data, the dimension values are set to the actual sizes in physical space. Note that these sizes often depend on whether the values are associated with grid nodes, cell centers or other physical locations with respect to the grid. In any event, they refer to the amount of data actually stored, not to any larger array from which it may have been extracted.

In the case of list data, the dimension value is the length of the list. Lists of characters may contain termination bytes such as ":code:`\n`"; this means an entire document can be stored in the data field.


The Data
^^^^^^^^

The portion of the node holding the actual stored data array.

CGNS imposes no conventions on the data itself.

.. note::
  
  It is a responsibility of the CGNS software to ensure that the amount and type of stored data agrees with the specification of the data type, number of dimensions, and dimension values.


The Node ID
^^^^^^^^^^^

The node ID is a unique identifier assigned to each existing node by a database manager when the file containing it is opened, and to new nodes as they are created.
Core routine inquiries generally return node IDs as a result and accept node IDs as input. By building a table of IDs, calling software can subsequently access specific nodes without a further search. The Node ID is a 64-bit real and is not under user control.


The Child Table
^^^^^^^^^^^^^^^

The database manager maintains a table recording the children of each node, which is adjusted when children are added or deleted

Children may be identified by their names and labels, and, thence, by their node IDs once these have been determined. There is no provision for the notion of order among children. In particular, the order of a list of children returned by the database manager may or may not have anything to do with the order in which they were inserted in the file. However, the order returned is consistent from call to call provided the file has not been closed and the node structure has not been modifed.

Note that there is no *parent* table; that is, a node has no direct knowledge of its parent. Since calling software must open the file from the root, it presumably cannot access a child without having first accessed the parent. It is the responsibility of the calling software to record the node ID of the parent if this information will be required.

The Child Table is completely controlled by the database manager, and it's role is exactly the same for CGNS. CGNS software accesses and modifies the child table only through calls to the database manager.

In addition to the meaning of attributes of individual nodes, the File Mapping specifies the relations between nodes in a CGNS database. Consequently, the File Mapping determines what kinds of nodes will lie in the child table.


Use of Nodes in CGNS
--------------------

There are certain attributes of nodes which are derived from context, i.e., which the node possesses by virtue of its location within a CGNS database. These are often needed by CGNS to properly interpret the data; namely,

- `Cardinality`_
- `Parameters`_
- `Functions`_ 

Cardinality
^^^^^^^^^^^

The *cardinality* of a CGNS node is the number of nodes of the same label permitted at one point in the tree, i.e., as children of the same parent. It consists of both lower and upper limits.

Since the notion of a CGNS database allows for work in progress, the lower limit is generally zero (although the database may be of little use until certain nodes are filled). The upper limit is usually either one or many (*N*).

Parameters
^^^^^^^^^^

CGNS relies on the fact that nodes cannot be found except by following the pointers from their parents. This means that software accessing a node has had an opportunity to note all the data above that node in the tree. Therefore, nodes do not repeat within themselves information which is necessary for their interpretation but which is available at a higher level.

A datum which is necessary for the proper interpretation of a node but which is derived from its ancestors is referred to as a *structure parameter*.

Functions
^^^^^^^^^

Occasionally the proper interpretation of a node depends on an implicitly understood function of its structure parameters. Usually these relate to the actual amount of data stored. Several of these functions are defined in the :ref:`SIDS <CGNS-SIDS>` and referenced in this document.


CGNS Databases
--------------

Definition of a CGNS Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A CGNS database is defined by the existence of a node or nodes which conforms to the :ref:`specifications given below <fmmcgnsbase>` for a node of type ":sidskey:`CGNSBase_t`". This node is conceptually the root of the CGNS database. Because it is created and controlled by the user, it is not the actual root of the database file. However, current CGNS conventions require that it be located directly below the database root node which is identified by the name "/".

Further, by the mechanism of links, a CGNS database may span multiple files. Thus there is no notion of a CGNS *file*, only of a CGNS *database* implemented within one or more *files*.

By virtue of its intended use, a CGNS database is dynamic in that its content at any time reflects the current state of a CFD problem of interest. For example, after the completion of a grid generation procedure, a CGNS file may contain a grid but no boundary conditions. Therefore, beyond the occurrence of a :sidskey:`CGNSBase_t` node, there is no minimum content required in a CGNS database.

Conversely, there is no proscription against the inclusion, anywhere within a CGNS database, of nodes of any form whatsoever, provided only that their naming and labeling does not mimic CGNS conventions. Such "non-CGNS" nodes, and those below them in the tree, are not regarded as part of the CGNS database. CGNS software will not detect the existence of non-CGNS nodes.

We may therefore take the following as a definition of a CGNS database:

   A CGNS database is a subtree of a file or files which is rooted at a node with label ":sidskey:`CGNSBase_t`" and which conforms to the :ref:`SIDS data model <CGNS-SIDS>` as implemented by the SIDS File Mapping.


Location of CGNS Databases within a File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A file may contain more than one :sidskey:`CGNSBase_t` node; i.e., there may be more than one CGNS database rooted within the same file.
CGNS software accepts the *name* of the desired database as an argument, and will locate the correct :sidskey:`CGNSBase_t` node within the specified file.
Obviously, each :sidskey:`CGNSBase_t` node in a single file must have a unique name.

A CGNS database may link to CGNS nodes in the same or other files. Thus, for example, a CGNS database may reference the grid from another CGNS database without physically copying the information.
In this case, the structure of the file into which the link is made is invisible except below the node to which the link is made.


File Management
^^^^^^^^^^^^^^^

Beyond *Open* and *Close* neither CGNS or the database manager provides any file management facilities. The user is responsible for ensuring that:

- The file containing the root of the required database is available and its permissions are properly set at runtime.
- If links are made to other files, including any not under the user's direct control, these are also available at runtime.
- No file is opened for writing by more than one program at a time. 

It is possible, within CGNS, to protect files from inadvertent writing by opening them as "read only".


Internal Organization of a CGNS Database
----------------------------------------

.. _fmmcgnsbase:

The ``CGNSBase_t`` Node
^^^^^^^^^^^^^^^^^^^^^^^

At the highest level of the tree defining a CGNS database there is always a node labeled ":sidskey:`CGNSBase_t`".
The name of this node is user defined, and serves essentially as the name of the database itself.
This name is used by the CGNS software to open the database.


The ``CGNSLibraryVersion_t`` Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A file may also contain other nodes below the root node beside :sidskey:`CGNSBase_t`, but these are not officially part of the CGNS database and will not be recognized by most CGNS software.
One exception to this is a node called :sidskey:`CGNSLibraryVersion_t`, which is a child of the root node.
This node stores the version number of the CGNS standard with which the file is consistent, and is created automatically when the file is created or modified using the :ref:`CGNS Mid-Level Library <StandardMLL>`.
Officially, the CGNS version number is not a part of the CGNS database (because it is not located below :sidskey:`CGNSBase_t`). But because the Mid-Level Library software makes use of it, the node is included in this document.


Topological Basis of CGNS Database Organization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below the root, the organization of a CGNS database reflects the problem topology.
Omitting detail, the :ref:`overall structure of the CGNS database <example-hierarchy>` file is shown in the first of the :ref:`CGNS File Mapping Figures <StandardFMMFigures>`. Below the root node is the CGNSLibraryVersion_t node, and one or more CGNSBase_t nodes. Each CGNSBase_t node is the root of a CGNS database.

At the next level below a :sidskey:`CGNSBase_t` node are general specifications which apply to the problem globally, such as reference states, units, and so on.
At this level we also find a collection of nodes labeled ":sidskey:`Zone_t`".
The tree below each of these holds all the data local to one of the various zones or subdomains which constitute the problem.

Beneath each :sidskey:`Zone_t` node there are nodes whose subtrees store: the grid (labeled :sidskey:`GridCoordinates_t`); flowfields (:sidskey:`FlowSolution_t`); boundary conditions (:sidskey:`ZoneBC_t`); information about the geometrical connection to other zones (:sidskey:`GridConnectivity_t`); and information defining time-dependent data.
Below these there may be additional nodes containing yet more geometrically local information. For example, under the :sidskey:`ZoneBC_t` node there are nodes defining individual boundary conditions on portions of faces of the zone (:sidskey:`BC_t`).

Certain types of nodes originally specified at a high level are optionally repeated below.
For example, immediately below a :sidskey:`Zone_t` node we may find another :sidskey:`ReferenceState_t` node.
The CGNS convention is that such a node overrides (for the associated portion of the topology only) any data found at a higher level.

Topics Not Currently Covered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No specification of the kind represented by this file mapping can ever be complete.
However, it is worth noting that there are certain entities common in CFD which are not currently specified by the file mapping.

Within nodes of type :sidsref:`FlowSolution_t`, the current file mapping permits the storage of fields of any number of dependent variables.
In addition to those whose names are specified in the SIDS the user may add any desired quantities, naming them appropriately. Names that are not currently codified in the SIDS will not be common between practitioners without separate communication.

Obviously any sort of physical field could be stored in a FlowSolution_t node. The problem with using CGNS for such applications lies in the probable need to specify additional physical information. Standardizing this information is tantamount to extending the SIDS and File Mapping to the disciplines in question.

Similarly, if a reacting flow problem requires the specification of rate tables or catalytic wall boundary conditions, extensions to the SIDS and File mapping will be needed. 


Node descriptions
-----------------

.. toctree::
   :maxdepth: 1

   FMM/nodes
   FMM/figures


.. last line
