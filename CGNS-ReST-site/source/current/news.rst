.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

News
====

The news below are listed by date. There is a specific section for
the documentation news and fixes and end of this page.

.. sidebar:: DO NOT MISS...

  - Next Telecon May 3rd, 4PM (CST)
  - AIAA Scitech 2021 Nashville

The latest news item:

.. topic:: March 4, 2020 - :version:`v4.1.0` of the CGNS Software is released.
	   
   - Added :ref:`CPEX 42` Storing bounding box of a grid (:issue:`CGNS-149`).
   - Added :ref:`CPEX 43` Family hierarchy as a tree (:issue:`CGNS-180`).

Previous releases
-----------------

.. topic:: Febuary 17, 2020 - :version:`v4.0.0` of the CGNS Software is released.
   - Added :ref:`CPEX 41` NGON modification proposal (:issue:`CGNS-121`).

.. topic:: Febuary 17, 2020 - :version:`v3.4.1` (patch) of the CGNS Software is released.

 - Removed :ref:`CPEX 41` NGON modification proposal (:issue:`CGNS-121`).

.. topic:: March 5, 2019: :version:`v3.4.0` of the CGNS Software is released.

   - :ref:`CPEX 40` Rind Plane Indexing (:issue:`CGNS-87`).
   - :ref:`CPEX 41` NGON modification proposal (:issue:`CGNS-121`).
   - Added support for NAG Fortran compilers (:issue:`CGNS-107`).
   - Enforce the HDF5 version >= 1.8 is used in building HDF5 (:issue:`CGNS-150`).
   - Automatic detection and linking of szip and zlib if required by HDF5 (:issue:`CGNS-156`).

.. topic:: July 16, 2017: :version:`v3.3.1` of the CGNS Software is released.

   - Serial and Parallel CGNS with Fortran enabled for Windows, PR-40.

.. topic:: January 25, 2016: :version:`v3.3.0` of the CGNS Software released.

   - Example build scripts for supercomputer systems can be found
     in src/SampleScripts of the CGNS source code. They include scripts for
     building zlib, hdf5 (assuming the user does not already have them
     installed system wide) and a script for building CGNS.
     All the scripts use autotools; cmake remains untested.
   - The Fortran compiler environment variable can now be set with "FC",
     this is the preferred method.
   - The Fortran compiler flags can now be set with "FCFLAGS", this is the
     preferred method. If both FFLAGS (which predates FCFLAGS) and FCFLAGS
     are set then FCFLAGS is ignored.
   - Replaced the hid_t to double (and vice-versa) utilities to_HDF_ID and
     to_ADF_ID from a type cast to a function which uses memcpy for the
     conversion. This is needed for the upcomming release of HDF5 1.10 where
     hid_t was changed from a 32 bit integer to a 64 bit integer.
     Should be transparent to user.
   - Implemented :ref:`CPEX 39` : To enable with CGNS_ENABLE_BASE_SCOPE
   - Implemented :ref:`CPEX 38` : Quadratic Elements for High Order
   - In the parallel library, the default parallel input/output mode was
     changed from CGP_INDEPENDENT to CGP_COLLECTIVE.
   - In the parallel library, a new function was added for passing MPI info
     to the CGNS library: cgp_mpi_info (cgp_mpi_info_f).
   - In the parallel library, a new parallel example benchmark program,
     benchmark_hdf5.c, was added to directory ptests.
   - In the parallel library, the cgp_*_read/write_dataset APIs now excepts
     non-allocated arrays, or NULL, as valid parameters for the datasets.
     Additionally, the dimensional arrays, rmin and rmax, can also be NULL.
     If the data array is NULL and the dimensional arrays are not NULL, then
     the validity of the dimensional arrays, rmin and rmax, is not checked.
     For collective parallel IO, this is used as a mechanism to indicated
     that processes with NULL API parameters will not write any data to the
     file.
   - In the parallel library, cgp_queue_set and cgp_queue_flush were
     depreciated in this release.
   - **SUPPORT WAS DROPPED FOR NON-FORTRAN 2003 COMPLIANT COMPILERS.**
   - Configure was changed to check if the Fortran compiler is Fortran 2003
     compliant.
   - In the Fortran library, the predefined CGNS constant parameters data
     types were changed from INTEGER to ENUM, BIND(C) for better C
     interoperability. The users should use the predefined constants whenever
     possible and not the numerical value represented by the constants.
     A variable expecting an enum value returned from a Fortran API should
     be declared, INTEGER(cgenum_t).
   - In the Fortran library, INCLUDE "cgnslib_f.h" was removed in favor of
     using a module, USE CGNS. This allows defining a KIND type for
     integers instead of the current way of using the preprocessor dependent
     cgsize_t. The user should be sure to declare the arguments declared int
     in the C APIs as INTEGER in Fortran. The ONLY Fortran arguments declared
     as type cgsize_t should be the arguments which are also declared cgsize_t
     in the C APIs. This is very important when building with
     option --enable-64bit. The test programs were updated in order
     to conform to this convention.
     Assuming the rules in step [enu:int64] were followed, users should not
     need to use parameter CG_BUILD_64BIT since Fortran's cgsize_t is now
     guaranteed to match C's cgsize_t.
     Fortran programs defining CGNS data types with a default INTEGER size
     of 8 bytes also then need to compile the CGNS library with the default
     INTEGER size of 8 bytes. This is independent of whether or
     not --enable-64bit is being used. For clarification,
     using --enable-64bit allows for data types (i.e. those declared
     as cgsize_t) to be able to store values which are too large to be stored
     as 4 byte integers (i.e. numbers greater than 2,147,483,647).
     It is not necessary, or advisable (since it waste memory),
     to have CGNS INTEGER types (types declared int in C) to be 8 bytes;
     the variables declared as cgsize_t will automatically handle data types
     that can not be stored as 4 byte integers when --enable-64bit
     is being used. If the CGNS library was not compiled
     with a default INTEGER of 8 bytes, but the calling program was,
     then all integers passed to CGNS with C type int should
     be declared INTEGER(C_INT).
     A new Fortran API was added for determining the CGNS data type of a
     variable which is interoperable with the C data type.

     ``Function cg_get_type(var)``
     ``type, INTENT(IN) :: var``
     ``INTEGER(KIND(enumvar)) :: cg_get_type``

     An example of using the new function to automatically specify the
     CGNS type corresponding to the Fortran data type is,

     ``INTEGER, DIMENSION(1:10) :: Array_i``
     ``CALL cgp_array_write_f("ArrayI",cg_get_type(Array_i(1)),1,INT(nijk(1),cgsize_t),Ai, err)``

   - Removed all parallel flush/queue functions
   - Removed support of "include cgnslib_f.h", all examples and tests were
     updated to reflect these changes.

.. topic:: December 8, 2015

   - Marc Poinot will be presenting a CGNS paper at AIAA SciTech in January: "CGNS test suites for CFD software components", Thursday January 7, 2016 at 2pm in session MVC-02.

.. topic:: December 7, 2015

   - Release candidate version 3.3.0-rc1 is now available and an be
     downloaded from: https://github.com/CGNS/CGNS/releases.

   - **Updates since the v3.3.0-alpha.2 release:**

     - Removed all parallel flush/queue functions (:issue:`CGNS-9`)
     - Removed support of include cgnslib_f.h, all examples and tests were
       updated to reflect these changes (:issue:`CGNS-34`)
     - Fixed parallel issue when not all processors involved in
       reading/writing (:issue:`CGNS-51`)
     - Fixed argument being passed to H5Pget_driver in ADFH.c (:issue:`CGNS-50`)
     - Added multiple Fortran and C tests to testing
     - Added a new PGI fortran compiler flag fix issue when passing
       to C varags (:issue:`CGNS-40`)
     
.. topic:: September 21, 2015:

   - Pre-release version 3.3.0 of CGNS is available for testing.
     Fortran testing is particularly needed.

.. topic:: May 19, 2015:

   - CGNS is making the move from SourceForge to GitHub.
     New download website is https://github.com/CGNS. SourceForge still has
     old stable releases (for the time being), but up-to-date code (via git)
     and future releases are all on GitHub.

.. topic:: December 2, 2014:

   - The CGNS Steering Committee voted to discontinue support for FORTRAN
     compilers that are not Fortran 2003 compliant.

.. topic:: February 7, 2014:

   - The CGNS Steering Committee recently voted to take Version 3.2 off beta
     status. As of this date, Version 3.2 is the default available from
     SourceForge. This version integrates parallel I/O (using HDF5),
     and also implements CPEX 0033, 0034, and 0036.

.. topic:: July 16, 2013:

   - Created Quick Guide to Upgrading from CGNS v2.5 to v3.x, also available
     from the download page.

.. topic:: July 15, 2013: Release 2 of Version 3.1.4 is now available.

   - This release adds checks for an open file to routines that don't take
     a file number (suggestion from Marc Poinet), adds HTMLHelp interface
     to cmake scripts, fixes a compiler complaint about comparison between
     int and enum, and fixes Fortran detection and MPI path problems
     in the CMake scripts. Compatability with version 2.5
     (file type CG_FILE_ADF2) is also fixed for both CG_MODE_WRITE
     and CG_MODE_MODIFY. The CGNStools documentation has been removed
     from the source distribution, and is now accessed from
     the NASA Glenn server or a local copy (as with Version 3.2).

.. topic:: July 15, 2013: Version 3.2.1 (beta) is now available.

   - This release fixes a problem with IS_FIXED_SIZE macro for cubic elements
     and adds AdditionalFamilyName to UserDefinedData. This also implements
     the cmake script and MPI communicator changes proposed by
     Cambridge Flow Solutions. There are also numerous updates to the test,
     tools, and CGNStools utility programs.

.. topic:: Feb 26, 2013: Version 3.2 (beta) is now available.

   - This release provides full integration of parallel I/O using HDF5
     with MPI. It also implements the Hierarchy of families (CPEX 0033),
     Multiple families (CPEX 0034), and Cubic elements (CPEX 0036).
     Compression (rewriting) of modified CGNS files is no longer automatically
     done, since this may interfere with parallel I/O. This may be reenabled
     within an application with the cg_set_compress function, or done later
     through the CGNSview GUI or with the cgnscompress program in the tools
     subdirectory. Conversion programs to and from AFLR3, FAST, and TetGen
     have also been added to CGNStools.

