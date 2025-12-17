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

Choosing an Interpolation Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following flowchart helps determine which interpolation type is appropriate for your application:

.. figure:: ../../images/sids/figs/visual_05_flowchart.svg
   :width: 700px
   :align: center

   Decision flowchart for selecting between ParametricLagrange and CartesianMonomials interpolation types. This diagram guides users through the selection process based on whether they need mesh geometry interpolation or solution field interpolation, and whether they prefer nodal (Lagrange) or modal (monomial) basis functions.

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

.. note::
   For space-time computations, see :ref:`Space-Time Extensions <spacetime_extensions>` for the extension to parametric time :math:`\tau \in [-1, 1]`.

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

The spatial parametric function spaces :math:`\mathcal{V}_p(u,v,w)` for each element type and order :math:`p` are listed in the table below. In addition to standard "complete" elements, incomplete or "serendipity" elements are supported in higher dimensions:

* **Edge Serendipity**: Control points are located only at vertices and edge nodes. All face-interior and volume-interior control points are excluded.
* **Face Serendipity**: Control points are located at vertices, edges, and face nodes. Only volume-interior control points are excluded.

The function spaces are defined by specific incomplete tensor products or monomial exclusion rules as detailed below.

.. figure:: ../../images/sids/figs/visual_02_tensor_modes.svg
   :width: 700px
   :align: center

   Visualization of Complete, Face Serendipity, and Edge Serendipity elements. The diagram shows how serendipity elements progressively "hollow out" the interior: Complete elements have all nodes (vertices, edges, faces, and interior), Face Serendipity excludes volume-interior nodes, and Edge Serendipity excludes both face-interior and volume-interior nodes, retaining only vertices and edges.

.. table:: **Lagrange Function Spaces by Element Type**

  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Element  | Base      | Complete                             | Edge Serendipity                         | Face Serendipity                         |
  | Type     | Type      |                                      |                                          |                                          |
  +==========+===========+======================================+==========================================+==========================================+
  | Line     | BAR_2     | :math:`\mathcal{L}_p(u)`             | n/a                                      | n/a                                      |
  |          |           |                                      |                                          |                                          |
  |          |           | :math:`N = p+1`                      |                                          |                                          |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Quad     | QUAD_4    | :math:`\mathcal{Q}_p^2(u,v)`         | :math:`\mathcal{L}_p(u) \otimes          | n/a                                      |
  |          |           |                                      | \mathcal{L}_1(v) \oplus                  |                                          |
  |          |           | :math:`N = (p+1)^2`                  | \mathcal{L}_p(v) \otimes                 |                                          |
  |          |           |                                      | \mathcal{L}_1(u)`                        |                                          |
  |          |           |                                      |                                          |                                          |
  |          |           |                                      | :math:`N = 4p`                           |                                          |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Hexa     | HEXA_8    | :math:`\mathcal{Q}_p^3(u,v,w)`       | :math:`\mathcal{L}_p(u) \otimes          | :math:`\mathcal{Q}_p^3(u,v,w) \setminus` |
  |          |           |                                      | \mathcal{L}_1(v) \otimes                 | \text{span}\{u^i v^j w^k :               |
  |          |           | :math:`N = (p+1)^3`                  | \mathcal{L}_1(w) \oplus                  | 2 \leq i,j,k \leq p-1\}`                 |
  |          |           |                                      | \mathcal{L}_1(u) \otimes                 |                                          |
  |          |           |                                      | \mathcal{L}_p(v) \otimes                 | :math:`N = (p+1)^3 - (p-1)^3`            |
  |          |           |                                      | \mathcal{L}_1(w) \oplus                  |                                          |
  |          |           |                                      | \mathcal{L}_1(u) \otimes                 |                                          |
  |          |           |                                      | \mathcal{L}_1(v) \otimes                 |                                          |
  |          |           |                                      | \mathcal{L}_p(w)`                        |                                          |
  |          |           |                                      |                                          |                                          |
  |          |           |                                      | :math:`N = 12(p-1) + 8`                  |                                          |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Triangle | TRI_3     | :math:`\mathcal{P}_p^2(u,v)`         | n/a                                      | n/a                                      |
  |          |           |                                      |                                          |                                          |
  |          |           | :math:`N = (p+1)(p+2)/2`             |                                          |                                          |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Tetra    | TETRA_4   | :math:`\mathcal{P}_p^3(u,v,w)`       | n/a                                      | :math:`\mathcal{P}_p^3(u,v,w) \setminus` |
  |          |           |                                      |                                          | \text{span}\{u^i v^j w^k :               |
  |          |           | :math:`N = (p+1)(p+2)(p+3)/6`        |                                          | i+j+k \leq p, \min(i,j,k) \geq 2\}`      |
  |          |           |                                      |                                          |                                          |
  |          |           |                                      |                                          | :math:`N = (p+1)(p+2)(p+3)/6 -`          |
  |          |           |                                      |                                          | :math:`(p-2)(p-1)p/6`                    |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Prism    | PENTA_6   | :math:`\mathcal{P}_p^2(u,v) \otimes` | n/a                                      | :math:`(\mathcal{P}_p^2(u,v) \otimes`    |
  |          |           | :math:`\mathcal{L}_p(w)`             |                                          | :math:`\mathcal{L}_p(w)) \setminus`      |
  |          |           |                                      |                                          | :math:`(\mathcal{P}_{p-2}^2(u,v) \otimes`|
  |          |           | :math:`N = (p+1)^2(p+2)/2`           |                                          | :math:`\mathcal{L}_{p-2}(w))`            |
  |          |           |                                      |                                          |                                          |
  |          |           |                                      |                                          | :math:`N = (p+1)^2(p+2)/2 -`             |
  |          |           |                                      |                                          | :math:`(p-1)^2p/2`                       |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+
  | Pyramid  | PYRA_5    | See [BergotCohenDurufle2010]_        | n/a                                      | See [BergotCohenDurufle2010]_            |
  +----------+-----------+--------------------------------------+------------------------------------------+------------------------------------------+

