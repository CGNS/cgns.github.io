.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _HistoryAndStatus:

Status and History
==================

CGNS has now more than 20 years of history.
The section below details its history, the current status and some of
the noticeable contribution to the standard.

Current Status
^^^^^^^^^^^^^^
**Current Status**

Since the initial release of the Mid-Level Library in
May 1998, interest in CGNS has continued to grow throughout the global
CFD community. The system is being used by engineers and scientists in
academia, industry, and government. By January 2002, 591 users from
more than 25 countries had formally registered at the CGNS web
site. As of September 2007, the CGNStalk mailing list had 224
participants from 20 different countries and at least 79 different
organizations.

Software The current "production" release of CGNS is Version 3.1,
released in January 2011.

Several extensions to CGNS have been formally proposed. Documentation
supporting these extensions, and information on their current status,
is available via the "Proposals for Extensions external link" link at
the CGNS web site external link.

History
^^^^^^^

Initial Development
~~~~~~~~~~~~~~~~~~~

The initial development of CGNS took place from March 1995 through May 1998,
when Version 1.0 of the CGNS software was released.
The project originated through a series of meetings in 1994-1995 between NASA,
Boeing, and McDonnell Douglas, who were then working under the
Integrated Wing Design element of NASA's Advanced Subsonic Technology Program.
The work being planned involved extensive use of CFD, and the possibility of
collaborative analyses by many organizations. It was thus necessary
to establish a common data format suitable to meet the needs of production
CFD tools in the mid- to late-1990s. This format would be used
to enable interchange of data among different CFD-related tools and
different computing platforms, and to provide a mechanism for archive and
retrieval of CFD data

.. list-table::
   :width: 100

   * - .. image:: ../../_images/members/NASA_logo.svg
          :align: center
          :width: 150
     -
     - .. image:: ../../_images/members/Boeing_logo.svg
          :align: center
          :width: 150
     -
     - .. image:: ../../_images/members/McDonnellDouglas_logo.svg
          :align: center
          :width: 150
   
At that time, the de facto standard for CFD data was the file format
used by Plot3D, a flow visualization program developed at NASA Ames.
However, the Plot3D format was developed to expedite post-processing,
and was never intended as a general-purpose standard for the storage
and exchange of CFD data. By the early 1990s, as CFD became more sophisticated,
the limitations of the Plot3D format as a general-purpose standard had become
apparent. It had no provisions for storing data associated with modern
CFD technology, such as unstructured grids, turbulence models based on
solutions of partial differential equations, and flows with multiple chemical
species.

Individual organizations were overcoming these limitations by defining
extensions to the Plot3D format to meet their needs. These extensions were not
coordinated among different organizations, and therefore data stored in these
extended formats generally could not be utilized outside the originating
organization. Further, the Plot3D format was not self-documenting,
and it was necessary to rely on file-naming conventions or external notes
to maintain awareness of the flow conditions and analyzed geometry
of each PLOT3D data file.

To overcome these limitations, several database options were considered
by the NASA / Boeing / McDonnell Douglas team from December 1994 to March 1995.
In March 1995, the decision was made to build a new data standard called
CGNS (Complex Geometry Navier Stokes). This standard was a "clean sheet"
development, but it was heavily influenced by
the McDonnell Douglas Common File Format (CFF),
which had been established and deployed in 1989 and heavily revised in 1992.

Agreement was reached to develop CGNS at Boeing,
under NASA Contract NAS1-20267, with active participation
by a team of CFD researchers from:

  - `NASA Langley Research Center <http://www.larc.nasa.gov/>`_
  - `NASA Glenn Research Center <http://www.grc.nasa.gov/>`_
  - `NASA Ames Research Center <http://www.arc.nasa.gov/>`_
  - `McDonnell Douglas Corporation (now Boeing St. Louis) <http://www.boeing.com/phantom/>`_
  - `Boeing Commercial Airplane Group (Seattle) <http://www.boeing.com/commercial/index.html>`_ Aerodynamics 
  - `Boeing Commercial Airplane Group (Seattle) <http://www.boeing.com/commercial/index.html>`_ Propulsion
  - `ICEM CFD Engineering Corporation <http://www-berkeley.ansys.com/>`_

The original development work itself occurred from 1995-1998, and consisted of essentially four activities:

 1. Development of the standalone database manager (the ADF Core)
 2. Identification and layout of the CFD data (the SIDS and File Mapping)
 3. Development of an API for use in applications codes (the Mid-Level Library)
 4. Demonstration of system capability
    
Development of ADF
~~~~~~~~~~~~~~~~~~