.. topic:: Feb 13, 2013: Version 3.1.4 is now available.

   - This release fixes some issues with goto for FamilyBCDataset for UserData,
     .etc; fixes cmake and configure scripts to allow MPI with HDF5 and
     some bugs in those scripts; updates CGNSplot to handle all element types
     and 1-d and 2-d cases; updates to cgnscheck; adds cgnsBuild.defs Makefile
     include to installation; allows CellCenter for BCs; and adds cg_precision
     and cg_precision_f functions to get integer size used to create
     the file (32 or 64).
   - Note: CGNStools no longer built automatically, you need to set the
     configure flag, --enable-cgnstools if using configure.

.. topic:: January 15, 2012: Release 4 of Version 3.1.3 is now available.

   - This release fixes an issue with descriptors under FamilyBCDataSet_t
     nodes; changes NormalIndexFlag to NormalIndexSize for cg_boco_info; and
     adds a new Fortran routine cg_exit_on_error_f. This function allows
     a Fortran application to set a flag which will cause the program
     to print an error message and exit automatically if an error
     is encountered.

.. topic:: December 19, 2011: Release 3 of Version 3.1.3 is now available.

   - This release adds a HDF5 CRT_ORDER fix and corrects the directory search
     order for linked files. Also newly available are complete V2.5 or V3.1
     documentation in the form of Windows compiled HTML files (chm).
     If you are using Windows or have a CHM viewer on Linux you can download
     these from the download page on the CGNS website or directly
     from SourceForge.

.. topic:: April 25, 2011: Version 3.1.3 released.

   - This release includes a fix to return HDF5 children in creation order.
     It also includes the implementation of :ref:`CPEX 27`
     (Time-dependent Connectivities), :ref:`CPEX 30` (Zone Sub-Regions) and
     :ref:`CPEX 31` (General SIDS Improvements), along with the alpha release
     of Parallel CGNS. These are described in the online documentation.

.. topic:: March 30, 2011: Version 3.1 updated and released as Version 3.1-2.

   - This release implements the bug fixes by Xiangmin Jiao (Jim), and
     adds two new functions to more easily read and write GridLocation data
     for boundary conditions, cg_boco_gridlocation_read and
     cg_boco_gridlocation_write.

.. topic:: March 13, 2011: Version 3.1 updated and released as Version 3.1-1.

   - This release fixes a bug with relative path names for ADF links and
     some cmake configuration options related to non-standard X installations
     and warning messages. Also, the configure script no longer supports
     multiple machine builds in the same directory due to
     the machine-dependent header files that are created.

.. topic:: March 1, 2011: Version 3.1 has been officially released.

   - This release includes 64-bit capability. The changes from version 3.0 beta
     is the reordering of the element types to put PYRA_13 after MIXED and
     the 64-bit support. Most of the documentation has been updated
     to identify the changes.

.. topic:: Feb 1, 2011:

   - Version 3.1 has recently been committed to the SVN repository on
     SourceForge. It has not been bundled up for release yet, but interested
     users can access it from the SVN repository. This version has
     true 64-bit capabilities, which overcomes the previous 32-bit integer
     limitation and allows the writing of very large grids.
     UserGuide example codes have also been updated to V3.1,
     to be able to take advantage of the 64-bit capability.

.. topic:: May 25, 2010: Version 3.0.8 (Beta) has been released

   - As a tarred source release on SourceForge.
     Parallel CGNS Version 0.2.0 (Alpha) is now available as well.
     A CGNS MediaWiki page has been created.

.. topic:: August 26, 2009: Version 3.0.5 (Beta) released.

   - This Beta version is intended for users to perform preliminary testing.
     Many changes have been made from 2.5, but a few of the more noticeable
     ones include the following: (1) Build system has been changed from
     autotools to CMake, (2) Moving forward the HDF5 back-end will have
     preference, (3) cgnscalc and cgnssh have been disabled since they do
     not currently work. The new beta can be downloaded from the subversion
     repository at SourceForge.

.. topic:: August 22, 2009: Version 2.5.4 released.

   - This release fixes a long standing issue of memory leakage in the CGNS
     library when closing a file or deleting a node. It also removes the
     internal storage of element data when reading and writing, and uses
     the user supplied buffer instead. In the case of partial reads and
     writes however, the element data is currently reloaded into memory
     to do the operations.

.. topic:: March 11, 2007: Version 2.5.3 released.

   - This version changes the mispelled Celcius to Celsius, fixes handling of
     soft links when rewriting the CGNS file, and fixes a number of gcc
     compiler warnings.

.. topic:: September 11, 2007:

   - A new instructor-led AIAA short course is being offered starting at
     the Aerospace Sciences Meeting in Reno, NV, January 5-6, 2008:
     "Effective Use of the CFD General Notation System (CGNS) for Commercial
     and Research Applications." A description can be found by going
     to: www.aiaa.org. Click on "Courses & Training", then "Schedule".
     The CGNS course is listed under the Heading: January 2008.
     Or go directly to: Summary of Short Course.

.. topic:: September 7, 2007: Version 2.5 taken off beta status.

   - This new release adds "CG_" prefixes to the C preprocessor
     defines MODE_xxx, Null, and UserDefined. For example, MODE_READ is
     now CG_MODE_READ and Null is now CG_Null. The old defines are still
     currently supported. Support has been added to build the cgns library
     as a DLL under Windows. The NormalIndex arguments to cg_boco_info,
     cg_boco_normal_write are now optional (pass as 0 or NULL to ignore).
   - Moved some of the CGNS utility programs, such as cgnscheck, to the
     subdirectory 'tools' in the cgns distribution. This may now be built
     without building cgnstools.
   - Also, final release of cgnsib_2.4 made (primarily an update of version
     number from 2.42 to 2.46, and some minor bug fixes). The last digit on
     the version number is now ignored when reporting that a file was created
     with a newer version than the current library. Finally, in cgnstools,
     changed cgnsplot to use a tree layout instead of lists, and added a
     cutting plane for viewing mesh cross-sections. Fixed a long standing
     bug in cgns_interpolate which was causing that program to work
     incorrectly or crash. Also added a VTK file export routine for CGNS files.

.. topic:: October 5, 2006: Version 2.5 (beta) of the CGNS library has been released (cgnslib_2.5-1.tar.gz).

   - This fixes problems with partial read and writes, and adds some
     additional capabilities (goto operation enhancements, type names,
     new cgns file checker, setting path to search for links, and
     new routine for configuring CGNS). Documentation is not available yet.
     Look in the "tests" subdirectory at "test_partial.c" and "test_goto.c"
     for examples of the use of these routines. In addition, there are 2 other
     new releases for download from SourceForge:
     
     (1) cgnslib_2.4-5.tar.gz:
         This release fixes some problems with ADF on Windows 64 bit machines,
         and adds a -64 option to the configure.bat file.
     
     (2) cgnstools-2-5-1.tar.gz: Adds support for CGNS version 2.5.
	 
     Configures the Tcl/Tk GUI to use the current color scheme rather
     than a "Windows" type color scheme. Fixes some minor bugs and adds some
     improvement to the cgnscheck program. Allows reading of both HDF5 and
     ADF - based CGNS files (requires the adf2hdf and hdf2adf
     convertor programs).

.. topic:: Spring, 2006:

   - There are two special CGNS "events" planned for the American Institute
     of Aeronautics and Astronautics (AIAA) meeting being
     held 5-8 June 2006 in San Francisco.
     The first is a Panel discussion, tentatively
     titled "CGNS Practical Applications in CFD". This will occur during
     the regular AIAA sessions at the conference.
     The second is a "CGNS Tutorial Session", currently scheduled for Wednsday,
     7 June 2006 in the evening. This session will be conducted in two parts:
     
     (1) Basic usage of CGNS (including examples for structured
	 and unstructured grids), and
     (2) Advanced topics (tentatively including HDF-5 usage, parallel
	 implementation, and SIDS high level representation).
	 
     The tutorial session will be taught by five experienced
     users/developers of CGNS and will be a great way to either
     get a basic introduction or to refine your knowledge of CGNS.
     Note that AIAA charges a registration fee for conference attendance,
     but there is no additional fee to attend the CGNS events. More information
     about the AIAA conference can be found at: www.aiaa.org.
     Click on "Conferences & Events", then
     click on "36th AIAA Fluid Dynamics Conference and Exhibit".

.. topic:: August 23, 2005: New releases of Version 2.3 and 2.4 of the CGNS library and CGNStools.

   - This is the final release for Version 2.3 - Version 2.4 is now
     the official version. The CGNS library releases fixed a bug
     in cg_family_write and others where the wrong file (when multiple are open)
     might be accessed or a segfault occur. Added unstructured mesh rind
     to Version 2.4, and support for that in CGNSplot and cgnscheck.
     Improved the Fortran to C interface, particularly under Windows,
     Also fixed some minor bugs in the CGNStools and improved
     the cgnscheck program.

.. topic:: August 8, 2005:

   - CGNStalk discussion list moved from cgnstalk@grc.nasa.gov to cgnstalk@lists.nasa.gov.

.. topic:: May 14, 2005: Version 2.4 (Revision 2) of the CGNS library released.

   - The HDF5 interface (ADFH) may now be selected at build time with
     the configuration script. Fixed some bugs.

.. topic:: December 2, 2004: Version 2.4 (beta) of the CGNS library has been released.
   - This version includes the extensions by Intelligent Light.
     These extensions include 8 base units, partial read/write,
     Electromagnetics, 1tot1 connectivity properties, and extensions to
     the FamilyBC, BCDataSet and UserDefinedData. Preliminary documentation
     for these extensions in the form of PDF files is also available
     for download. 

.. topic:: October 1, 2004: Released an update to Version 2.3 of the CGNS library.
   - This update fixes some problems with MLL routines returning the wrong
     error code (or terminating prematurely). Also, checks are now performed
     when creating a CGNS file to prevent writing a file which fails to read.
     A new version of cgnstools has also been released with improvements
     to both adfviewer and cgnsplot.
     The cgnscheck program has been significantly improved.
     It should now check the validity of all CGNS 2.3 nodes. 

.. topic:: March 22, 2004: ADFH has been released as beta.

   - This is a complete implementation of CGNS using HDF5 instead of ADF. 

.. topic:: January 22, 2004: Version 2.3 of the CGNS library has been released.

   - The major changes in this version over that of 2.2 is a significant
     speedup in reading and writing when dealing with a large number of zones
     and the reimplementation of ElementList and ElementRange for
     specifying boundary conditions. 

.. topic:: December 13, 2003:

   - An initial prototype has been released which replaces ADF with HDF5.
     Thanks to Marc Poinot at Onera and Greg Power's group at Arnold.
     The source is currently only available with CVS as module adfh. 

