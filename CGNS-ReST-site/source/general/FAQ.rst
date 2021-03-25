.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _SupportFAQ:

FAQ
===

General Questions
-----------------

How do I obtain CGNS?
^^^^^^^^^^^^^^^^^^^^^^^^

CGNS is distributed via `https://github.com/CGNS <https://github.com/CGNS>`_ .
All CGNS software is free, and is governed by the license described at the bottom of the :ref:`What is CGNS? <WhatIsCGNS>` page.
You can obtain the software by going to the :ref:`Download <SupportDownload>` section.
 

How can I get help if I run into problems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no full-time CGNS *"help desk"*. Instead, the CGNS community relies on both extensive documentation and other CGNS users for help and support.
The documentation is available at :ref:`Documentation Home <CGNSHomePage>`.
In particular, we recommend that beginning users consult the :ref:`User's Guide <DocUserGuide>`, which includes many example programs in both Fortran and C.
If you still need help, please make use of the :ref:`Discussion Group <SupportCGNSTalk>`, via e-mail: cgnstalk@lists.nasa.gov. We strongly encourage you to join this group so you can be a part of ongoing CGNS discussions and updates.

.. tip::
  
  Issues should be reported on the dedicated `bug tracker <https://cgnsorg.atlassian.net/jira/core/projects/CGNS/issues/>`_ .

  **Coming soon!** The discussion group will be opening a github discussion forum.
 

There is a lot of documentation... which are most important for me to read?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend the :ref:`User's Guide <DocUserGuide>` as a first *"must read"*.
This will introduce you to CGNS and guide you through many basic examples.
As a tutorial overview, the "CGNS Tutorial Session" (slide format) may also be useful.
It can be found under :ref:`Papers and Slides <DocPapers>` (Slides section).
The full details about the intellectual content of CGNS data model is given in the :ref:`SIDS document <CGNS-SIDS>` (which is also an AIAA Recommended Practice).
Finally, when you start programming, you will probably need to refer to the :ref:`Mid-Level Library <StandardMLL>` documentation, which describes the Fortran and C calls used to read and write the CGNS files.
 

What does SIDS mean?
^^^^^^^^^^^^^^^^^^^^

SIDS stands for *"Standard Interface Data Structures"*.
It defines the details of how data is stored in a CGNS file. CGNS files themselves are entities that are organized internally into a set of "nodes" in a tree-like structure.
The top-most node is referred to as the "root node," and each node has an associated name, label, data, and (possible) children nodes. It is the SIDS that tells you how those nodes are organized, and what data is contained therein.
 

What do I do if CGNS is not capable of handling my particular application?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CGNS has been designed to be very flexible, for handling a wide range of physics applications.
However, if you find an application that is not covered, you are encouraged to utilize the "``UserDefined``" construct as needed.
In fact, the ``UserDefined`` node can be used to create an entire tree consisting of multilpe levels of ``UserDefined`` children nodes, so you can create an entire "pattern" for storing particular information.
Furthermore, if you feel that a change or addition is needed to the SIDS, or if you feel that a particular "pattern" you have created might be useful to others, please consider submitting a proposal for extension (see :ref:`CPEX guidelines <CPEXguidelines>` and :ref:`Proposed Extensions page <CPEX>`).
 

When there are multiple ZONES associated with a given CGNS file, is there a particular way that they should be named?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As application should not rely on zone naming, there should not be a particular naming way.
However, it is important for CGNS users to know that when a CGNS file is opened via the :code:`cg_open()` MLL function, the zones are sorted alphanumerically by name (the creation order is ignored/discarded).
This mechanism is provided to enable ordinal zone indexing. 
Therefore, if ordinal zone indexing is desired, it is considered good standard practice to always *choose zone names to be alphabetically increasing*.
For example, Zone0001, Zone0002, etc. is appropriate for up to 9999 zones. 

.. important::

  Because the *cgnsview* tool uses the low-level :ref:`cgio API <StandardCGIO>`, it does not sort the zones by name and zone order presented may not match that of the MLL API. Generally, *cgnsview* presents the zones in creation order for both ADF and HDF5 formats.
  One exception is CGNS files that are either created or opened using the HDF5 v1.6 library (or older) will always be presented alphabetically (creation order tracking was added to HDF5 in v1.8).
 

How do I view my CGNS files?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CGNS files are most easily viewed using the tool "*cgnsview*" (part of the cgnstools).
This tool is Tcl/Tk based. *Cgnsview* also has the capability to plot and to translate to/from PLOT3D format, for example.
 