As noted earlier, the decision to develop CGNS was made after an examination
of several existing formats. Because of its hierarchical structure,
the CFF (Common File Format) that was then in use at McDonnell Douglas was
judged the most compatible with the SIDS. However, CFF had known limitations,
and it was decided to adopt the CFF structure but recast it in a more general
form. This gave the developers control over the software and facilitated the
development of a robust, portable, reliable, and flexible database manager,
which could be distributed freely within the system.

These low-level routines were developed during 1995, and make up the
ADF (Advanced Data Format) Core. ADF was written and extensively tested at
Boeing by a small subteam familiar with standard software development
practices, and it may now be considered a stable product.

Identification and layout of the CFD data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another task, undertaken in parallel with the development of ADF, was to
identify the data associated with CFD and establish a means of encoding
it within the ADF format. This task was the primary concern of the national
team, with Boeing proposing the standards and the remainder of the team
serving to critique, test, and improve them. This began with the development
of the SIDS and its language. The hierarchical nature of the SIDS was used to
suggest the SIDS-to-ADF File Mapping conventions, which were developed
slightly after the SIDS but along the same track.

Development of an API
~~~~~~~~~~~~~~~~~~~~~

At a review in June 1997, the CGNS team (NASA, Boeing, and McDonnell
Douglas) determined that additional support would be required to
produce an adequate Mid-Level Library. Subcontracts were issued to the
ICEM CFD Engineering Company, in Berkeley, CA, following this
decision. ICEM CFD in effect became the lead organization for the
development of the Mid-Level Library.

Also at this time, the acronym "CGNS" was re-defined to mean "CFD
Generalized Notation System", which was more in keeping with the
evolved goals of this project.

Version 1.0 of the Mid-Level Library, which met the original goal of
supporting structured multi-block analysis codes, was released in
May 1998. This set of higher-level routines enables a user to
implement the CFD standards defined by the SIDS, without specific
knowledge of the File Mapping or the ADF Core. This activity was
crucial to the acceptance and implementation of CGNS among the CFD
community.

NASA and the informal CGNS committee determined that there was no need
for export authority so the CGNS standard, the ADF Core and the
Mid-Level Library, and all supporting documentation could be
distributed worldwide as freeware. Appropriate legal reviews and
approvals were obtained at both NASA and Boeing to validate this
decision.

Demonstration of system capability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Prototypes.**


To test the CGNS data
recording and retrieval mechanisms and to gain experience with the
installation of the software into common applications codes, the
developers modified two CFD solvers (namely, NPARC and TLNS3D) to
operate in the CGNS environment. In addition, NASA Langley Research
Center modified CFL3D similarly. These modifications were made early
in the project and predate the Mid-Level Library and some later
portions of the SIDS.

Separate data cases were prepared for each of the prototypes. Each
prototype proved capable of starting, exiting, and restarting its data
case as expected. In addition, in all three cases, transfer of the
CGNS data between workstation (SGI) and mainframe (CRAY) platforms was
successfully demonstrated.

Dissimilarity of the content of the data required by NPARC and the
other two codes (i.e., nodal vs. cell-centered data) prevented
restarting NPARC from TLNS3D/CFL3D data and vice versa. However, this
type of restart was demonstrated between TLNS3D and CFL3D.

These prototypes were limited in certain ways and, therefore, were not
suitable as a final implementation of their respective capabilities in
CGNS. The principal limitations are:

 - The prototypes implement only the grid coordinates, flow solution,
   boundary condition, and 1-to-1 interface connectivity portions of
   the CGNS data specification.

 - No attempt was made to modify the internal structure of any of the
   codes in order to improve compatibility with CGNS data
   organization.

 - The prototypes accessed the ADF files primarily using routines at
   the ADF Core level. There were some higher-level routines included,
   and these, in many cases, suggested the content of the CGNS
   Mid-Level Libraries. But the high-level prototype routines often
   intermingled ADF functions with CGNS functions and, in some cases,
   were code-specific or dependent on internal directives to make them
   so. They were thus less broadly applicable than the current
   Mid-Level Library routines.

 - These codes exercised only a portion of the CGNS boundary condition
   specifications.

 - The prototypes sometimes incorporated extra nodes into their ADF
   files to carry code-specific data. This practice arose partially
   from the lack of complete CGNS data specifications at the time the
   prototypes were written, but it resulted also, in part, because the
   current code input structure required a different (but equivalent)
   form of the CGNS data, and the developers opted to duplicate it
   within the CGNS database.

The general lesson learned from the construction of the prototypes was
that professional programmers had no conceptual difficulty in
implementing CGNS at the ADF Core level. But the resulting code was
cumbersome, and the development of the Mid-Level Library was needed
to facilitate dissemination of CGNS among those disinclined to work
with the ADF Core.