.. figure:: ../../images/sids/figs/visual_03_pyramid_map.svg
   :width: 600px
   :align: center

   Pyramid element parametric mapping from reference cube to pyramid. The diagram illustrates the singular mapping at the pyramid apex where the top face of the reference cube :math:`w=1` collapses to a single point. This singularity requires special polynomial spaces as detailed in [BergotCohenDurufle2010]_.

where the standard function spaces of order :math:`p` are:

* Linear space: :math:`\mathcal{L}_p(u) = \text{span}\{u^i, 0 \leq i \leq p\}`
* Tensor product spaces (:math:`N = (p+1)^d`):

  * :math:`\mathcal{Q}_p^2(u,v) = \mathcal{L}_p(u) \otimes \mathcal{L}_p(v) = \text{span}\{u^i v^j, 0 \leq i,j \leq p\}`
  * :math:`\mathcal{Q}_p^3(u,v,w) = \mathcal{L}_p(u) \otimes \mathcal{L}_p(v) \otimes \mathcal{L}_p(w) = \text{span}\{u^i v^j w^k, 0 \leq i,j,k \leq p\}`

* Pascal triangle/tetrahedron (:math:`N = (p+1) \cdots (p+d)/d!`):

  * :math:`\mathcal{P}_p^2(u,v) = \text{span}\{u^i v^j, 0 \leq i+j \leq p\}`
  * :math:`\mathcal{P}_p^3(u,v,w) = \text{span}\{u^i v^j w^k, 0 \leq i+j+k \leq p\}`

.. note::
   For space-time interpolation (e.g., ALE meshes), see :ref:`Space-Time Extensions <spacetime_extensions>` for the extension to temporal interpolation with order :math:`q`.

Reference Control Point Locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure actionability and enable validation, this section provides concrete control point locations for common element types and polynomial orders. These reference configurations can be used to verify implementations.

**Triangle (TRI) - Order p=2**

6 control points in parametric space :math:`(u, v)`:

.. code-block:: text

   Node 0: u=-1.0, v=-1.0  (vertex, bottom-left)
   Node 1: u= 1.0, v=-1.0  (vertex, bottom-right)
   Node 2: u=-1.0, v= 1.0  (vertex, top-left)
   Node 3: u= 0.0, v=-1.0  (edge midpoint, bottom)
   Node 4: u= 0.0, v= 0.0  (edge midpoint, diagonal)
   Node 5: u=-1.0, v= 0.0  (edge midpoint, left)

Total: :math:`N = (2+1)(2+2)/2 = 6`

**Quadrilateral (QUAD) - Order p=2**

9 control points in parametric space :math:`(u, v)` using tensor product ordering:

.. code-block:: text

   // Column-major: j outer, i inner
   Node 0: u=-1.0, v=-1.0  (j=0, i=0)
   Node 1: u= 0.0, v=-1.0  (j=0, i=1)
   Node 2: u= 1.0, v=-1.0  (j=0, i=2)
   Node 3: u=-1.0, v= 0.0  (j=1, i=0)
   Node 4: u= 0.0, v= 0.0  (j=1, i=1) - CENTER
   Node 5: u= 1.0, v= 0.0  (j=1, i=2)
   Node 6: u=-1.0, v= 1.0  (j=2, i=0)
   Node 7: u= 0.0, v= 1.0  (j=2, i=1)
   Node 8: u= 1.0, v= 1.0  (j=2, i=2)

Total: :math:`N = (2+1)^2 = 9`

**Quadrilateral Edge Serendipity (QUAD_8) - Order p=2**

8 control points (no center node):

.. code-block:: text

   Node 0: u=-1.0, v=-1.0  (vertex, bottom-left)
   Node 1: u= 1.0, v=-1.0  (vertex, bottom-right)
   Node 2: u= 1.0, v= 1.0  (vertex, top-right)
   Node 3: u=-1.0, v= 1.0  (vertex, top-left)
   Node 4: u= 0.0, v=-1.0  (edge midpoint, bottom)
   Node 5: u= 1.0, v= 0.0  (edge midpoint, right)
   Node 6: u= 0.0, v= 1.0  (edge midpoint, top)
   Node 7: u=-1.0, v= 0.0  (edge midpoint, left)

Total: :math:`N = 4 \times 2 = 8`

**Tetrahedron (TETRA) - Order p=2**

10 control points in parametric space :math:`(u, v, w)`:

.. code-block:: text

   // Vertices
   Node 0: u=-1.0, v=-1.0, w=-1.0
   Node 1: u= 1.0, v=-1.0, w=-1.0
   Node 2: u=-1.0, v= 1.0, w=-1.0
   Node 3: u=-1.0, v=-1.0, w= 1.0

   // Edge midpoints
   Node 4: u= 0.0, v=-1.0, w=-1.0  (edge 0-1)
   Node 5: u= 0.0, v= 0.0, w=-1.0  (edge 1-2)
   Node 6: u=-1.0, v= 0.0, w=-1.0  (edge 2-0)
   Node 7: u= 0.0, v=-1.0, w= 0.0  (edge 0-3)
   Node 8: u= 0.0, v= 0.0, w= 0.0  (edge 1-3)
   Node 9: u=-1.0, v= 0.0, w= 0.0  (edge 2-3)

Total: :math:`N = (2+1)(2+2)(2+3)/6 = 10`

**Hexahedron (HEXA) - Order p=2**

27 control points in parametric space :math:`(u, v, w)` using tensor product ordering:

.. code-block:: text

   // Column-major: k outermost, j middle, i innermost
   // Plane w=-1 (k=0):
   Node 0:  u=-1.0, v=-1.0, w=-1.0  (k=0, j=0, i=0)
   Node 1:  u= 0.0, v=-1.0, w=-1.0  (k=0, j=0, i=1)
   Node 2:  u= 1.0, v=-1.0, w=-1.0  (k=0, j=0, i=2)
   Node 3:  u=-1.0, v= 0.0, w=-1.0  (k=0, j=1, i=0)
   Node 4:  u= 0.0, v= 0.0, w=-1.0  (k=0, j=1, i=1) - face center
   Node 5:  u= 1.0, v= 0.0, w=-1.0  (k=0, j=1, i=2)
   Node 6:  u=-1.0, v= 1.0, w=-1.0  (k=0, j=2, i=0)
   Node 7:  u= 0.0, v= 1.0, w=-1.0  (k=0, j=2, i=1)
   Node 8:  u= 1.0, v= 1.0, w=-1.0  (k=0, j=2, i=2)

   // Plane w=0 (k=1):
   Node 9:  u=-1.0, v=-1.0, w= 0.0  (k=1, j=0, i=0)
   Node 10: u= 0.0, v=-1.0, w= 0.0  (k=1, j=0, i=1)
   Node 11: u= 1.0, v=-1.0, w= 0.0  (k=1, j=0, i=2)
   Node 12: u=-1.0, v= 0.0, w= 0.0  (k=1, j=1, i=0)
   Node 13: u= 0.0, v= 0.0, w= 0.0  (k=1, j=1, i=1) - VOLUME CENTER
   Node 14: u= 1.0, v= 0.0, w= 0.0  (k=1, j=1, i=2)
   Node 15: u=-1.0, v= 1.0, w= 0.0  (k=1, j=2, i=0)
   Node 16: u= 0.0, v= 1.0, w= 0.0  (k=1, j=2, i=1)
   Node 17: u= 1.0, v= 1.0, w= 0.0  (k=1, j=2, i=2)

   // Plane w=1 (k=2):
   Node 18: u=-1.0, v=-1.0, w= 1.0  (k=2, j=0, i=0)
   Node 19: u= 0.0, v=-1.0, w= 1.0  (k=2, j=0, i=1)
   Node 20: u= 1.0, v=-1.0, w= 1.0  (k=2, j=0, i=2)
   Node 21: u=-1.0, v= 0.0, w= 1.0  (k=2, j=1, i=0)
   Node 22: u= 0.0, v= 0.0, w= 1.0  (k=2, j=1, i=1) - face center
   Node 23: u= 1.0, v= 0.0, w= 1.0  (k=2, j=1, i=2)
   Node 24: u=-1.0, v= 1.0, w= 1.0  (k=2, j=2, i=0)
   Node 25: u= 0.0, v= 1.0, w= 1.0  (k=2, j=2, i=1)
   Node 26: u= 1.0, v= 1.0, w= 1.0  (k=2, j=2, i=2)

Total: :math:`N = (2+1)^3 = 27`

**Hexahedron Edge Serendipity (HEXA_20) - Order p=2**

20 control points (8 vertices + 12 edge midpoints, no face/volume centers):

.. code-block:: text

   // 8 vertices
   Node 0: u=-1.0, v=-1.0, w=-1.0
   Node 1: u= 1.0, v=-1.0, w=-1.0
   Node 2: u= 1.0, v= 1.0, w=-1.0
   Node 3: u=-1.0, v= 1.0, w=-1.0
   Node 4: u=-1.0, v=-1.0, w= 1.0
   Node 5: u= 1.0, v=-1.0, w= 1.0
   Node 6: u= 1.0, v= 1.0, w= 1.0
   Node 7: u=-1.0, v= 1.0, w= 1.0

   // 12 edge midpoints
   Node 8:  u= 0.0, v=-1.0, w=-1.0  (bottom face, bottom edge)
   Node 9:  u= 1.0, v= 0.0, w=-1.0  (bottom face, right edge)
   Node 10: u= 0.0, v= 1.0, w=-1.0  (bottom face, top edge)
   Node 11: u=-1.0, v= 0.0, w=-1.0  (bottom face, left edge)
   Node 12: u= 0.0, v=-1.0, w= 1.0  (top face, bottom edge)
   Node 13: u= 1.0, v= 0.0, w= 1.0  (top face, right edge)
   Node 14: u= 0.0, v= 1.0, w= 1.0  (top face, top edge)
   Node 15: u=-1.0, v= 0.0, w= 1.0  (top face, left edge)
   Node 16: u=-1.0, v=-1.0, w= 0.0  (vertical edge, back-left)
   Node 17: u= 1.0, v=-1.0, w= 0.0  (vertical edge, back-right)
   Node 18: u= 1.0, v= 1.0, w= 0.0  (vertical edge, front-right)
   Node 19: u=-1.0, v= 1.0, w= 0.0  (vertical edge, front-left)

Total: :math:`N = 12(2-1) + 8 = 20`

.. note::
   **Implementation Validation**: Use these reference values to verify your control point generation and ordering logic. If your implementation produces different coordinates for the same element type and order, it is **not** CGNS-compliant.

Node Ordering Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following figures provide visual atlases of the node ordering for common element types at order p=3:

.. figure:: ../../images/sids/figs/visual_01a_atlas_triangle.svg
   :width: 600px
   :align: center

   Triangle P=3 node ordering atlas. Each node is labeled with its linear index and corresponding (i,j) tuple in the Pascal triangle ordering. This visual reference can be used to verify control point generation for triangular elements.

.. figure:: ../../images/sids/figs/visual_01b_atlas_quad.svg
   :width: 700px
   :align: center

   Quadrilateral P=3 node ordering: Complete (left) vs Edge Serendipity (right). The complete QUAD shows all 16 nodes including interior nodes, while the edge serendipity variant shows only the 12 perimeter nodes (vertices and edges), with interior nodes excluded. Nodes are labeled with linear indices and (i,j) tuples.

