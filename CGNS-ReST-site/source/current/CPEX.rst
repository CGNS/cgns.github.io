.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _CPEX:
   
CPEX
====

The CGNS Proposals for Extension (CPEX) is a design document or documents that describe a new feature for CGNS.
The CPEX should provide a concise technical specification of the feature and a rationale for the feature.
The CPEX is intended to be the primary mechanism for proposing new features and for collecting community input on an issue.
The CPEX author is responsible for building consensus within the community and documenting dissenting opinions.

The CPEX editors assign CPEX numbers and change their status.
All CPEX-related email should be sent to cgnstalk@lists.nasa.gov and a CPEX issue should be created on `cgnsorg.atlassian.net <https://cgnsorg.atlassian.net/issues/?jql=project%20%3D%20%22CGNS%22%20AND%20component%20%3D%20%22CPEX%22>`_ to track review and CPEX evolution.
Each CPEX must have a champion - someone who writes the CPEX, shepherds the discussions, and attempts to build community consensus around the idea. The CPEX champion must first try to determine if their idea is appropriate for a CPEX. (Small enhancements or patches may not need a CPEX.) If a CPEX is appropriate, the champion must write a proposal, following the guidelines below. A CPEX number is then assigned. This is typically followed by a period of discussion, comments, input, and consensus-building, as well as an in-depth critical review.
The CGNS Steering Committee ultimately votes for or against adoption.

The proposals listed below that were "not accepted" never made it to implementation, possibly because of lack of unified support, incomplete details, lack of champion involvement in the process, or because they were not generalizable to a wide enough class of problems. It is possible to resurrect and/or revise and resubmit older proposals. Some additional guidelines regarding changes or additions to the CGNS standard can be found in the CGNS Steering Committee Charter.

The CPEX should include the following information:

   - Name(s) and organization(s) of proposer(s)
   - E-mail contact information
   - General description of extension
   - Reason or need for extension
   - Detailed description of extension using similar documentation style found in the SIDS
   - File Mapping description of Node Attributes, following the prescription given in existing `Node Description Documentation <FMMNodeDescriptions>`
   - Specific example(s) of extension

.. note::
  
  **It is possible for a feature to be implemented in the SIDS and Filemap documentation, but not yet be implemented in the MLL software. If/when this occurs, it means that an "official" CGNS file can still be constructed with this feature, but the user must make use of means other than the MLL to accomplish it.**

A primary requirement of all proposals for modifications will be to support and maintain code compatibility.
No additions or changes to the CGNS standard will be adopted - without overwhelmingly compelling reasons - which invalidate existing software or data.

.. note::
  
  CPEX work flow and requirements are new as of 09/2009, so older proposals may be missing some of the required information.

Comments on proposals should be sent to cgnstalk@lists.nasa.gov and/or written directly in the comment section of the jira issue.

.. note::

  The CPEX is loosely patterned after the Python-based PEP (`Python Enhancement Proposal <http://www.python.org/dev/peps/pep-0001/>`_). We gratefully acknowledge their well-documented methodology.



..
  _Comment: Bellow should be listed all CPEX implemented or waiting for review


.. _CPEX0046:

CPEX0046
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0046
  * - Scope
    - Particle Data
  * - Contacts
    - Thomas Hauser
  * - Documentation
    - `CPEX-0046 Particle Data <https://cgnsorg.atlassian.net/browse/CGNS-183>`_
  * - Date First Posted
    - Mar.26.19
  * - Date of Last Revision
    - Mar.26.19
  * - SIDS Status
    - under review
  * - Filemap Status
    - under review
  * - MLL Status
    - under review

.. _CPEX0045:

CPEX0045
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0045
  * - Scope
    - Polynomial Data and Curved Grid Elements
  * - Contacts
    - `Koen Hillewaert <koen.hillewaert@cenaero.be>`_
  * - Documentation
    - `CPEX-0045 High Order <https://cgnsorg.atlassian.net/browse/CGNS-182>`_
  * - Date First Posted
    - Mar.26.19
  * - Date of Last Revision
    - Jun.25.19
  * - SIDS Status
    - accepted; awaiting implementation
  * - Filemap Status
    - accepted; awaiting implementation
  * - MLL Status
    - accepted; awaiting implementation

.. _CPEX0044:

CPEX0044
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0044
  * - Scope
    - Encoding Functions
  * - Contacts
    - `Koen Hillewaert <koen.hillewaert@cenaero.be>`_
  * - Documentation
    - `CPEX-0043 familytrees <https://cgnsorg.atlassian.net/browse/CGNS-181>`_
  * - Date First Posted
    - Mar.26.19
  * - Date of Last Revision
    - Mar.28.19
  * - SIDS Status
    - under review
  * - Filemap Status
    - under review
  * - MLL Status
    - under review


.. _CPEX0043:

CPEX0043
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0043
  * - Scope
    - Family Hierarchy as a Tree
  * - Contacts
    - marc.poinot@safrangroup.com; yoan.collet@numeca.com
  * - Documentation
    - :download:`CPEX-0043-familytrees-v2.pdf <../../proposed_extensions/CPEX-0043-familytrees-v2.pdf>`
  * - Date First Posted
    - Nov.06.18
  * - Date of Last Revision
    - Jun.13.19
  * - SIDS Status
    - implemented version 4.1
  * - Filemap Status
    - implemented version 4.1
  * - MLL Status
    - implemented version 4.1


.. _CPEX0042:

CPEX0042
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0042
  * - Scope
    - Storing the Bounding Box of a Grid
  * - Contacts
    - `Mickael Philit <mickey.phy@gmail.com>`_
  * - Documentation
    - :download:`CPEX-0042-boundingbox-v2.pdf <../../proposed_extensions/CPEX-0042-boundingbox-v2.pdf>`
  * - Date First Posted
    - Nov.06.18
  * - Date of Last Revision
    - May.29.19
  * - SIDS Status
    - implemented version 4.1
  * - Filemap Status
    - implemented version 4.1
  * - MLL Status
    - implemented version 4.1


.. _CPEX0041:

CPEX0041
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0041
  * - Scope
    - NGON Modification Proposals
  * - Contacts
    - `Pierre-Jacques Legay <pierre-jacques.legay@onera.fr>`_
  * - Documentation
    - :download:`NGON-CPEX-0041-v0.16.pdf <../../proposed_extensions/NGON-CPEX-0041-v0.16.pdf>`
  * - Date First Posted
    - May.05.17
  * - Date of Last Revision
    - Sep.15.17
  * - SIDS Status
    - implemented version 4.0
  * - Filemap Status
    - implemented version 4.0
  * - MLL Status
    - implemented version 4.0


.. _CPEX0040:

CPEX0040
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0040
  * - Scope
    - Rind Plane Indexing
  * - Contacts
    - `Stephen Guzik <Stephen.Guzik@colostate.edu>`_
  * - Documentation
    - :download:`rind_plane_indexing_5_14_2015.pdf <../../proposed_extensions/rind_plane_indexing_5_14_2015.pdf>`
  * - Date First Posted
    - May.05.14
  * - Date of Last Revision
    - May.14.15
  * - SIDS Status
    - implemented version 3.4
  * - Filemap Status
    - no change required
  * - MLL Status
    - implemented version 3.4


.. _CPEX0039:

CPEX0039
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0039
  * - Scope
    - Inter-Base Reference Extension
  * - Contacts
    - Marc Poinot
  * - Documentation
    - :download:`CGNS-0039-Inter-Base-References1.pdf <../../proposed_extensions/CGNS-0039-Inter-Base-References1.pdf>`
  * - Date First Posted
    - Jan.07.14
  * - Date of Last Revision
    - Jan.10.14
  * - SIDS Status
    - implemented version 3.3
  * - Filemap Status
    - no change required
  * - MLL Status
    - implemented version 3.3


.. _CPEX0038:

CPEX0038
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0038
  * - Scope
    - Quartic Elements for High Order
  * - Contacts
    - Meilin Yu and Z. J. Wang
  * - Documentation
    - :download:`CGNS_P4_elem_defn2.pdf <../../proposed_extensions/CGNS_P4_elem_defn2.pdf>`
  * - Date First Posted
    - Aug.08.13
  * - Date of Last Revision
    - Sep.10.13
  * - SIDS Status
    - implemented version 3.3
  * - Filemap Status
    - no change required
  * - MLL Status
    - implemented version 3.3


.. _CPEX0037:

