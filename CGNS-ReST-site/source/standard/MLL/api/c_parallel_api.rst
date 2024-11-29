.. _cgns_api_c_par-ref:

The Parallel Mid-level Library (aka PMLL) is an extension of CGNS/MLL C and Fortran APIs to enable parallel aware file mapping.

##############################
CGNS Parallel API Overview
##############################

This document describes parallel input/output (I/O) in the CGNS library and
the associated routines. It utilizes MPI-IO through the HDF5 library to support
parallel I/O operations. As a result, the CGNS library must be built with HDF5
to enable the parallel CGNS APIs.

******************************
Parallel File Operations
******************************

.. _ParallelFile-ref:

.. doxygengroup:: ParallelFile
    :content-only:

******************************
Parallel Grid Coordinate Data
******************************

.. _ParallelGridCoordinate-ref:

.. doxygengroup:: ParallelGridCoordinate
    :content-only:

*********************************
Parallel Particle Coordinate Data
*********************************

.. _ParallelParticleCoordinate-ref:

Parallel Particle Coordinates
________________________________________________

.. doxygengroup:: ParallelParticleCoordinate
    :content-only:

------

*********************************************
Parallel Element Connectivity Data
*********************************************

.. _ElementConnectivityData-ref:

.. doxygengroup:: ElementConnectivityData
    :content-only:

******************************
Parallel Flow Solution Data
******************************

.. note::
   The application is responsible for ensuring that the data type for the solution
   data matches that defined in the file; no conversions are done.

.. _SolutionData-ref:

.. doxygengroup:: SolutionData
    :content-only:

.. _ParallelParticleSolutionData-ref:

Parallel Particle Solution Data
________________________________________________

.. doxygengroup:: ParallelParticleSolutionData
    :content-only:

------

******************************
Parallel Array Data
******************************

.. _ArrayData-ref:

.. doxygengroup:: ArrayData
    :content-only:

*********************************************
Parallel Miscellaneous Routines
*********************************************

.. _ParallelMisc-ref:

.. doxygengroup:: ParallelMisc
    :content-only:


