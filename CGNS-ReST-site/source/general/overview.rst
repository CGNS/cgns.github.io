.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _Overview:

Overview
========

This document describes the structure of CGNS, its software, and
its documentation. The
Overview, which was written primarily for new and prospective users of
CGNS,

1. introduces terminology,
2. identifies the elements of the system and their relationships,
3. describes the various documents that elaborate the details.

Reading the material on the
purpose and general description of CGNS should help users determine
whether CGNS will meet their needs. Those wanting a bit more detail
should read the section describing the various elements of CGNS. For
those interested only in understanding the scope and capabilities of
CGNS, or for the end user unconcerned with the internal workings of
the system, the Overview may prove sufficient documentation by itself.

The Overview also includes certain information that is current as of
the document date but which may change with time. All information on
CGNS compatible "applications" software (i.e., external programs such
as grid generators, flow codes, or postprocessors) is of this
type. Also subject to change is the information on the acquisition of
the software and documentation, and the current status of CGNS.

Purpose and Scope
-----------------

The general purpose of CGNS is to provide a standard for recording and
recovering computer data associated with the numerical solution of the
equations of fluid dynamics.

CGNS consists of a collection of conventions, and software
implementing those conventions, for the storage and retrieval of CFD
(Computational Fluid Dynamics) data. The system consists of two
parts: (1) a standard format for recording the data, and (2) software
that reads, writes, and modifies data in that format. The format is a
conceptual entity established by the documentation, and is intended to
be general, portable, expandable, and durable. The software is a
physical product supplied to enable developers to access and produce
data recorded in that format. All CGNS software is completely free and
open to anyone.

The CGNS standard, applied through the use of the supplied software,
is intended to:

facilitate the exchange of CFD data between sites between applications
codes across computing platforms stabilize the archiving of CFD data
The principal target of CGNS is data normally associated with
compressible viscous flow (i.e., the Navier-Stokes equations), but the
standard is also applicable to subclasses such as Euler and potential
flows. The CGNS standard addresses the following types of data.

Structured, unstructured, and hybrid grids Flow solution data, which
may be nodal, cell-centered, face-centered, or edge-centered Multizone
interface connectivity, both abutting and overset Boundary conditions
Flow equation descriptions, including the equation of state, viscosity
and thermal conductivity models, turbulence models, and multi-species
chemistry models Time-dependent flow, including moving and deforming
grids Dimensional units and nondimensionalization information
Reference states Convergence history Association to CAD geometry
definitions Much of the standard and the software is applicable to
computational field physics in general. Disciplines other than fluid
dynamics would need to augment the data definitions and storage
conventions, but the fundamental database software, which provides
platform independence, is not specific to fluid dynamics.

General Description
-------------------

A CGNS database describes the current state of one or more entire CFD
(Computational Fluid Dynamics) problems, including the following:

grid
flowfield
boundary conditions
topological connection information
auxiliary data (e.g., nondimensionalization parameters, reference states)
Not all of these data need to be present at any particular time. The overall view is that of a shared database that can be accessed by the various software tools common to CFD, such as solvers, grid generators, field visualizers, and postprocessors. Each of these "applications" serves as an editor of the data, adding to, modifying, or interpreting it according to that application's specific role.

CGNS conventions and software provide for the recording of a complete
and flexible problem description. The exact meaning of a subsonic
inflow boundary condition, for example, can be described in complete
detail if desired. User comments can be included nearly anywhere,
affording the opportunity, for instance, for date stamping or history
information to be included. Dimension and sizing information is
carefully defined. Any number of flow variables may be recorded, with
or without standard names, and it is also possible to add user-defined
or site-specific data. These features afford the opportunity for
applications to perform extensive error checking if desired.

Because of this generality, CGNS provides for the recording of much
more descriptive information than current applications normally
use. However, the provisions for this data are layered so that much of
it is optional. It should be practical to convert most current
applications to CGNS with little or no conceptual change, retaining
the option to take advantage of more detailed descriptions as that
becomes desirable.

