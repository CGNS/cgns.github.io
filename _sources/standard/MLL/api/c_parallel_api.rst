.. _cgns_api_c_par-ref:

The Parallel Mid-level Library (aka PMLL) is an extension of CGNS/MLL C and Fortran APIs to enable parallel aware file mapping.

.. note::
   Please refer to :ref:`MLLGeneralRemarks-ref` for details and conventions regarding
   the equivalent Fortran APIs, paying special attention to :ref:`CGNSFortranPort-ref`.

##############################
CGNS Parallel API Overview
##############################

This document describes parallel input/output (I/O) in the CGNS library and
the associated routines. It utilizes MPI-IO through the HDF5 library to support
parallel I/O operations. As a result, the CGNS library must be built with HDF5
to enable the parallel CGNS APIs.

.. cgns-group-function-summary:: ParallelFile File Operations
.. cgns-group-function-summary:: ParallelGridCoordinate Grid Coordinate Data
.. cgns-group-function-summary:: ParallelParticleCoordinate Particle Coordinate Data
.. cgns-group-function-summary:: ElementConnectivityData
.. cgns-group-function-summary:: SolutionData Flow Solution Data
.. cgns-group-function-summary:: ParallelParticleSolutionData Particle Solution Data
.. cgns-group-function-summary:: ArrayData
.. cgns-group-function-summary:: ParallelMisc Miscellaneous Routines
.. cgns-group-function-summary:: PointListData PointList Data


.. _ParallelFile-ref:

************************
Parallel File Operations
************************

.. doxygengroup:: ParallelFile
    :content-only:


.. _ParallelGridCoordinate-ref:

*****************************
Parallel Grid Coordinate Data
*****************************

.. doxygengroup:: ParallelGridCoordinate
    :content-only:


.. _ParallelParticleCoordinate-ref:

*********************************
Parallel Particle Coordinate Data
*********************************

.. doxygengroup:: ParallelParticleCoordinate
    :content-only:


.. _ElementConnectivityData-ref:

**********************************
Parallel Element Connectivity Data
**********************************

.. doxygengroup:: ElementConnectivityData
    :content-only:


.. _SolutionData-ref:

***************************
Parallel Flow Solution Data
***************************

.. note::
   The application is responsible for ensuring that the data type for the solution
   data matches that defined in the file; no conversions are done.

.. doxygengroup:: SolutionData
    :content-only:


.. _ParallelParticleSolutionData-ref:

*******************************
Parallel Particle Solution Data
*******************************

.. note::
   The application is responsible for ensuring that the data type for the solution
   data matches that defined in the file; no conversions are done.

.. doxygengroup:: ParallelParticleSolutionData
    :content-only:


.. _ArrayData-ref:

*******************
Parallel Array Data
*******************

.. doxygengroup:: ArrayData
    :content-only:


*******************************
Parallel Miscellaneous Routines
*******************************

.. _ParallelMisc-ref:

Miscellaneous Routines
________________________________________________

.. doxygengroup:: ParallelMisc
    :content-only:

.. _PointListData-ref:

PointList Data
________________________________________________

.. doxygengroup:: PointListData
    :content-only:
