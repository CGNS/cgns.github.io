.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _YeMightySteeringCommittee:

Steering Committee
==================

The CGNS Steering Committee is a public forum made up of international
representatives from government and private industry,
responsible for the development, evolution, support,
and promotion of the CGNS.

Background
----------

History
+++++++

In the early 1980s, the PLOT3D data format gained acceptance as a de
facto standard to enable the storage and exchange of CFD data within
analysis processes, and among collaborating organizations. This
initial CFD data standard today continues to be the most common
storage and exchange standard for CFD data, based on structured grids.

However, by the early 1990s several limitations in the PLOT3D standard
had become apparent. Individual organizations were overcoming these
limitations by defining extensions to the PLOT3D standard to meet
their needs. These extensions were not coordinated among different
organizations, and therefore data stored in these extended formats
generally could not be utilized outside the originating
organization. Further, the PLOT3D standard had not anticipated several
key trends in CFD technology, such as unstructured grids, turbulence
models based on solutions of partial differential equations, and the
need to include chemical species concentrations as part of a CFD
solution. Also, the PLOT3D format, which was originally developed
simply to expedite post-processing (visualization) did not include
self-documenting features. Therefore, it was necessary to rely on
file-naming conventions or external notes to maintain awareness of the
flow conditions and analyzed geometry of each PLOT3D data file.

The CGNS Data Standard was initially conceived in 1994 by NASA, Boeing
external link, and then-McDonnell Douglas teams working under the
Integrated Wing Design element of NASA's Advanced Subsonic Technology
Program. The objective of this work was to greatly reduce the time
required to design a transport wing. Implicit in this goal was
increased extensive use of Computational Fluid Dynamics (CFD) and the
possibility of collaborative analyses by many organizations.

To achieve this vision, it was necessary to establish a common data
format suitable to meet the needs of production CFD tools in the mid-
to late-1990s. This format would be used to enable interchange of data
among different CFD-related tools and different computing platforms,
and to provide a mechanism for archive and retrieval of CFD data. The
chief tools that were taken into consideration for this goal were two
structured-grid multi-block codes, OVERFLOW and TLNS3D. The available
data standard, the PLOT3D format, was increasingly proving to be
inadequate for this purpose. Some of these shortcomings included:

Requirement to read the entire file to retrieve any data.  No
provision for multi-block connectivity data.  Requirement to convert
to ASCII format to transfer data between dissimilar computing
platforms.  Lack of self-documentation; descriptive information must
be separately maintained outside the data file.  Several database
options were considered by the NASA / Boeing / McDonnell Douglas team
during the period December 1994 to March 1995. In March 1995, a
decision was taken to build a new data standard called CGNS (Complex
Geometry Navier Stokes). This standard was a "clean sheet"
development, but it was heavily influenced by the McDonnell Douglas
Common File Format (CFF) external link standard, which had been
established and deployed in 1989 and significantly revised in 1992.

It should be noted that the CGNS data standard consists of two major elements:

Data Content and Format The definition of the intellectual
content of the data to be represented in this standard, and the format
of the representation in the standard-conforming data file.
Implementing Software Software packages developed to ease the process
of establishing CGNS-compliant database references within an
applications code.  In accepted standards contexts such as ISO / STEP,
the "standard" consists only of the first item, a definition of the
data content and format. In this regard, the CGNS development team
went beyond the traditional role in setting standards, by also
developing software to easily implement the standard in a code. The
implementing software, in turn, was developed in two layers:

Low-level routines to perform elementary operations on the database,
known as the ADF (Advanced Data Format) Library. This low-level ADF
library performs basic direct I/O operations on the file. It does not
have any built-in knowledge of the data structure or the content of
the data. The user must provide this knowledge; thus, a user who
writes ADF calls must have a complete understanding of the CGNS data
structures and content.

When CGNS Version 2.4 was released, support for HDF5 (Hierarchical
Data Format) as the underlying database was added. The ADF routines
were "mapped" to equivalent HDF5 routines, and the Mid-Level Library
could be built using either ADF or HDF5.

With the release of CGNS Version 3.1, new low-level routines were
created (the CGIO interface) as a replacement for the direct ADF
calls. This interface supports both ADF and HDF5 simultaneously and
transparently to the application code.

Higher-level routines to perform common operations required by a CFD
code, known as the CGNS Mid-Level Library. The CGNS Mid-Level Library
is an Application Programming Interface (API) that allows the use of
CGNS data files without any knowledge of the underlying data
structures and file format. The person who writes code using this
mid-level library needs only to have a general understanding of the
standard data structure and content. The purpose of the mid-level
library is to shield the user from the complexity of the basic
database manager calls, and to ensure that the data are written in the
proper structure to create a CGNS-compliant file.  The data standards
are controlled by two documents, which are available at the CGNS
Documentation Home Page. These key control documents are:

Standard Interface Data Structures (SIDS)
SIDS File Mapping Manual
The ADF library was developed during 1995, and the first large-scale deployment was made by (then) McDonnell Douglas - St. Louis in November 1995, as part of an upgrade to the Common File Format system. During 1995-97, the NASA - Boeing - McDonnell Douglas team focused on adding content to the control documents, and laying out the requirements of the mid-level library.

At a review in June 1997, the CGNS team (NASA, Boeing, and McDonnell
Douglas) determined that additional professional support would be
required to produce an adequate mid-level library. Subcontracts were
issued to the ICEM CFD Engineering Company external link, in Berkeley,
CA, following this decision. ICEM CFD Engineering in effect became the
lead organization for the development of the mid-level library. At
this time, the acronym "CGNS" was re-defined to mean "CFD General
Notation System", which was more in keeping with the evolved goals of
this project.

An initial mid-level software library (version 1.0), which met the
original goals of structured multi-block analysis codes, was released
in May 1998. At this time, a decision also was taken whereby NASA and
Boeing (McDonnell Douglas by this time had been absorbed by Boeing)
would relinquish all rights to ICEM CFD Engineering. Concurrently,
NASA and the informal CGNS committee determined that there was no need
for export authority, so the CGNS standard, the ADF and mid-level
library, and all supporting documentation could be distributed
worldwide as freeware. Appropriate legal reviews and approvals were
obtained at both NASA and Boeing to validate this decision.

At meetings in March, May, and October 1998, the mid-level library was
extended to support a wide range of unstructured grid types. The SIDS
document defining the standard was modified, and extended versions of
the mid-level library were released at intervals in late 1998 and
early 1999. By May 1999, the extension to unstructured grids was
released.

Management
++++++++++

Up to this time, all activities related to the development of the
standard, the implementing software, and the related documentation had
been coordinated and largely funded by NASA under the Advanced
Subsonic Technology Program. In 1998, NASA took a decision that the
Advanced Subsonic Technology program would end on September 30, 1999,
which was approximately one year earlier than their original
plan. Further, NASA indicated that they would not be able to manage
the development of a standard or a software system such as CGNS, once
it ceased to be the focus of an ongoing NASA program.

At this time, a number of U.S. and international organizations had
established plans to use the CGNS standard and the ADF and mid-level
library, and in several cases they had begun implementation. These
organizations had a clear interest in the existence of an organization
to coordinate future use and extensions of the CGNS standard and its
supporting software and documentation. Also during this same period
(1998-99), The Boeing Company launched an initiative to establish an
ISO standard for aerodynamic data, to be based on the CGNS
standard. However, in a best-case scenario CGNS will not become an ISO
standard until roughly 2005-2006, and acceptance of CGNS as an ISO
standard is not a certainty. It became clear that CGNS needed to find
an organizational home, to coordinate its extension and utilization.

The organizations interested in the CGNS standard met in Hampton, VA,
on May 20, 1999 to discuss options for a CGNS management
organization. Out of this meeting, the CGNS Steering Committee was
established. This Steering Committee is a voluntary organization to
coordinate the further development and dissemination of the CGNS
standard and its supporting software and documentation. In January
2000, the CGNS Steering Committee became an official subcommittee
under the purview of the American Institute of Aeronautics and
Astronautics (AIAA) Committee on Standards. The AIAA also distributes
the CGNS SIDS document as an AIAA Recommended Practice. However, this
AIAA affiliation does not preclude the CGNS committee from public
dissemination of the SIDS and other CGNS documentation.

The following sections of this document present the vision of how the
CGNS Steering Committee will operate.


Mission/Vision/Responsibilities
-------------------------------

Ensure the maintenance of the existing software, documentation and web
site Provide mechanisms for the evolution of the standard Promote the
acceptance of CGNS Provide mechanism for answering questions and
exchanging ideas Determine the means by which the CGNS activities are
supported The mission of the CGNS Steering Committee is to ensure the
continuation of the CFD General Notation System. The survival of a
standard depends entirely on its level of use. Therefore the CGNS
Steering Committee must aim at providing a standard that is widely
accepted by the CFD community.

Several elements must be satisfied to ensure the acceptance of the
CGNS standard. The most obvious asset is that CGNS must be useful. Not
only must it answer the current needs for the recording of fluid
dynamics data, but it must also follow the changes in requirements as
CFD progresses. A second important element is that CGNS must be easy
to implement. The CGNS Mid-Level Library (or Application Programming
Interface, API) must be user-friendly and well documented, and online
support must be available for all users at all times. The standard
must also be easily accessible, meaning that all the sources,
binaries, documents and any other pertinent information must be
available to anyone without restrictions. Finally, it is of utmost
importance that CGNS retains its public nature, encouraging
contributions from all users.