CGNS specifications currently cover the bulk of CFD data that one
might wish to exchange among sites or applications; for instance,
nearly any type of field data can be recorded, and, based on its name,
found and understood by any code that needs it. Global data (e.g.,
freestream Mach number, Reynolds number, angle of attack) and physical
modeling instructions (e.g., thin layer assumptions, turbulence model)
may be specified. Nevertheless, there are items specific to individual
applications for which there is currently no specification within
CGNS. Most commonly, these are operational instructions, such as
number of sweeps, solution method, multigrid directives, and so
on. Owing to the miscellaneous nature of this data, there has been no
attempt to codify it within a global standard. It is therefore
expected that many applications will continue to require small
user-generated input files, presumably in ASCII format.

CGNS itself does not initiate action or undertake any function
normally handled by the operating system. The user still performs CFD
tasks according to existing processes. This includes selecting the
computing platform, maintaining the files, and launching the
applications.

However, the ease of communication between applications that CGNS
provides should motivate the development of new batch and interactive
mechanisms for the convenient application of CFD tools.

Elements and Documentation
--------------------------

Introduction Structure of a CGNS Database Standard Interface Data
Structures (SIDS) SIDS File Mapping Database Manager Mid-Level
Library, or API Documentation Introduction CGNS concerns itself with
the recording and retrieval of data associated with the computation of
fluid flows. Included are such structures as grids, flowfields,
boundary conditions, and zone connectivity information. CGNS
"understands" this data in the sense that it contains conventions for
recording it based on its structure and its role in CFD.

The underlying design of CGNS is that of a common database that is
accessed (read, written, or modified) by a collection of
"applications" programs such as solvers, grid generators, and
postprocessors.

CGNS itself does not synthesize, modify, or interpret the data it
stores. The applications create, edit, or display the data; CGNS is
limited to recording and retrieving it. Each application's program
accesses the data directly using CGNS function calls installed in the
application by its developer. The applications are not regarded as
part of CGNS itself.

CGNS is passive. It does not initiate action and cannot "push"
information into the applications codes or "pull" information
out. Rather, the codes must request the information they seek and
store the information they produce. The applications must be launched
by a user who organizes the location and content of the database. The
process and sequence of events remain under user control. Thus CGNS
facilitates, but does not incorporate, the development of batch or
interactive environments designed to control the CFD process.

The elements of CGNS address all activities associated with the
storage of the data on external media and its movement to and from the
applications programs. These elements include the following:

The Standard Interface Data Structures (SIDS), which specify the
intellectual content of CFD data and the conventions that govern
naming and terminology.  The SIDS File Mapping, which specifies the
exact location where the CFD data defined by the SIDS is to be stored
within a database file.  The Database Manager, which consists of both
a file format specification and its I/O software, which handles the
actual reading and writing of data from and to external storage media.
The following sections discuss in more detail the roles of the CGNS
elements and introduce their documentation.

Structure of a CGNS Database In this section, the conceptual structure
of a CGNS database, and the nodes from which it is built, are
discussed. This describes the way in which the CGNS software "sees"
the database, not necessarily the way in which it is
implementated. The details of the implementation are left to the
underlying database manager.

A CGNS database consists of a collection of elements called
nodes. These nodes are arranged in a tree structure that is logically
similar to a UNIX file system. The nodes are said to be connected in a
"child-parent" relationship according to the following simple rules:

Each node may have any number of child nodes.  Except for one node,
called the root, each node is the child of exactly one other node,
called its parent.  The root node has no parent.  Structure of a Node
Each node has exactly the same internal structure. The entities
associated with each node are the following: Node Identifier (ID) Name
Label Data Type Dimension Dimension Values Data Child Table Node
Identifier. The Node ID is a floating point number assigned by the
system when the database is opened or created. Applications may record
the ID and use it to return directly to the corresponding node when
required. The Node ID is valid only while the database is open;
subsequent openings of the same database may be expected to yield
different IDs.

Name. The Name field holds a character string chosen by the user or
specified by the SIDS to identify the particular instance of the data
being recorded.