.. figure:: ../../images/sids/figs/visual_01c_atlas_tetra.svg
   :width: 600px
   :align: center

   Tetrahedron P=3 node ordering in exploded view. The diagram shows all 20 control points for a complete tetrahedral element, with nodes labeled by their linear index. The exploded view separates vertices, edge nodes, and face nodes for clarity.

Parametric Modal Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
~~~~~

Parametric modal interpolation applies only to solution fields, not to mesh geometry.

Monomial Basis Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

For modal interpolation, the interpolation functions are based on an ordered set of monomials in parametric coordinates. The ordering depends on the element topology:

**Tensor Product Elements** (Quadrilaterals, Hexahedra):

* **1D** (BAR): The monomials :math:`1, u, u^2, u^3, \ldots, u^p`

* **2D** (QUAD): Tensor product ordered as::

    idx = 0;
    for (int j=0; j<=p; j++)        // v direction (outer loop)
      for (int i=0; i<=p; i++)      // u direction (inner loop)
        f[idx++] = u^i * v^j;

  This produces the ordering: :math:`\{u^i v^j : 0 \leq i,j \leq p\}` in **column-major** order.

  **Total basis functions**: :math:`N = (p+1)^2`

* **3D** (HEXA): Tensor product ordered as::

    idx = 0;
    for (int k=0; k<=p; k++)        // w direction (outermost loop)
      for (int j=0; j<=p; j++)      // v direction (middle loop)
        for (int i=0; i<=p; i++)    // u direction (innermost loop)
          f[idx++] = u^i * v^j * w^k;

  This produces the ordering: :math:`\{u^i v^j w^k : 0 \leq i,j,k \leq p\}` in **column-major** order.

  **Total basis functions**: :math:`N = (p+1)^3`

.. danger::
   **Critical Loop Ordering Error**: Do **NOT** use simplex (Pascal) loop ordering for tensor product elements. Using the wrong loop order will produce an incorrect basis that is incompatible with the CGNS standard.

**Simplex Elements** (Triangles, Tetrahedra):

* **2D** (TRI): Pascal triangle ordered as::

    idx = 0;
    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        f[idx++] = u^(i-j) * v^j;

  This produces the ordering: :math:`\{u^i v^j : 0 \leq i+j \leq p\}`.

  **Total basis functions**: :math:`N = (p+1)(p+2)/2`

* **3D** (TETRA): Pascal tetrahedron ordered as::

    idx = 0;
    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        for (int k=0; k<=i-j; k++)
          f[idx++] = u^(i-j-k) * v^k * w^j;

  This produces the ordering: :math:`\{u^i v^j w^k : 0 \leq i+j+k \leq p\}`.

  **Total basis functions**: :math:`N = (p+1)(p+2)(p+3)/6`

**Hybrid Elements** (Prisms):

* **3D** (PENTA): Tensor product of Pascal triangle with linear space::

    idx = 0;
    for (int h=0; h<=p; h++)        // w direction (tensor product axis)
      for (int i=0; i<=p; i++)      // Pascal triangle in (u,v)
        for (int j=0; j<=i; j++)
          f[idx++] = u^(i-j) * v^j * w^h;

  This produces: :math:`\mathcal{P}_p^2(u,v) \otimes \mathcal{L}_p(w)`.

  **Total basis functions**: :math:`N = (p+1)^2(p+2)/2`

.. note::
   For space-time formulations, see :ref:`Space-Time Extensions <spacetime_extensions>` for the extension to parametric time :math:`\tau`.

Cartesian Modal Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope
~~~~~

Cartesian modal interpolation applies only to solution fields, not to mesh geometry.

Element-Local Coordinate System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Cartesian modal interpolation, a local Cartesian coordinate system is defined per element. The element barycenter :math:`\mathbf{R}^e` is computed as the arithmetic mean of the locations of the **principal vertices**, which are strictly defined as:

**Principal Vertices Definition**: The principal vertices of a high-order element are the vertex nodes of the associated linear sub-element. Specifically:

* For a high-order element of type :sidskey:`ElementType_t`, the principal vertices are the first :math:`N_v` nodes in the element's connectivity list, where :math:`N_v` is the number of vertices of the corresponding linear element.
* Examples:

  * TETRA_10: principal vertices are nodes 1-4 (corresponding to TETRA_4)
  * HEXA_20 or HEXA_27: principal vertices are nodes 1-8 (corresponding to HEXA_8)
  * TRI_6: principal vertices are nodes 1-3 (corresponding to TRI_3)
  * QUAD_8 or QUAD_9: principal vertices are nodes 1-4 (corresponding to QUAD_4)

The element barycenter is then computed as:

.. math::

   \mathbf{R}^e = \frac{1}{N_v} \sum_{i=1}^{N_v} \mathbf{R}_i^{\text{vertex}}

where :math:`\mathbf{R}_i^{\text{vertex}}` are the global coordinates of the principal vertices only.

.. warning::
   The barycenter must **NOT** be computed using all nodes of a high-order element (e.g., including edge, face, or interior nodes), as this would shift the origin and invalidate the basis function definitions.

.. figure:: ../../images/sids/figs/visual_06_barycenter.svg
   :width: 600px
   :align: center

   Barycenter computation for Cartesian modal interpolation. The diagram contrasts the correct approach (using only principal vertices/corner nodes, shown in green) with the incorrect approach (using all nodes including edge and interior nodes, shown in red with X). For a curved high-order element, only the corner vertices should be used to compute the element barycenter that serves as the origin of the local Cartesian coordinate system.

