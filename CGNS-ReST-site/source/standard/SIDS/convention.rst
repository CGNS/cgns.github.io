.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

Conventions
-----------

Data Structure Notation Conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Structured Grid Notation and Indexing Conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unstructured Grid Element Numbering Conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1-D (Line) Elements
~~~~~~~~~~~~~~~~~~~

1-D elements represent geometrically a line (or bar).
The linear form, ``BAR_2``, is composed of two nodes at each extremity
of the line.
The quadratic form, ``BAR_3``, has an additional node located at
the middle of the line.
The cubic form of the line, ``BAR_4``, contains two nodes
interior to the endpoints.
The quartic form of the line, ``BAR_5``, contains three nodes
interior to the endpoints.

Linear and Quadratic Elements
+++++++++++++++++++++++++++++

.. figure:: ../../../images/sids/figs/bar_2.png
   :width: 400px
   :align: center

   ``BAR_2``
   
.. figure:: ../../../images/sids/figs/bar_3.png
   :width: 400px
   :align: center

   ``BAR_3``
   
Cubic Elements
++++++++++++++

.. figure:: ../../../images/sids/figs/bar_4.png
   :width: 400px
   :align: center

   ``BAR_4``
   
Quartic Elements
++++++++++++++++

.. figure:: ../../../images/sids/figs/bar_5.png
   :width: 400px
   :align: center

   ``BAR_5``
   
.. note::

   Nodes are uniformly spaced on all edges for all higher order elements.

2D (Surface) Elements
~~~~~~~~~~~~~~~~~~~~~

.. |inline_image_N21| image:: ../../../images/sids/eqs/N21.gif
			      
.. |inline_image_N31| image:: ../../../images/sids/eqs/N31.gif
			      
.. |inline_image_N| image:: ../../../images/sids/eqs/N.gif
			      
.. |inline_image_normal| image:: ../../../images/sids/eqs/normal.gif

2-D elements represent a surface in either 2-D or 3-D space.
Note that in physical space, the surface need not be planar, but
may be curved.
In a 2-D mesh the elements represent the cells themselves; in a 3-D
mesh they represent faces.
CGNS supports two shapes of 2-D elements - triangles
and quadrangles.

The normal vector of a 2-D element is computed using the cross product
of a vector from the first to second node, with a vector from the first
to third node.
The direction of the normal is such that the three vectors
(i.e., |inline_image_N21|, |inline_image_N31|, and
|inline_image_N|) form a right-handed triad.

|inline_image_normal| 

In a 2-D mesh, all elements must be oriented the same way; i.e., all
normals must point toward the same side of the mesh.

3D (Volume) Elements
~~~~~~~~~~~~~~~~~~~~

Six types of triangular elements are supported in CGNS, ``TRI_3``,
``TRI_6``, ``TRI_9``, ``TRI_10``, ``TRI_12``, and ``TRI_15``.
``TRI_3`` elements are composed of three nodes located at the
three geometric corners of the triangle.
``TRI_6`` elements have three additional nodes located at the
middles of the three edges.
The cubic forms of triangular elements, ``TRI_9`` and ``TRI_10``
contain two interior nodes along each edge, and an interior face node
in the case of ``TRI_10``.
The quartic forms of triangular elements, ``TRI_12`` and ``TRI_15``
contain three interior nodes along each edge, and three interior face nodes
in the case of ``TRI_15``.

Linear and Quadratic Elements
+++++++++++++++++++++++++++++

.. figure:: ../../../images/sids/figs/tri_3_6.png
   :width: 800px
   :align: center
	   
Cubic Elements
++++++++++++++

.. figure:: ../../../images/sids/figs/tri_9_10.png
   :width: 800px
   :align: center

Unstructured Grid Example
~~~~~~~~~~~~~~~~~~~~~~~~~

Multizone interfaces
~~~~~~~~~~~~~~~~~~~~

.. last line