Label. The Label, also a character string, is specified by the CGNS
mapping conventions and identifies the kind of data being
recorded. For example, a node with label Zone_t may record (at and
below it) information on the zone with Name "UnderWing." No node may
have more than one child with the same name, but the CGNS mapping
conventions commonly specify many children with the same label. For
some nodes, the mapping conventions specify that the name field has
significance for the meaning of the data (e.g.,
EnthalpyStagnation). Although the user may specify another name, these
"paper" conventions serve the transfer of data between users and
between applications. These names and their meanings are established
by the SIDS.

Data Type, Dimension, Dimension Values, Data. Nodes may or may not
contain data. For those that do, CGNS specifies a single array whose
type (integer, etc.), dimension, and size are recorded in the Data
Type, Dimension, and Dimension Value fields, respectively. The mapping
conventions specify some nodes that serve to establish the tree
structure and point to further data below but contain no data
themselves. For these nodes, the Data Type is MT, and the other fields
are empty. A link to another node within the current or an external
CGNS database is indicated by a Data Type of LK

Child Table. The Child Table contains a list of the node's
children. It is maintained by the database manager as children are
created and deleted.

High-Level Organization of the CGNS Database For a full specification
of the location of CFD data in the CGNS database, the user should see
the SIDS File Mapping document. For convenience, we summarize the
high-level structure below.  A CGNS database consists of a tree of
nodes implemented as all or part of one or more database files. All
information is identified by and accessed through a single node in one
of these files.

By definition, the root node of a CGNS database has the Label
CGNSBase_t. The name of the CGNS database can be specified by the user
and is stored in the "Name" field of the CGNSBase_t node. Current CGNS
conventions require that the CGNSBase_t node be located directly below
a "root node" in the database file indentified by the name "/".

A database file may contain multiple CGNS databases, and thus multiple
CGNSBase_t nodes. However, each node labeled CGNSBase_t in a single
file must have a unique name. The user or application must know the
name of the file containing the entry-level node and, if there is more
than one node labeled CGNSBase_t in that file, the name of the
database as well.

Below the CGNSBase_t node, the mapping conventions specify a subnode
for each zone. This node has label Zone_t. Its Name refers to the
particular zone whose characteristics are recorded at and below the
node, such as "UnderWing." In general, names can be specified by the
user, but defaults are specified for nodes that the user does not
choose to name. For the Zone_t nodes, the defaults are Zone1, Zone2,
and so forth, in order of creation. A similar convention for default
names applies elsewhere. It is impossible to create a node without a
name (or with a name of zero length). The CGNS Mid-Level Library
conforms to the default convention.

Below each zone node will be found nodes for the grid, flowfield,
boundary conditions, and connectivity information; these, in turn, are
parents of nodes specifying extent, spatial location, and so on.

The file mapping specifies that one or more "Descriptor" nodes may be
inserted anywhere in the file. Descriptor nodes are used to record
textual information regarding the file contents. The size of
Descriptor nodes is unlimited, so entire documents could be named and
stored within the data field if desired. Descriptors are intended to
store human-readable text, and they are not processed by any supplied
CGNS software (except, of course, that the text may be stored and
retrieved).

It is possible, by using the linking capability of CGNS, for a child
of any node to be a node in another database file, or elsewhere within
the same file. This mechanism enables one database to share a grid,
for example, with another database without duplicating the
information.

Standard Interface Data Structures (SIDS) The establishment of a
standard for storing CFD-related information requires a detailed
specification of the content and meaning of the data to be stored. For
example, it is necessary to state the meaning of the words "boundary
condition" in a form sufficiently concrete to be recorded precisely,
and yet sufficiently flexible to embrace current and future
practice. The Standard Interface Data Structures (SIDS) document
describes this "intellectual content" of CFD-related data in detail.

An exact description of the intellectual content is required not only
to define the precise form of the data but also to guarantee that the
meaning of the data is consistently interpreted by practitioners. Thus
the SIDS include a collection of naming conventions that specify the
precise meaning of nomenclature (e.g., the strings DensityStatic and
BCWallViscous).