The element-local coordinates are then defined as :math:`\mathbf{r} = \mathbf{R} - \mathbf{R}^e`, using notation :math:`\mathbf{r} = x\mathbf{e}_x + y\mathbf{e}_y + z\mathbf{e}_z`.

**Normalization for Numerical Stability**

.. danger::
   **Critical Numerical Stability Requirement**: Using physical coordinates directly in monomial basis functions can lead to catastrophic floating-point overflow or underflow, especially for high polynomial orders.

   **Problem**: If spatial coordinates span kilometers or micrometers, monomials like :math:`x^p`, :math:`y^p`, :math:`z^p` with :math:`p \geq 3` will cause numerical issues.

   **Requirement**: Implementations **MUST** normalize spatial coordinates to a reference domain to ensure numerical stability and data portability.

**Recommended Normalization**: Define normalized element-local coordinates :math:`(\xi, \eta, \zeta)` by scaling with a characteristic element length :math:`h^e`:

.. math::

   \xi = \frac{x}{h^e}, \quad \eta = \frac{y}{h^e}, \quad \zeta = \frac{z}{h^e}

where the characteristic length :math:`h^e` is computed as:

.. math::

   h^e = \max_{i,j \in \{1, \ldots, N_v\}} \|\mathbf{R}_i^{\text{vertex}} - \mathbf{R}_j^{\text{vertex}}\|

This ensures :math:`\xi, \eta, \zeta \in \mathcal{O}([-1, 1])`, providing well-conditioned Vandermonde matrices and preventing overflow/underflow.

**Storage Convention**: When using normalized coordinates, the characteristic length :math:`h^e` should be stored alongside the modal coefficients to enable proper reconstruction of physical values.

Cartesian Monomial Basis Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interpolation space for Cartesian modal interpolations uses ordered sets of monomials in the **normalized** element-local Cartesian coordinates :math:`(\xi, \eta, \zeta)` (or :math:`(x, y, z)` if physical coordinates are pre-normalized). The monomial ordering depends on the element topology and **must match** the parametric modal ordering:

**Tensor Product Elements** (Quadrilaterals, Hexahedra):

* **1D** (BAR): The monomials :math:`1, \xi, \xi^2, \xi^3, \ldots, \xi^p`

* **2D** (QUAD): Tensor product ordered as::

    idx = 0;
    for (int j=0; j<=p; j++)        // eta direction (outer loop)
      for (int i=0; i<=p; i++)      // xi direction (inner loop)
        f[idx++] = xi^i * eta^j;

  **Total basis functions**: :math:`N = (p+1)^2`

* **3D** (HEXA): Tensor product ordered as::

    idx = 0;
    for (int k=0; k<=p; k++)        // zeta direction (outermost loop)
      for (int j=0; j<=p; j++)      // eta direction (middle loop)
        for (int i=0; i<=p; i++)    // xi direction (innermost loop)
          f[idx++] = xi^i * eta^j * zeta^k;

  **Total basis functions**: :math:`N = (p+1)^3`

**Simplex Elements** (Triangles, Tetrahedra):

* **2D** (TRI): Pascal triangle ordered as::

    idx = 0;
    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        f[idx++] = xi^(i-j) * eta^j;

  **Total basis functions**: :math:`N = (p+1)(p+2)/2`

* **3D** (TETRA): Pascal tetrahedron ordered as::

    idx = 0;
    for (int i=0; i<=p; i++)
      for (int j=0; j<=i; j++)
        for (int k=0; k<=i-j; k++)
          f[idx++] = xi^(i-j-k) * eta^k * zeta^j;

  **Total basis functions**: :math:`N = (p+1)(p+2)(p+3)/6`

**Hybrid Elements** (Prisms):

* **3D** (PENTA): Tensor product of Pascal triangle with linear space::

    idx = 0;
    for (int h=0; h<=p; h++)        // zeta direction (tensor product axis)
      for (int i=0; i<=p; i++)      // Pascal triangle in (xi,eta)
        for (int j=0; j<=i; j++)
          f[idx++] = xi^(i-j) * eta^j * zeta^h;

  **Total basis functions**: :math:`N = (p+1)^2(p+2)/2`

.. note::
   **Notation**: The symbols :math:`\xi, \eta, \zeta` represent normalized coordinates. If the documentation or implementation uses :math:`x, y, z`, these should be understood as already-normalized coordinates scaled to :math:`\mathcal{O}([-1, 1])`.

.. note::
   For space-time interpolation, see :ref:`Space-Time Extensions <spacetime_extensions>` for the extension to normalized temporal coordinate :math:`\theta`.

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

Validation and Compliance Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides concrete test cases that implementations can use to verify correctness and CGNS compliance.

Partition of Unity Test
~~~~~~~~~~~~~~~~~~~~~~~~

All Lagrange interpolation schemes must satisfy the partition of unity property: the sum of all basis functions at any point in the parametric domain must equal 1.

**Test Procedure**:

1. Generate Lagrange control points for element type and order :math:`p`
2. Compute Lagrange basis functions :math:`\lambda_i(\mathbf{u})` at a test point :math:`\mathbf{u}_{\text{test}}`
3. Verify: :math:`\sum_{i=1}^{N} \lambda_i(\mathbf{u}_{\text{test}}) = 1.0` within tolerance :math:`\epsilon = 10^{-12}`

**Reference Test Points**:

* QUAD :math:`p=2`: Test at :math:`(u, v) = (0.3, -0.7)` → Expected sum = 1.0
* HEXA :math:`p=2`: Test at :math:`(u, v, w) = (0.5, -0.5, 0.2)` → Expected sum = 1.0
* TRI :math:`p=2`: Test at :math:`(u, v) = (-0.5, -0.3)` → Expected sum = 1.0
* TETRA :math:`p=2`: Test at :math:`(u, v, w) = (-0.6, -0.2, -0.1)` → Expected sum = 1.0