.. topic:: September 28, 2003: CGNS library Version 2.3 beta release.

   - This version currently adds no additional functionality to
     that of Version 2.2, but speeds up read/write times by orders
     of magnitude when a large number of zones are present. 

.. topic:: May 10, 2003: CGNS Version 2.2 has been released.

.. topic:: May 3, 2003:
	   
   - The CGNS source code is now available as a download of the latest
     release or anonymous CVS access to the current beta version at
     SourceForge.net. There is now a GNU configure script for
     configuring compiler options.

.. topic:: January 23, 2003:
	   
   - The CGNS documentation and Technical Papers link now points to a single
     website location at NASA Glenn. All documentation, papers and
     the minutes of the CGNS Steering Committee meetings are available there.

.. topic:: September 18, 2002:

   - Minutes of the CGNS Steering Committee meetings and teleconferences
     are available at the NASA Glenn website. 

.. topic:: January 16, 2002:

   - paper AIAA 2002-0752, "CFD General Notation System (CGNS):
     Status and Future Directions" presented at the 40th Aerospace Sciences
     Meeting & Exhibit, Reno, Nevada.

.. topic:: December 1, 2000: Release of Version 2.0 beta 2

   - Supports grid motion and iterative or time accurate data.

.. topic:: October 31, 2001:

   - Review the new "User's Guide to CGNS" created by Chris Rumsey of
     NASA Langley Research Center.

.. topic:: October 18, 2000:

   - CGNS has now its own discussion group. Users can exchange opinions
     and experiences via CGNS Talk.

.. topic:: March 15, 2000:

   - Added support for MIXED element sections.

.. topic:: January 10, 2000:

   - The CGNS Steering Committee becomes a sub-committee
     of the AIAA Committee on Standards.

.. topic:: January 12, 2000:

   - paper AIAA 2000-0681, "Advances in the CGNS Database Standard for
     Aerodynamics and CFD." presented at the 38th Aerospace Sciences
     Meeting & Exhibit, Reno, Nevada.

.. topic:: October 14, 1999:

   - The CGNS Steering Committee Charter has been unanimously adopted
     at the CGNS Meeting at UTRC, East Hartford.

.. topic:: September 1999: First release!

   - The CGNS Library and the ADF File Browser are now available on
     Windows NT and Linux !!!

.. _DocNews:

Documentation news
==================

.. topic:: 04 Sep 2019	

  - Posted draft minutes from the Sep 03, 2019 (PDF) Steering Committee telecon.
Updated new CGNS Committee chair information on CGNS Steering Committee Site page.
.. topic:: 19 July 2019	

  - Fixed a few typos among the HEX element tables for Unstructured Grid Element Numbering Conventions. This included fixing a typo in F3 corner nodes definition for HEXA_8, HEXA_20, HEXA_27, HEXA_32, HEXA_56, HEXA_64, HEXA_44, HEXA_98, and HEXA_125. Also, there was a fix in the F5 mid-face node ordering in HEXA_56, HEXA_64, HEXA_98, and HEXA_125.
.. topic:: 25 Jun 2019	

  - Posted draft minutes from the Jun 25, 2019 (PDF) Steering Committee telecon.
.. topic:: 21 May 2019	

  - Revised all element figures and tables for Unstructured Grid Element Numbering Conventions. This included a few corrections to the tables for some of the higher-order elements (face F1 for PYRA_50 and PYRA_55; face F4 for PENTA_66 and PENTA_75; face F1 for HEXA_98 and HEXA_125). For everything else, the reason for the update was to improve the figure quality.
Posted draft minutes from the May 21, 2019 (PDF) Steering Committee telecon.
.. topic:: 26 Mar 2019	

  - Posted draft minutes from the Mar 26, 2019 (PDF) Steering Committee telecon.
.. topic:: 22 Jan 2019	

  - Posted draft minutes from the Jan 22, 2019 (PDF) Steering Committee telecon.
.. topic:: 26 Nov 2018	

Updated SIDS documentation to V3.4, including changes associated with CPEX 0041.
.. topic:: 08 Nov 2018	

  - Posted draft minutes from the Nov 06, 2018 (PDF) Steering Committee telecon.
.. topic:: 18 Sep 2018	

  - Posted draft minutes from the Sep 18, 2018 (PDF) Steering Committee telecon.
.. topic:: 05 Jun 2018	

  - Posted draft minutes from the Jun 05, 2018 (PDF) Steering Committee telecon.
.. topic:: 29 Mar 2018	

  - Posted draft minutes from the Mar 27, 2018 (PDF) Steering Committee telecon.
.. topic:: 31 Jan 2018	

  - Posted revised draft minutes from the Jan 30, 2018 (PDF) Steering Committee telecon.
.. topic:: 25 Oct 2017	

  - Posted draft minutes from the Oct 24, 2017 (PDF) Steering Committee telecon.
.. topic:: 12 Sep 2017	

  - Posted draft minutes from the Sep 12, 2017 (PDF) Steering Committee telecon.
.. topic:: 25 Jul 2017	

  - Posted draft minutes from the Jul 25, 2017 (PDF) Steering Committee telecon.
.. topic:: 05 May 2017	

  - Posted draft minutes from the May 05, 2017 (PDF) Steering Committee telecon.
.. topic:: 01 Feb 2017	

  - Posted draft minutes from the Jan 31, 2017 (PDF) Steering Committee telecon.
.. topic:: 29 Nov 2016	

  - Posted draft minutes from the Nov 29, 2016 (PDF) Steering Committee telecon.
.. topic:: 23 Sep 2016	

  - Posted draft minutes from the Sep 23, 2016 (PDF) Steering Committee telecon.
.. topic:: 06 Jul 2016	

  - Posted draft minutes from the Jul 05, 2016 (PDF) Steering Committee telecon.
.. topic:: 20 May 2016	

  - Fixed typo in Section 10.3 (GasModelType_t changed to ModelType_t). Also created more complete index to the SIDS, including section and subsection numbering.
.. topic:: 09 Apr 2016	

  - Posted draft minutes from the Apr 05, 2016 (PDF) Steering Committee telecon.
.. topic:: 04 Mar 2016	

  - Posted draft minutes from the Mar 01, 2016 (PDF) Steering Committee telecon.
.. topic:: 10 Dec 2015	

  - Posted draft minutes from the Dec 08, 2015 (PDF) Steering Committee telecon.
.. topic:: 21 Oct 2015	

  - Posted draft minutes from the Oct 20, 2015 (PDF) Steering Committee telecon.
.. topic:: 25 Sep 2015	

  - Updated SIDS documentation to V3.3, including changes associated with CPEX 0039.
.. topic:: 23 Sep 2015	

  - Updated documentation to V3.3. This was mostly simply a change to the posted numbering conventions, other than the addition of the new quartic elements from CPEX 0038 to the MLL in Typedefs.
.. topic:: 09 Sep 2015	

   - Posted draft minutes from the Sep 08, 2015 (PDF) Steering Committee telecon.
.. topic:: 22 May 2015	

   - Posted draft minutes from the May 19, 2015 (PDF) Steering Committee telecon.
.. topic:: 05 Mar 2015	

   - Posted draft minutes from the March 3, 2015 (PDF) Steering Committee telecon.
.. topic:: 02 Dec 2014	

   - Posted draft minutes from the December 2, 2014 (PDF) Steering Committee telecon.
.. topic:: 07 Oct 2014	

   - Posted draft minutes from the October 2, 2014 (PDF) Steering Committee telecon.
.. topic:: 04 Sep 2014	

   - Posted draft minutes from the September 3, 2014 (PDF) Steering Committee telecon.
.. topic:: 02 Sep 2014	

   - Added quartic element definitions (CPEX 0038) to Line Elements, Surface Elements, and Volume Elements to the SIDS definitions only. Not coded into the MLL yet (when it is, the CGNS Version designation will be changed to 3.3). Also fixed some typos, grammar, and did some minor formatting fixes.
.. topic:: 24 Feb 2014	

   - Posted draft minutes from the February 18, 2014 (PDF) Steering Committee telecon.
.. topic:: 07 Feb 2014	

   - Official release of version 3.2.1. The 3.2 (beta) documentation has been switched to be primary documentation.
.. topic:: 04 Feb 2014	

   - Posted draft minutes from the January 28, 2014 (PDF) Steering Committee telecon.
.. topic:: 18 Dec 2013	

   - Posted draft minutes from the December 17, 2013 (PDF) Steering Committee telecon.
.. topic:: 19 Sep 2013	

   - Posted draft minutes from the September 18, 2013 (PDF) Steering Committee telecon.
.. topic:: 26 Jul 2013	

   - Minor change in SIDS docs: differences from previous versions put in reverse chronological order.
.. topic:: 16 Jul 2013	

   - Posted draft minutes from the July 16, 2013 (PDF) Steering Committee telecon.
.. topic:: 8 July 2013	

   - Added documentation for CGNS_CONFIG_HDF5_MPI_COMM option to cg_configure. Added cgp_mpi_comm routine documentation.
.. topic:: 14 May 2013	

   - Added AdditionalFamilyName to UserDefinedData in SIDS and in File Mapping.
.. topic:: 30 Apr 2013	

   - Posted draft minutes from the April 30, 2013 (PDF) Steering Committee telecon.
.. topic:: 29 Mar 2013	

   - Added description of CG_CONFIG_FILE_TYPE that was missing; also added more description of cg_set_file_type on MLL File Operations page.
.. topic:: 14 Mar 2013	

   - Made minor mods in overview and intro of PDF version of SIDS v3.2, to remove stale discussion, add abstract, and add some clarity.
.. topic:: 13 Mar 2013	

   - Posted draft minutes from the March 12, 2013 (PDF) Steering Committee telecon.
.. topic:: 27 Feb 2013	

   - Minor correction from *ptset_type to ptset_type in argument of cg_ptset_write in Point Sets of MLL documentation.
.. topic:: 26 Feb 2013	

   - Added AdditionalFamilyName_t node documentation to structures.html, sids and filemap.
.. topic:: 23 Feb 2013	

   - Updated the CGNStools documentation.
Added external link image to places it was missing.
New Parallel CGNS capability.
.. topic:: 15 Feb 2013	

   - Introduced Version 3.2 (beta).
