.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardCGIO:
   
CGNS/CGIO - Basic node implementation
=====================================

The CGIO interface provides low-level access to the database manager which underlies CGNS.
The CGIO interface supports both ADF and HDF5 database managers simultaneously, and in a fashion transparent to the application code.

This document defines the general structure of a database file, but not the specific implementation details.
See the ADF and HDF5 Implementations for the details.
The CGIO core routines used to store and retrieve data from the database manager are also described.

Node - The Building Block
-------------------------

A database is a hierarchical system that is built around the concept of a "node". Each node contains information about itself and its ancestors and possibly data (e.g., arrays, vectors, character strings, etc.). Each of these nodes, in turn, may be connected to an arbitrary number of children, each of which is itself a node. In this system, a node contains user-accessible information related to identification, name, type, and amount of data associated with it, and pointers to child nodes. Basic nodal information includes:

  - a unique ID (node locator)
  - a name (character string) used to describe the node and its data
  - a label (character string) an additional field used to describe the node and its data. It is analogous to, but not exactly the same as, the name.
  - information describing the type and amount of data
  - data
  - IDs of child nodes 

There are no restrictions on the number of child nodes that a node can have associated with it in the database.
This structure allows the construction of a hierarchical system as shown in the figure below.
As illustrated in the figure, it is possible to reference nodes in a second file (*File_Two*) from the original file (*File_One*).
This is the concept of "linking."

.. _ExampleNodeDatabase:

.. figure:: ../../images/cgio/figs/database.gif
   :width: 600px
   :align: center
   :alt: Example database showing node connections and links.
    
   *Example Database Hierarchy of Nodes*
	


A node knows about itself and its children, but it does not know anything about its parent. This means that it is possible to traverse "down" the tree by making queries about what lies below the current node, but it is not possible to traverse "up" the tree by making queries about nodes above a given node. If it is desired to move back up the tree, the user must keep track of that information.

All database files start with a root node, which is created automatically when a new file is opened. There is only one root node in a database file, and may be referenced by the database Root ID or by name as "/".

Node Attributes
---------------
Each node in the database may have zero to many subnodes that are associated with it, as well as its own data. The following are a list of attributes accessible by the user for a node in the hierarchical database system.

:Data:	   	The data associated with a node.
 
:Data Type:		A 2-byte character field, blank filled, case sensitive. Specifies the type of data (e.g., real, integer, character) associated with this node. The supported data types are listed below.
 
:Dimensions:		An integer vector containing the number of elements within each dimension. For example, if the array A was declared (Fortran) as A(10,20), the Dimension vector would contain two entries (10,20).

:ID:    A unique identifier to access a given node within a file. This field contains sufficient information for the database manager to locate the node within a file. For any given node, the ID is generated only after the file it resides in has been opened by a program and the user requests information about the node. The ID is valid only within the program that opened the file and while that file is open. If the file is closed and reopened, the ID for any given node may be different. Within different programs, the node ID for the same node may also be different. The ID is never actually written into a file.
 
:Label: A 32-byte character field. The rules for Labels are identical to those for Names. Unlike names, Labels do not have to be unique. The Label field was introduced to allow "data typing" similar to the "typedef" concept in C. Using the Label field in this way allows programs to know some additional information about the use of the node itself or its child nodes and to call specific subroutines to read the data or react in specific ways upon detection of the type.
 
:Name:  A 32-byte character field. The names of child nodes directly attached to a parent node must be unique. For example, in the example database figure, all nodes directly attached to N3 must have unique names. When a request to create a new node is made, the database manager checks the requested name against the other names of the child nodes of the specified parent. If the requested name is not unique, an error is returned.
        Legal characteristics of a name are a A-Z, a-z, 0-9, and special characters (ASCII values from 32 to 126, except for the forward slash "/" (ASCII number 47)). Names will be blank filled to 32 bytes; they are case sensitive. Leading blanks are discarded and trailing blanks are ignored, whereas internal blanks are significant.

        .. note::
          Names passed from C must have the null "\0" character appended to them.
          Names returned through the C interface will have the null character appended to them. Therefore, C programs should allocate 33 bytes for any Name in order to accommodate the null character.

          Fortran programs can allocate 32 characters for Names. The Fortran interface takes care of adding or removing the null character as required.
 
:Names of Subnodes:  A list of names of the subnodes (children) of a node.
 
