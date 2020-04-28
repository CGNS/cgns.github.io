.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. CGNS documentation master files
   04/2020 - (marc.poinot@safrangroup.com)
             start Markdown translation and change layout, see how pages
	     are changed/moved in the MIGRATION.txt file

.. IGNORE warning message produced by the image directive below	     
.. image:: ./images/logo/CGNS_logo.png
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

Quick Links
-----------

.. list-table::
   :widths: 33 34 33
   :width: 100%
   :align: center
   
   * - :ref:`What is CGNS? <WhatIsCGNS>`
     - Getting Started
     - Latest News
   * - Switch to HDF5
     - Steering Committee
     - Implementations
   * - Discussion Group (CGNSTalk)
     - Download the Software
     - Contributed CGNS Utilities
   * - Example CGNS Files
     - Proposals for Extensions (CPEX)
     - FAQs
       
Documentation links
-------------------
       
.. list-table::
   :widths: 33 34 33
   :width: 100%
   :align: center
	   
   * - Documentation Home Page
     - :ref:`Standard Interface Data Structures (CGNS/SIDS) <CGNS-SIDS>`
     - Meeting and Telecon Minutes
   * - A User's Guide to CGNS
     - Overview and Entry-Level Document
     - Conference Papers and Slide Presentations
   * - SIDS File Mapping Manual (FMM)
     - Mid-Level Library (MLL)
     - CGIO User's Guide                          

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