Added AdditionalFamilyName_t under BC_t, Zone_t, and ZoneSubRegion_t, and added FamilyName_t under Family_t (a hierarchy of families is now possible); according to CPEX 0033 and 0034.
Added new cubic elements in Conventions, according to CPEX 0036.
.. topic:: 15 Feb 2013	

   - Changes associated with update to 3.1.4.
Updated MLL to version 3.1.15: One set of changes is in BC and include new description under location, as well as under "Notes: (see CPEX 0031)". Another change is in File Operations to the default for CG_CONFIG_COMPRESS.
Added new function, cg_precision, to read precision (32 or 64 bit) in the MLL File Operations.
Updated SIDS to version 3.1.8: Changes are in BC and include modified table describing usage of GridLocation vis CellDimension under BC_t.
Updated CGNSTools to version 3.1.2: Added new Tools description under CGNSTools.
.. topic:: 11 Dec 2012	

   - Posted draft minutes from the December 10, 2012 (PDF) Steering Committee telecon.
.. topic:: 25 Oct 2012	

   - Posted draft minutes from the October 23, 2012 (PDF) Steering Committee telecon.
.. topic:: 28 Sep 2012	

   - Posted draft minutes from the September 25, 2012 (PDF) Steering Committee telecon.
.. topic:: 29 Aug 2012	

   - Corrected the description of the cg_where MLL call in section on Navigating a CGNS File.
.. topic:: 31 Jul 2012	

   - Added reminder that max number for DataDimension is 12 for Data Arrays.
.. topic:: 01 May 2012	

   - Posted draft minutes from the April 24, 2012 (PDF) Steering Committee telecon.
.. topic:: 16 Mar 2012	

   - Posted draft minutes from the March 13, 2012 (PDF) Steering Committee telecon.
.. topic:: 3 Feb 2012	

   - Changes associated with new MLL doc number 3.1.12: Added section "Interfacing with CGIO" under "File Operations"; also updated Midlevel Sitemap to add "Interfacing with CGIO". Also corrected type for "pnts" under cg_sol_ptset_write, cg_subreg_ptset_write, and cg_discrete_ptset_write (should be const cgsize_t *, and not cgsize_t *).
.. topic:: 24 Jan 2012	

   - Posted draft minutes from the January 24, 2012 (PDF) Steering Committee telecon.
.. topic:: 17 Jan 2012	

   - Changed NormalListFlag to NormalListSize in MLL's cg_boco_info and updated MLL doc number from 3.1.10 to 3.1.11. Added LongInteger as possible type for DataType in Data Arrays and for datatype in Flow Solution Data.
.. topic:: 05 Jan 2012	

   - Added a link to FamilyBCDataSet_t in the File Mapping Manual Sitemap.
.. topic:: 04 Jan 2012	

   - Added AIAA Paper 2012-1264 ("Recent Updates to the CFD General Notation System (CGNS)") and associated Slides.
.. topic:: 03 Jan 2012	

   - Added CGNSTalk archives from 2010-2011.
.. topic:: 20 Dec 2011	

   - In File Mapping, added info about cgsize_t for 64-bit integers. In some places in text, I4 replaced by cgsize_t. Added "bit" to DataType description for DataArray_t. Many updated figures to reflect 64-bit integer changes (I4 changed to cgsize_t).
.. topic:: 09 Dec 2011	

   - Added statement under all Input/Output listings in the MLL noting that for Fortran calls, all integer arguments are integer*4 in 32-bit mode and integer*8 in 64-bit mode, along with a link to: 64-bit Fortran Portability and Issues.
.. topic:: 08 Dec 2011	

   - Posted draft minutes from the December 06, 2011 (PDF) Steering Committee telecon.
.. topic:: 21 Nov 2011	

   - Minor change: removal of link to stale ISO page on Charter background page.
.. topic:: 24 Oct 2011	

   - Minor corrections in CGIO docs (pdf file also updated due to missing figure reference), Midlevel docs, and Sitemap.
.. topic:: 31 Aug 2011	

.. topic::    - Posted draft minutes from the August 30, 2011 (PDF) Steering Com
   -    mittee telecon. (Other Minutes from April 19, 2011 (PDF) and June 7, 2011 (PDF) are also available.)
.. topic:: 11 Aug 2011	

   - Added minor clarification in Element Connectivity in the Mid Level documentation, regarding global numbering system to insure that every element within a zone has a unique number.
.. topic:: 06 Jul 2011	

   - Corrected index range in the documentation for NFaceElements in Example - NGON_N and NFACE_n Element Types in the SIDS. Also removed typo in the PDF version of the SIDS (note 8 in section 8.4).
.. topic:: 07 Jun 2011	

   - Updated the list of major changes in the SIDS.
.. topic:: 06 Jun 2011	

   - In MLL, corrected the fact that error_message is a const char (not char) in Error Handling.
In MLL, added clarity that in Fortran, float values are Real*4, in: Special Boundary Condition Properties, Gravity, Axisymmetry, Rotating Coordinates, Special Grid Connectivity Properties.
In MLL, added clarity that for RotationAngle, if rotating about more than 1 axis, then it is done in a particular order in Special Grid Connectivity Properties.
In SIDS, added clarity that if rotating about more than 1 axis, then it is done in a particular order in Periodic_t and in Data-Name Identifiers for Rigid Grid Motion.
In SIDS, corrected GridLocation definitions for ZoneSubRegion_t.
.. topic:: 28 Apr 2011	

   - In SIDS, added ZoneSubRegion_t node under Zone_t (mistakenly left out) in Zone_t. Also minor descriptor change regarding file mapping in intro.
.. topic:: 26 Apr 2011	

   - Minor changes to Charter, Overview document, and User's Guide to refer to CGIO rather than ADF, to refer to 3.1 as the latest version, and to update some stale references.
.. topic:: 25 Apr 2011	

   - Reorganized File Mapping documentation to separate context from content. SIDS-to-ADF File Mapping Manual changed to SIDS File Mapping Manual, which contains context. The content is now in ADF Implementation, HDF5 Implementation and Python Implementation.
SIDS, SIDS File Mapping and MLL documentation all updated to include CPEX 0027 (Time-dependent Connectivities), CPEX 0030 (Regions) and CPEX 0031 (General SIDS Improvements).
Added CGIO User's Guide which documents the low-level interface replacement for the ADF Core routines. The CGIO calls work for both ADF and HDF5.
.. topic:: 23 Mar 2011	

   - Added cg_boco_gridlocation_read and write functions to Mid-Level Library.
.. topic:: 04 Mar 2011	

   - Corrected document version numbers of the Mid-Level Library and SIDS online pages.
.. topic:: 03 Mar 2011	

   - Re-posted the correct version of new SIDS-to-Python file mapping manual (PDF only). This is Version 3.1.1, corresponding to CGNS Version 3.1.
.. topic:: 02 Mar 2011	

   - Posted draft minutes from the March 2, 2011 Steering Committee telecon. (PDF).
Posted new SIDS-to-Python file mapping manual (PDF only).
Updated version numbering for User's Guide, SIDS-to-ADF, and SIDS-to-HDF documents (no other changes to the documents), to reflect the release of CGNS Version 3.1.
.. topic:: 01 Mar 2011	

   - In Mid-Level Library, added information in File Operations about file_type = CG_FILE_ADF2, which can be used to write a Version 2.5 file from Version 3 when compiled in 32-bit.
.. topic:: 25 Feb 2011	

   - Made Version 3.1 the current official document release, moved 2.5 to "prior version" status.
.. topic:: 25 Feb 2011	

   - Modified Mid-Level Library:
Moved PYRA_13 in list to come after MIXED in Typedefs.
Moved Acquiring the Software and Documentation and Organization of This Manual sections to come first.
Minor correction of ParentData in cg_parent_data_write and cg_parent_data_partial_write to no longer be slanted typeface (because it is input type) in Element Connectivity section.
New Document Version is 3.1.4, corresponding to CGNS Version 3.1.
.. topic:: 23 Feb 2011	

   - Modified Mid-Level Library:
Added particular changes of "int" to "cgsize_t" throughout.
Added new sections on 64-bit C and Fortran Portability and Issues.
Added references to xxxxNull and xxxxUserDefined under Typedefs.
New Document Version is 3.1.3, corresponding to CGNS Version 3.1.
Modified SIDS Document:
Changed description of BCType_t slightly, to clarify the simple and compound types.
Added section Model Type Structure Definition.
Corrected ModelTypeNull and ModelTypeUserDefined listings (where enumerated values are a subset of the ModelType_t enumeration).
New Document Version is 3.1.2, corresponding to CGNS Version 3.1.
.. topic:: 04 Feb 2011	

   - Modified Mid-Level Library:
Changed Null to CG_Null and UserDefined to CG_UserDefined, and added comment under General Remarks about their usage.
New Document Version is 3.1.2, corresponding to CGNS Version 3.1.
Modified SIDS Document:
Changed Null to xxxxNull and UserDefined to xxxxUserDefined, as appropriate.
Also made sure that the xxxxNull is listed first, and the xxxxUserDefined is listed second.
New Document Version is 3.1.1, corresponding to CGNS Version 3.1.
.. topic:: 01 Feb 2011	

   - Modified doc home page to change mention of ADFviewer to CGNSview.
Modified User's Guide
Changed references of ADFviewer to CGNSview.
Updated code snippet examples to reflect changes in new UserGuideCodeV3.1, including changes of MODE_READ to CG_MODE_READ (for example) in cg_open calls.
Added mention of cg_error_handler.
Changes to user/index.html, faq.html, intro.html, additional.html, started.html, trouble.html.
New Document Version of Guide is 1.1.13, corresponding to CGNS Version 3.1.
Modified Mid-Level Library
Added new table of Typedef Name Access Functions under General Remarks.
Added description of cg_elements_partial_write.
Added descriptions of cg_save_as, cg_set_file_type, cg_get_file_type, cg_error_handler, cg_set_compress, cg_get_compress, cg_set_path, and cg_add_path.
New Document Version is 3.1.1, corresponding to CGNS Version 3.1.
On Sitemap for CGNS Tools and Utilities, updated old ADFviewer to new CGNSview, along with relevant new information.
Major update of CGNS tools and utilities, including switch from use of ADFviewer to CGNSview; New Document Version is 2.0.
.. topic:: 11 Jan 2011	

.. topic::    - Caught up with postings of telecon minutes. Added CGNS Tutorial
   -    slides from Orlando Jan 2010. Added 2008-2009 CGNSTalk archives.
.. topic:: 26 May 2009	

   - In the Applications Software section of the CGNS Overview and Entry-Level Document, changed the contact person for notification about new CGNS applications.