**System Demonstrator.**

As the CGNS effort progressed, an additional activity was undertaken to
demonstrate the capability of the mature system.
Known as the "system demonstrator", this tested the ability of CGNS to
transfer data seamlessly between applications that had never operated
together before. The system demonstrator used most of that portion of
the currently existing SIDS that has been included in the Mid-Level Library.

The geometry chosen for the test was a high-lift configuration known
as the trapezoidal wing. This is a multielement airfoil with a full-span
slat and flap, and a generic fuselage.

Three separate CGNS-compatible application codes were involved in the
system demonstrator.

  - `GMAN <http://www.grc.nasa.gov/WWW/winddocs/gman/>`_ A
    pre-processor and grid generation tool developed by Boeing
    St. Louis
  - `OVERFLOW
    <http://aaac.larc.nasa.gov/~buning/codes.html#overflow>`_ A CFD
    flow solver developed by NASA Ames
  - `Visual3 <http://www-berkeley.ansys.com/visual3/index.html>`_ A
    flow visualization tool from ICEM CFD, originally developed at MIT

The system demonstrator consisted of the following tasks:

 1. The grid was generated using NASA Ames grid tools and written as a
    Plot3D file.

 2. The grid file was sent to Boeing St. Louis, where it was processed
    by a locally-modified version of GMAN. GMAN calculated the grid
    connectivity information, and wrote the grid and connectivity data
    into a CGNS database. Boundary conditions were also added to the
    CGNS database at this time.

 3. The CGNS file was returned to NASA Ames, where it was read by the
    newly-modified OVERFLOW code. (Some iteration was necessary here,
    because the definition of overset holes used by GMAN differs from
    that normally expected by OVERFLOW. The CGNS file was intact, and
    served, as intended, to highlight the discrepancy.) OVERFLOW
    computed the flow field, writing the results into the CGNS
    database.

  4. The CGNS file was next sent to ICEM CFD. There, the CGNS database
     was read and displayed using Visual3.

The system demonstrator involved significant cross-platform transfer
among various workstation and mainframe computing facilities. The
results indicated that universal data exchange was well supported by
CGNS.

Subsequent Development
~~~~~~~~~~~~~~~~~~~~~~

**Software**

Since the release of Version 1.0 of the CGNS software in May 1998,
several improvements and extensions have been made to the SIDS, the
File Mapping, and the Mid-Level Library.

Version 1.1, released in June 1999, added support for unstructured
grids, and for associating CAD geometric entities with grid surfaces.

Version 2.0, released in December 2000, added support for moving
and/or deforming grids, and for iterative/time-dependent data.

Version 2.1, released in May 2002, added support for user-defined data
arrays, chemistry, and linked nodes.

Version 2.2, released in May 2003, added support for axisymmetry
information, rotating coordinates, special properties associated with
particular grid connectivity patches, such as periodicity or
averaging, special properties associated with particular boundary
condition patches, such as wall functions and bleed, and gravity.

Version 2.3, released in Jan 2004, restored the capability to specify
a boundary condition patch using ElementRange or ElementList.

Version 2.4, released in Aug 2005, added support for describing
electric field, magnetic field, and conductivity models used in
electromagnetic flows, specification of units for electric current,
substance amount, and luminous intensity, more flexible specification
of boundary condition locations, and additional user-defined
data. Also new in Version 2.4 is the ability to choose, at build time,
either ADF or HDF5 external link as the underlying database manager.

Version 2.5, released in Sep 2007, added Mid-Level Library functions
to check file validity, configure some internal CGNS library options,
and provide alternate ways to access a node. Some changes were also
made in the use of functions for partial writes of coordinate,
element, and solution data. Support was also added for building the
CGNS library as a DLL under Windows.  Version 3.1, released in Jan
2011, added 64-bit capabilities, support for both ADF and HDF5
concurrently, and the CGIO interface routines to access these database
managers in a generic fashion.  A more detailed list of revisions
external link to the CGNS software is available at the CGNS web site.
ICEM CFD external link served as the focal point for CGNS software
development through the release of Version 2.0, plus the changes in
Version 2.5, using internal company resources. New features in Version
2.1 and 2.4 were added by Intelligent Light external link, with
funding from NASA Langley. Eagle Aeronautics external link, with
additional participation by ICEM CFD, added the new features in
Version 2.2, again with funding from NASA Langley. Support for HDF as
the underlying database in Version 2.4 was added by personnel from
ONERA external link, ICEM CFD, and the U. S. Air Force Arnold
Engineering Development Center external link.

**Management and Support**

