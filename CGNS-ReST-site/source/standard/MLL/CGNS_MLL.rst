.. _api-label:

.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _StandardMLL:

.. index::
   single: standard; API; CGNS/MLL;

.. _MLLIntroduction:

CGNS/MLL - An API for C and Fortran applications
================================================

The **Mid-Level Library** (aka MLL) is an example implementation of the
:term:`CGNS/HDF5` file mapping providing both a C and a Fortran API.

**********************
Mid-Level Library
**********************

This document outlines a CGNS library designed to ease implementation of CGNS by
providing developers with a collection of handy I/O functions. Since knowledge of
the database manager and file structure is not required to use this library, it 
greatly facilitates the task of interfacing with CGNS.

The CGNS **Mid-Level Library** (aka MLL) is based on the TODO:ADDLINK (SIDS File Mapping Manual).
It allows reading and writing all of the information described in that manual
including grid coordinates, block interfaces, flow solutions, and boundary conditions.
Use of the mid-level library functions insures efficient communication between the
user application and the internal representation of the CGNS data.

It is assumed that the reader is familiar with the information in the TODO:ADDLINK (CGNS Standard Interface Data Structures (SIDS)), as well as the TODO:ADDLINK (SIDS File Mapping Manual). The reader is also strongly encouraged to read the TODO:ADDLINK (User's Guide to CGNS),
which contains coding examples using the Mid-Level Library to write and read simple files containing CGNS databases. 

.. toctree::
   api/general_remarks
   api/c_api

***************************
Parallel Mid-Level Library
***************************

The Parallel Mid-level Library (aka PMLL) is an extension of CGNS/MLL C and Fortran API to enable parallel aware file mapping.

.. toctree::
   api/c_parallel_api

This document was originally written by Diane Poirier of ICEM CFD Engineering for the CGNS Project Group.