In the SIDS document, deleted the contact info for questions about the SIDS, since it was no longer valid, and is now covered by the CGNStalk mailing list.
.. topic:: 22 May 2009	

   - Posted draft minutes from the May 20 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 21 May 2009	

   - In the Accessing a Node description in the "Navigating a CGNS File" section of the Mid-Level Library document, corrected an error in the syntax for the cg_gopath_f Fortran routine. The last two arguments were reversed. Thanks to Richard McDonald at the USGS for the correction.
.. topic:: 20 May 2009	

   - In the Steering Committee Charter, deleted the list of current member organizations in the Organization/Bylaws section. This is now available at the CGNS web site.
.. topic:: 12 May 2009	

   - In the Zone Information description in the "Structural Nodes" section of the Mid-Level Library document, added a sentence emphasizing that zones must be named alphanumerically to ensure proper retrieval.
.. topic:: 6 Apr 2009	

   - Posted draft minutes from the Apr 1 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 14 Jan 2009	

   - Modified the CGNS Steering Committee Charter to delete Pacific Northwest National Laboratory external link and add Stony Brook University external link to the list of current member organizations.
.. topic:: 9 Jan 2009	

   - Posted draft minutes from the Jan 7 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 19 Nov 2008	

   - Posted draft minutes from the Nov 5 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 9 Oct 2008	

   - Added AIAA Paper 2008-0479, titled "Benchmarking the CGNS I/O Performance," by Thomas Hauser, presented at the 46th AIAA Aerospace Sciences Meeting and Exhibit. [HTML, PDF (318K, 8 pages)]
.. topic:: 23 Sep 2008	

   - Posted draft minutes from the Sep 10 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 11 Sep 2008	

   - Modified the description of the Elements_t structure in the SIDS to modify how NGON_n and NFACE_n are used to define general polyhedral elements. Each face of an element (except for boundary faces) must be shared by another element; faces may not be duplicated in NGON_n with opposite orientations. The sign of the face number for a particular polyhedral element in NFACE_n determines the direction of its normal with respect to that element - positive for outward, negative for inward. Also modified the NGON_n/NFACE_n example for consistency with the above change.
.. topic:: 17 July 2008	

   - Modified each page to use server-side includes for adding the footer.
.. topic:: 11 July 2008	

   - Posted draft minutes from the July 2 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 19 June 2008	

   - Modified the description of the Elements_t structure in the SIDS to incorporate the new definition of the NGON_n element type, and add the NFACE_n element type. Also added examples illustrating their use.
.. topic:: 17 June 2008	

   - In the Typedefs section of the Mid-Level Library documentation, added PYRA_13 and NFACE_n to the list of supported key words for ElementType_t.
.. topic:: 27 May 2008	

   - Posted draft minutes from the May 7 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 14 May 2008	

   - In the SIDS document, added a PYRA_13 element to the description of the unstructured grid element numbering conventions for pyramid elements.
Made a minor change in the Getting Started section of the User's Guide to CGNS, involving the use of PointList or PointRange with GridLocation set to FaceCenter.
.. topic:: 12 Mar 2008	

   - In the CGNS Tools and Utilities, modified the description of ADF_Edit to note that it's been superseded by the more capable ADFviewer.
In the Overview and Entry-Level Document, removed references to the utility ADF_Edit, in favor of ADFviewer.
.. topic:: 7 Mar 2008	

   - Modified the User's Guide to CGNS, primarily in the section on writing boundary conditions for an unstructured grid to illustrate the recommended procedure using ElementList, rather than PointList with GridLocation=FaceCenter. Also removed references to the utility ADF_Edit, in favor of ADFviewer.
.. topic:: 8 Feb 2008	

   - Added HTML versions of all the PDF attachments to meeting and telecon minutes.
.. topic:: 29 Jan 2008	

   - Added HTML versions of (almost) all the slide presentations.
.. topic:: 23 Jan 2008	

   - Added HTML versions of the following papers.
.. topic:: "Advances in the CGNS Database Standard for Aerodynamics and CFD" (AI
   - AA Paper 2000-0681)
.. topic:: "CFD General Notation System (CGNS): Status and Future Directions" (A
   - IAA Paper 2002-0752)
.. topic:: "Benchmarking Parallel I/O Performance for Computational Fluid Dynami
   - cs Applications" (AIAA Paper 2005-1381)
.. topic:: 18 Jan 2008	

   - Posted draft minutes from the Jan 6 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 5 Dec 2007	

   - Added an "external link" symbol (external link symbol) to all links to non-NASA sites, per NASA policy.
.. topic:: 29 Nov 2007	

   - Posted draft minutes from the Nov 28 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 7 Nov 2007	

   - Modified the description of the TurbulenceModel_t structure to add references to the specific models that correspond to the TurbulenceModelType names, and to add a recommendation for handling subsequent changes to the models.
.. topic:: In the User's Guide to CGNS, added a note that it was originally publ
   - ished as NASA/TM-2001-211236, October 2001.
.. topic:: 9 Oct 2007	

   - Modified the list of current member organizations in the CGNS Steering Committee Charter to reflect the name change of Thaerocomp Technical Corporation to TTC Technologies.
.. topic:: 19 Sep 2007	

   - Posted minutes from the Sept 12 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 14 Sep 2007	

   - Due to the release of CGNS Version 2.5, the CGNS documentation has been moved as shown below:
CGNS Version 2.5
index.html
CGNS Version 2.4
rel2.4/index.html
Documentation for CGNS Version 2.3 has been deleted.
Updated the Overview and Entry-Level Document to reflect the release of CGNS Version 2.5.
In the SIDS document, modified the description of the GridConnectivity_t structure to clarify the use of CellListDonor and InterpolantsDonor for both structured and unstructured grids. Also added some General Interface Connectivity Examples.
Modified the CGNS Steering Committee Charter to add Concepts NREC external link to the list of current member organizations.
.. topic:: 11 July 2007	

   - Updated the SIDS document to include information on the newly-released AIAA Recommended Practice R-101A-2005, and made the PDF version of the Recommended Practice available.
.. topic:: 5 July 2007	

   - In the SIDS document, rearranged discussion of the AIAA Recommended Practice version of the SIDS, noting that it's out of date, and removed links to it on the CGNS documentation home page.
.. topic:: 19 June 2007	

   - Posted minutes from the May 22 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 26 Mar 2007	

   - Posted minutes from the Mar 21 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 30 Jan 2007	

   - Corrected a minor error in Mid-Level Library document, changing the error status names ALL_OK, ERROR, NODE_NOT_FOUND, and INCORRECT_PATH to CG_OK, CG_ERROR, CG_NODE_NOT_FOUND, and CG_INCORRECT_PATH, respectively.
.. topic:: 17 Jan 2007	

   - Corrected an error in SIDS document, in the description of the unstructured grid element numbering conventions for pyramid elements. For the PYRA_14 element, node 14 should be at the center of the quadrilateral face, not the center of the element.
Several modifications to the Mid-Level Library manual, for consistency with the current CGNS Version 2.5 beta.
New functions to check file validity and configure some internal CGNS library options.
Additional functions providing alternate ways to access a node.
Changes in the use of functions for partial writes of coordinate, element, and solution data. The result is now always the union of the existing and new data. As part of this, the functions cg_section_read_ext and cg_elements_read_ext are no longer needed and have been removed, and new functions cg_ElementPartialSize and cg_elements_partial_read have been added.
Corrected typo in the data type of the argument data in the Mid-Level Library function cg_free.
.. topic:: 30 Nov 2006	

   - Corrected error in the table at the top of the Export Utilities section. cgns_to_tecplot converts from CGNS to Tecplot, not the other way round.
.. topic:: 16 Oct 2006	

   - Corrected an error in the Mid-Level Library manual, in the argument list for cg_conn_write_short. Even though the specific cell connectivity data aren't needed, the name of the donor zone is still required. Thanks to Thorsten Schwarz for spotting the problem.
.. topic:: 11 Oct 2006	

   - Posted minutes from the Oct 4 CGNS Steering Committee telecon. (HTML, PDF).
In the CGNS Steering Committee Charter, added Tecplot external link to the list of current member organizations.
.. topic:: 25 Sep 2006	

   - Updated some links and contact points listed in the Applications Software section of the CGNS Overview and Entry-Level Document.
.. topic:: 5 Sep 2006	

   - In the CGNS Steering Committee Charter,
Added Thaerocomp to the list of current member organizations.
Added a paragraph in the Representation section about the responsibilities of individual Steering Committee members.
In the Mid-Level Library, modified the description of the size argument for the Zone Information routines, attempting to clarify the definition for unstructured grids.
In the SIDS,
Modified the description of VertexSize for the Zone_t structure to clarify its definition for unstructured grids.
Modified the description of the GridConnectivity_t structure to allow GridLocation to be either Vertex or FaceCenter for Abutting and Abutting1to1 interfaces.
.. topic:: 8 Aug 2006	

   - Posted minutes from the Aug 2 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 28 July 2006	

   - Various changes due to the new capability for rind data with unstructured grids.
In the SIDS document, changes to the descriptions and/or components of the following structures: Rind_t, GridCoordinates_t, Elements_t, FlowSolution_t, ArbitraryGridMotion_t, DiscreteData_t.
In the SIDS-to-ADF File Mapping Manual, changes to the descriptions of the Rind_t, GridCoordinates_t, and FlowSolution_t nodes, and to the figures for the GridCoordinates_t, Elements_t, and FlowSolution_t nodes. Corresponding changes were also made in the SIDS-to-HDF File Mapping Manual.
In the Mid-Level Library manual, changes in the Rind Layers section.
In the User's Guide to CGNS, wording changes in the sections describing a single-zone grid and flow solution for structured and unstructured grids, and in the Structured Zone Example in the "Overview of the SIDS" section.
Added the Mid-Level Library function cg_free, which frees memory allocated by the library for character data returned by some routines.
Made the following mods due to the SIDS change making zone connectivity donor information optional for generalized multizone interfaces.
Modified the description of the GridConnectivity_t structure in the SIDS document.
In the GridConnectivity node figure in both the SIDS-to-ADF and SIDS-to-HDF File Mapping Manual, changed the Cardinality of CellListDonor/PointListDonor from "1" to "0,1".
Added the function cg_conn_write_short in the Mid-Level Library Manual, to write generalized zone connectivity data without donor information.
In the SIDS document, added a sentence to the description of ElementRange for the Elements_t structure to clarify the use of the global numbering system.
.. topic:: 14 June 2006	

.. topic::    - Added slides from the special "CGNS Tutorial Session" at the 36t
.. topic::    -    h AIAA Fluid Dynamics Conference in San Francisco, California
   -    , June 5-8, 2006.
.. topic:: 17 May 2006	

   - Posted minutes from the May 10 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 13 Apr 2006	

   - Updated the paragraph in the Overview and Entry-Level Document about the status of the inclusion of CGNS as part of an ISO standard.
In the list of current member organizations in the CGNS Steering Committee Charter, changed the name "ICEM CFD Engineering" to "ANSYS-ICEM CFD".
.. topic:: 10 Apr 2006	

   - Updated some links and contact points listed in the Applications Software section of the CGNS Overview and Entry-Level Document.
.. topic:: 27 Mar 2006	

   - Added Pacific Northwest National Laboratory external link to the list of current member organizations in the CGNS Steering Committee Charter.
Posted minutes from the Mar 22 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 1 Mar 2006	

   - Corrected a couple of typos in the Time-Dependent Flow and Conventions for Data-Name Identifiers sections of the SIDS document, and in the Navigating a CGNS File section of the Mid-Level Library Manual (where FlowSolution had been written as FlowSolutions).
.. topic:: 3 Feb 2006	

   - In the Mid-Level Library Manual, corrected a typo in the name of the Fortran routine cg_array_read_as_f, used to read data arrays (the "_f" was left off).
.. topic:: 17 Jan 2006	

   - Updated (and alphabetized) the list of current member organizations in the CGNS Steering Committee Charter.
Posted minutes from the Jan 11 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 10 Jan 2006	

   - Corrected a typo in the PDF version of the SIDS document involving an escaped underscore. Thanks to Marc Poinot for spotting it.
.. topic:: 21 Dec 2005	

   - Updated all links to the NASA Privacy and Accessibility Policies to conform with the latest NASA requirement.
.. topic:: 15 Dec 2005	

   - In the SIDS document,
Added a paragraph at the start of the Introduction intended to better explain the importance and benefits of using CGNS.
Added a bit to the description of the RotatingCoordinates_t data structure to more clearly explain its use, and deleted the sentence saying that it doesn't cover cases where the zone interfaces are not perpendicular to the axis of rotation.
Made a few other changes in various places to correct typos and add clarification.
Thanks to Kurt Weber for his review of the updated AIAA Recommended Practice, and for suggesting these changes.
.. topic:: 7 Dec 2005	

   - Modified the User's Guide to CGNS to refer users to the CGNS site at SourceForge external link to download the source code examples.
.. topic:: 21 Nov 2005	

   - Eliminated most usage of images for equation elements throughout the HTML version of the CGNS documentation, in favor of the appropriate HTML character entities. E.g., instead of using a GIF image to represent the Greek letter rho, the character entity &rho; is used instead. Images were originally used because HTML browsers typically didn't support character entities for many of the symbols that were used. Current-generation browsers, however, are much better. Mozilla Firefox 1.0.7 supports all the character entities used in the CGNS documentation, and Microsoft Internet Explorer 6.0 supports all but a couple. See the list of standard HTML 4.0 character entities for Symbols and Greek Letters external link to see how they are displayed in your browser.
.. topic:: 17 Nov 2005	

   - Corrected typos in the Solution Data section of the Mid-Level Library manual. (GridLocation_t was mistakenly written as GridLocationType_t.)
.. topic:: 16 Nov 2005	

   - Corrected a minor cross-referencing error in the PDF version of the SIDS document.
.. topic:: 2 Nov 2005	

   - In the description of the Generalized Connectivity routines in the Mid-Level Library Manual, clarified the definitions of ndata_donor and donor_data.
.. topic:: 19 Oct 2005	

   - In the description of GridConnectivity_t, in the Multizone Interface Connectivity section of the SIDS document, modified the description of the use of GridLocation to clarify its allowed values for different types of interfaces.
.. topic:: 18 Oct 2005	

   - Added a couple of sentences in the Multizone Interface Connectivity and Boundary Conditions sections of the SIDS document to clarify that a given zone boundary segment is intended to be defined as either a boundary condition segment or a multizone connectivity segment, but not both.
.. topic:: 17 Oct 2005	

   - Updated the Elements and Documentation section of the Overview and Entry-Level Document to reflect the option of using HDF instead of ADF. (Thanks to Chris Rumsey for doing the update.)
.. topic:: 5 Oct 2005	

   - Posted minutes from the Oct 4 CGNS Steering Committee telecon. (HTML, PDF).
Added ERF Paper 31-107, titled "Application of CGNS software components for helicopter blade fluid-structure strong coupling," by M. Poinot, M. Costes, and B. Cantaloube, presented at the 31st European Rotorcraft Forum, Florence, Italy. [PDF (174K, 10 pages)]
.. topic:: 7 Sep 2005	

   - In the History section of the Overview document, added a sentence crediting ONERA, ICEM CFD, and AEDC for the addition of support for HDF5.
.. topic:: 6 Sep 2005	

   - Due to the release of CGNS Version 2.4, the CGNS documentation has been moved as shown below:
CGNS Version 2.4
index.html
CGNS Version 2.3
rel2.3/index.html
Documentation for CGNS Version 2.2 has been deleted.
Added the SIDS-to-HDF File Mapping Manual, created by Marc Poinot using the SIDS-to-ADF File Mapping Manual as a basis.
Updated the Overview and Entry-Level Document to reflect the release of CGNS Version 2.4, and the option of using HDF instead of ADF.
Modified the CGNS Steering Committee Charter to note the addition of the HDF5 option, change the license covering the allowed distribution and use of the CGNS software, and to update a few links.
Added a note in the Introduction section of the User's Guide about the option of using HDF instead of ADF as the underlying database manager.
Minor modifications to the SIDS document, in the Introduction, Conventions, Hierarchical Structures, Multizone Interface Connectivity, and Boundary Conditions sections, due to the option of using HDF instead of ADF.
Minor modifications to the Mid-Level Library document, in the Introduction, General Remarks, Opening and Closing a CGNS File, and Navigating a CGNS File sections, due to the option of using HDF instead of ADF.
Minor modifications to the SIDS-to-ADF File Mapping Manual, in the Brief Description of CGNS, CGNS Documentation, and Summary Description of ADF, sections, due to the option of using HDF instead of ADF.
Added a note to the list of CGNS Data Structures saying that the "File Mapping" links connect to the SIDS-to-ADF File Mapping Manual.
Added the SIDS-to-HDF File Mapping Manual to the lists in the instructions for downloading the HTML and LaTeX source files.
Added the SIDS-to-HDF File Mapping Manual to the document sitemaps.
.. topic:: 23 Aug 2005	

.. topic::    - Posted slides CFD General Notation System, an overview of the CG
.. topic::    -    NS project and its current status, presented by Bruce Wedan o
   -    f ANSYS/ICEM CFD at NASA Ames, Jan 2005. [PowerPoint (345K, 46 pages)].
In the Mid-Level Library manual, added a paragraph to the description of the function cg_bcdata_write about writing the boundary condition data itself.
.. topic:: 14 Jul 2005	

   - Modified the information on the CGNS Documentation Home Page about the CGNStalk mailing list, due to the move to a new list server.
.. topic:: 20 Jun 2005	

   - Updated the documentation for consistency with CGNS version 2.4. In the SIDS document this includes:
GridConnectivityProperty_t has been added to the GridConnectivity1to1_t data structure.
GridLocation_t, PointRange, and PointList have been added to the BCDataSet_t data structure, allowing boundary conditions to be specified at locations different from those used to defined the BC patch. An example of this has also been added.
Data structures have been added to FlowEquationSet_t for describing the electric field, magnetic field, and conductivity models used for electromagnetic flows. Corresponding recommended data-name identifiers have also been added.
RotatingCoordinates_t has been added to the Family_t data structure.
A BCDataSet_t list has been added to the FamilyBC_t data structure, allowing specification of boundary condition data arrays for CFD families.
GridLocation_t, PointRange, PointList, FamilyName_t, UserDefinedData_t, and Ordinal have been added to the UserDefinedData_t data structure.
The DimensionalUnits_t and DimensionalExponents_t structures have been expanded to include units for electric current, substance amount, and luminous intensity.
In the SIDS-to-ADF File Mapping Manual:
Details have been added for the new nodes AdditionalUnits_t, AdditionalExponents_t, EMElectricFieldModel_t, EMMagneticFieldModel_t, EMConductivityModel_t.
The description of ListLength for the BCDataSet_t node has been modified due to the addition of GridLocation_t to the BCDataSet_t structure.
Minor modifications to some of the File Mapping Figures due to the addition of optional child nodes to some nodes, primarily affecting Cardinality values.
Added new child nodes in the GridConnectivity1to1, BCDataSet, FlowEquationSet, Family, and UserDefinedData figures.
Added new figures for the DimensionalExponents, DimensionalUnits, EMElectricFieldModel, EMMagneticFieldModel, EMConductivityModel, and FamilyBC nodes.
And in the Mid-Level Library manual:
In the list of Typedefs, added the typedefs ElectricCurrentUnits_t, SubstanceAmountUnits_t, and LuminousIntensityUnits_t, and added some new key words to the ModelType_t typedef.
Modified the description of the routines for reading/writing dimensional units and exponents due to the addition of electric current, substance amount, and luminous intensity.
Added routines for reading/writing point sets (i.e., PointRange and PointList nodes).
For user-defined data, added detail about reading/writing point set information.
Added a routine for writing a partial set of grid coordinates.
Added new routines related to element connectivity, including routines for reading/writing partial lists of element and parent data.
Added a routine for writing a partial flow solution.
Added routines for reading/writing special grid connectivity information for 1-to-1 grid connectivity.
Added detail about reading/writing point set information to BCDataSet_t nodes that are children of a BC_t node.
Added routines for reading/writing BCDataSet_t nodes for a CFD family.
Added a routine for reading electromagnetic equation set info, and added types for electromagnetic models.
.. topic:: 6 Jun 2005	

   - Posted minutes from the May 25 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 27 May 2005	

   - Updated some links and contact points listed in the Applications Software section of the CGNS Overview and Entry-Level Document.
.. topic:: 26 May 2005	

   - Modified the Organization/Bylaws section of the CGNS Steering Committee Charter to allow the appointment of a Vice-Chairperson.