The SIDS are written in a self-contained C-like descriptive
language. SIDS data structures are defined in a hierarchical manner in
which more complex entities are built from simpler ones. These
structures are closely reflected in CGNS-compliant files: simple
entities are often stored in single nodes, while more complex
structures are stored in entire subtrees.

SIDS File Mapping Because of the generality of the tree structure,
there are many conceivable means of encoding CFD data. But for any
application to access, say, the boundary conditions for zone
"UnderWing", requires a single convention with regard to where in the
file that data has been stored. The SIDS File Mapping document,
sometimes referred to as the "File Mapping," establishes the precise
node, and properties of that node, where each piece of CGNS data
should be recorded. The CGNS Mid-Level Library relies on the File
Mapping to locate CFD-related data within the file.  The mapping
provides locations for an extensive set of CFD data. Most applications
will make use of only a small subset of this data. Further, inasmuch
as applications are viewed as editors that are in the process of
building the database, most of them are intended for use on incomplete
data sets. Therefore, it is not required that all the data elements
specified by the CGNS conventions be complete in order for a database
to be CGNS compliant. The user must ensure that the current state of
the database will support whatever application he may launch. Of
course, the application should gracefully handle any absence or
deficiency of data.

CGNS conventions do not specify the following:

the use the applications programs may make of the data the means by
which the applications programs modify the data the form in which the
data is stored internal to an application The validity, accuracy and
completeness of the data are determined entirely by the applications
software.  The tree structure also makes it possible for applications
to ignore data for which they have no use. (In fact, they cannot even
discover the data's existence without a specific inquiry.) Therefore,
it is permissible for an file containing a CGNS database to contain
additional nodes not specified by the mapping. Such nodes will be
disregarded by software not prepared to use them. However, if data
essential to the CFD process is stored in a manner not consistent with
CGNS conventions, that data becomes invisible and therefore useless to
other applications.

Note that the SIDS serve not only to facilitate the mapping of data
onto the file structure but also to standardize the meaning of the
recorded data. Thus there are two kinds of conventions operative
within CGNS. Adherence to the File Mapping conventions guarantees that
the software will be able to find and read the data. Adherence to the
SIDS guarantees uniformity of meaning among users and between
applications. The SIDS File Mapping document establishes the context
of CGNS for a database manager; the SIDS define the nomenclature,
content, and meaning of the stored data.

The File Mapping generally avoids the storage of redundant
data. Sometimes an application may require an alternate (but
intellectually equivalent) form of the data; in such cases it is
recommended that the alternate form be prepared at the time of use and
kept separate from the CGNS data. This avoids habitual reliance on the
alternate form, which would invalidate the standard.

Database Manager A database manager contains the I/O software, which
handles the actual reading and writing of data from and to external
storage media. It must conform, at least in context, to that specified
by the SIDS File Mapping document, and provide a minimal number of
data access routines (referred to as core routines). In principle, it
is possible to install CGNS I/O into an application using only these
core routines. However, such an approach would require the installer
to access the data at a very fundamental level and would result in
lengthy sequences of core function calls. Therefore, the CGNS system
also includes a Mid-Level Library, an API (Application Programming
Interface) that contains additional routines intended to facilitate
higher-level access to the data. These are CFD-knowledgeable routines
suitable for direct installation into applications codes.  The CGNS
software was originally developed around ADF (Advanced Data Format) as
it's database manager, thus much of the concepts and structures of
CGNS originated from there.

In version 2.4 of the CGNS software, HDF5 (Hierarchical Data Format
was introduced as an alternative database manager. At that time,
either ADF or HDF5 (but not both) was selectable at build time.

It should be noted that because of HDF5's parallel and compression
capability as well as its support, the CGNS Steering Committee has
made the decision to slowly transition (beginning in 2005) to HDF5 as
the official data storage mechanism. However, ADF will continue to be
available for use, with the CGNS mid-level library capable of (1)
using either format and (2) translating back and forth between the
two.

Beginning with CGNS version 3.0, both ADF and HDF5 are supported
concurrently and transparently by CGNS. To facilitate this, a new set
of core routines, described in the CGIO User's Guide, have been
developed as a replacement to the individual ADF and HDF5 core
routines. These allow general access to the low-level I/O,
irrespective of the underlying database manager.

Mid-Level Library, or API The CGNS Mid-Level Library, or Applications
Programming Interface (API), is one of the most directly visible parts
of CGNS, and it is of particular interest to applications code
developers. It consists of a set of routines that are designed to
allow applications to access CGNS data according to the role of the
data in CFD. Unlike the ADF (or HDF5) Core, routines in the CGNS
Mid-Level Library "understand" the SIDS-defined CFD data structures
and the File Mapping. This enables applications developers to insert
CGNS I/O into their applications without having detailed knowledge of
the File Mapping. For instance, an application might use CGNS
mid-level calls to retrieve all boundary conditions for a given zone.

The CGNS Mid-Level Library document contains complete descriptions and
usage instructions for all mid-level routines. All calls are provided
in both C and Fortran.

Documentation The CGNS elements described above are documented
individually, and are available as follows:

Standard Interface Data Structures
SIDS File Mapping Manual
Mid-Level Library
CGIO User's Guide
ADF Implementation
HDF5 Implementation
In addition, the following documentation is also recommended:

CGNS Overview and Entry-Level Document (this document) A User's Guide
to CGNS "The CGNS System", AIAA Paper 98-3007 [PDF (496K, 16 pages)]
"Advances in the CGNS Database Standard for Aerodynamics and CFD",
AIAA Paper 2000-0681 [PDF (106K, 11 pages)] "CFD General Notation
System (CGNS): Status and Future Directions", AIAA Paper 2002-0752,
[PDF (289K, 13 pages)] The specific documents of interest vary with
the level of intended use of CGNS.  Prospective Users Prospective
users are presumably unfamiliar with CGNS. They will probably wish to
begin with the current Overview document, or, if they require more
detailed information, the AIAA papers listed above. Beyond that, most
will find a quick read of the SIDS File Mapping Manual (or
enlightening as to the logical form of the contents of CGNS
files. Browsing the figures in the File Mapping Manual, as well as the
SIDS itself, will provide some feel for the scope of the system. The
User's Guide to CGNS, and the CGNS Mid-Level Library document, should
give an indication of what might be required to implement CGNS in a
given application. Prospective users should probably not concern
themselves with the details of ADF or HDF5.

End Users The end user is the practitioner of CFD who generates the
grids, runs the flow codes and/or analyzes the results. For this user,
a scan of this Overview document will sufficiently explain the overall
workings of the system. This includes end user responsibilities for
matters not governed by CGNS, such as the maintenance of files and
directories. The end user will also find useful the User's Guide to
CGNS, as well as those portions of the SIDS which deal with standard
data names. The AIAA papers listed above may also be useful if more
details about the capabilities of CGNS are desired.

Applications Code Developers The applications code developer builds or
maintains code to support the various sub-processes encountered in
CFD, e.g., grid generation, flow solution, post-processing, or flow
visualization. The code developer must be able to install CGNS
compliant I/O. The most convenient method for doing so is to utilize
the CGNS Mid-Level Library. The User's Guide to CGNS is the starting
point for learning to use the Mid-Level Library to create and use CGNS
files. The CGNS Mid-Level Library document itself should also be
considered essential. This library of routines will perform the most
common I/O operations in a CGNS-compliant manner. However, even when
the Mid-Level Library suffices to implement all necessary I/O, an
understanding of the file mapping and SIDS will be useful. It will
likely be necessary to consult the SIDS to determine the precise
meaning of the nomenclature.

Applications code developers wishing to read or write data that isn't
supported by the Mid-Level Library, will need to use the CGIO
low-level routines to access the underlying database manager
directly. The CGIO User's Guide documents these routines in detail.

CGNS System Developers CGNS System development can be kept somewhat
compartmentalized. Developers responsible for the maintenance or
building of supplements to the ADF Core, need not concern themselves
with documentation other than the ADF User Guide. (Development and
maintenance of HDF5 is under the purview of NCSA, so has no relevance
here.) System developers wishing to add to the CGNS Mid-Level Library
will need all the documents. Theoretical developments, such as
extensions to the SIDS, may possibly be undertaken with a knowledge of
the SIDS alone, but such contributions must also be added to the SIDS
File Mapping before they can be implemented.

Applications Software
---------------------

CGNS-Compatible Applications CGNS Utilities The development of
CGNS-compliant applications, e.g., grid generators, postprocessors,
and the like, has not been a direct undertaking of the CGNS
team. Rather, it has been the intent to make the attractiveness of
interoperable CFD applications, together with general acceptance of
the CGNS standard by Boeing, NASA, and others, sufficient to induce
applications developers to incorporate CGNS I/O into their offerings.

Several CGNS-compatible applications have indeed been developed, and
more continue to appear. This section lists the known applications at
the time of publication. Please contact Tony Iannetti to modify or add
to the lists.

CGNS-Compatible Applications This section lists major software
packages that read and/or write CGNS files. The software listed here
is taken from Table 1 of AIAA Paper 2002-0752, and is for
informational purposes only. The CGNS Project Group cannot endorse
specific software packages.

CGNS-Compatible Grid Generators and Pre-Processors

Organization	  	Application	  	Contact
Commercial
Ansys, Inc. external link		ANSYS ICEM CFD external link		ansysinfo@ansys.com
NUMECA external link		IGG external link		http://www.numeca.be/index.php?id=offices external link
Pointwise, Inc. external link		GRIDGEN external link		http://www.pointwise.com/pointwise/contact.shtml external link

Industry
Pratt & Whitney Rocketdyne external link		APPT		
CGNS-Compatible Flow Solvers

Organization	  	Application	  	Contact
Commercial
Ansys, Inc. external link		CFX5 external link		ansysinfo@ansys.com
CFX-TASCFlow external link		ansysinfo@ansys.com
Aerosoft, Inc. external link		GASP external link		http://www.aerosft.com/Misc/contact.php external link
CD ADAPCO external link		STAR-CD external link		http://www.cd-adapco.com/about/global_locations.html external link
Fluent, Inc. external link		Fluent external link		http://www.fluent.com/contact/ external link
Newmerical Tech. external link		FENSAP external link		http://www.newmerical.com/public/eng/index.php?pageId=about&language=en external link
NUMECA external link		EURANUS		http://www.numeca.be/index.php?id=offices external link

Government
DLR/MTU external link		TRACE external link		Frank.Eulitz@dlr.de
NASA Langley		PEGSUS		Pieter.G.Buning@nasa.gov
OVERFLOW		Pieter.G.Buning@nasa.gov
Cart3D		http://people.nas.nasa.gov/~aftosmis/
NASA Glenn		NCC		Nan-Suey.Liu-1@nasa.gov
NASA Langley		CFL3D external link		http://cfl3d.larc.nasa.gov/Cfl3dv6/cfl3dv6.html#contact external link
UPS		
NPARC Alliance external link		WIND		npsupport@info.arnold.af.mil
ONERA external link		elsA external link		http://elsa.onera.fr/elsA/contacts.html external link

Industry
Boeing Seattle external link		TLNS3D		
Rolls-Royce Allison external link		ADPAC		
Rolls-Royce Oxford external link		HYDRA external link		pierre.moinier@comlab.ox.ac.uk
CGNS-Compatible Post Processors

Organization	  	Application	  	Contact
Commercial
Advanced Visual Sys. external link		AVS/Express external link		http://www.avs.com/contact/ external link
Aerosoft, Inc. external link		GASP external link		http://www.aerosft.com/Misc/contact.php external link
Tecplot, Inc. external link		Tecplot external link		http://www.tecplot.com/contact_us/ external link
CEI external link		Ensight external link		http://www.ensight.com/contact-us-3.html external link
Ensight Gold external link		http://www.ensight.com/contact-us-3.html external link
Fluent, Inc. external link		Fluent external link		http://www.fluent.com/contact/ external link
Ansys, Inc. external link		ANSYS ICEM CFD external link		ansysinfo@ansys.com
Intelligent Light external link		Fieldview external link		fieldview@ilight.com
Newmerical Tech. external link		DROP3D external link		http://www.newmerical.com/public/eng/index.php?pageId=about&language=en external link
ICE3D external link		http://www.newmerical.com/public/eng/index.php?pageId=about&language=en external link
NUMECA external link		CFView external link		http://www.numeca.be/index.php?id=offices external link

Government
NASA Ames		PLOT3D		Cetin.C.Kiris@nasa.gov
CGNS Utilities
A variety of CGNS utility packages have been developed, both by CGNS team members and by CGNS users. While not formally a part of CGNS itself, these utilities are available from the CGNS web site external link.

  	Plot3dg_to_CGNS external link	  	Converts a "standard" Plot3D grid file to a CGNS grid file.
Contact: Chris Rumsey (Christopher.L.Rumsey@nasa.gov)
 
CGNS_to_Plot3d external link		Converts a CGNS file with a cell-centered solution to "standard" Plot3D grid and solution files.
Contact: Chris Rumsey (Christopher.L.Rumsey@nasa.gov)
 
CGNS_readhist external link		Reads a CGNS file and writes history data to a formatted file.
Contact: Chris Rumsey (Christopher.L.Rumsey@nasa.gov)
 
FTU external link		Converts CGNS files to and from Plot3D format. Has a text-based menu allowing the manipulation of a CGNS base.
Contact: Bob Bush (bushrh@pweh.com)
 
CGNSview external link		A CGNS file viewer and editor; requires Tcl/Tk 8.3 or above. The GUI allows complete editing of CGNS files (both ADF and HDF5), and handles links and data conversions. It works at the CGIO interface level, and thus is not affected by "bad" CGNS files. It includes built-in CGNS node and label information, and documentation support through HTML (including access to all CGNS docs).
Contact: Bruce Wedan (leavingdust@gmail.com)
 
CGNS Tools external link		A variety of tools for viewing, editing, and manipulating the contents of CGNS files; requires Tcl/Tk 8.3 or above. Included are:
CGNSplot, for plotting grids
CGNScalc, a calculator using data in CGNS files
Utilities for converting from Patran, and from/to PLOT3D and Tecplot
Utilities for modifying the grid location (vertex or cell-center), solution variables (primitive or conservative), and data class (Dimensional, NormalizedByDimensional, or NormalizedByUnknownDimensional)
Utilities for creating a subset or interpolated version of a CGNS file
These may be used as stand-alone utilities, or initiated from CGNSview, which is included.
Contact: Bruce Wedan (leavingdust@gmail.com)
 
PyCGNS external link		A Python binding to the ADF Core and Mid-Level Library. For more information, see the pyCGNS home page external link.
Contact: Marc Poinot (Marc.Poinot@onera.fr)
 
ADFM external link		A development version of software for managing an in-memory representation of ADF trees. Contact: Marc Poinot (Marc.Poinot@onera.fr)
 
CGNS++ external link		A C++ binding to the ADF Core and Mid-Level Library. For more information, see the CGNS++ home page external link.
Contact: Manuel Kessler (kessler@iag.uni-stuttgart.de)

Acquiring CGNS
--------------

Software
Documentation
Software
The CGNS software is available free of charge, under the terms of the CGNS License, from http://www.cgns.org external link. Also available there are the cgnstools utilities, the source code examples from A User's Guide to CGNS, and additional Fortran source code examples.

The CGNS Library contains source code for the Mid-Level Library, the CGIO core, and the ADF and HDF5 implementations, plus CMake and configure scripts for building the library for a variety of platforms.

Documentation
The CGNS documentation may be accessed via the CGNS Documentation home page. In addition to current version, documentation may also be available for the previous and beta versions of CGNS. All the CGNS documentation is available in HTML form (PDF is no longer being supported except for the SIDS).

In addition to the CGNS documentation itself, several conference papers and slide presentations are available, as well as minutes from the CGNS meetings and telecons.


.. last line
