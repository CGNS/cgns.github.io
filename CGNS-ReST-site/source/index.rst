.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. CGNS documentation master files
   04/2020 - (marc.poinot@safrangroup.com)
             start Markdown translation and change layout, see how pages
	     are changed/moved in the MIGRATION.txt file
	     See governance/support about this web site migration

.. IGNORE warning message produced by the image directive below	     
.. image:: /images/logo/CGNS_logo_1.png
   :width: 400px
   :align: center
	   

The official CGNS home page
===========================
	   
The **CFD General Notation System** (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data.  It consists of a collection of
conventions, and free and open software implementing those
conventions. It is self-descriptive, machine-independent,
well-documented, and administered by an international steering
committee.
     
It is also an :ref:`American Institute of Aeronautics and
Astronautics (AIAA) Recommended Practice <AIAAPractice>`.
The system consists of two
parts: (1) a standard data model and mapping format for recording the
data, and (2) software that reads, writes, and modifies data in that
format.  The format is a conceptual entity established by the
documentation; the software is a physical product supplied to enable
developers to access and produce data recorded in that format.

The CGNS system is designed to facilitate the exchange of data between
sites and applications, and to help stabilize the archiving of
aerodynamic data.  The data are stored in a compact, binary format and
are accessible through a complete and extensible library of functions.
The API (Application Program Interface) is platform independent and
can be easily implemented in C, C++, Fortran and Fortran90
applications.

Main Topics
-----------

.. cssclass:: table-bordered

.. list-table::
   :widths: 33 34 33
   :width: 100%
   :align: center
   
   * - :ref:`What is CGNS? <WhatIsCGNS>`
     - :ref:`Getting Started <QuickStartGuide>`
     - :ref:`News <LatestNews>`
   * - :ref:`Switch to HDF5 <HDF5Implementation>`
     - :ref:`Steering Committee <YeMightySteeringCommittee>`
     - :ref:`Implementations <IntroImplementations>`
   * - :ref:`Discussion Group (CGNSTalk) <SupportCGNSTalk>`
     - :ref:`Download the Software <SupportDownload>`
     - :ref:`Contributed CGNS Utilities <Contributed>`
   * - :ref:`Example CGNS Files <SupportExamples>`
     - :ref:`Proposals for Extensions (CPEX) <CPEX>`
     - :ref:`FAQ <SupportFAQ>`

Reference Documentation
-----------------------

.. cssclass:: table-bordered
	      
.. list-table::
   :widths: 33 34 33
   :width: 100%
   :align: center
	   
   * - :ref:`Documentation map <DocMap>`
     - :ref:`Standard Interface Data Structures (CGNS/SIDS) <CGNS-SIDS>`
     - :ref:`Meeting and Telecon Minutes <DocMinutes>`
   * - :ref:`A User's Guide to CGNS <DocUserGuide>`
     - :ref:`Overview and Entry-Level Document <Overview>`
     - :ref:`Conference Papers and Slide Presentations <DocExtra>`
   * - :ref:`SIDS File Mapping Manual (FMM) <StandardFMM>`
     - :ref:`Mid-Level Library (MLL) <StandardMLL>`
     - :ref:`CGIO User's Guide (CGIO) <StandardCGIO>`                        

Site map
-------------

.. toctree::
   :maxdepth: 4

   general
   standard
   current
   doc
   governance

.. last line 