.. topic:: 22 Mar 2005	

   - Posted minutes from the Mar 16 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 4 Feb 2005	

   - Added AIAA Paper 2005-1381, titled "Benchmarking Parallel I/O Performance for Computational Fluid Dynamics Applications," by P. D. Pakalapati and T. Hauser, presented at the 43rd AIAA Aerospace Sciences Meeting and Exhibit. [PDF (3.6M, 8 pages)]
.. topic:: 24 Jan 2005	

   - Corrected an error in the Mid-Level Library manual, in the description of the data conversion routines cg_conversion_write and cg_conversion_read. The scale and offset factors are stored in a two-element array, not as separate scalars.
Corrected an error in the SIDS document, in the Elements_t data structure examples. The examples included DataArray_t data structures defining ParentData for 3-D elements, where it doesn't apply.
.. topic:: In the list of :issue:`CGNS-related` conference papers, added R. Magn
   - an as an author for AIAA Paper 2005-0334. Apologies for inadvertantly omitting him in the original update.
.. topic:: 19 Jan 2005	

   - Added AIAA Paper 2005-0334, titled ":issue:`CGNS-Based` Data Model for Turbine Blade Optimization," by H. Iepan, F. Guibault, M.-G. Vallet, and R. Magnan, presented at the 43rd AIAA Aerospace Sciences Meeting and Exhibit. [PDF (379K, 11 pages)]
.. topic:: 18 Jan 2005	

   - Posted minutes from the Jan 12 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: Added AIAA Paper 2005-1155, titled "Checking CFD interfaces in a mult
   - i-disciplinary workflow with an XML/CGNS compiler" by M. Poinot, E. Montreuil, and E. Henaux, presented at the 43rd AIAA Aerospace Sciences Meeting and Exhibit. [PDF (662K, 11 pages)]
.. topic:: 19 Nov 2004	

   - Corrected (as Marc Poinot put it) the "smallest typo ever known", in the "Deforming Grid Motion" example in the Time-Dependent Flow section of the SIDS document. Thanks to Marc for spotting this.
Modified the Steering Committee Charter to add Utah State University, Stanford University, and ANSYS-CFX as Steering Committee members.
Posted minutes from the Nov 17 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 20 Oct 2004	

   - Corrected an error in the section on Unstructured Grid Element Numbering Conventions in the SIDS document. For pyramid elements, the oriented edges for face F4 were listed as E6,E8,-E7, and the correct values are E3,E8,-E7. Thanks to Alan Sayre for spotting this.
.. topic:: 6 Oct 2004	

   - Added SoundIntensityDB (sound intensity level in decibels) and SoundIntensity (sound power per unit area) to the list of recommended flow solution data-name identifiers.
.. topic:: 30 Sep 2004	

   - Posted minutes from the Sep 28 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 29 Sep 2004	

   - Added files and instructions for downloading and using the LaTeX source for the CGNS documentation.
.. topic:: 7 Jul 2004	

   - Posted minutes from the June 30 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: Added AIAA Paper 2004-2142, titled "Impact of CGNS on CFD Workflow" b
   - y M. Poinot, C. L. Rumsey, and M. Mani, presented at the 34th AIAA Fluid Dynamics Conference and Exhibit. [PDF (729K, 12 pages)]
.. topic:: 22 Jun 2004	

   - Added AIAA Paper 2004-1088, titled "Parallel I/O for the CGNS system" by Th. Hauser, presented at the 42nd AIAA Aerospace Sciences Meeting and Exhibit. [PDF (1.5M, 11 pages)]
.. topic:: 2 Jun 2004	

   - Removed the wording "in the same manner as grid connectivity" in the description of the BC_t node in the SIDS-to-ADF File Mapping Manual, that was inadvertantly left in when the documentation was updated with the release of CGNS Version 2.3.
.. topic:: 18 May 2004	

   - Changed the description of Ordinal in the Mid-Level Library manual to say that it may be any integer value, and is not limited to values > 0.
.. topic:: 2 Apr 2004	

   - Posted minutes from the Mar 25 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 26 Mar 2004	

   - Due to the release of CGNS Version 2.3, the CGNS documentation has been moved as shown below:
CGNS Version 2.3
index.html
CGNS Version 2.2
rel2.2/index.html
Documentation for CGNS Version 2.1 has been deleted.
Updated the Overview document to reflect the release of CGNS Version 2.3.
.. topic:: 19 Mar 2004	

   - Removed the web page showing access stats for the CGNS documentation web pages. The widespread use of indexing robots for search engines, and the local use of link validation tools, have made the access stats pretty meaningless.
.. topic:: 13 Feb 2004	

   - Changed the description of the BC_t data structure in the SIDS manual to reflect the addition of ElementRange and ElementList.
In the Mid-Level Library manual, modified the description of the routines related to the Boundary Condition Type and Location to reflect the addition of ElementRange and ElementList in the BC_t structure.
In the File Mapping manual, modified the BC_t figure to reflect the addition of ElementRange and ElementList.
In the User's Guide to CGNS, modified the "Getting Started" section to reflect the addition of ElementRange and ElementList in the BC_t structure.
.. topic:: 29 Jan 2004	

   - Changed names of some .gif files used in the HTML version of the SIDS document, to avoid file name conflicts on Windows systems, which (unfortunately) uses case-insensitive file names.
.. topic:: 13 Jan 2004	

   - Updated CGNS Steering Committee Charter.
Posted minutes from the Jan 7 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 24 Nov 2003	

   - Posted minutes from the Nov 20 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 24 Sep 2003	

   - Posted minutes from the Sep 18 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 12 Sep 2003	

   - Corrected typos in the Grid Connectivity section of the Mid-Level Library manual. (GridLocation_t was mistakenly written as GridLocationType_t.)
.. topic:: 4 Jun 2003	

   - Added an alphabetical list of data structures, with links to the appropriate sections in the various manuals.
.. topic:: 2 Jun 2003	

   - Posted minutes from the May 29 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 20 May 2003	

   - Added documentation for the CGNS Tools and Utilities, including ADFviewer, CGNSplot, and other utilities included in the CGNStools package.
.. topic:: 13 May 2003	

   - Due to the release of production Version 2.2 of the CGNS software, the CGNS documentation has been moved as shown below:
Software Release 2.2
index.html
Software Release 2.1
rel2.1/index.html
Documentation for Software Release 2.0 has been deleted.
Updated the Overview document to reflect the release of Version 2.2 of the CGNS software.
In the ADF User's Guide, modified the section on Acquiring the Software and Documentation to reflect the current use of SourceForge external link for distribution.
In the Mid-Level Library, modified the section on Acquiring the Software and Documentation to reflect the current use of SourceForge external link for distribution.
.. topic:: 29 Apr 2003	

   - Added site maps for the major CGNS documents.
.. topic:: 23 Apr 2003	

   - A search capability has been added. Words and/or phrases may be searched for in a specific document, or in all documents combined.
.. topic:: 27 Mar 2003	

   - Added a paragraph about the CGNStalk mailing list, with a link to the list archive.
Modified the description of cg_goto in the Mid-Level Library manual to note that when accessing a BCData_t node, the index must be set to either Dirichlet or Neumann.
.. topic:: 26 Mar 2003	

   - Posted minutes from the Mar 20 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 20 Mar 2003	

   - Added a sentence to the description of the ZoneBC_t data structure in the SIDS document to clarify that each boundary condition patch must be represented by a single BC_t data structure.
Expanded Note 2 for the BC_t data structure in the SIDS document, to add some discussion about the interpretation of the points defining a BC patch when GridLocation is set to Vertex.
.. topic:: 28 Jan 2003	

   - Added a separate page describing the AIAA Recommended Practice R-101-2002, with a more obvious link near the top of the CGNS Documentation Home Page.
.. topic:: 23 Jan 2003	

   - Added a paragraph to the CGNS Documentation Home Page, in the description of the SIDS document, noting that it represents a draft revision of the AIAA Recommended Practice, with links to the AIAA Online Store external link and to the PDF version of the Recommended Practice.
Updated the History and Current Status section to reflect the publication of the AIAA Recommended Practice.
In the SIDS document, corrected use of ParentData in the examples of the Elements_t data structure; change suggested by Diane Poirier an embarrassingly long time ago.
.. topic:: 22 Jan 2003	

   - Added a paragraph to the SIDS document noting that it represents a draft revision of the AIAA Recommended Practice, and made the PDF version of the Recommended Practice available.
.. topic:: 15 Jan 2003	

   - Posted minutes from the Jan 6 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 10 Dec 2002	

   - In the Overview document, added an entry for the CGNS Tools in the list of CGNS Utilities.
.. topic:: 6 Dec 2002	

   - Posted minutes from the Dec 4 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 26 Sep 2002	

   - Posted minutes from the Sep 18 CGNS Steering Committee telecon. (HTML, PDF).
In the General Remarks/Typedefs section of the Mid-Level Library manual, added the typedefs WallFunctionType_t, AreaType_t, and AverageInterfaceType_t.
.. topic:: 25 Sep 2002	

   - In the Mid-Level Library manual:
Corrected a minor error in the syntax of the C call for cg_geo_read.
Added several nodes to the list of nodes that can't be deleted by cg_delete_node.
Corrected the order of arguments for the routines used to read and write rotating coordinates.
In the HTML version of the SIDS document, fixed a typo in the definition of the OversetHoles_t data structure.
.. topic:: 20 Sep 2002	

   - Updated the documentation for consistency with Release 2.2, Beta 1, of the CGNS software. In the SIDS document this includes:
New data structures Axisymmetry_t, RotatingCoordinates_t, GridConnectivityProperty_t, Periodic_t, AverageInterface_t, BCProperty_t, WallFunction_t, Area_t, and Gravity_t.
New flow solution data-name identifiers for variables in rotating coordinate systems.
In the File Mapping Manual:
Detailed descriptions for the Axisymmetry_t, RotatingCoordinates_t, GridConnectivityProperty_t, Periodic_t, AverageInterface_t, BCProperty_t, WallFunction_t, Area_t, and Gravity_t nodes.
Added figures for the Axisymmetry_t, RotatingCoordinates_t, GridConnectivityProperty_t, Periodic_t, AverageInterface_t, BCProperty_t, WallFunction_t, Area_t, and Gravity_t nodes.
And in the Mid-Level Library manual:
Added the routine cg_delete_node for deleting a node.
Added routines for reading/writing the Axisymmetry_t, RotatingCoordinates_t, GridConnectivityProperty_t, BCProperty_t, and Gravity_t nodes.
.. topic:: 12 Sep 2002	

   - Added an FAQ in the User's Guide to CGNS about writing data sets associated with boundary conditions.