:Number of Dimensions: The dimensionality of the data. All data is viewed as an array with from zero (i.e., no data) to 12 dimensions. A "0" is used if the data type is empty. Thus, a scalar is viewed as a vector with one dimension and length 1.
 
:Number of Subnodes:	The number of child nodes directly attached to any given node. Each node can have zero or more child nodes directly associated with it.

The following table lists the data types supported by CGNS.

========== ========================== ================ ==============
 Notation    Data Type                 C Type	   	    Fortran Type
========== ========================== ================ ==============
    MT      No Data				
    I4      32-bit Integer             int              integer*4
    I8      64-bit Integer             cglong_t         integer*8
    U4      32-bit Unsigned Integer    unsigned int     integer*4
    U8      64-bit Unsigned Integer    cgulong_t        integer*8
    R4      32-bit Real                float            real*4
    R8      64-bit Real                double           real*8
    X4      64-bit Complex             complex          complex*8
    X8      128-bit Complex            complex double   complex*16
    C1      Character                  char             character
    B1      Byte (unsigned byte)       unsigned char    character*1
    LK      Link				
========== ========================== ================ ==============

The "MT" node contains no data, and is typically used as a container for subnodes (children).

A link is denoted by "LK", and defines the linkage between nodes and subnodes. A link provides a mechanism for referring to a node that physically resides in a different part of the hierarchy or a different database file. The link parallels a soft link in the UNIX operating system in that it does not guarantee that the referenced node exists. The database manager will "resolve" the link only when information is requested about the linked node or it's children.


Glossary of Terms
-----------------

:Child:	   	One of the subnodes of a Parent. A child node does not have knowledge of its parent node. The user must keep track of this relationship.
 
:Database:		The representation of a hierarchy of nodes on disk files. By use of links, it may physically span multiple files.
 
:File:	The database file, with a single root node and its underlying structure.
 
:ID:		A unique identifier to access a given node within a database file. This field contains sufficient information for the database manager to locate the node within a file. For any given node, the ID is generated only after the file it resides in has been opened by a program and the user requests information about the node. The ID is valid only within the program that opened the file and while that file is open. If the file is closed and reopened, the ID for any given node may be different. Within different programs, the node-ID for the same node may also be different. The ID is never actually written into a file.
 
:Link-Node:		A special type of node. Links are created using the cgio_create_link subroutine. The data type of this node is LK, and its data is a one-dimensional array containing the name of the file (if other than the current file) containing the node to be linked and the full path name in that file from the root node to the desired node.
                    Links provide a mechanism for referring to a node that physically resides in a different part of the hierarchy. The node pointed to by a link may or may not reside in the same file as the link itself. A link is very similar to a "soft" link in the UNIX operating system in that it does not guarantee that the referenced node exists. The database manager will "resolve" the link only when information is requested about the node. If the ID of a link-node is used in an CGIO call, the effect of the call is the same as if the ID of the linked-to node was actually used. Note that a link node does not have children itself. In the example database figure, the children seen for L3 are F4 and F5. If a child is "added" to L3, then in reality, the child is added to F3. There are specialized subroutines provided to create link nodes and extract the link details.
 
:Node:		The single component used to construct a database.
 
:Node name:		A node has a 32-character name. Every child node directly under a given parent must have a unique name. Legal characteristics in a name are A-Z, a-z, 0-9, and special characters (ASCII values from 32 to 126, omitting the forward slash "/", ASCII number 47). Names will be blank filled to 32 bytes; they are case sensitive. Leading blanks are discarded and trailing blanks are ignored, whereas internal blanks are significant.

:Parent:		A node that has subnodes directly associated with it.
 
:Pathname:		Within a database, nodes can be referenced using the name of a node along with its parent ID, or by using a "pathname" whose syntax is roughly the same as a path name in the UNIX environment. A pathname that begins with a leading slash "/" is assumed to begin at the root node of the file. If no leading slash is given, the name is assumed to begin at the node specified by the parent ID. Although there is a 32-character limitation on the node Name, there is no restriction on the length of the pathname. For example, equivalent ways to refer to node N8 in the hierarchy in the :ref:`example database` figure are:

                     - Node-ID for N6 and name = "N8"
                     - Node-ID for N4 and name = "N6/N8"
                     - Node-ID for N1 and name = "N4/N6/N8"
                     - Node-ID for the Root_Node and name = "/N1/N4/N6/N8" 

Conventions and Implementations
-------------------------------