How do I know if a CGNS file is correct according to the SIDS definitions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are currently tools being developed to evaluate how well a file complies with the CGNS rules (**"SIDS-compliance"**).
For example, the utility "*cgnsview*" (available as part of the cgnstools), has a capability called "check CGNS" that checks for compliance to some degree (this tool can also be run independently of *cgnsview*).
There are still ongoing discussions about this subject.
For example, it is possible that **different levels of compliance may be defined in the future**.
 

What do the CGNS Version numbers mean, and does the CGNS/MLL library maintain backward/forward compatibility?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CGNS versions are currently numbered as follows: "Version x.y, Revision z", or "Version x.y-z".
(However, the revision number is often left off, so you will typically only see "Version x.y".)
The first number represents the "major" version number.
Within this number, the library maintains forward compatibility. 
For example, Version 4.0 of the library can read a Version 4.1 CGNS file, but Version 3.y cannot necessarily read any Version 4.y (or later) file.
A new "major" version number is assigned either when forward compatibility is lost, or else when there is a significant change made to the API.
The second number is the "point release" number. It increments when there are relatively minor changes to the API, or with the addition of new features.
The third number (the revision number) changes with bug fixes.
Major releases and point releases are announced (via the :ref:`Latest News <LatestNews>` page and via the :ref:`CGNSTalk Discussion Group <SupportCGNSTalk>`), whereas revisions are generally not announced.
Note that CGNS always maintains backward compatibility: the most recent version of the library will be able to read all older versions CGNS files.
 

How do I keep up with the goings-on of the Steering Committee?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CGNS Steering Committee meets and/or holds telecons about 5 times per year.
The minutes are posted on the :ref:`Meeting Minutes <DocMinutes>` page.
Also, the meetings are an open forum: anyone is welcome to attend.
To find out the date and time of the next meeting, please e-mail to cgnstalk@lists.nasa.gov.


Can I use the CGNS logo as part of my website or other documentation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We encourage anyone to freely use the CGNS logo when distributing or documenting CGNS related information.
The logo adds prestige and credibility to web sites, publications, displays, announcements, and activities.
However, the use of the logo in such a way as to imply approval, endorsement, or responsibility of the CGNS committee is prohibited without written permission.

  :download:`Logo file (color) in .gif format (13 kB)<../../../images/logo/cgns_color.gif>`        :download:`Logo file (black & white) in .gif format (12 kB)<../../../images/logo/cgns_bw.gif>`

  :download:`Logo file (color) in .jpg format (12 kB)<../../../images/logo/cgns_color.jpg>`        :download:`Logo file (black & white) in .jpg format (9 kB)<../../../images/logo/cgns_bw.jpg>`
 

Is CGNS an ISO standard?
^^^^^^^^^^^^^^^^^^^^^^^^

Between 1999 and 2002, an effort was spearheaded by Boeing to establish an ISO-STEP standard for the representation, storage, and exchange of digital data in fluid dynamics based on the CGNS standard.
Unfortunately, the effort had to be curtailed because of budget problems.
It was subsequently decided that an existing ISO standard on finite element solid mechanics would be rewritten and submitted to include CGNS as well as an integrated engineering analysis framework.
Some details on this subsequent effort can be found in archives of the :ref:`Meeting and Telecon Minutes <DocMinutes>`.
This new ISO effort was being conducted completely outside of the control of the CGNS committee. Therefore, the current status is not known.

Installation Questions
----------------------

How to install CGNS on Windows from source with HDF5 also built from source using Microsoft C compiler?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two components to consider: (1) Installation of HDF5 from source and (2) Installation of CGNS using the HDF5 built in (1).

(1) Installation of HDF5 from source.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This guide is a quick start summary of the HDF5 build instruction provided by The HDF Group.
CGNS does not need the Fortran HDF5 APIs, so it is not required to enable Fortran when building HDF5.
CGNS also does not use compression, so Zlib and SZIP can be disabled when building HDF5.

Prerequisites
+++++++++++++

   #. *CMake* MUST be installed. The configuration scripts require a minimum CMake version 3.8, the current version of *CMake* is strongly encouraged.
   #. (Optional, but strongly encouraged) `NSIS <https://nsis.sourceforge.io/Main_Page>`_ or `WiX <https://wixtoolset.org/>`_ should be installed to create an install image with *CPack*. NSIS will create a .exe installer. WiX will create a .msi installer. This guide assumes WiX is installed.
   #. *Git* for cloning the *HDF5* and *CGNS* source.
   #. Blank spaces **MUST NOT** be used in directory path names as this will cause the build to fail.
   #. Perl needs to be installed if building from source from the repository. If building from released `HDF5 source <https://www.hdfgroup.org/downloads/hdf5/source-code/#src>`_ then it is not needed.

Installation
++++++++++++

In a directory (Noting item #4 of the `Prerequisites`_) download the HDF5 source,

.. code-block:: console

  git clone https://bitbucket.hdfgroup.org/scm/hdffv/hdf5.git

Copy three files in the HDF5 source directory hdf5\config\cmake\scripts to the current directory.

.. code-block:: console

  copy hdf5\config\cmake\scripts\HDF5options.cmake .

  copy hdf5\config\cmake\scripts\CTestScript.cmake .

  copy hdf5\config\cmake\scripts\HDF5config.cmake .

The only file that needs to be edited is HDF5options.cmake. Disable Zlib and Szip by setting the lines in HDF5options to,

.. code-block:: cmake

  ### disable ext zlib building
  set(ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_Z_LIB_SUPPORT:BOOL=OFF")

  ### disable ext szip building
  set(ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_SZIP_SUPPORT:BOOL=OFF")
  set(ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_SZIP_ENCODING:BOOL=OFF")

Create a batch script, *gen.bat*, to build HDF5. The contents will be,

.. code-block:: console

  ctest -S HDF5config.cmake,BUILD_GENERATOR=VS201764,CTEST_SOURCE_NAME=hdf5,STATIC_ONLY=NO -C Release -VV -O hdf5.log

If you are using a different version of Visual Studio, then change ``BUILD_GENERATOR=`` to the matching one found in *HDF5config.cmake* in the section "Following describes compiler".

Execute *gen.bat*,

.. code-block:: console

  gen.bat

Doing so will build and test the installation of HDF5. The HDF5 build directory will be called '*build*'. Change into the '*build*' directory and run *cpack*,

.. code-block:: console

  cpack -C Release

Assuming WiX is installed, cpack will create an HDF5-X.X.X-win64.msi installer. Select the msi file and follow the installation GUI instructions, which will install HDF5.

(2) Installation of CGNS from source.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download CGNS source,

.. code-block:: console

  git clone https://github.com/CGNS/CGNS.git

Create a directory which will contain the build of CGNS, don't build CGNS in the source directory.

.. code-block:: console
  
  mkdir build_cgns
  cd build_cgns

Create a batch script which will be used to build CGNS with cmake, the contents will vary depending on the options you chose to build CGNS with, but a sample file, *build_cgns_MS.bat*, would be:

.. code-block:: bat

  @echo OFF
  :: Run the cmake command
  cmake -G "Visual Studio 15 2017" -A "x64"^
    -D CMAKE_PREFIX_PATH:PATH="C:\Program Files\HDF_Group\HDF5\1.11.2\cmake" ^
    -D CMAKE_BUILD_TYPE=Release ^
    -D CGNS_ENABLE_FORTRAN:BOOL=OFF ^
    -D CGNS_BUILD_SHARED:BOOL=OFF ^
    -D CMAKE_STATIC_LINKER_FLAGS:STRING="/NODEFAULTLIB:library" ^
    -D CMAKE_EXE_LINKER_FLAGS:STRING="/NODEFAULTLIB:library" ^
    -D CGNS_USE_SHARED:BOOL=OFF ^
    -D CGNS_ENABLE_LEGACY=OFF ^
    -D CGNS_ENABLE_64BIT=BOOL=ON ^
    -D CGNS_ENABLE_LFS:BOOL=ON ^
    -D CGNS_BUILD_CGNSTOOLS:BOOL=OFF ^
    -D CGNS_ENABLE_TESTS:BOOL=ON ^
    -D CMAKE_VERBOSE_MAKEFILE:BOOL=ON ^
    -D CGNS_ENABLE_HDF5:BOOL=ON ^
    -D CGNS_ENABLE_PARALLEL:BOOL=OFF ^
    -D HDF5_BUILD_SHARED_LIBS:BOOL=OFF ^
    -D HDF5_NEED_MPI:BOOL=OFF ^
    -D HDF5_NEED_ZLIB:BOOL=OFF ^
    -D HDF5_NEED_SZIP:BOOL=OFF ^
    ../CGNS
  cmake --build .

.. note:: 

  :CMAKE_PREFIX_PATH: -- Set to where HDF5 was installed in Step (1).
  :-G: -- Set to the correct Visual Studio edition.
  :-A: -- Set to the target architecture.
  :../CGNS: -- This is the path to the CGNS source

To test the CGNS installation run ctest,

.. code-block:: console

  ctest .


.. last line
