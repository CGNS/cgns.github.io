.. _cgns_api_c_par-ref:

The Parallel Mid-level Library (aka PMLL) is an extension of CGNS/MLL C and Fortran API to enable parallel aware file mapping.

##############################
CGNS Parallel C API
##############################

This document describes the use of parallel input/output within the CGNS library, 
and the associated routines. It utilizies MPI-IO within the context of HDF5 external 
link to do the IO, and thus the CGNS library must be built with this support.

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

*********************************************
Parallel Element Connectivity Data
*********************************************

.. _ElementConnectivityData-ref:

.. doxygengroup:: ElementConnectivityData
    :content-only:

******************************
Parallel Solution Data
******************************

.. _SolutionData-ref:

.. doxygengroup:: SolutionData
    :content-only:

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