Kronecker Delta Property Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lagrange basis functions must satisfy the Kronecker delta property: :math:`\lambda_i(\mathbf{u}_j) = \delta_{ij}`.

**Test Procedure**:

1. For each control point :math:`\mathbf{u}_j`:
2. Evaluate all basis functions :math:`\lambda_i(\mathbf{u}_j)` for :math:`i = 1, \ldots, N`
3. Verify: :math:`\lambda_j(\mathbf{u}_j) = 1.0` within tolerance :math:`\epsilon = 10^{-12}`
4. Verify: :math:`\lambda_i(\mathbf{u}_j) = 0.0` for all :math:`i \neq j` within tolerance :math:`\epsilon = 10^{-12}`

**Example** (QUAD_8, p=2):

At control point Node 4: :math:`(u, v) = (0.0, -1.0)`:

.. code-block:: text

   λ₀(Node 4) = 0.0  ✓
   λ₁(Node 4) = 0.0  ✓
   λ₂(Node 4) = 0.0  ✓
   λ₃(Node 4) = 0.0  ✓
   λ₄(Node 4) = 1.0  ✓  (diagonal element)
   λ₅(Node 4) = 0.0  ✓
   λ₆(Node 4) = 0.0  ✓
   λ₇(Node 4) = 0.0  ✓

