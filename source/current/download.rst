.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _SupportDownload:

Download
========

All CGNS files are stored on GitHub (https://github.com/CGNS). Issue tracking is located under
*Issues* of the same repository. Please star the repository if you find the software useful.

We also **strongly** recommend that you join the `CGNStalk <https://github.com/CGNS/CGNS/discussions/categories/cgnstalk>`_
Discussion Group. This forum is the primary
method to keep CGNS users updated on releases and other important information updates.
It is also used to discuss important problems/issues and obtain help from CGNS users.

What to Download
----------------
.. note::

   First and most importantly, we recommend that you read :ref:`DocUserGuide`. This guide also includes
   sample code (UserGuideCode) for helping to get started with CGNS.

For the up-to-date **development** source, visit `GitHub Development <https://github.com/CGNS/CGNS/tree/develop>`_.

.. code-block:: shell

  git clone https://github.com/CGNS/CGNS.git

For the **stable** source, visit `GitHub Stable <https://github.com/CGNS/CGNS/tree/master>`_.

.. code-block:: shell

  git clone -b master https://github.com/CGNS/CGNS.git

At the minimum, you will need to download and compile the CGNS library code. Compilation requires
an ANSI-compliant C99 compiler. The source code may be downloaded as a gzipped tar file.

Current Stable Release:
^^^^^^^^^^^^^^^^^^^^^^^

  The latest stable release can always be found at: `CGNS Latest Version <https://github.com/CGNS/CGNS/releases/latest>`_


Historical Stable Releases:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::

   Please see the release notes at: `CGNS Releases <https://github.com/CGNS/CGNS/releases>`_ 
   for CGNS versions 4.2.0 and up.


* :`CGNS Version 4.1.1 (Patch) <https://github.com/CGNS/CGNS/releases/tag/v4.1.1>`_:

  Patched version v4.1.1 addressed backward compatibility and tools compilation errors.

* :`CGNS Version 4.1.0 <https://github.com/CGNS/CGNS/releases/tag/v4.1.0>`_:

  | This version implements:
  |   - CPEX42 (Storing bounding box of a grid, CGNS-149)
  |   - CPEX43 (Family hierarchy as a tree, CGNS-180)

  CGNS switched to using HDF5 compact storage for smaller datasets.

  | The following APIs were removed:
  |   cgio_read_all_data, cgio_read_data, cgio_read_block_data
  |   cgio_read_all_data_f, cgio_read_data_f, cgio_read_block_data_f

  | These APIs should be used instead:
  |   cgio_read_all_data_type, cgio_read_data_type, cgio_read_block_data_type
  |   cgio_read_all_data_type_f, cgio_read_data_type_f, cgio_read_block_data_type_f

  See RELEASE.txt for additional bug fixes.

* :`CGNS Version 4.0.0 <https://github.com/CGNS/CGNS/releases/tag/v4.0.0>`_:

  **Background** [`1 <https://cgnsorg.atlassian.net/wiki/spaces/CGNS/pages/220463122/Resolve+issue+with+release+s+3.4.0+version+compatibility+the+4.0.0+release+and+forward+compatibility.>`_]: The CGNS versions are currently numbered as follows: "Version x.y, Revision z", or "Version x.y-z".The first number represents the "major" version number. **Within this number, the library maintains forward compatibility**.

  **Issue**: With the introduction of CPEX 0041 "NGON modification proposal", CGNS 3.4.0 broke the convention of maintaining forward compatibility within the major versioning of CGNS.

  Version 4.0.0 was released with CPEX 0041 implemented (essentially, this is CGNS 3.4.0 released as version 4.0.0).

* :`CGNS Version 3.4.1 (patch) <https://github.com/CGNS/CGNS/releases/tag/v3.4.2>`_:

  Patched version v3.4.1 removed CPEX 0041.

* :`CGNS Version 3.4.0 <https://github.com/CGNS/CGNS/releases/tag/v3.4.0>`_:

  In addition to numerous bug fixes, this version added new features: CPEX 40 Rind Plane Indexing, CPEX 41 NGON modification proposal, added support for NAG Fortran compilers, enforce the HDF5 version >= 1.8 is used in building HDF5, automatic detection and linking of szip and zlib if required by HDF5.

* :`CGNS Version 3.3.0 <https://github.com/CGNS/CGNS/releases/tag/v3.3.0>`_:

  This Version implements CPEX 0038 and 0039, adds new functionality to the parallel capability, and makes extensive changes related to the Fortran library.

  Important note for Fortran users: V3.3 removes the usage of "include cgnslib_f.h." Instead, from this release forward, one must now employ the module "use CGNS." Also, if using 64-bit integers, Fortran programs must declare the relevant 64-bit integers via, e.g., integer(cgsize_t) integer KIND.

* :CGNS Version 3.2.1:

  This Version 3.2 release partially integrates parallel I/O using HDF5 with MPI. It also implements the Hierarchy of families (CPEX 0033), Multiple families (CPEX 0034), and Cubic elements (CPEX 0036). Conversion programs to and from AFLR3, FAST, and TetGen have also been added to CGNStools.

  Release 3.2.1 implements the suggestions by Cambridge Flow Solutions to the CMake scripts and adds routines to set the MPI communicator for parallel I/O. There are also numerous updates and fixes to the test cases, tools and CGNStools utilities.

  .. note:

    CGNStools is no longer built automatically, you need to set the configure flag, --enable-cgnstools if using configure.

* :CGNS Version 3.1.4:

  It includes 64-bit integer capability and updated tools for viewing and editing CGNS files. When CGNS is built with HDF5 version 1.8 or later, HDF5 is now the default file type. (CGNS can always read or write both HDF5 and ADF file types.)

Older recent release versions are also available from https://github.com/CGNS/CGNS/releases.

Even earlier releases can be found in the archives: https://github.com/CGNS/CGNS_archives.


.. last line
