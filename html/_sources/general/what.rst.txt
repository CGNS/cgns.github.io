.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _WhatIsCGNS:

What is CGNS?
=============

The CFD General Notation System (CGNS) provides a general, portable,
and extensible standard for the storage and retrieval of computational
fluid dynamics (CFD) analysis data. It consists of a collection of
conventions, and free and open software implementing those
conventions. It is self-descriptive, machine-independent,
well-documented, and administered by an international steering
committee. It is also an American Institute of Aeronautics and
Astronautics (AIAA) Recommended Practice.  The system consists of two
parts:

1. a standard format for recording the data,
2. a software that reads, writes, and modifies data in that format.
   
The format is a conceptual entity established by the documentation;
the software is a physical product supplied to enable developers to
access and produce data recorded in that format.

The CGNS system is designed to facilitate the exchange of data between
sites and applications, and to help stabilize the archiving of
aerodynamic data.  The data are stored in a compact, binary format and
are accessible through a complete and extensible library of functions.
The API (Application Program Interface) is platform independent and
can be easily implemented in C, C++, Fortran and Fortran90
applications.

**How can CGNS help you?**

 - It improves the longevity (archival quality) of data
 - It makes it easier to share data files between sites and collaborators
 - It is easily extendible to include almost any type of additional data you
   can think of

**How can you help CGNS?**

**CGNS genesis**

The CGNS project originated in 1994 as a joint effort
between Boeing and NASA, and has since grown to include many other
contributing organizations worldwide. In 1999, control of CGNS was
completely transferred to a public forum known as the CGNS Steering
Committee. This Steering Committee is made up of international
representatives from government and private industry. Additional
history on the development of CGNS is available :ref:`here <HistoryAndStatus>`.

**Main scope**

The principal target of CGNS is data normally associated with
compressible viscous flow (i.e., the Navier-Stokes equations), but the
standard is also applicable to subclasses such as Euler and potential
flows. The CGNS standard includes the following types of data:

 - Structured, unstructured, and hybrid grids
 - Flow solution data, which may be nodal, cell-centered, face-centered,
   or edge-centered
 - Multizone interface connectivity, both abutting and overset
 - Boundary conditions
 - Flow equation descriptions, including the equation of state, viscosity and
   thermal conductivity models, turbulence models, multi-species chemistry
   models, and electromagnetics
 - Time-dependent flow, including moving and deforming grids
 - Dimensional units and nondimensionalization information
 - Reference states
 - Convergence history
 - Association to CAD geometry definitions
 - User-defined data
   
Much of the standard and the software is applicable to computational
field physics in general. Disciplines other than fluid dynamics would
need to augment the data definitions and storage conventions, but the
fundamental database software, which provides platform independence,
is not specific to fluid dynamics.

**License**

All CGNS software is free. The
distribution and use of the CGNS software is covered by the following
license:

This software is provided "as-is", without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
   not claim that you wrote the original software. If you use this
   software in a product, an acknowledgment in the product
   documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must
   not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source
   distribution.  This license is borrowed from the zlib/libpng License,
   and supercedes the GNU Lesser General Public License (LGPL) which
   previously governed the use and distribution of the software.

**Reference**

We encourage anyone to freely use the CGNS logo when distributing or
documenting CGNS related information. The logo adds prestige and
credibility to web sites, publications, displays, announcements, and
activities. However, the use of the logo in such a way as to imply
approval, endorsement, or responsibility of the CGNS committee is
prohibited without written permission.

.. last line