:C:  All input strings are to be null terminated. All returned strings will have the trailing blanks removed and will be null terminated. Variables declared to hold Names, Labels, and Data-Types should be at least 33 characters long. *cgns_io.h* has a number of variables defined. An example declaration would be:

     .. code-block:: c

       char name[CGIO_MAX_NAME_LENGTH+1];
       

:Fortran:  Strings will be determined using inherited length. Returned strings will be blank filled to the specified length. All returned names will be left justified and blank filled on the right. There will be no null character. An example declaration would be:
           
           .. code-block:: fortran

             PARAMETER CGIO_MAX_NAME_LENGTH=32
             CHARACTER*(CGIO_MAX_NAME_LENGTH) NAME

           or include the Fortran header file *cgns_io_f.h* which defines these parameters.
 
:ID:		A unique identifier to access a given node within a database. For any given node, the ID is generated only after the file it resides in has been opened by a program and the user requests information about the node. The ID is valid only within the program that opened the file and while that file is open. If the file is closed and reopened, the ID for any given node may be different. Within different programs, the node ID for the same node may also be different. The ID is not ever actually written into a file.
                The declaration for variables that will hold node IDs should be for an 8-byte real number.
 
:Indexing:  All indexing is Fortran-like in that the starting index is 1 and the last is N for N items in an index or array dimension. The array structure is assumed to be the same as in Fortran with the first array dimension varying the fastest and the last dimension varying the slowest.
            The index starting at one is used in :code:`cgio_read_data_type`, :code:`cgio_write_data`, :code:`cgio_children_names`, and :code:`cgio_children_ids`.
            The user should be aware of the differences in array indexing between Fortran and C. The subroutines :code:`cgio_read_all_data_type` and :code:`cgio_write_all_data` merely take a pointer to the beginning of the data, compute how much data is to be read/written, and process as many bytes as have been requested. Thus, these routines effectively make a copy of memory onto disk or vice versa. Given this convention, it is possible for a C program to use standard C conventions for array indexing and use :code:`cgio_write_all_data` to store the array on disk. Then a Fortran program might use cgio_read_all_data_type_f to read the data set. Unless the user is aware of the structure of the data, it is possible for the array to be transposed relative to what is expected.
            The implications of the assumed array structure convention can be quite subtle. The subroutines :code:`cgio_write_data` and :code:`cgio_read_data_type` assume the Fortran array structure in order to index the data. Again, unless the user is aware of the implications of this, it is possible to write an array on disk and later try to change a portion of the data and not change the correct numbers.
            As long as users are aware of how their data structure maps onto the database, there will not be any problems.
 
:return codes:  The CGIO routines return an integer code indicating whether they were successfull or not. On success, :code:`0` (:code:`CGIO_ERR_NONE`) is returned. A non-zero return indicates an error. Return codes < 0 indicate an error at the CGIO level; codes > 0 indicate an error in the database manager. See Error Messages for a list of error codes and mesages.


Limits and Sizes
----------------

The following default values, sizes, and limits are defined in the header file *cgns_io.h*.

================================== ======= =================================
Define                             Value   Attribute
================================== ======= =================================
:code:`CGIO_MAX_DATATYPE_LENGTH`    2       Data type length	
:code:`CGIO_MAX_DIMENSIONS`         12      Maximum dimensions	
:code:`CGIO_MAX_NAME_LENGTH`        32      Maximum node name length	
:code:`CGIO_MAX_LABEL_LENGTH`       32      Maximum node label length	
:code:`CGIO_MAX_VERSION_LENGTH`     32      Maximum version length	
:code:`CGIO_MAX_DATE_LENGTH`        32      Maximum date length	
:code:`CGIO_MAX_ERROR_LENGTH`       80      Maximum length of error string	
:code:`CGIO_MAX_LINK_DEPTH`         100     Maximum link depth	
:code:`CGIO_MAX_FILE_LENGTH`        1024    Maximum file name length	
:code:`CGIO_MAX_LINK_LENGTH`        4096    Maximum link data size
================================== ======= =================================


.. _CGIOCoreRoutines:

CGIO core routines
------------------

.. toctree::
   :maxdepth: 2

   CGIO/CGNS_CGIO_database
   CGIO/CGNS_CGIO_structure
   CGIO/CGNS_CGIO_links
   CGIO/CGNS_CGIO_node
   CGIO/CGNS_CGIO_dataio
   CGIO/CGNS_CGIO_errors
   CGIO/CGNS_CGIO_misc
   CGIO/CGNS_CGIO_example
   

.. last line