Modal Coefficient Orthogonality Test (for Modal Interpolations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For modal interpolations, verify that the basis ordering matches the specification by computing modal coefficients for a known function.

**Test Case**: Represent the polynomial :math:`f(u,v) = u^2 + v` using QUAD p=2 modal basis.

**Expected Modal Coefficients** (column-major ordering):

.. code-block:: text

   // for j=0,1,2; i=0,1,2
   c[0] = coefficient of u⁰v⁰ = 0.0
   c[1] = coefficient of u¹v⁰ = 0.0
   c[2] = coefficient of u²v⁰ = 1.0  ← u² term
   c[3] = coefficient of u⁰v¹ = 1.0  ← v term
   c[4] = coefficient of u¹v¹ = 0.0
   c[5] = coefficient of u²v¹ = 0.0
   c[6] = coefficient of u⁰v² = 0.0
   c[7] = coefficient of u¹v² = 0.0
   c[8] = coefficient of u²v² = 0.0

If your modal ordering produces different indices for the u² or v terms, your implementation is **not CGNS-compliant**.

Geometry Reconstruction Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Test Case**: Curved quadrilateral element with p=2.

**Physical Control Point Coordinates** (9 points for QUAD_9):

.. code-block:: text

   X[0] = (0.0, 0.0)     Y[0] = (0.0, 0.0)     // j=0, i=0
   X[1] = (0.5, 0.0)     Y[1] = (0.5, 0.0)     // j=0, i=1
   X[2] = (1.0, 0.0)     Y[2] = (1.0, 0.0)     // j=0, i=2
   X[3] = (0.0, 0.5)     Y[3] = (0.0, 0.5)     // j=1, i=0
   X[4] = (0.5, 0.5)     Y[4] = (0.5, 0.6)     // j=1, i=1 - CURVED (offset in Y)
   X[5] = (1.0, 0.5)     Y[5] = (1.0, 0.5)     // j=1, i=2
   X[6] = (0.0, 1.0)     Y[6] = (0.0, 1.0)     // j=2, i=0
   X[7] = (0.5, 1.0)     Y[7] = (0.5, 1.0)     // j=2, i=1
   X[8] = (1.0, 1.0)     Y[8] = (1.0, 1.0)     // j=2, i=2

**Verification**: Evaluate geometry at :math:`(u, v) = (0.0, 0.0)` (center in parametric space):

.. math::

   X(0, 0) = \sum_{i=1}^{9} X_i \lambda_i(0, 0) \approx 0.5

   Y(0, 0) = \sum_{i=1}^{9} Y_i \lambda_i(0, 0) \approx 0.6

The curved center point should reconstruct to :math:`(0.5, 0.6)`, reflecting the curvature.

Numerical Stability Test (Cartesian Modal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Test Case**: Verify that implementations use normalized coordinates.

**Problem Setup**: QUAD element with physical vertices at extreme scales:

.. code-block:: text

   Vertex 0: (X, Y) = (0.0,     0.0)
   Vertex 1: (X, Y) = (1000.0,  0.0)      // kilometers
   Vertex 2: (X, Y) = (1000.0,  1000.0)
   Vertex 3: (X, Y) = (0.0,     1000.0)

**Expected Behavior**:

* Characteristic length: :math:`h^e = \max(\text{distances}) \approx 1414.2` km
* Normalized coordinates should be computed: :math:`\xi = x / h^e`, :math:`\eta = y / h^e`
* All normalized coordinates: :math:`\xi, \eta \in \mathcal{O}([-1, 1])`
* Monomial basis values (e.g., :math:`\xi^3`) should remain in range :math:`[-1, 1]`

**Failure Mode**: If physical coordinates are used directly, :math:`x^3 \sim (1000)^3 = 10^9`, causing overflow in Vandermonde matrix inversion.

**Test**: Verify that the implementation can successfully generate modal basis coefficients for :math:`p=3` without numerical overflow or NaN values.

Compliance Checklist
~~~~~~~~~~~~~~~~~~~~

An implementation is CGNS-compliant for high-order interpolation if it passes ALL of the following tests:

☐ Partition of unity test for all supported element types

☐ Kronecker delta property for all control points

☐ Correct modal coefficient ordering (column-major for tensor products, Pascal ordering for simplices)

☐ Geometry reconstruction within tolerance :math:`\epsilon < 10^{-10}`

☐ Numerical stability for extreme coordinate scales (no overflow/underflow)

☐ Time-major ordering for space-time cases (if implemented)

☐ Principal vertices correctly identified (Cartesian modal only)

☐ Normalization applied for Cartesian modal interpolation

.. _spacetime_extensions:

Space-Time Extensions
^^^^^^^^^^^^^^^^^^^^^

This section describes the extension of the spatial high-order interpolation framework to space-time methods, including ALE (Arbitrary Lagrangian-Eulerian) computations and space-time discontinuous Galerkin methods.

.. important::
   **For users working with static meshes only**: The spatial-only interpolation methods described in the previous sections are complete and self-contained. This space-time section can be safely skipped if you are not using time-dependent mesh motion or space-time formulations.

.. figure:: ../../images/sids/figs/visual_04_spacetime.svg
   :width: 700px
   :align: center

   Space-time element as temporal extrusion of spatial element. The diagram illustrates how a 2D spatial element (triangle or quadrilateral) is extruded along the time dimension :math:`\tau \in [-1, 1]` to form a (d+1)-dimensional space-time element. The spatial control points at :math:`\tau = -1` (time :math:`T_n`) and :math:`\tau = +1` (time :math:`T_{n+1}`) define the space-time interpolation slab.

Parametric Time Coordinate
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For space-time computations, the parametric coordinate system is extended with a temporal dimension using the parameter :math:`\tau \in [-1, 1]` in parametric time, which corresponds to a physical time slab :math:`[T_n, T_{n+1}]`.

The mapping from parametric time :math:`\tau` to physical time :math:`T` is:

.. math::

   T(\tau) = \frac{T_n + T_{n+1}}{2} + \frac{T_{n+1} - T_n}{2} \tau

where :math:`\tau = -1` corresponds to :math:`T = T_n` and :math:`\tau = +1` corresponds to :math:`T = T_{n+1}`.

Space-Time Functional Spaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For space-time Lagrange interpolation, the complete functional space is formed by the tensor product of the spatial function space with the temporal linear space:

.. math::

   \mathcal{V}_{p,q}(u,v,w,\tau) = \mathcal{V}_p(u,v,w) \otimes \mathcal{L}_q(\tau)

where:

* :math:`p` is the spatial interpolation order
* :math:`q` is the temporal interpolation order
* :math:`\mathcal{V}_p(u,v,w)` is any of the spatial function spaces defined in the Lagrange function space table (Complete, Edge Serendipity, or Face Serendipity)
* :math:`\mathcal{L}_q(\tau) = \text{span}\{\tau^i, 0 \leq i \leq q\}` is the temporal linear space

The total number of space-time control points is:

.. math::

   N_{\text{total}} = N_{\text{space}} \times (q+1)

where :math:`N_{\text{space}}` is the number of spatial control points for the chosen element type and spatial order :math:`p`.

Data Layout for Space-Time Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _data_layout_spacetime:

When temporal interpolation is used (:math:`q > 0`), the data arrays for both control points and solution values must follow a **time-major ordering** convention:

.. important::
   **Array Ordering Convention**: Data is organized with the **temporal index varying in the outer loop** and the **spatial indices varying in the inner loops**. This is denoted as **[Time][Space]** ordering.

For Lagrange control points with spatial order :math:`p` and temporal order :math:`q`:

* Number of spatial control points: :math:`N_{\text{space}}` (depends on element type and :math:`p`)
* Number of temporal control points: :math:`N_{\text{time}} = q + 1`
* **Total number of space-time control points**: :math:`N_{\text{total}} = N_{\text{space}} \times N_{\text{time}}`

The :sidskey:`LagrangeControlPoints` arrays (parametric coordinates :math:`u, v, w, \tau`) are ordered as:

.. code-block:: c

   for (int t = 0; t <= q; t++)           // Temporal index (outer)
     for (int s = 0; s < N_space; s++)    // Spatial index (inner)
       idx = t * N_space + s;
       // u[idx], v[idx], w[idx], tau[idx] define control point

**Example**: For a QUAD element with :math:`p=2` (spatial) and :math:`q=1` (temporal):

* :math:`N_{\text{space}} = (p+1)^2 = 9` spatial control points
* :math:`N_{\text{time}} = q+1 = 2` temporal control points
* :math:`N_{\text{total}} = 9 \times 2 = 18` total control points
* Array layout: ``[spatial_0_at_t0, spatial_1_at_t0, ..., spatial_8_at_t0, spatial_0_at_t1, spatial_1_at_t1, ..., spatial_8_at_t1]``

For solution data in :sidsref:`FlowSolution_t`, the same **time-major** ordering applies:

* Solution values at each space-time control point are stored in the same order as the control points
* Element :math:`e` with :math:`N_{\text{total}}^e` control points contributes entries :math:`[e \times N_{\text{total}}^e, (e+1) \times N_{\text{total}}^e)` to the global solution array
* Within each element's data block, time varies in the outer loop, space in the inner loop

.. warning::
   Using the wrong array ordering (space-major instead of time-major) will result in incorrect interpolation and transposition errors that may be difficult to debug. Always verify that temporal indices vary in the outer loop.

Space-Time Parametric Modal Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For space-time parametric modal interpolation, the spatial monomials are multiplied by monomials in parametric time :math:`\tau`. The loop ordering depends on the element topology and **must extend** the spatial ordering with time as the outermost loop:

**Tensor Product Elements** (BAR, QUAD, HEXA):

* **1D in space plus time** (BAR)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int i=0; i<=p; i++)      // u (space)
        f[idx++] = tau^h * u^i;

* **2D in space plus time** (QUAD)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int j=0; j<=p; j++)      // v (space)
        for (int i=0; i<=p; i++)    // u (space)
          f[idx++] = tau^h * u^i * v^j;

