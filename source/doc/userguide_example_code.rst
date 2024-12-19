.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

Example Computer Codes
----------------------

The following computer codes are complete, workable versions of the codes mentioned in the text of this User's Guide (plus some that are not mentioned). They can be obtained from the CGNS site external link. They read and write very simple example CGNS files, in order to help the user understand the CGNS concepts as well as the usage of the API calls. Instructions for compiling them on LINUX systems is contained in comment lines in each program. The following codes are written in both FORTRAN and C. Note that these programs are very unsophisticated, purposefully for ease of readability. Real working codes would be written more generally, with more checks, and would not be as hardwired for particular cases. The codes are listed here by corresponding section.

Structured Grid
^^^^^^^^^^^^^^^

Single-Zone Structured Grid:
  - write_grid_str.f	   	writes grid
  - write_grid_str.c		writes grid (C-program example)
  - read_grid_str.f		reads grid

Single-Zone Structured Grid and Flow Solution
  - write_flowvert_str.f	   	writes vertex-based flow solution
  - read_flowvert_str.f		reads vertex-based flow solution
  - write_flowcent_str.f		writes cell centered flow solution
  - read_flowcent_str.f		reads cell centered flow solution
  - write_flowcentrind_str.f		writes cell centered flow solution with rind cells
  - read_flowcentrind_str.f		reads cell centered flow solution with rind cells

Single-Zone Structured Grid with Boundary Conditions
  - write_bc_str.f	   	writes PointRange boundary condition patches
  - read_bc_str.f		reads PointRange boundary condition patches
  - write_bcpnts_str.f		writes PointList boundary condition patches
  - read_bcpnts_str.f		reads PointList boundary condition patches

Multi-Zone Structured Grid with 1-to-1 Connectivity
  - write_grid2zn_str.f	   	writes 2-zone grid
  - read_grid2zn_str.f		reads 2-zone grid
  - write_con2zn_str.f		writes 1-to-1 connectivity for 2-zone example
  - read_con2zn_str.f		reads 1-to-1 connectivity for 2-zone example
  - write_con2zn_genrl_str.f		writes general 1-to-1 connectivity for 2-zone example
  - read_con2zn_genrl_str.f		reads general 1-to-1 connectivity for 2-zone example

Unstructured Grid
^^^^^^^^^^^^^^^^^

Single-Zone Unstructured Grid
	- write_grid_unst.f	   	writes grid
	- read_grid_unst.f		reads grid

Single-Zone Unstructured Grid and Flow Solution
	- write_flowvert_unst.f	   	writes vertex-based flow solution
	- read_flowvert_unst.f		reads vertex-based flow solution

Single-Zone Unstructured Grid with Boundary Conditions
	- write_bcpnts_unst.f	   	writes PointList boundary condition patches (FaceCenter)
	- read_bcpnts_unst.f		reads PointList boundary condition patches (FaceCenter)

General
^^^^^^^

Convergence History
	- write_convergence.f	   	writes convergence history
	- read_convergence.f		reads convergence history

Descriptor Nodes
	- write_descriptor.f	   	writes descriptor node under CGNSBase_t
	- read_descriptor.f		reads descriptor node under CGNSBase_t

Dimensional Data
	- write_dimensional.f	   	writes dimensional data to an existing grid + flow solution
	- read_dimensional.f		reads dimensional data from an existing grid + flow solution

Nondimensional Data
	- write_nondimensional.f	   	writes nondimensional data to an existing CGNS file
	- read_nondimensional.f		reads nondimensional data from an existing CGNS file

Flow Equation Sets
	- write_floweqn_str.f	   	writes flow equation information for structured example
	- read_floweqn_str.f		reads flow equation information for structured example

Time-Dependent Data
	- write_timevert_str.f	   	writes time-dependent flow soln (as Vertex) for structured example
	- read_timevert_str.f		reads time-dependent flow soln (as Vertex) for structured example

.. last line