.. topic:: 6 Sep 2002	

   - In the PDF version of the Mid-Level Library manual, corrected a typo in the definition of "A" in Section 8.1.
.. topic:: 23 Aug 2002	

   - Fixed a typo in the equations for the lift and drag coefficients in the Conventions for Data-Name Identifiers section of the SIDS document. In the denominator, the area is Sref, not S.
.. topic:: 20 Aug 2002	

   - Corrected error in the SIDS document. In the GeometryReference_t data structure, GeometryFormat_t and GeometryFile_t are required, not optional.
.. topic:: 12 Aug 2002	

   - In the PDF version of the Mid-Level Library manual, corrected error in the input/output labeling for fn in the cg_open, cg_version, and cg_close routines.
.. topic:: 30 Jul 2002	

.. topic::    - Updated the Overview document to reflect the release of Version
   -    2.1 of the CGNS software on May 24, 2002.
.. topic:: 3 Jul 2002	

.. topic::    - Posted slides presented by John Steinbrenner of Pointwise, Inc.,
.. topic::    -    at the 8th International Conference on Numerical Grid Generat
   -    ion in Honolulu, Hawaii, June 2-6, 2002. [PDF (131K, 12 pages), PowerPoint (143K, 12 pages)].
.. topic:: 2 Jul 2002	

   - Posted minutes from the June 24 CGNS Steering Committee meeting. (HTML, PDF).
.. topic:: 31 May 2002	

   - Due to the release of production Version 2.1 of the CGNS software on May 24, the CGNS documentation has been moved as shown below:
Software Release 2.1
index.html
Software Release 2.0
rel2.0/index.html
.. topic:: 23 May 2002	

   - Corrected a minor error in the OversetHoles_t structure definition. PointRange and PointList are not both optional; one must be specified, but not both.
.. topic:: 22 May 2002	

   - Posted minutes from the May 15 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 20 May 2002	

   - In the Overview and Entry-Level Document, corrected the location of APPT in the tables in the CGNS-Compatible Applications section
.. topic:: 7 May 2002	

   - Added the document version number and the applicable CGNS software release number to the home or title page for each of the CGNS documents. Also added the CGNS logo, and in the HTML version changed the heading color to match the logo.
Updated and reorganized the Overview and Entry-Level Document.
Modified the definition of NormalListFlag for the Boundary Condition Type and Location routines in the Mid-Level Library manual.
Added a list summarizing the change history for the CGNS documentation.
.. topic:: 25 Mar 2002	

   - In the SIDS document, modified the introductory paragraph under Forces and Moments in the Conventions for Data-Name Identifiers section to note that the standard location for storing forces and moments is under a ConvergenceHistory_t node.
.. topic:: 20 Mar 2002	

   - Posted minutes from the Mar 13 CGNS Steering Committee telecon. (HTML, PDF).
.. topic:: 15 Mar 2002	

   - In the ADF User's Guide, added documentation for the routines ADF_Read_Block_Data and ADF_Write_Block_Data, for reading/writing a contiguous block of data to/from a node.
.. topic:: 13 Mar 2002	

   - Clarified/fixed the units for HeatOfFormationSymbol, HeatOfFormation, and VibrationalElectronEnergy in the lists of data-name identifiers for Chemical Kinetics Models and Flow Solution Quantities
.. topic:: 11 Mar 2002	

   - Changed the three non-PDF slide presentations to PDF files, supplied by Diane Poirier. (Thanks, Diane!)
.. topic:: 6 Mar 2002	

   - Added a page with the monthly access statistics for the CGNS documentation web site.
.. topic:: 14 Feb 2002	

   - In the SIDS document:
Modified the GasModelType_t enumeration, and added the ThermalRelaxationModel_t and ChemicalKineticsModel_t data structures, for supporting multi-species flows and chemistry.
Added flow solution data-name identifiers for multi-species flows and chemistry.
Added the UserDefinedData_t data structure for the storage of arbitrary user defined data in Descriptor_t and DataArray_t children without the restrictions or implicit meanings imposed on these node types at other node locations.
In the File Mapping Manual:
Added the detailed node descriptions for the ThermalRelaxationModel_t, ChemicalKineticsModel_t, and UserDefinedData_t nodes.
Added a UserDefinedData_t child to many of the File Mapping Figures
Added ThermalRelaxationModel_t and ChemicalKineticsModel_t children to the FlowEquationSet figure.
Added figures for the ThermalRelaxationModel, ChemicalKineticsModel, and UserDefinedData nodes.
In the Mid-Level Library Manual:
Added routines for including user-defined data.
Added material related to multi-species flows and chemistry..
Added routines for links in CGNS files.
In the User's Guide:
Added a bit to the section on Using Links.
.. topic:: 5 Feb 2002	

   - Added HTML versions of the minutes for all the CGNS Steering Committee Meetings and Telecons.
.. topic:: 4 Feb 2002	

   - Changed the attachments to the minutes from the Jan 14 CGNS Steering Committee meeting to PDF files, supplied by Diane Poirier. (Thanks, Diane!)
.. topic:: 31 Jan 2002	

   - Posted minutes from the Jan 14 CGNS Steering Committee meeting in Reno, NV, along with PDF files for the following presentations:
ISO Status (Ray Cosner)
Documentation (Theresa Benyo)
Extension Status (Chris Rumsey)
PyCGNS (Marc Poinot)
.. topic:: 25 Jan 2002	

   - Added AIAA Paper 2002-0752, titled "CFD General Notation System (CGNS): Status and Future Directions", presented at the 40th AIAA Aerospace Sciences Meeting and Exhibit. [PDF (289K, 13 pages)]
.. topic:: 23 Jan 2002	

   - Added the CGNS Steering Committee charter.
Changed the link for the software change history to point to the CGNS Software Revisions external link page on the cgns.sourceforge.net external link web site, which is more up-to-date.
.. topic:: 14 Nov 2001	

   - Posted minutes from the Nov 6 CGNS Steering Committee telecon.
.. topic:: 2 Nov 2001	

   - Changed the cardinality of FamilyBC_t to (0,1). This affects:
the description of the FamilyBC_t node in the File Mapping Manual
the definitions of nFamBC and BC in the Mid-Level Library Manual.
Modified the docs to reflect the fact that the cardinality of GeometryReference_t is (0,N). This affects:
the description of the Family_t and GeometryReference_t structures in the SIDS Manual
the text for the Family Group nodes in the File Mapping Manual.
Added the FamilySpecified boundary condition type, for specifying boundary conditions for a family. This affects:
the list of typedefs in the Mid-Level Library Manual
the definition of bocotype in the Mid-Level Library Manual
the description of FamilyName for the BC_t structure in the SIDS Manual
the description of the BCTypeSimple_t structure and the table of Simple Boundary Condition Types in the SIDS Manual
the description of the Family_t structure in the SIDS Manual
Tried to clarify the definition of the family name, by adding to the description of FamilyName_t node in the File Mapping Manual.
.. topic:: 1 Nov 2001	

   - Added files and instructions for installing the HTML version of the CGNS documentation on a local system.
.. topic:: 10 Oct 2001	

   - In the File Mapping Manual, corrected the cardinality specified for the FamilyName_t node.
.. topic:: 26 Sep 2001	

   - In the SIDS document, fixed error in the units listed for the ideal gas constant in the tables of Data-Name Identifiers for Perfect Gas and Data-Name Identifiers for Flow Solution Quantities.
In the Mid-Level Library manual, fixed error in the description of the donor_datatype argument for the Generalized Connectivity functions.
.. topic:: 17 Sep 2001	

   - Posted minutes from the Sep 6 CGNS Steering Committee telecon.
.. topic:: 6 Sep 2001	

   - Posted minutes from the June 12 CGNS Steering Committee Meeting in Anaheim, CA. (And, I apologize for the delay.)
.. topic:: 23 Aug 2001	

   - The User's Guide to CGNS has been updated, with new sections on time-dependent data and guidelines for writing and reading PLOT3D data in CGNS files.
.. topic:: 21 Aug 2001	

   - Corrected an couple of errors in the File Mapping Manual. The InwardNormalIndex is actually a vector with IndexDimension elements, and the name of the GeometryEntity_t node is user defined, not GeometryEntity.
.. topic:: 10 Jul 2001	

   - In the Mid-Level Library manual, changed to a slanted red font for the output variables, to better distinguish them from the input variables.
.. topic:: 27 Jun 2001	

   - Corrected a minor bug in the Flow Solution Example in the SIDS manual. The nondimensionalization factor for the momentum in the example is sqrt(p*rho), not sqrt(p/rho), and the corresponding ConversionScale values for MomentumX and MomentumY are both 352.446.
.. topic:: 17 Apr 2001	

   - Reorganized the Mid-Level Library manual, and created a PDF version. The content is basically the same as the previous version, but mostly follows the organization used in the Detailed CGNS Node Descriptions section of the File Mapping Manual.
Converted the hard-copy version of the ADF User's Guide to LaTeX, and added an HTML version.
.. topic:: 5 Apr 2001	

   - Posted minutes from the Mar 14 CGNS Steering Committee telecon.
.. topic:: 14 Mar 2001	

   - In the SIDS manual, added statements in the sections describing the BaseIterativeData_t and ZoneIterativeData_t data structures clarifying that iterative data stored in a CGNS database corresponds to values at the end of the associated iteration.
.. topic:: 7 Mar 2001	

   - In the SIDS manual, added a statement in the 2-D (Surface) Elements subsection clarifying the normal direction for 2-D unstructured grid elements.
In the SIDS manual, added a statement in the section on data-name identifiers for flowfield variables stating that for vector quantities, data-name identifiers for components in cylindrical and spherical coordinates are established, even when they're not explicitly listed.
.. topic:: 6 Mar 2001	

   - Included software change history in this "What's New?" page.
.. topic:: 22 Feb 2001	

   - Documentation web pages moved to .
Added HTML versions of the CGNS Overview and Entry-Level Document, A User's Guide to CGNS, and the SIDS-to-ADF File Mapping Manual. Also converted the hard-copy versions of the CGNS Overview and Entry-Level Document and the SIDS-to-ADF File Mapping Manual to LaTeX.
Corrected some errors in the description of ArbitraryGridMotion_t in the SIDS manual.
Updated the SIDS-to-ADF File Mapping Manual for consistency with the current version of the SIDS. Modified the description of the CGNSBase_t node, noting that current CGNS conventions require that it be located directly below the ADF root node, and added a description of the CGNSLibraryVersion_t node.

.. last line