CPEX0037
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0037
  * - Scope
    - Improvements for Multiblock Unstructured
  * - Contacts
    - Micah Howard and Srini Arunajatesan
  * - Documentation
    - :download:`README.improv_mblk_uns.txt <../../proposed_extensions/README.improv_mblk_uns.txt>`
      :download:`CGNS-MultiBlockUnst.pdf <../../proposed_extensions/CGNS-MultiBlockUnst.pdf>`
      :download:`bump_3df_unstr_native_pw.cgns <../../proposed_extensions/bump_3df_unstr_native_pw.cgns>`
      :download:`bump_3df_unstr.cgns <../../proposed_extensions/bump_3df_unstr.cgns>`
      :download:`bump_3df_hybrid.cgns <../../proposed_extensions/bump_3df_hybrid.cgns>`
  * - Date First Posted
    - May.05.00
  * - Date of Last Revision
    - Sep.15.00
  * - SIDS Status
    - current version not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0036:

CPEX0036
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0036
  * - Scope
    - Cubic Elements for High Order
  * - Contacts
    - Meilin Yu and Z. J. Wang
  * - Documentation
    - :download:`CGNS_extended_elem_defn2.pdf <../../proposed_extensions/CGNS_extended_elem_defn2.pdf>`
  * - Date First Posted
    - Nov.05.12
  * - Date of Last Revision
    - Nov.13.12
  * - SIDS Status
    - implemented version 3.2
  * - Filemap Status
    - no changed required
  * - MLL Status
    - implemented version 3.2


.. _CPEX0035:

CPEX0035
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0035
  * - Scope
    - Rigid Motion in a Family (requires CPEX #0034)
  * - Contacts
    - Marc Poinot
  * - Documentation
    - :download:`CGNS-prop-ext-FamilyRigidMotion-5.pdf <../../proposed_extensions/CGNS-prop-ext-FamilyRigidMotion-5.pdf>`
  * - Date First Posted
    - Feb.07.11
  * - Date of Last Revision
    - Feb.07.11
  * - SIDS Status
    - Current version not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0034:

CPEX0034
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0034
  * - Scope
    - Multiple Families
  * - Contacts
    - Marc Poinot
  * - Documentation
    - :download:`CGNS-0034-6.pdf <../../proposed_extensions/CGNS-0034-6.pdf>`
      (Note: AdditionalFamilyName also to be added under UserDefinedData)
  * - Date First Posted
    - Feb.03.11
  * - Date of Last Revision
    - Nov.16.11
  * - SIDS Status
    - implemented version 3.2
  * - Filemap Status
    - implemented version 3.2
  * - MLL Status
    - implemented version 3.2


.. _CPEX0033:

CPEX0033
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0033
  * - Scope
    - Hierarchy of Families
  * - Contacts
    - Marc Poinot
  * - Documentation
    - :download:`CGNS-0033-6.pdf <../../proposed_extensions/CGNS-0033-6.pdf>`
  * - Date First Posted
    - Feb.03.11
  * - Date of Last Revision
    - Nov.16.11
  * - SIDS Status
    - implemented version 3.2
  * - Filemap Status
    - implemented version 3.2
  * - MLL Status
    - implemented version 3.2


.. _CPEX0032:

CPEX0032
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0032
  * - Scope
    - Rigid Motion Improvement
  * - Contacts
    - Marc Poinot
  * - Documentation
    - :download:`IterativeData.pdf <../../proposed_extensions/IterativeData.pdf>`
      :download:`FrameReference.pdf <../../proposed_extensions/FrameReference.pdf>`
      :download:`FamilyRigidMotion.pdf <../../proposed_extensions/FamilyRigidMotion.pdf>`
      :download:`RigidMotion.pdf <../../proposed_extensions/RigidMotion.pdf>`
  * - Date First Posted
    - Jul.01.08
  * - Date of Last Revision
    - Oct.07.08
  * - SIDS Status
    - withdrawn
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0031:

CPEX0031
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0031
  * - Scope
    - General SIDS Improvement
  * - Contacts
    - Steven Allmaras
  * - Documentation
    - :download:`intro_parts_of_sids.pdf <../../proposed_extensions/intro_parts_of_sids.pdf>`
      :download:`parts_of_sids.pdf <../../proposed_extensions/parts_of_sids.pdf>`
  * - Date First Posted
    - Jun.09.08
  * - Date of Last Revision
    - Jun.09.08
  * - SIDS Status
    - implemented version 3.1.3
  * - Filemap Status
    - implemented version 3.1.3
  * - MLL Status
    - implemented version 3.1.3


.. _CPEX0030:

CPEX0030
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0030
  * - Scope
    - Regions
  * - Contacts
    - Chris Rumsey, Marc Poinot, Bob Bush, Mark Fisher, Steven Allmaras
  * - Documentation
    - :download:`Regions.pdf <../../proposed_extensions/Regions.pdf>`
      :download:`Regions_filemap.pdf <../../proposed_extensions/Regions_filemap.pdf>`
  * - Date First Posted
    - Nov.09.06
  * - Date of Last Revision
    - May.29.11
  * - SIDS Status
    - implemented version 3.1.3
  * - Filemap Status
    - implemented version 3.1.3
  * - MLL Status
    - implemented version 3.1.3


.. _CPEX0029:

CPEX0029
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0029
  * - Scope
    - Interface Connectivity
  * - Contacts
    - Chris Rumsey
  * - Documentation
    - :download:`InterpolantDonor.pdf <../../proposed_extensions/InterpolantDonor.pdf>`
  * - Date First Posted
    - Apr.13.07
  * - Date of Last Revision
    - May.22.07
  * - SIDS Status
    - implemented version 2.5
  * - Filemap Status
    - implemented version 2.5
  * - MLL Status
    - implemented version 2.5


.. _CPEX0028:

CPEX0028
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0028
  * - Scope
    - Face-Based Storage
  * - Contacts
    - Steve Allmaras
  * - Documentation
    - :download:`FacebasedIntro.pdf <../../proposed_extensions/FacebasedIntro.pdf>`
      :download:`FacebasedSIDS.pdf <../../proposed_extensions/FacebasedSIDS.pdf>`
  * - Date First Posted
    - Nov.09.06
  * - Date of Last Revision
    - Nov.09.06
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0027:

CPEX0027
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0027
  * - Scope
    - Multiple Zone Connectivities for Time-Dependent
  * - Contacts
    - Christopher Rumsey, Robert Bush
  * - Documentation
    - :download:`Timedepconn.pdf <../../proposed_extensions/Timedepconn.pdf>`
      :download:`Timedepconn_filemap.pdf <../../proposed_extensions/Timedepconn_filemap.pdf>`
  * - Date First Posted
    - Mar.08.06
  * - Date of Last Revision
    - Mar.08.06
  * - SIDS Status
    - implemented version 3.1.3
  * - Filemap Status
    - implemented version 3.1.3
  * - MLL Status
    - implemented version 3.1.3


.. _CPEX0026:

CPEX0026
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0026
  * - Scope
    - Face Center Connectivity
  * - Contacts
    - Laurent de Vito
  * - Documentation
    - :download:`Facecenter.pdf <../../proposed_extensions/Facecenter.pdf>`
  * - Date First Posted
    - Mar.08.06
  * - Date of Last Revision
    - Mar.08.06
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0025:

CPEX0025
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0025
  * - Scope
    - Averaging Interfaces
  * - Contacts
    - Robert Magnan
  * - Documentation
    - :download:`AveragingInterfaces.pdf <../../proposed_extensions/AveragingInterfaces.pdf>`
  * - Date First Posted
    - Mar.28.06
  * - Date of Last Revision
    - Mar.28.06
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0024:

CPEX0024
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0024
  * - Scope
    - FSI with Deformable Boundaries
  * - Contacts
    - Daniel Einstein
  * - Documentation
    - :download:`FSIDeformableBdy.pdf <../../proposed_extensions/FSIDeformableBdy.pdf>`
  * - Date First Posted
    - Dec.17.03
  * - Date of Last Revision
    - Dec.17.03
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0023:

CPEX0023
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0023
  * - Scope
    - Rind Data for Unstructured Zones
  * - Contacts
    - Robert A. Fiedler
  * - Documentation
    - :download:`UnstructuredRind.pdf <../../proposed_extensions/UnstructuredRind.pdf>`
  * - Date First Posted
    - Dec.15.03
  * - Date of Last Revision
    - Dec.15.03
  * - SIDS Status
    - implemented version 2.4.3
  * - Filemap Status
    - implemented version 2.4.3
  * - MLL Status
    - implemented version 2.4.3


.. _CPEX0022:

CPEX0022
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0022
  * - Scope
    - Partial Connectivity Read/Write
  * - Contacts
    - Edwin van der Weide
  * - Documentation
    - :download:`PartialConn.pdf <../../proposed_extensions/PartialConn.pdf>`
  * - Date First Posted
    - Sep.25.03
  * - Date of Last Revision
    - Sep.25.03
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0021:

CPEX0021
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0021
  * - Scope
    - Connectivity Property
  * - Contacts
    - Edwin van der Weide
  * - Documentation
    - :download:`GridConnectivityProperty.pdf <../../proposed_extensions/GridConnectivityProperty.pdf>`
  * - Date First Posted
    - Sep.25.03
  * - Date of Last Revision
    - Sep.25.03
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0020:

CPEX0020
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0020
  * - Scope
    - FamilyBC Extension
  * - Contacts
    - Edwin van der Weide
  * - Documentation
    - :download:`FamilyBCExtension.pdf <../../proposed_extensions/FamilyBCExtension.pdf>`
  * - Date First Posted
    - Apr.21.03
  * - Date of Last Revision
    - Apr.21.03
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0019:

CPEX0019
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0019
  * - Scope
    - UserDefined data Extension
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`UserDefinedExtensions.pdf <../../proposed_extensions/UserDefinedExtensions.pdf>`
  * - Date First Posted
    - Apr.21.03
  * - Date of Last Revision
    - Apr.21.03
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0018:

CPEX0018
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0018
  * - Scope
    - BCDataSet Extension
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`BCDataSetExtensions.pdf <../../proposed_extensions/BCDataSetExtensions.pdf>`
  * - Date First Posted
    - May.05.00
  * - Date of Last Revision
    - Sep.15.00
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0017:

CPEX0017
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0017
  * - Scope
    - Chemical Species
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`ChemicalSpecies.pdf <../../proposed_extensions/ChemicalSpecies.pdf>`
  * - Date First Posted
    - Oct.25.02
  * - Date of Last Revision
    - Oct.25.02
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0016:

CPEX0016
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0016
  * - Scope
    - Element Regions
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`ElementRegions.pdf <../../proposed_extensions/ElementRegions.pdf>`
  * - Date First Posted
    - Oct.25.02
  * - Date of Last Revision
    - Oct.25.02
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0015:

CPEX0015
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0015
  * - Scope
    - Elemental Components
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`ElementalComponents.pdf <../../proposed_extensions/ElementalComponents.pdf>`
  * - Date First Posted
    - Oct.25.02
  * - Date of Last Revision
    - Oct.25.02
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0014:

CPEX0014
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0014
  * - Scope
    - Boundary Type Extensions
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`BCTypeExtensions.pdf <../../proposed_extensions/BCTypeExtensions.pdf>`
  * - Date First Posted
    - Oct.25.02
  * - Date of Last Revision
    - Oct.25.02
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0013:

CPEX0013
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0013
  * - Scope
    - Solution BC proposal
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`SolutionBCproposal.pdf <../../proposed_extensions/SolutionBCproposal.pdf>`
  * - Date First Posted
    - Jul.03.02
  * - Date of Last Revision
    - Jul.03.02
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0012:

CPEX0012
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0012
  * - Scope
    - Electromagnetic proposal
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`EMproposals.pdf <../../proposed_extensions/EMproposals.pdf>`
  * - Date First Posted
    - Jul.03.02
  * - Date of Last Revision
    - Jul.03.02
  * - SIDS Status
    - implemented version 2.4
  * - Filemap Status
    - implemented version 2.4
  * - MLL Status
    - implemented version 2.4


.. _CPEX0011:

CPEX0011
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0011
  * - Scope
    - Wall Function, Periodic, Rotor/Stator
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`WallPeriodicRS.pdf <../../proposed_extensions/WallPeriodicRS.pdf>`
  * - Date First Posted
    - Jul.01.02
  * - Date of Last Revision
    - Jul.31.02
  * - SIDS Status
    - implemented version 2.2
  * - Filemap Status
    - implemented version 2.2
  * - MLL Status
    - implemented version 2.2


.. _CPEX0010:

CPEX0010
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0010
  * - Scope
    - Multi-Phase / Liquid Spray
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`MultiPhaseExtension.pdf <../../proposed_extensions/MultiPhaseExtension.pdf>`
  * - Date First Posted
    - Dec.01.00
  * - Date of Last Revision
    - Dec.14.00
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0009:

CPEX0009
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0009
  * - Scope
    - User Defined Data Arrays
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`UserDefinedDataArrays2.pdf <../../proposed_extensions/UserDefinedDataArrays2.pdf>`
  * - Date First Posted
    - Nov.15.00 
  * - Date of Last Revision
    - Feb.02.01
  * - SIDS Status
    - implemented version 2.1
  * - Filemap Status
    - implemented version 2.1
  * - MLL Status
    - implemented version 2.1


.. _CPEX0008:

CPEX0008
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0008
  * - Scope
    - Hierarchical Elements
  * - Contacts
    - Michel Delanaye, Etienne Robin, Alpesh Patel
  * - Documentation
    - :download:`HierarchicalElements.pdf <../../proposed_extensions/HierarchicalElements.pdf>` , Response from M.Aftosmis: :download:`hierarchicalResponse.pdf <../../proposed_extensions/hierarchicalResponse.pdf>`
  * - Date First Posted
    - Aug.02.00
  * - Date of Last Revision
    - Dec.01.00
  * - SIDS Status
    - not accepted
  * - Filemap Status
    - N/A
  * - MLL Status
    - N/A


.. _CPEX0007:

CPEX0007
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0007
  * - Scope
    - Gravity
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`Gravity.pdf <../../proposed_extensions/Gravity.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Mar.15.00
  * - SIDS Status
    - implemented version 2.2
  * - Filemap Status
    - implemented version 2.2
  * - MLL Status
    - implemented version 2.2


.. _CPEX0006:

CPEX0006
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0006
  * - Scope
    - Rotating Coordinates
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`RotatingCoordinates.pdf <../../proposed_extensions/RotatingCoordinates.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Dec.09.99
  * - SIDS Status
    - implemented version 2.2
  * - Filemap Status
    - implemented version 2.2
  * - MLL Status
    - implemented version 2.2


.. _CPEX0005:

CPEX0005
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0005
  * - Scope
    - Axisymmetry for 2D grids
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`axisymmetry.pdf <../../proposed_extensions/axisymmetry.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Mar.15.00
  * - SIDS Status
    - implemented version 2.2
  * - Filemap Status
    - implemented version 2.2
  * - MLL Status
    - implemented version 2.2


.. _CPEX0004:

CPEX0004
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0004
  * - Scope
    - Chemical Species
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`Chemistry.pdf <../../proposed_extensions/Chemistry.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Sep.15.00
  * - SIDS Status
    - implemented
  * - Filemap Status
    - implemented
  * - MLL Status
    - implemented


.. _CPEX0003:

CPEX0003
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0003
  * - Scope
    - Iterative or Time-accurate data
  * - Contacts
    - Christopher Rumsey, Robert Bush, Mark Fisher
  * - Documentation
    - :download:`IterativeOrTemp.pdf <../../proposed_extensions/IterativeOrTemp.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Mar.14.00
  * - SIDS Status
    - implemented
  * - Filemap Status
    - implemented
  * - MLL Status
    - implemented


.. _CPEX0002:

CPEX0002
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0002
  * - Scope
    - Point by Point Grid Motion
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`ArbitraryGridMotion.pdf <../../proposed_extensions/ArbitraryGridMotion.pdf>` , :download:`see example 1 <../../proposed_extensions/Example_Motion.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Mar.14.00
  * - SIDS Status
    - implemented
  * - Filemap Status
    - implemented
  * - MLL Status
    - implemented


.. _CPEX0001:

CPEX0001
--------

.. list-table::
  :stub-columns: 1

  * - CPEX#
    - 0001
  * - Scope
    - Rigid Body Grid Motion
  * - Contacts
    - Robert Bush
  * - Documentation
    - :download:`RigidGridMotion.pdf <../../proposed_extensions/RigidGridMotion.pdf>` , :download:`see example 1 <../../proposed_extensions/Example_Motion.pdf>`
  * - Date First Posted
    - Aug.04.99
  * - Date of Last Revision
    - Mar.14.00
  * - SIDS Status
    - implemented
  * - Filemap Status
    - implemented
  * - MLL Status
    - implemented



.. last line
