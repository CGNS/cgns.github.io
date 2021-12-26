.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _PMLLGeneral:
   
General Remarks
---------------

The Parallel CGNS mid-level library, or PMLL, is built on top of the collective
I/O support in HDF5 using MPI-IO. PMLL provides specialized routines
to open and close a file for parallel I/O and read and write grid
coordinates, element data, solution data, and general arrays in a
collective fashion. The PMLL functions
are prefixed with *cgp_*, and documented in :ref:`The CGNS/PMLL Software Library <PMLLdocumentation>`.

All additional accesses to the data use the standard serial Mid-Level Library (MLL)
functions. A typical use of the PMLL routines in a parallel I/O program
would be:

.. parsed-literal::

  cgp_open              --- open file for parallel I/O
  cg_base_write         --- create base and zone using MLL
  cg_zone_write
  cgp_coord_write       --- create coordinate dataset for parallel I/O
  cgp_coord_write_data  --- write the coordinates collectively
  cgp_close             --- close the file

An example Fortran and C program are given in :ref:`Example Program <PMLLexample>`.

A detailed discussion on the implementation may be found in the PDF paper
**An Efficient and Flexible Parallel I/O implementation for the CFD General
Notation System** by Horne, Bensen, and Hauser.

.. last line
