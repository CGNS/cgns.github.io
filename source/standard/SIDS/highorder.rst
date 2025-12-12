.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _HighOrderInterpolation:

High-Order Interpolation
========================

This section describes high-order polynomial interpolation for both grid elements and flow solutions.
The CGNS standard allows users to specify their own interpolation approach, enabling support for a wide variety of high-order computational methods.

Overview and Motivation
^^^^^^^^^^^^^^^^^^^^^^^^

The aim of high-order interpolation support is to cater for the large diversity of high-order methods by including a specification of the interpolation spaces in the CGNS file. This approach:

* Allows accurate representation of data in a range of popular interpolation spaces which could otherwise only be approximated
* Enables use of the native storage format of applications, leading to:

  * Simpler, more robust, and generic implementation of I/O drivers
  * More efficient I/O by straightforwardly dumping data blocks
  * Avoiding loss of precision for very specific point distributions

* Avoids the need to redefine the format for each new interpolation type or order
* Supports space-time methods and ALE computations by including time in the functional expressions

Currently, high-order intra-element interpolation is restricted to unstructured mesh computations, as structured meshes do not offer the possibility to individually list elements per order and do not support curved elements. Both modal and nodal interpolations are supported.

Basic Principles
^^^^^^^^^^^^^^^^

The CGNS standard for high-order interpolation follows these basic principles:

1. The element coordinate system per element type is a fixed convention (see :ref:`Parametric Coordinate Systems <parametric_coords>`)
2. For solution interpolation, for each element type and interpolation order, a separate interpolation specification is added, providing one of four choices:

   * The set of control points for Lagrange interpolants (:sidskey:`ParametricLagrange`)
   * The maximum degree of a Pascal polynomial space defined in parametric coordinates (:sidskey:`ParametricMonomialsPascal`)
   * The maximum degree of a Pascal polynomial space defined in Cartesian (non-parametric) coordinates (:sidskey:`CartesianMonomialsPascal`)
   * Use the same interpolation as the mesh geometry (:sidskey:`IsoParametric`)

3. The mesh is always defined using interpolations in parametric space by specifying control points
4. The interpolation is not supposed to be the same for the geometry as for the solution, unless explicitly specified via :sidskey:`IsoParametric`
5. In addition to spatial coordinates, time can be used as an independent variable for space-time methods

.. _InterpolationType_t:

Interpolation Type Enumeration: :sidskey:`InterpolationType_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`InterpolationType_t` specifies how the high-order interpolants for the solution are defined.

.. code-block:: sids

  InterpolationType_t := Enumeration(
    InterpolationTypeNull,
    InterpolationTypeUserDefined,
    ParametricLagrange,
    ParametricMonomialsPascal,
    CartesianMonomialsPascal,
    IsoParametric ) ;

The four interpolation types are:

:sidskey:`ParametricLagrange`
  Lagrange interpolation based upon a set of specified control point coordinates in parametric space for a standard interpolation space.

:sidskey:`ParametricMonomialsPascal`
  Modal interpolation functions in parametric coordinates, based on monomials according to the classical Pascal sets (triangle, tetrahedron).

:sidskey:`CartesianMonomialsPascal`
  Modal interpolation functions in a Cartesian coordinate system, centered on the element and parallel to the main axes. The interpolation functions are based on monomials according to the classical Pascal sets.

:sidskey:`IsoParametric`
  Uses the same interpolation functions for the solution as for the mesh geometry.

.. _parametric_coords:

Parametric Coordinate Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The parametric coordinate system is defined per element type. For standard element types, the parametric coordinates are:

* **Line elements** (BAR_2, BAR_3, etc.): Use parameter :math:`u \in [-1, 1]`
* **Triangular elements** (TRI_3, TRI_6, etc.): Use parameters :math:`(u, v)` with :math:`u, v \geq -1` and :math:`u + v \leq 1`
* **Quadrilateral elements** (QUAD_4, QUAD_8, QUAD_9, etc.): Use parameters :math:`(u, v) \in [-1, 1] \times [-1, 1]`
* **Tetrahedral elements** (TETRA_4, TETRA_10, etc.): Use parameters :math:`(u, v, w)` with :math:`u, v, w \geq -1` and :math:`u + v + w \leq 1`
* **Hexahedral elements** (HEXA_8, HEXA_20, HEXA_27, etc.): Use parameters :math:`(u, v, w) \in [-1, 1] \times [-1, 1] \times [-1, 1]`
* **Prismatic elements** (PENTA_6, PENTA_15, PENTA_18, etc.): Use triangular base :math:`(u, v)` and linear parameter :math:`w \in [-1, 1]`
* **Pyramidal elements** (PYRA_5, PYRA_14, etc.): Use parameters :math:`(u, v, w)` with specific coordinate system for pyramids

For space-time computations, the coordinate system is extended with one dimension by the tensor product of the spatial coordinate system with the parameter interval :math:`\tau \in [-1, 1]` in parametric time, which corresponds to the physical time slab :math:`[T_n, T_{n+1}]`.

Parametric Lagrange Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
~~~~~

Parametric Lagrange interpolation can be used for specifying both curved mesh elements and high-order solution fields. For elements, this convention allows redefinition of the position and order of control points with respect to the standard definitions for each :sidsref:`ElementType_t`. The standard definition continues to be used if no interpolation is explicitly specified.

Function Spaces
~~~~~~~~~~~~~~~

Lagrange interpolants require specification of both the control point locations and the function space :math:`\mathcal{V}`. The cardinality :math:`N` of the function space defines the number of control points that must be specified.

The Lagrange interpolant corresponding to control point :math:`\mathbf{u}_i` is denoted :math:`\lambda_i(\mathbf{u})`. Using an arbitrary set of basis functions :math:`\psi_j` for :math:`\mathcal{V}` (such that :math:`\mathcal{V} = \text{span}(\psi_j, j=0..N-1)`), the Lagrange interpolants are found as:

.. math::

   \lambda_i(\mathbf{u}) = \sum_j V_{ij}^{-1} \psi_j(\mathbf{u})

using the inverse of the Vandermonde matrix :math:`V` associated with the control points :math:`\mathbf{u}_i` and basis :math:`\psi`:

.. math::

   V_{ij} = \psi_j(\mathbf{u}_i)

The spatial parametric function spaces :math:`\mathcal{V}_p(u,v,w)` for each element type and order :math:`p` are listed in the table below. In addition to standard "complete" elements, incomplete or "serendipity" elements are supported in higher dimensions. Edge serendipity elements specify control points only on edges. Face serendipity elements exclude only interior control points.

.. table:: **Lagrange Function Spaces by Element Type**

  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Element  | Base      | Complete                             | Edge Serendipity                         | Face Serendipity    |
  | Type     | Type      |                                      |                                          |                     |
  +==========+===========+======================================+==========================================+=====================+
  | Line     | BAR_2     | :math:`\mathcal{L}_p(u)`             | n/a                                      | n/a                 |
  |          |           |                                      |                                          |                     |
  |          |           | :math:`N = p+1`                      |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Quad     | QUAD_4    | :math:`\mathcal{Q}_p^2(u,v)`         | :math:`\mathcal{L}_p(u) \otimes          | n/a                 |
  |          |           |                                      | \mathcal{L}_1(v) \oplus                  |                     |
  |          |           | :math:`N = (p+1)^2`                  | \mathcal{L}_p(v) \otimes                 |                     |
  |          |           |                                      | \mathcal{L}_1(u)`                        |                     |
  |          |           |                                      |                                          |                     |
  |          |           |                                      | :math:`N = 4p`                           |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Hexa     | HEXA_8    | :math:`\mathcal{Q}_p^3(u,v,w)`       |                                          |                     |
  |          |           |                                      |                                          |                     |
  |          |           | :math:`N = (p+1)^3`                  |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Triangle | TRI_3     | :math:`\mathcal{P}_p^2(u,v)`         | n/a                                      | n/a                 |
  |          |           |                                      |                                          |                     |
  |          |           | :math:`N = (p+1)(p+2)/2`             |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Tetra    | TETRA_4   | :math:`\mathcal{P}_p^3(u,v,w)`       |                                          |                     |
  |          |           |                                      |                                          |                     |
  |          |           | :math:`N = (p+1)(p+2)(p+3)/6`        |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Prism    | PENTA_6   | :math:`\mathcal{P}_p^2(u,v) \otimes` |                                          |                     |
  |          |           | :math:`\mathcal{L}_p(w)`             |                                          |                     |
  |          |           |                                      |                                          |                     |
  |          |           | :math:`N = (p+1)^2(p+2)/2`           |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+
  | Pyramid  | PYRA_5    | See [BergotCohenDurufle2010]_        |                                          |                     |
  +----------+-----------+--------------------------------------+------------------------------------------+---------------------+

where the standard function spaces of order :math:`p` are:

* Linear space: :math:`\mathcal{L}_p(u) = \text{span}\{u^i, 0 \leq i \leq p\}`
* Tensor product spaces (:math:`N = (p+1)^d`):

  * :math:`\mathcal{Q}_p^2(u,v) = \mathcal{L}_p(u) \otimes \mathcal{L}_p(v) = \text{span}\{u^i v^j, 0 \leq i,j \leq p\}`
  * :math:`\mathcal{Q}_p^3(u,v,w) = \mathcal{L}_p(u) \otimes \mathcal{L}_p(v) \otimes \mathcal{L}_p(w) = \text{span}\{u^i v^j w^k, 0 \leq i,j,k \leq p\}`

* Pascal triangle/tetrahedron (:math:`N = (p+1) \cdots (p+d)/d!`):

  * :math:`\mathcal{P}_p^2(u,v) = \text{span}\{u^i v^j, 0 \leq i+j \leq p\}`
  * :math:`\mathcal{P}_p^3(u,v,w) = \text{span}\{u^i v^j w^k, 0 \leq i+j+k \leq p\}`

For space-time interpolation (e.g., for ALE meshes), the complete functional space is:

.. math::

   \mathcal{V}_{p,q}(u,v,w,\tau) = \mathcal{V}_p(u,v,w) \otimes \mathcal{L}_q(\tau)

where :math:`p` and :math:`q` are the spatial and temporal orders, respectively.

Parametric Modal Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
~~~~~

Parametric modal interpolation applies only to solution fields, not to mesh geometry.

Monomial Basis Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

For modal interpolation, the interpolation functions are based on an ordered set of monomials spanning the Pascal spaces in parametric coordinates. The ordering is defined as:

* **1D**: The monomials :math:`1, u, u^2, u^3, \ldots, u^p`

* **2D**: The Pascal triangle ordered as::

    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        f[idx++] = u^(i-j) * v^j

* **3D**: The Pascal tetrahedron ordered as::

    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        for (int k=0; k<=i-j; k++)
          f[idx++] = u^(i-j-k) * v^k * w^j

Space-Time Modal Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For space-time formulations, the spatial monomials are multiplied by monomials in parametric time :math:`\tau`:

* **1D in space plus time**::

    for (int h=0; h<=q; h++)
      for (int i=0; i<=p; i++)
        f[idx++] = tau^h * u^i

* **2D in space plus time**::

    for (int h=0; h<=q; h++)
      for (int i=0; i<=p; i++)
        for (int j=0; j<=i; j++)
          f[idx++] = tau^h * u^(i-j) * v^j

* **3D in space plus time**::

    for (int h=0; h<=q; h++)
      for (int i=0; i<=p; i++)
        for (int j=0; j<=i; j++)
          for (int k=0; k<=i-j; k++)
            f[idx++] = tau^h * u^(i-j-k) * v^k * w^j

This space-time formulation reverts to purely spatial interpolation (including the ordering) for the default temporal order :math:`q=0`.

Cartesian Modal Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
~~~~~

Cartesian modal interpolation applies only to solution fields, not to mesh geometry.

Element-Local Coordinate System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Cartesian modal interpolation, a local Cartesian coordinate system is defined per element. The element barycenter :math:`\mathbf{R}^e` is computed as the arithmetic mean of the locations of the principal vertices (nodes corresponding to those of the associated linear element):

.. math::

   \mathbf{R}^e = \frac{1}{N} \sum_{i=1}^{N} \mathbf{R}_i^e

where :math:`\mathbf{R}_i^e` are the global coordinates of the principal vertices.

The element-local coordinates are then defined as :math:`\mathbf{r} = \mathbf{R} - \mathbf{R}^e`, using notation :math:`\mathbf{r} = x\mathbf{e}_x + y\mathbf{e}_y + z\mathbf{e}_z`.

For space-time methods, an element-local origin of the time dimension is defined as the midpoint of the relevant physical time slab :math:`[T_n, T_{n+1}]`:

.. math::

   t = T - \frac{T_n + T_{n+1}}{2}

Cartesian Monomial Basis Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interpolation space for Cartesian modal interpolations uses ordered sets of monomials in the element-local Cartesian coordinates :math:`(x, y, z)` and physical time :math:`t`. The ordering for purely spatial interpolation is:

* **1D**: The monomials :math:`1, x, x^2, x^3, \ldots, x^p`

* **2D**: The Pascal triangle::

    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        f[idx++] = x^(i-j) * y^j

* **3D**: The Pascal tetrahedron::

    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        for (int k=0; k<=i-j; k++)
          f[idx++] = x^(i-j-k) * y^k * z^j

For space-time interpolation, multiply with temporal monomials in physical time :math:`t` using the same ordering pattern as parametric modal interpolation.

IsoParametric Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`IsoParametric` interpolation indicates that the solution uses the same interpolation functions as the mesh geometry. In this case:

* The element's own node coordinates from :sidsref:`GridCoordinates_t` serve as control points
* No :sidskey:`LagrangeControlPoints` need to be specified in :sidsref:`SolutionInterpolation_t`
* The interpolation type is simply marked as :sidskey:`IsoParametric`

This approach is commonly used in finite element methods where the solution is interpolated using the same basis functions as the geometric mapping.

Usage in CGNS Files
^^^^^^^^^^^^^^^^^^^

Element interpolation metadata is stored in :sidsref:`ElementInterpolation_t` nodes within :sidsref:`Family_t`.
Solution interpolation metadata is stored in :sidsref:`SolutionInterpolation_t` nodes within :sidsref:`Family_t`.
The actual interpolation orders for solution data are specified in :sidsref:`FlowSolution_t` using the :sidskey:`SpatialOrder` and :sidskey:`TemporalOrder` fields.

See :ref:`Element Interpolation Structure Definition <ElementInterpolation_t>` and :ref:`Solution Interpolation Structure Definition <SolutionInterpolation_t>` for detailed structure definitions.

References
^^^^^^^^^^

.. [BergotCohenDurufle2010] M. Bergot, G. Cohen, and M. Duruflé, "Higher-order Finite Elements for Hybrid Meshes Using New Nodal Pyramidal Elements," Journal of Scientific Computing 42, pp. 345-381 (2010), doi: 10.1007/s10915-009-9334-9