* **3D in space plus time** (HEXA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int k=0; k<=p; k++)      // w (space)
        for (int j=0; j<=p; j++)    // v (space)
          for (int i=0; i<=p; i++)  // u (space)
            f[idx++] = tau^h * u^i * v^j * w^k;

**Simplex Elements** (TRI, TETRA):

* **2D in space plus time** (TRI)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int i=0; i<=p; i++)      // Pascal triangle in (u,v)
        for (int j=0; j<=i; j++)
          f[idx++] = tau^h * u^(i-j) * v^j;

* **3D in space plus time** (TETRA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int i=0; i<=p; i++)      // Pascal tetrahedron in (u,v,w)
        for (int j=0; j<=i; j++)
          for (int k=0; k<=i-j; k++)
            f[idx++] = tau^h * u^(i-j-k) * v^k * w^j;

**Hybrid Elements** (PENTA):

* **3D in space plus time** (PENTA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // tau (time, outermost)
      for (int m=0; m<=p; m++)      // w (prism axis)
        for (int i=0; i<=p; i++)    // Pascal triangle in (u,v)
          for (int j=0; j<=i; j++)
            f[idx++] = tau^h * u^(i-j) * v^j * w^m;

This space-time formulation reverts to purely spatial interpolation (including the ordering) for the default temporal order :math:`q=0`.

.. note::
   The loop ordering shown above (temporal index ``h`` in the outermost loop) defines both the **basis function ordering** and the **data layout** for modal coefficients. This **time-major** ordering is consistent with the data layout convention for Lagrange interpolation.

Space-Time Cartesian Modal Interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For space-time Cartesian modal interpolation, an element-local origin for the time dimension is defined as the midpoint of the relevant physical time slab :math:`[T_n, T_{n+1}]`:

.. math::

   t = T - \frac{T_n + T_{n+1}}{2}

**Temporal Normalization for Numerical Stability**

.. danger::
   **Critical Numerical Stability Requirement**: Using physical time units directly in temporal monomials can lead to catastrophic floating-point overflow or underflow.

   **Problem**:

   * If :math:`\Delta t = T_{n+1} - T_n` is very small (microseconds, nanoseconds): :math:`t^2, t^3, \ldots` will **underflow** to zero
   * If :math:`\Delta t` is very large (years, centuries): :math:`t^2, t^3, \ldots` will **overflow** to infinity
   * The same applies to spatial coordinates in physical units (millimeters vs. kilometers)

   **Requirement**: Implementations **MUST** normalize temporal coordinates to ensure numerical stability and data portability across different unit systems.

**Recommended Temporal Normalization**: Define a normalized temporal coordinate :math:`\theta` by scaling with the time slab width:

.. math::

   \theta = \frac{t}{\Delta t / 2} = \frac{2(T - T_n)}{T_{n+1} - T_n} - 1

This maps :math:`\theta \in [-1, 1]`, matching the parametric time convention and ensuring :math:`\theta^h \in \mathcal{O}(1)` for all :math:`h \leq q`.

**Combined Space-Time Normalization**: The spatial monomials (in normalized element-local Cartesian coordinates :math:`\xi, \eta, \zeta`) are multiplied by temporal monomials in **normalized time** :math:`\theta`. The loop ordering depends on the element topology and **must extend** the spatial ordering with time as the outermost loop:

**Tensor Product Elements** (BAR, QUAD, HEXA):

* **1D in space plus time** (BAR)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int i=0; i<=p; i++)      // xi (space)
        f[idx++] = theta^h * xi^i;

* **2D in space plus time** (QUAD)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int j=0; j<=p; j++)      // eta (space)
        for (int i=0; i<=p; i++)    // xi (space)
          f[idx++] = theta^h * xi^i * eta^j;

* **3D in space plus time** (HEXA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int k=0; k<=p; k++)      // zeta (space)
        for (int j=0; j<=p; j++)    // eta (space)
          for (int i=0; i<=p; i++)  // xi (space)
            f[idx++] = theta^h * xi^i * eta^j * zeta^k;

**Simplex Elements** (TRI, TETRA):

* **2D in space plus time** (TRI)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int i=0; i<=p; i++)      // Pascal triangle in (xi,eta)
        for (int j=0; j<=i; j++)
          f[idx++] = theta^h * xi^(i-j) * eta^j;

* **3D in space plus time** (TETRA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int i=0; i<=p; i++)      // Pascal tetrahedron in (xi,eta,zeta)
        for (int j=0; j<=i; j++)
          for (int k=0; k<=i-j; k++)
            f[idx++] = theta^h * xi^(i-j-k) * eta^k * zeta^j;

**Hybrid Elements** (PENTA):

* **3D in space plus time** (PENTA)::

    idx = 0;
    for (int h=0; h<=q; h++)        // theta (time, outermost)
      for (int m=0; m<=p; m++)      // zeta (prism axis)
        for (int i=0; i<=p; i++)    // Pascal triangle in (xi,eta)
          for (int j=0; j<=i; j++)
            f[idx++] = theta^h * xi^(i-j) * eta^j * zeta^m;

.. note::
   The loop ordering shown above (temporal index ``h`` in the outermost loop) defines both the **basis function ordering** and the **data layout** for modal coefficients.

.. important::
   **Storage**: When using normalized coordinates :math:`(\xi, \eta, \zeta, \theta)`, the normalization parameters (characteristic length :math:`h^e` and time slab bounds :math:`T_n, T_{n+1}`) must be stored to enable reconstruction of physical values. This ensures data portability and prevents ambiguity in interpreting modal coefficients.

References
^^^^^^^^^^

.. [BergotCohenDurufle2010] M. Bergot, G. Cohen, and M. Duruflé, "Higher-order Finite Elements for Hybrid Meshes Using New Nodal Pyramidal Elements," Journal of Scientific Computing 42, pp. 345-381 (2010), doi: 10.1007/s10915-009-9334-9