The Steering Committee has the responsibility to oversee that the CGNS
standard remains useful, accessible, easy to use, and preserves its
public nature. This implies multiple activities, which can be
subdivided in the following groups:

Ensure the maintenance of the existing software, documentation and web
site The CGNS Steering Committee is responsible for appointing a prime
source, and overseeing the prime source activities. The Steering
Committee must ensure that the prime source maintains the existing
software, documentation and web site. This includes, but is not
limited to:

correcting/updating the documentation if necessary fixing any reported
software bug collecting a list of CGNS users via the web site keeping
the web site up to date with the latest versions of the documentation
and software informing the user base of new releases and major
software problems posting proposals for new features or modifications
to the CGNS standard on the web site and collect comments from the
user base maintaining a distribution site for contributed software
utilities which utilize the CGNS standard Provide mechanisms for the
evolution of the standard The CGNS Steering Committee has the
responsibility to support and even encourage the evolution of the
standard in order for CGNS to remain useful. Therefore, the committee
must solicit technical support and "in-kind" contributions. In
addition, the Steering Committee must follow the policies described in
the section of this document on Changes or Additions to the Standard
regarding the collection and evaluation of technical proposals.

Promote the acceptance of CGNS The CGNS Steering Committee has the
responsibility to promote the acceptance of CGNS throughout the CFD
community. This can be achieved through various means, including word
of mouth, advertising, business articles, and presentations at
conferences and technical meetings.

Provide mechanism for answering questions and exchanging ideas
Electronic mail constitutes the main point of contact between CGNS
users and CGNS developers. Therefore, the CGNS Steering Committee must
maintain an electronic mail forum, to which users can post questions,
answer questions, and exchange ideas. Members of the CGNS Steering
Committee and/or appointed qualified persons will respond to the
posted questions on the forum.

Determine the means by which the CGNS activities are supported The
CGNS Steering Committee has the obligation to determine the means by
which all CGNS activities are supported. The Committee is also
responsible for identifying and obtaining sources of funding, if
appropriate. Finally the CGNS Steering Committee has the
responsibility to distribute the tasks and funds to the most
appropriate candidate, in the best interests of CGNS.

Organization/Bylaws
-------------------

Representation Standing Committees Software and Documentation Support
Team The CGNS Steering Committee is a voluntary organization that will
determine its own policies and internal structure, and will govern by
consensus whenever possible. In the absence of consensus, a two-thirds
majority of the Committee members will be required to adopt changes to
the standard, alter this Charter, or take other official actions.

The CGNS Steering Committee will meet at a minimum of one time per
year. The time and location will be determined by consensus of the
Committee, and all members of the Committee will be notified in
advance.

The members of the CGNS Steering Committee will appoint a Chairperson
whose responsibilities will include coordinating activities,
facilitating meetings and serving as a focal point for the
Committee. The Chairperson will be a member of the Committee, be
elected by consensus, and serve for a two-year term. There is no limit
on how many terms the Chairperson can be elected. At the discretion of
the Chairperson, a Vice-Chairperson may be appointed by consensus of
the Committee, to assist the Chairperson with his or her duties. The
Vice-Chairperson will also be a member of the Committee. The
appointment of a secretary to maintain records will be at the
discretion of the Chairperson.

The CGNS Steering Committee may decide to suggest appropriate
contributions from its members. The Steering Committee is not
prohibited from charging membership fees; the decision whether to do
so, and the amount of the fees, lies within the purview of the
Steering Committee.

All parties are welcome to bring forward issues and participate in
development of the CGNS Standard, whether or not they are members of
the Steering Committee.

The decision whether to support the migration of the CGNS standard to
ISO/STEP, or any other organization, lies within the purview of the
Steering Committee.

Representation The CGNS Steering Committee will be made up of
representatives from specific institutions, rather than
individuals. Changes or additions to Steering Committee membership
will be based on potential contribution to the standard. Membership on
the Steering Committee will be limited to 30 institutions that
actively participate in the development, maintenance, distribution and
use of the CGNS Standard. No more than 5 institutions may be related,
i.e., have the same parent organization. Changes to the Membership
(including the limit on the number of institutions) will be determined
by consensus, or if required, a two-thirds majority of the existing
Membership.

To help satisfy the duties of the Steering Committee as a whole, the
minimal responsibilities of each individual Steering Committee member
are to:

Attend as many telecons/meetings as possible, but not less than one
per year Read and send comments on proposals or other issues when
asked to do so Vote when asked to do so More active participation -
including support, software development, and actively working to
improve and promote CGNS - is encouraged.  Standing Committees The
CGNS Steering Committee may constitute Standing Committees, in an
ongoing or temporary basis, to which it may delegate various
responsibilities. The Standing Committees will report and make
recommendations to the Steering Committee who will retain the
authority to act and make final decisions.