In 1998 NASA announced that the Advanced Subsonic Technology program,
which had funded the initial CGNS development, would end in
September 1999. Several organizations interested in the continued
development of CGNS met in May 1999 to discuss options. The decision
was made to create the CGNS Steering Committee, a voluntary public
forum made up of international representatives from government and
private industry.

The Steering Committee is responsible for coordinating the further
development and dissemination of the CGNS standard and its supporting
software and documentation. In Jan 2000, the CGNS Steering Committee
became a Sub-committee of the AIAA CFD Committee on Standards external
link. Additional details about the mission and responsibilities of the
Steering Committee, and its organization, are in the CGNS Steering
Committee Charter.

The basic CGNS documentation has of course been updated to reflect the
software changes described above. In addition, all the documentation
has been converted to LaTeX (used to create PDF versions for
printing), and to HTML (for interactive use). A new document, A User's
Guide to CGNS, was made available in October 2001, and is very useful
for new and prospective users of the Mid-Level Library.

To encourage communication between CGNS users, a mailing list called
CGNStalk was created in Oct 2000. See :ref:`support` page for more info.

**Standards**

Between 1999 and 2002, an effort was spearheaded by Boeing to
establish an :index:`ISO-STEP <pair: ISO; STEP>` standard for
the representation, storage, and
exchange of digital data in fluid dynamics based on the CGNS
standard. Unfortunately, the effort had to be curtailed because of
budget problems. It was subsequently decided that an existing ISO
standard on finite element solid mechanics would be rewritten and
submitted to include CGNS as well as an integrated engineering
analysis framework.

As part of its role as a sub-committee of the AIAA CFD Committee on
Standards, the CGNS Steering Committee is also involved in the
development of the AIAA Recommended Practice for the storage of CFD
data. The Recommended Practice consists of the CGNS Standard Interface
Data Structures (SIDS) document, reformatted to conform to AIAA's
requirements. The current AIAA Recommended Practice (corresponding to
CGNS Version 2.4) is available at the AIAA Online Store external link,
and as a PDF file (1.01M, 200 pages) at the CGNS Documentation web
site.

Noteworthy Contributions
^^^^^^^^^^^^^^^^^^^^^^^^

The entire CGNS team deserves credit for its accomplishments. The
project might easily be cited as a prime example of effective
voluntary cooperation between government and industry. Every member
has contributed ideas, enthusiasm, and improvements, and enabled us to
represent a cross-section of knowledge and practice from the CFD
community.

It would not be practical to outline each member's contributions to a
project of this complexity. Nevertheless, it is appropriate to note
the contributions of a few individuals who dedicated special effort
during the crucial stages leading to the initial release of CGNS in
May 1998.

 - Steve Allmaras conceived, pursued, and completed the SIDS and
   developed the language in which it is written.

 - Tom Dickens, Matt Smith, and Wayne Jones designed the ADF Core.

 - Tom Dickens wrote the ADF Core.

 - Dan Owen maintained and tuned the ADF Core after Tom left the group.

 - Chuck Keagle designed and executed stringent testing procedures for
   the ADF Core; that is to say, he did everything he could think of
   to break it.

 - Diane Poirier designed and wrote the CGNS Mid-Level Library and
   drafted the original proposals for unstructured grid. She and Alan
   Magnuson drafted the proposals for CAD-to-geometry specifications.

 - Gary Shurtleff wrote the TLNS3D and NPARC prototypes and provided
   us with what was, for a long time, the only examples of working
   CGNS software.

 - Chris Rumsey served as liaison with NASA Langley, responding in
   detail to requests for criticism and improvements and testing the
   system by writing the CFL3D prototype.

 - Cetin Kiris converted the OVERFLOW code to CGNS, twice.

 - Wayne Jones tested our abstractions with real code, which found its
   way into the ADF Mid-Level Library and the CGNS Toolkit.

 - Matt Smith wrote much of the File Mapping and ADF Core documents
   and, with knowledge of both CFD and software design, brought good
   sense to bear on proposals that needed it.

 - Ray Cosner's retrospective vantage point made him a reliable
   supporter who was often able to move things forward when progress
   slowed.

 - Susan Jacob supplied initial guidance as a Productivity+ coach and
   got us all moving in (more or less) the same direction.

 - Doug McCarthy led the project to completion.

 - Shay Gould made the documentation intelligible and presentable.

.. admonition:: And, a particularly special mention

   **Ben Paul** secured the initial funding and shepherded the project
   through the early phases of the contract. We will never forget the
   many meetings Ben held to make sure that he thought that he knew
   that we thought that we knew what we needed to do, and that we were
   doing it. His patience and good-natured perseverance could not have
   been replaced.

.. last line