Software and Documentation Support Team The CGNS Steering Committee
will be responsible for selecting one or more organizations to
maintain and distribute existing documentation and software, to
develop and distribute new software resulting from extensions to the
standard, and to post or distribute meeting minutes and other new
documentation.

The organization(s) selected to maintain CGNS software will determine
the form of newly developed software and maintain compatibility with
the existing ADF Core and CGNS API.

The organization(s) selected to maintain CGNS Documentation will be
responsible for posting and maintaining on the web the Steering
Committee meeting minutes, Charter, and archive information.

Standard and Software Governing Principles
------------------------------------------

Distribution
^^^^^^^^^^^^

This section describes the policy governing the distribution of the CGNS
standard and software to the engineering and scientific community at
large. By definition, the CGNS standard refers to the Standard
Interface Data Structures (SIDS) definitions, the SIDS File Mapping,
and the CGNS Mid-Level Library structure (API), as well as all
documentation. The CGNS software refers to the CGNS Library source
code, the CGIO core routines, and the ADF and HDF5 database manager
implementations. The CGNS software may also include sample programs
demonstrating the application and use of the CGNS and ADF libraries,
as well as some utility programs to assist with the implementation and
analysis of CGNS-based files and systems.

Implementation and maintenance of the CGNS distribution policy is the
responsibility of the CGNS Steering Committee. The distribution policy
dictates that both the CGNS standard and the CGNS software are
publicly available, and that the standard and software itself are free
of charge. The CGNS software may be used for any purpose, including
commercial applications, and may be altered and redistributed, subject
to the restrictions described in the CGNS License.

It is the responsibility of the CGNS Steering Committee to enable
distribution mechanisms that comply with the following principles:

The CGNS standard (documentation and definitions) will be publicly
available at no more than the cost of distribution.  The CGNS software
(CGNS Library and CGIO, ADF and HDF5 core), including source code,
will also be available at no more than the cost of distribution.  The
CGNS API (Mid-Level Library), including source code will be similarly
available.  Development, sale, and licensing of proprietary packages
based on CGNS that perform substantive operations on the data, beyond
the I/O performed by the API, are encouraged. Such packages must abide
by the restrictions described in the CGNS License.  The sale of
services designed to assist in the conversion of existing software to
the CGNS standard is acceptable.  The voluntary contribution of
software that performs operations on CGNS data is encouraged.  The
CGNS Steering Committee will provide mechanisms for the accumulation
and distribution of contributed software, but will not be responsible
for the function of contributed software.  Contributed software does
not become part of the CGNS Standard, that is, either the SIDS or the
API, without the approval of the CGNS Steering Committee.  The
Steering Committee may agree to support or endorse additional utility
software.  The Steering Committee will not endorse third party
software.

Changes or Additions to the Standard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CGNS is a standard that has been developed with the key concepts of flexibility and
extendibility in mind. The standard can accommodate the majority of
CFD data quantities in practical usage today; however, some additional
capabilities are still being implemented. It is also understood that
in the future other additional capabilities will need to be
implemented as well. For these reasons, a process for adding to or
modifying the existing CGNS standard is necessary.

To address a particular need or deficiency in CGNS, a proposal for a
potential change to the standard first must be made. A Technical Team
will prepare all proposals. A Technical Team may voluntarily submit
the proposal, or a Technical Team may be specifically appointed by the
Steering Committee to author the proposal.

A primary requirement of all proposals for modifications will be to
support and maintain code compatibility. No additions or changes to
the CGNS standard will be adopted which invalidate existing software
or data.

Prior to adoption, the Technical Team must present all proposals in an
open and public forum. Included with the proposal, a draft of the
necessary changes to the SIDS and File Mapping must be provided by the
team introducing the modifications. The open forum will then review
the proposal, identify any possible shortcomings, and suggest
alternatives or improvements.

After the proposal has been presented and deliberated upon, only the
Steering Committee has final authority of approval and may elect to do
one of three things. First, the Steering Committee may vote by
consensus (or a two-thirds majority if necessary) to accept the
proposal as is, and thus the changes are approved for
implementation. If such approval does not occur, the Steering
Committee may still feel there is merit to the proposal, and may
choose to defer acceptance of the proposal under the provision that
specific changes be made. Finally, the Steering Committee may deem
there is little merit in the proposed changes to CGNS, and reserves
the right to reject the proposal outright. Whatever the disposition of
the proposal, individual organizations may implement UserDefined
functions, provided that they adhere to the conventions and standards
as defined in the SIDS.

Please read the :ref:`CGNS License terms <CGNSLicense>`.

.. last line
