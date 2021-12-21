.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)



Grid Coordinates, Elements, and Flow Solution
---------------------------------------------
This section defines structure types for describing the grid coordinates, element data, and flow solution data pertaining to a zone. Entities of each of the structure types defined in this section are contained in the :sidsref:`Zone_t` structure.

.. _GridCoordinates_t:

Grid Coordinates Structure Definition: :sidskey:`GridCoordinates_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 The physical coordinates of the grid vertices are described by the :sidskey:`GridCoordinates_t` structure. This structure contains a list for the data arrays of the individual components of the position vector. It also provides a mechanism for identifying rind-point data included within the position-vector arrays.

.. code-block:: sids

 GridCoordinates_t< int IndexDimension, int VertexSize[IndexDimension], int PhysicalDimension> :=
    {
    DataArray_t<DataType, PhysicalDimension, 2> BoundingBox ;          (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    Rind_t<IndexDimension> Rind ;                                      (o/d)

    List( DataArray_t<DataType, IndexDimension, DataSize[]>
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of GridCoordinates_t and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, or :sidskey:`Rind`.
    2. There are no required fields for :sidskey:`GridCoordinates_t`. :sidsref:`Rind` has a default if absent; the default is equivalent to having a :sidskey:`Rind` structure whose :sidskey:`RindPlanes` array contains all zeros.
    3. The structure parameter DataType must be consistent with the data stored in the :sidsref:`DataArray_t` substructures.

:sidskey:`GridCoordinates_t` requires two structure parameters: :sidskey:`IndexDimension` identifies the dimensionality of the grid-size arrays, and :sidskey:`VertexSize` is the number of vertices in each index direction excluding rind points. For unstructured zones, :sidskey:`IndexDimension` is always 1 and :sidskey:`VertexSize` is the total number of vertices, excluding rind points.

The grid-coordinates data is stored in the list of :sidskey:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity may contain a single component of the position vector (e.g., three separate :sidskey:`DataArray_t` entities are used for x, y, and z).

Standardized data-name identifiers for the grid coordinates are described in :ref:`Conventions for Data-Name Identifiers <dataname_grid>`.

:sidskey:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points (for unstructured grids) included in the grid-coordinates data. If :sidskey:`Rind` is absent, then the :sidskey:`DataArray_t` structure entities contain only "core" vertices of a zone; core refers to all interior and bounding vertices of a zone - :sidskey:`VertexSize` is the number of core vertices. Core vertices in a zone begin at [1,1,1] (for a structured zone in 3-D) and end at :sidskey:`VertexSize`. If :sidskey:`Rind` is present, it will provide information on the number of "rind" points in addition to the core points that are contained in the :sidskey:`DataArray_t` structures. Indices in :sidskey:`DataArray_t` structures have the range :math:`[1 - a,1 - c,1 - e]` to :math:`[II + b,JJ + d,KK + f]` where :code:`VertexSize = [II,JJ,...]` and :code:`RindPlanes = [a,b,...]` (see the :sidsref:`Rind_t` structure for the definition of :sidskey:`RindPlanes`).

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional grid coordinates, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`. An example that uses these grid-coordinate defaults is shown under :ref:`Grid Coordinates Examples<grid_example>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

The :sidskey:`BoundingBox` array is optional and provides a measure within which all the grid points lie. It stores minima and maxima of Coordinates values sorted by alphabetical order for Cartesian and Cylindrical coordinate systems while Spherical and Auxiliary coordinate systems retain a specific order to be coherent with the existing SIDS notation:

.. table::
  :width: 400px
  :align: center

  ================  ========================================================================
  System   	       Bounding Box
  ================  ========================================================================
  Cartesian 3-D     .. math::
                      [[Min(CoordinateX), Min(CoordinateY), Min(CoordinateZ)], \\
                       [Max(CoordinateX), Max(CoordinateY), Max(CoordinateZ)]]
  ----------------  ------------------------------------------------------------------------
  Cylindrical 3-D    .. math::
                       [[Min(CoordinateR), Inf(CoordinateTheta), Min(CoordinateX)], \\
                        [Max(CoordinateR), Sup(CoordinateTheta), Max(CoordinateX)]]

                     or

                     .. math::
                       [[Min(CoordinateR), Inf(CoordinateTheta), Min(CoordinateY)], \\
                        [Max(CoordinateR), Sup(CoordinateTheta), Max(CoordinateY)]]

                     or

                     .. math::
                       [[Min(CoordinateR), Inf(CoordinateTheta), Min(CoordinateZ)], \\
                        [Max(CoordinateR), Sup(CoordinateTheta), Max(CoordinateZ)]]
  ----------------  ------------------------------------------------------------------------
  Spherical         .. math::
                      [[Min(CoordinateR), Inf(CoordinateTheta), Inf(CoordinatePhi)], \\
                       [Max(CoordinateR), Sup(CoordinateTheta), Sup(CoordinatePhi)]]
  ----------------  ------------------------------------------------------------------------
  Auxiliary 3-D     .. math::
                      [[Min(CoordinateXi), Min(CoordinateEta), Min(CoordinateZeta)], \\
                       [Max(CoordinateXi), Max(CoordinateEta), Max(CoordinateZeta)]]
  ================  ========================================================================

Thus, all coordinate systems are handled in a deterministic way. For 2-D coordinate system, the order is kept the same as for 3-D.
Angle coordinate part of a bounding box is defined by :math:`Inf(CoordinateTheta)` and :math:`Sup(CoordinateTheta)` (respectively :math:`Inf(CoordinatePhi)` and :math:`Sup(CoordinatePhi)` for spherical coordinate angle) where :math:`Inf` and :math:`Sup` operators ensure unicity of the angle interval. The constraints for valid angle bounding box limits are:

- :math:`Inf(CoordinateTheta)` is included in :math:`[0; 2 π]`
- :math:`Inf(CoordinateTheta) < Sup(CoordinateTheta)`
- :math:`Sup(CoordinateTheta) - Inf(CoordinateTheta) ≤ 2 π`

.. _DataSize_grid:

.. c:function:: FUNCTION DataSize()

   :return value: one-dimensional ``int`` array of length :sidskey:`IndexDimension`
   :dependencies: :sidskey:`IndexDimension`, :sidskey:`VertexSize[]`, :sidskey:`Rind`

   :sidskey:`GridCoordinates_t` requires a single structure function, named :sidskey:`DataSize`, to identify the array sizes of the grid-coordinates data. A function is required for the following reasons:

     - the entire grid, including both core and rind points, is stored in the :sidsref:`DataArray_t` entities;
     - the :sidskey:`DataArray_t` structure is simple in that it doesn't know anything about core versus rind data; it just knows that it contains data of some given size;
     - to make all the :sidskey:`DataArray_t` entities syntactically consistent in their size (i.e., by syntax entities containing x, y and z must have the same dimensionality and dimension sizes), the size of the array is passed onto the :sidskey:`DataArray_t` structure as a parameter.

   .. code-block:: sids

     if (Rind is absent) then
       {
       DataSize[] = VertexSize[] ;
       }
     else if (Rind is present) then
       {
       DataSize[] = VertexSize[] + [a + b,...] ;
       }

   where :code:`RindPlanes = [a,b,...]` (see the :sidsref:`Rind_t` structure for the definition of :sidskey:`RindPlanes`).


.. _grid_example:

Grid Coordinates Examples
^^^^^^^^^^^^^^^^^^^^^^^^^
This section contains examples of grid coordinates. These examples show the storage of the grid-coordinate data arrays, as well as different mechanisms for describing the class of data and the system of units or normalization.

Example - Cartesian Coordinates for a 2-D Structured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses Cartesian coordinates for a 2-D grid of size 17 × 33; the data arrays include only core vertices, and the coordinates are in units of feet.

.. code-block:: sids

  !  IndexDimension = 2
  !  VertexSize = [17,33]
  GridCoordinates_t<2, [17,33]> GridCoordinates =
    {{
    DataArray_t<real, 2, [17,33]> CoordinateX =
      {{
      Data(real, 2, [17,33]) = ((x(i,j), i=1,17), j=1,33) ;

      DataClass_t DataClass = Dimensional ;

      DimensionalUnits_t DimensionalUnits =
        {{
        MassUnits        = MassUnitsNull ;
        LengthUnits      = Foot ;
        TimeUnits        = TimeUnitsNull ;
        TemperatureUnits = TemperatureUnitsNull ;
        AngleUnits       = AngleUnitsNull ;
        }} ;
      }} ;

    DataArray_t<real, 2, [17,33]> CoordinateY =
      {{
      Data(real, 2, [17,33]) = ((y(i,j), i=1,17), j=1,33) ;

      DataClass_t DataClass = Dimensional ;

      DimensionalUnits_t DimensionalUnits =
        {{
        MassUnits        = MassUnitsNull ;
        LengthUnits      = Foot ;
        TimeUnits        = TimeUnitsNull ;
        TemperatureUnits = TemperatureUnitsNull ;
        AngleUnits       = AngleUnitsNull ;
        }} ;
      }} ;
    }} ;

From the :ref:`Conventions for Data-Name Identifiers <dataname>`, the identifiers for :math:`x` and :math:`y` are :sidskey:`CoordinateX` and :sidskey:`CoordinateY`, respectively, and both have a data type of :sidskey:`real`. The value of :sidsref:`DataClass` in :sidskey:`CoordinateX` and :sidskey:`CoordinateY` indicate the data is dimensional, and :sidsref:`DimensionalUnits` specifies the appropriate units are feet. The :sidsref:`DimensionalExponents` entity is absent from both :sidskey:`CoordinateX` and :sidskey:`CoordinateY`; the information that :math:`x` and :math:`y` are lengths can be inferred from the :ref:`data-name identifier conventions for coordinate systems <dataname_grid>`.

Note that FORTRAN multidimensional array indexing is used to store the data; this is reflected in the FORTRAN-like implied do-loops for :code:`x(i,j)` and :code:`y(i,j)`.

Because the dimensional units for both :math:`x` and :math:`y` are the same, an alternate approach is to set the data class and system of units using :sidsref:`DataClass` and :sidsref:`DimensionalUnits` at the :sidsref:`GridCoordinates_t` level, and eliminate this information from each instance of :sidsref:`DataArray_t`.

.. code-block:: sids

  GridCoordinates_t<2, [17,33]> GridCoordinates =
    {{
    DataClass_t DataClass = Dimensional ;

    DimensionalUnits_t DimensionalUnits =
      {{
      MassUnits        = MassUnitsNull ;
      LengthUnits      = Foot ;
      TimeUnits        = TimeUnitsNull ;
      TemperatureUnits = TemperatureUnitsNull ;
      AngleUnits       = AngleUnitsNull ;
      }} ;

    DataArray_t<real, 2, [17,33]> CoordinateX =
      {{
      Data(real, 2, [17,33]) = ((x(i,j), i=1,17), j=1,33) ;
      }} ;

    DataArray_t<real, 2, [17,33]> CoordinateY =
      {{
      Data(real, 2, [17,33]) = ((y(i,j), i=1,17), j=1,33) ;
      }} ;
    }} ;


Since the :sidsref:`DataClass` and :sidsref:`DimensionalUnits` entities are not present in :sidskey:`CoordinateX` and :sidskey:`CoordinateY`, the established rules for dimensional data dictate that :sidskey:`DataClass` and :sidskey:`DimensionalUnits` specified at the :sidsref:`GridCoordinates_t` level be used to retrieve the information.

Example - Cylindrical Coordinates for a 3-D Structured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses cylindrical coordinates for a 3-D grid whose core size is 17 × 33 × 9; the grid contains a single plane of rind on the minimum and maximum k faces. The coordinates are nondimensional.

.. code-block:: sids

  !  IndexDimension = 3
  !  VertexSize = [17,33,9]
  GridCoordinates_t<3, [17,33,9]> GridCoordinates =
    {{
    Rind_t<3> Rind =
      {{
      int[6] RindPlanes = [0,0,0,0,1,1] ;
      }} ;

    ! DataType = real
    ! IndexDimension = 3
    ! DataSize = VertexSize + [0,0,2] = [17,33,11]
    DataArray_t<real, 3, [17,33,11]> CoordinateRadius =
      {{
      Data(real, 3, [17,33,11]) = (((r(i,j,k), i=1,17), j=1,33), k=0,10) ;

      DataClass_t DataClass = NormalizedByUnknownDimensional ;
      }} ;

    DataArray_t<real, 3, [17,33,11]> CoordinateZ     = {{ }} ;
    DataArray_t<real, 3, [17,33,11]> CoordinateTheta = {{ }} ;
    }} ;

The value of :sidskey:`RindPlanes` specifies two rind planes on the minimum and maximum k faces. These rind planes are reflected in the structure function :sidsref:`DataSize` which is equal to the number of core vertices plus two in the k dimension. The value of :sidskey:`DataSize` is passed to the :sidsref:`DataArray_t` entities. The value of :sidsref:`DataClass` indicates the data is nondimensional. Note that if :sidskey:`DataClass` is set as :sidskey:`NormalizedByUnknownDimensional` at a higher level (:sidsref:`CGNSBase_t` or :sidsref:`Zone_t`), then it is not needed here.

Note that the entities :sidskey:`CoordinateZ` and :sidskey:`CoordinateTheta` are abbreviated.

Example - Cartesian Coordinates for a 3-D Unstructured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses Cartesian grid coordinates for a 3-D unstructured zone where :sidskey:`VertexSize` is 15.

.. code-block:: sids

  GridCoordinates_t<1, 15> GridCoordinates =
    {{

    ! DataType = real
    ! IndexDimension = 1
    ! DataSize = VertexSize = 15
    DataArray_t<real, 1, 15> CoordinateX =
      {{
      Data(real, 1, 15) = (x(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> CoordinateY =
      {{
      Data(real, 1, 15) = (y(i), i=1,15) ;
      }} ;

    DataArray_t<real, 1, 15> CoordinateZ =
      {{
      Data(real, 1, 15) = (z(i), i=1,15) ;
      }} ;
    }} ;


Elements Structure Definition: ``Elements_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 The :sidskey:`Elements_t` data structure is required for unstructured zones, and contains the element connectivity data, the element type, the element range, the parent elements data, and the number of boundary elements.

.. code-block:: sids

  Elements_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    Rind_t<IndexDimension> Rind ;                                      (o/d)

    IndexRange_t ElementRange ;                                        (r)

    int ElementSizeBoundary ;                                          (o/d)

    ElementType_t ElementType ;                                        (r)

    DataArray_t<int, 1, ElementDataSize> ElementConnectivity ;         (r)
    DataArray_t<int, 1, ElementSize + 1> ElementStartOffset ;          (r)

    DataArray_t<int, 2, [ElementSize, 2]> ParentElements;              (o)
    DataArray_t<int, 2, [ElementSize, 2]> ParentElementsPosition;      (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`Elements_t` and shall not include the names :sidskey:`ElementConnectivity`, :sidskey:`ElementRange`, :sidskey:`ParentElements`, :sidskey:`ParentElementsPosition`, or :sidskey:`Rind`.
    2. :sidsref:`IndexRange_t`, :sidsref:`ElementType_t`, and :sidsref:`ElementConnectivity` are the required fields within the :sidskey:`Elements_t` structure. :sidskey:`ElementStartOffset` is required only for :sidskey:`MIXED`, :sidskey:`NGON_n` and :sidskey:`NFACE_n` element type. :sidskey:`Rind` has a default if absent; the default is equivalent to having a :sidskey:`Rind` structure whose :sidskey:`RindPlanes` array contains all zeros.


:sidsref:`Rind` is an optional field that indicates the number of rind elements included in the elements data. If :sidskey:`Rind` is absent, then the :sidsref:`DataArray_t` structure entities contain only core elements of a zone. If :sidskey:`Rind` is present, it will provide information on the number of rind elements, in addition to the core elements, that are contained in the :sidskey:`DataArray_t` structures.

Note that the usage of rind data with respect to the size of the :sidskey:`DataArray_t` structures is different under :sidskey:`Elements_t` than elsewhere. For example, when rind coordinate data is stored under :sidsref:`GridCoordinates_t`, the parameter :sidskey:`VertexSize` accounts for the core data only. The size of the :sidskey:`DataArray_t` structures containing the grid coordinates is determined by the :sidskey:`DataSize` function, which adds the number of rind planes or points to :sidskey:`VertexSize`. But for the element connectivity, the size of the :sidskey:`DataArray_t` structures containing the connectivity data is just :sidskey:`ElementDataSize`, which depends on :sidskey:`ElementSize`, and includes both the core and rind elements.

:sidskey:`ElementRange` contains the index of the first and last elements defined in :sidsref:`ElementConnectivity`. The elements are indexed with a global numbering system, starting at 1, for all element sections under a given :sidsref:`Zone_t` data structure. The global numbering insures that each element, whether it's a cell, a face, or an edge, is uniquely identified by its number. They are also listed as a continuous list of element numbers within any single element section. Therefore the number of elements in a section is:

.. parsed-literal::
  ElementSize\  = ElementRange.end - ElementRange.start + 1

The element indices are used for the boundary condition and zone connectivity definition.

:sidskey:`ElementSizeBoundary` indicates if the elements are sorted, and how many boundary elements are recorded. By default, :sidskey:`ElementSizeBoundary` is set to zero, indicating that the elements are not sorted. If the elements are sorted, :sidskey:`ElementSizeBoundary` is set to the number of elements at the boundary. Consequently:

.. parsed-literal::
  ElementSizeInterior\  = ElementSize - ElementSizeBoundary

:sidskey:`ElementType_t` is an enumeration of the supported element types:

.. code-block:: sids

  ElementType_t := Enumeration(
     ElementTypeNull, ElementTypeUserDefined, NODE, BAR_2, BAR_3,
     TRI_3, TRI_6, QUAD_4, QUAD_8, QUAD_9,
     TETRA_4, TETRA_10, PYRA_5, PYRA_14,
     PENTA_6, PENTA_15, PENTA_18, HEXA_8, HEXA_20, HEXA_27,
     MIXED, PYRA_13, NGON_n, NFACE_n,
     BAR_4, TRI_9, TRI_10, QUAD_12, QUAD_16,
     TETRA_16, TETRA_20, PYRA_21, PYRA_29, PYRA_30,
     PENTA_24, PENTA_38, PENTA_40, HEXA_32, HEXA_56, HEXA_64 );

The conventions for element numbering for the various supported types are described in :ref:`Unstructured Grid Element Numbering Conventions <unstructgrid>`.

For all element types except :sidskey:`MIXED`, :sidskey:`ElementConnectivity` contains the list of nodes for each element. If the elements are sorted, then it must first list the connectivity of the boundary elements, then that of the interior elements.

.. parsed-literal::
  ElementConnectivity = Node1\ :sub:`1`\ , Node2\ :sub:`1`\ , ... NodeN\ :sub:`1`\ ,
                        Node1\ :sub:`2`\ , Node2\ :sub:`2`\ , ... NodeN\ :sub:`2`\ ,
                        ...
                        Node1\ :sub:`M`\ , Node2\ :sub:`M`\ , ... NodeN\ :sub:`M`

where :literal:`M` is the total number of elements (i.e. :sidskey:`ElementSize` ), and :literal:`N` is the number of nodes per element.

:sidskey:`ElementDataSize` indicates the total size (number of integers) of the array :sidskey:`ElementConnectivity`. For all element types except :sidskey:`MIXED`, :sidskey:`NGON_n`, and :sidskey:`NFACE_n`, :sidskey:`ElementDataSize` is given by:

.. parsed-literal::
  ElementDataSize = ElementSize \* NPE[ElementType]

where :sidskey:`NPE[ElementType]` is a function returning the number of nodes for the given :sidskey:`ElementType`. For example, :sidskey:`NPE[HEXA_8]=8`.

When the section :sidskey:`ElementType` is :sidskey:`MIXED`, the data array :sidskey:`ElementConnectivity` contains
one extra integer per element, to hold each individual element type:

.. parsed-literal::

  ElementConnectivity = Etype\ :sub:`1`\ , Node1\ :sub:`1`\ , Node2\ :sub:`1`\ , ... NodeN\ :sub:`1`\ ,
                        Etype\ :sub:`2`\ , Node1\ :sub:`2`\ , Node2\ :sub:`2`\ , ... NodeN\ :sub:`2`\ ,
                        ...
                        Etype\ :sub:`M`\ , Node1\ :sub:`M`\ , Node2\ :sub:`M`\ , ... NodeN\ :sub:`M`

where again :literal:`M` is the total number of elements, and :math:`\scriptsize\mathsf{N}_\mathrm{i}` :literal:`Ni`  is the number of nodes in element :literal:`i`.
The data array :sidskey:`ElementStartOffset` contains the starting positions of each element in the :sidskey:`ElementConnectivity` data array
and its last value corresponds to the :sidskey:`ElementConnectivity` total size:

.. parsed-literal::

  ElementStartOffset  = 0, NPE[Etype\ :sub:`1`\ ] + 1, ... ElementStartOffset[n-1] + NPE[Etype\ :sub:`n`\ ] + 1,
                        ..., ElementStartOffset[M-1] + NPE[Etype\ :sub:`M`\ ] + 1 = ElementDataSize

In the case of :sidskey:`MIXED` element section, :sidskey:`ElementDataSize` is given by:

.. parsed-literal::

  ElementDataSize = ∑(NPE[ElementType\ :sub:`n`\ ] + 1)

where the summation is over :literal:`n`, and :literal:`n` represents a specific element type.

Arbitrary polyhedral elements may be defined using the :sidskey:`NGON_n` and :sidskey:`NFACE_n` element types. The :sidskey:`NGON_n` element type is used to specify all the faces in the grid, and the :sidskey:`NFACE_n` element type is then used to define the polyhedral elements as a collection of these faces. Except for boundary faces, each face of a polyhedral element must be shared by another polyhedral element.

For example, for :sidskey:`NGON_n`, the data array :sidskey:`ElementConnectivity` contains a list of nodes making up each face in the grid while :sidskey:`ElementStartOffset` provides the starting position of each face in the :sidskey:`ElementConnectivity` array:

.. parsed-literal::

  ElementConnectivity = Node1\ :sub:`1`\ , Node2\ :sub:`1`\ , ... NodeN\ :sub:`1`\ ,
                        Node1\ :sub:`2`\ , Node2\ :sub:`2`\ , ... NodeN\ :sub:`2`\ ,
                        ...
                        Node1\ :sub:`M`\ , Node2\ :sub:`M`\ , ... NodeN\ :sub:`M`

  ElementStartOffset  = 0, Nnodes\ :sub:`1`\ , Nnodes\ :sub:`1`\  + Nnodes\ :sub:`2`\ , ...
                        ..., ElementStartOffset[i-1] + Nnodes\ :sub:`i`\ ,
                        ..., ElementStartOffset[M-1] + Nnodes\ :sub:`M` = ElementDataSize

where here :literal:`M` is the total number of faces, and :literal:`Nnodesi` is the number of nodes in face :literal:`i`.
The :sidskey:`ElementDataSize` is the total number of nodes defining all the faces.
Note that the number of nodes in face :literal:`i` is given by:

.. parsed-literal::

  Nnodes\ :sub:`i` = ElementStartOffset[i+1] - ElementStartOffset[i]

Then for :sidskey:`NFACE_n`, :sidskey:`ElementConnectivity` contains the list of face elements making up each polyhedral element,
while :sidskey:`ElementStartOffset` provides the starting position of each polyhedral element in the :sidskey:`ElementConnectivity` array:

.. parsed-literal::

  ElementConnectivity = Face1\ :sub:`1`\ , Face2\ :sub:`1`\ , ... FaceN\ :sub:`1`\ ,
                        Face1\ :sub:`2`\ , Face2\ :sub:`2`\ , ... FaceN\ :sub:`2`\ ,
                        ...
                        Face1\ :sub:`M`\ , Face2\ :sub:`M`\ , ... FaceN\ :sub:`M`

  ElementStartOffset  = 0, Nfaces\ :sub:`1`\ , Nfaces\ :sub:`1`\  + Nfaces\ :sub:`2`\ , ...
                        ..., ElementStartOffset[i-1] + Nfaces\ :sub:`i`\ ,
                        ..., ElementStartOffset[M-1] + Nfaces\ :sub:`M`\  = ElementDataSize

where now :literal:`M` is the total number of polyhedral elements, and :literal:`Nfacesi` is the number of faces in element :literal:`i`.
The sign of the face number determines its orientation (i.e., the direction of the face normal, constructed as defined by the convention for 2-D elements). If the face number is positive, the face normal is directed outward; if it's negative, the face normal is directed inward. The ElementDataSize is the sum of the number of faces defining each polyhedral element.
Note that the number of faces in element :literal:`i` is given by:

.. parsed-literal::

  Nfaces\ :sub:`i`\  = ElementStartOffset[i+1] - ElementStartOffset[i]

For face elements in 3-D, or bar element in 2-D, additional data may be provided for each element in :sidskey:`ParentElements` and :sidskey:`ParentElementsPosition`.
The element numbers of the two adjacent cells for each face are given in :sidskey:`ParentElements`.
The corresponding canonical positions of the face in the two parent cells is given in :sidskey:`ParentElementsPosition`;
these canonical face positions are defined in the section :ref:`Unstructured Grid Element Numbering Conventions <unstructgrid>`.
For faces on the boundary of the domain, the second parent is set to zero.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and
:sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Elements Examples
^^^^^^^^^^^^^^^^^

This section contains four examples of elements definition in CGNS.
The first example is for a simple three-element tetrahedral grid, using the :sidskey:`TETRA_4` element type.
The second example is for the same grid as the first example, but the elements are treated as general polyhedra to illustrate the use of the :sidskey:`NGON_n` and :sidskey:`NFACE_n` element types.
The third and fourth examples are for an unstructured zone with 15 tetrahedral and 10 hexahedral elements, with the third example defining the elements in separate sections for the :sidskey:`TETRA_4` and :sidskey:`HEXA_8` element types, and the fourth example combining them using the :sidskey:`MIXED` element type.

Example - TETRA_4 Element Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses the simple three-element tetrahedral grid shown below.

.. figure:: ../../../images/sids/figs/ex_tetra.gif
   :width: 400px
   :align: center
   :alt: Unstructured grid consisting of three tetrahedra

   *Example Tetrahedral Grid*

The element type is :sidskey:`TETRA_4`, and the connectivity is defined in :sidskey:`ElementConnectivity` by specifying the four nodes comprising each element, with the order consistent with the :ref:`numbering conventions for tetrahedral elements <unst_tetra>`. The data in :sidskey:`ElementConnectivity` is grouped by element; note that the parentheses are added here for presentation purposes only.

.. code-block:: sids

  Zone_t UnstructuredZone =
    {{
    Elements_t TetraElements =
      {{
      IndexRange_t ElementRange = [1,3] ;

      ElementType_t ElementType = TETRA_4 ;

      DataArray_t<int, 1, NPE[TETRA_4] × 3> ElementConnectivity =
        {{
        Data(int, 1, NPE[TETRA_4] × 3) =
          (1, 2, 3, 4), (2, 5, 3, 6), (2, 6, 3, 4) ;
        }} ;
      }} ;
    }} ;

Example - NGON_n and NFACE_n Element Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses the same grid as in the previous example, but treats the elements as general polyhedra to illustrate the use of the :sidskey:`NGON_n` and :sidskey:`NFACE_n` element types. The grid consists of three volume elements, each made up of four face elements, with each face defined by three nodes.

For each face, the nodes comprising that face are listed in :sidskey:`ElementConnectivity` for the :sidskey:`NGON_n` element type.
The :sidskey:`ElementRange` is ``[1,10]``, corresponding to the 10 total faces in the grid. The :sidskey:`ElementDataSize` is 30, corresponding to the total of 30 nodes defining the 10 faces.

The faces making up the three volume elements are then listed in :sidskey:`ElementConnectivity` for the :sidskey:`NFACE_n` element type. The :sidskey:`ElementRange` is ``[11,13]``, corresponding to the three volume elements. The :sidskey:`ElementDataSize` is 12, corresponding to three volume elements with four faces per element. Note that the face numbers for faces 3 and 8 are negative in the definition of volume element 3, since their normals point inward for that element. Again, the parentheses in :sidskey:`ElementConnectivity` are for presentation purposes only.

.. code-block:: sids

  Zone_t UnstructuredZone =
    {{
    Elements_t NgonElements =
      {{
      IndexRange_t ElementRange = [1,10] ;

      ElementType_t ElementType = NGON_n ;

      DataArray_t<int, 1, 30> ElementConnectivity =
        {{
        Data(int, 1, 30) =
          (1, 3, 2), (1, 2, 4), (2, 3, 4), (3, 1, 4),
          (2, 3, 5), (2, 5, 6), (5, 3, 6), (3, 2, 6),
          (2, 6, 4), (6, 3, 4) ;
        }} ;
      DataArray_t<int, 1, 11> ElementStartOffset =
        {{
        Data(int, 1, 11) =
           0,  3,  6,  9,
          12, 15, 18, 21,
          24, 27, 30 ;
        }} ;
      }} ;
    Elements_t NfaceElements =
      {{
      IndexRange_t ElementRange = [11,13] ;

      ElementType_t ElementType = NFACE_n ;

      DataArray_t<int, 1, 12> ElementConnectivity =
        {{
        Data(int, 1, 12) =
          ( 1,  2,  3,  4),
          ( 5,  6,  7,  8),
          (-8,  9, 10, -3) ;
        }} ;
      DataArray_t<int, 1, 4> ElementStartOffset =
        {{
        Data(int, 1, 4) =
           0,  4,  8,  12 ;
        }} ;
      }} ;
    }} ;

Example - Separate Element Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, elements are defined for an unstructured zone with 15 tetrahedral and 10 hexahedral elements. The elements are written in two separate sections, one for the tetrahedral elements and one for the hexahedral elements.

.. code-block:: sids

  Zone_t UnstructuredZone =
    {{
    Elements_t TetraElements =
      {{
      IndexRange_t ElementRange = [1,15] ;

      int ElementSizeBoundary = 10 ;

      ElementType_t ElementType = TETRA_4 ;

      DataArray_t<int, 1, NPE[TETRA_4] × 15> ElementConnectivity =
        {{
        Data(int, 1, NPE[TETRA_4] × 15) = (node(i,j), i=1,NPE[TETRA_4], j=1,15) ;
        }} ;
      }} ;
    Elements_t HexaElements =
      {{
      IndexRange_t ElementRange = [16,25] ;

      int ElementSizeBoundary = 0 ;

      ElementType_t ElementType = HEXA_8 ;

      DataArray_t<int, 1, NPE[HEXA_8] × 10> ElementConnectivity =
        {{
        Data(int, 1, NPE[HEXA_8] × 10) = (node(i,j), i=1,NPE[HEXA_8], j=1,10) ;
        }} ;
      }} ;
    }} ;

Example - MIXED Element Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, the same unstructured zone described in the previous example is written in a single element section of type :sidskey:`MIXED` (i.e., an unstructured grid composed of mixed elements).

.. code-block:: sids

  Zone_t UnstructuredZone =
    {{
    Elements_t MixedElementsSection =
      {{
      IndexRange_t ElementRange = [1,25] ;

      ElementType_t ElementType = MIXED ;

      DataArray_t<int, 1, ElementDataSize> ElementConnectivity =
        {{
        Data(int, 1, ElementDataSize) = (etype(j),(node(i,j),
             i=1,NPE[etype(j)]), j=1,25) ;
        }} ;
      }} ;
      DataArray_t<int, 1, 26> ElementStartOffset =
        {{
        Data(int, 1, 26) =
           0, (NPE[etype(j)]+ElementStartOffset[j]+1, j=1,25) ;
        }} ;
    }} ;


Axisymmetry Structure Definition: ``Axisymmetry_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 The :sidskey:`Axisymmetry_t` data structure allows recording the axis of rotation and the angle of rotation around this axis for a two-dimensional dataset that represents an axisymmetric database.

.. code-block:: sids

  Axisymmetry_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    DataArray_t<real,1,2> AxisymmetryReferencePoint ;                  (r)
    DataArray_t<real,1,2> AxisymmetryAxisVector ;                      (r)
    DataArray_t<real,1,1> AxisymmetryAngle ;                           (o)
    DataArray_t<char,2,[32,2]> CoordinateNames ;                       (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of Axisymmetry_t and shall not include the names AxisymmetryAngle, AxisymmetryAxisVector, AxisymmetryReferencePoint, CoordinateNames, DataClass, or DimensionalUnits.
    2. :sidskey:`AxisymmetryReferencePoint` and :sidskey:`AxisymmetryAxisVector` are the required fields within the :sidskey:`Axisymmetry_t` structure.

:sidskey:`AxisymmetryReferencePoint` specifies the origin used for defining the axis of rotation.

:sidskey:`AxisymmetryAxisVector` contains the direction cosines of the axis of rotation, through the :sidskey:`AxisymmetryReferencePoint`. For example, for a 2-D dataset defined in the :math:`(x,y)` plane, if :sidskey:`AxisymmetryReferencePoint` contains :math:`(0,0)` and :sidskey:`AxisymmetryAxisVector` contains :math:`(1,0)`, the x-axis is the axis of rotation.

:sidskey:`AxisymmetryAngle` allows specification of the circumferential extent about the axis of rotation. If this angle is undefined, it is assumed to be 360°.

:sidskey:`CoordinateNames` may be used to specify the first and second coordinates used in the definition of :sidskey:`AxisymmetryReferencePoint` and :sidskey:`AxisymmetryAxisVector`. If not found, it is assumed that the first coordinate is :sidskey:`CoordinateX` and the second is :sidskey:`CoordinateY`. The coordinates given under :sidskey:`CoordinateNames`, or implied by using the default, must correspond to those found under :sidsref:`GridCoordinates_t`.

:sidsref:`DataClass` defines the default class for numerical data contained in the :sidsref:`DataArray_t` entities. For dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Rotating Coordinates Structure Definition: ``RotatingCoordinates_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 The :sidskey:`RotatingCoordinates_t` data structure is used to record the rotation center and rotation rate vector of a rotating coordinate system.

.. code-block:: sids

  RotatingCoordinates_t :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    DataArray_t<real,1,PhysicalDimension> RotationCenter ;             (r)
    DataArray_t<real,1,PhysicalDimension> RotationRateVector ;         (r)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`RotatingCoordinates_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`RotationCenter`, or :sidskey:`RotationRateVector`.
    2. :sidskey:`RotationCenter` and :sidskey:`RotationRateVector` are the required fields within the :sidskey:`RotatingCoordinates_t` structure.

:sidskey:`RotationCenter` specifies the coordinates of the center of rotation, and :sidskey:`RotationRateVector` specifies the components of the angular velocity of the grid about the center of rotation. Together, they define the angular velocity vector. The direction of the angular velocity vector specifies the axis of rotation, and its magnitude specifies the rate of rotation.

For example, for the common situation of rotation about the x-axis, :sidskey:`RotationCenter` would be specified as any point on the x-axis, like :math:`(0,0,0)`. :sidskey:`RotationRateVector` would then be specified as :math:`(ω,0,0)`, where ω is the rotation rate. Using the right-hand rule, ω would be positive for clockwise rotation (looking in the +x direction), and negative for counter-clockwise rotation.

Note that for a rotating coordinate system, the axis of rotation is defined in the inertial frame of reference, while the grid coordinates stored using the :sidsref:`GridCoordinates_t` data structure are relative to the rotating frame of reference.

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

If rotating coordinates are used, it is useful to store variables relative to the rotating frame. Standardized data-name identifiers should be used for these variables, as defined for flow-solution quantities in the section :ref:`Conventions for Data-Name Identifiers <dataname>`.

Flow Solution Structure Definition: :sidskey:`FlowSolution_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 The flow solution within a given zone is described by the :sidskey:`FlowSolution_t` structure. This structure contains a list for the data arrays of the individual flow-solution variables, as well as identifying the grid location of the solution. It also provides a mechanism for identifying rind-point data included within the data arrays.

.. code-block:: sids

  FlowSolution_t< int CellDimension, int IndexDimension,
                  int VertexSize[IndexDimension],
                  int CellSize[IndexDimension] > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridLocation_t GridLocation ;                                      (o/d)

    Rind_t<IndexDimension> Rind ;                                      (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (o)
    IndexArray_t<IndexDimension, ListLength[], int> PointList ;        (o)

    List( DataArray_t<DataType, IndexDimension, DataSize[]>
            DataArray1 ... DataArrayN ) ;                              (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`FlowSolution_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`GridLocation`, :sidskey:`PointList`, :sidskey:`PointRange`, or :sidskey:`Rind`.
    2. There are no required fields for :sidskey:`FlowSolution_t`. :sidsref:`GridLocation` has a default of :sidskey:`Vertex` if absent. :sidskey:`Rind` also has a default if absent; the default is equivalent to having an instance of :sidskey:`Rind` whose :sidskey:`RindPlanes` array contains all zeros.
    3. Both of the fields :sidskey:`PointList` and :sidskey:`PointRange` are optional. Only one of these two fields may be specified.
    4. The structure parameter :sidskey:`DataType` must be consistent with the data stored in the :sidsref:`DataArray_t` structure entities; :sidskey:`DataType` is :code:`real` for all flow-solution identifiers defined in the section :ref:`Conventions for Data-Name Identifiers<dataname>`.
    5. For unstructured zones :sidsref:`GridLocation` options are limited to :sidskey:`Vertex` or :sidskey:`CellCenter`, unless one of :sidskey:`PointList` or :sidskey:`PointRange` is present.
    6. Indexing of data within the :sidsref:`DataArray_t` structure must ne consistent with the associated numbering of vertices or elements.

:sidskey:`FlowSolution_t` requires four structure parameters; :sidskey:`CellDimension` identifies the dimensionality of cells or elements, :sidskey:`IndexDimension` identifies the dimensionality of the grid-size arrays, and :sidskey:`VertexSize` and :sidskey:`CellSize` are the number of core vertices and cells, respectively, in each index direction, excluding rind points. For structured zones, core vertices and cells begin at :code:`[1,1,1]` (in 3-D) and end at :sidskey:`VertexSize` and :sidskey:`CellSize`, respectively. For unstructured zones, :sidskey:`IndexDimension` is always 1.

The flow solution data is stored in the list of :sidsref:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity may contain a single component of the solution vector. Standardized data-name identifiers for the flow-solution quantities are described in the section :ref:`Conventions for Data-Name Identifiers<dataname>`. The field :sidsref:`GridLocation` specifies the location of the solution data with respect to the grid; if absent, the data is assumed to coincide with grid vertices (i.e., :sidskey:`GridLocation = Vertex`). All data within a given instance of :sidskey:`FlowSolution_t` must reside at the same grid location.

For structured grids, the value of :sidskey:`GridLocation` alone specifies the location and indexing of the flow solution data. Vertices are explicity indexed. Cell centers and face centers are indexed using the minimum of the connecting vertex indices, as described in the section :ref:`Structured Grid Notation and Indexing Conventions <structgrid>`.

For unstructured grids, the value of :sidskey:`GridLocation` alone specifies location and indexing of flow solution data only for vertex and cell-centered data. The reason for this is that element-based grid connectivity provided in the :sidsref:`Elements_t` data structures explicitly indexes only vertices and cells. For data stored at alternate grid locations (e.g., edges), additional connectivity information is needed. This is provided by the optional fields :sidskey:`PointRange` and :sidskey:`PointList`; these refer to vertices, edges, faces or cell centers, depending on the values of :sidskey:`CellDimension` and :sidskey:`GridLocation`. The following table shows these relations. The :sidskey:`NODE` element type should not be used in place of the vertex. A vertex :sidskey:`GridLocation` should use the :sidskey:`GridLocation = Vertex` pattern, which implies an indexing on the grid coordinates arrays and not a :sidskey:`NODE Elements_t` array.

.. table::
  :align: center
  :widths: 20 12 16 17 35

  +---------------+----------------------------------------------------------------+
  |               |                        GridLocation                            |
  | CellDimension +----------+-------------+-------------+-------------------------+
  |               | Vertex   | EdgeCenter  | \*FaceCenter|        CellCenter       |
  +===============+==========+=============+=============+=========================+
  |       1       | vertices |      \-     |      \-     | cells (line elements)   |
  +---------------+----------+-------------+-------------+-------------------------+
  |       2       | vertices |    edges    |      \-     | cells (area elements)   |
  +---------------+----------+-------------+-------------+-------------------------+
  |       3       | vertices |    edges    |    faces    | cells (volume elements) |
  +---------------+----------+-------------+-------------+-------------------------+

.. note::
  In the table, **\*FaceCenter** stands for the possible types: :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter`, :sidskey:`KFaceCenter`, or :sidskey:`FaceCenter`.


Although intended for edge or face-based solution data for unstructured grids, the fields :sidskey:`PointRange/List` may also be used to (redundantly) index vertex and cell-centered data. In all cases, indexing of flow solution data corresponds to the element numbering as defined in the :sidsref:`Elements_t` data structures.

:sidsref:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points or elements (for unstructured grids) included in the data. Its purpose and function are identical to those described for the :sidsref:`GridCoordinates_t` structure. Note, however, that the :sidskey:`Rind` in this structure is independent of the :sidskey:`Rind` contained in :sidskey:`GridCoordinates_t`. They are not required to contain the same number of rind planes or elements. Also, the location of any flow-solution rind points is assumed to be consistent with the location of the core flow solution points (e.g., if :sidskey:`GridLocation = CellCenter`, rind points are assumed to be located at fictitious cell centers).

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional flow solution data, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. c:function:: FUNCTION ListLength()

   :return value: ``int``
   :dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`FlowSolution_t` requires the structure function :sidskey:`ListLength`, which is used to specify the number of entities (e.g. vertices) corresponding to a given :sidskey:`PointRange` or :sidskey:`PointList`. If :sidskey:`PointRange` is specified, then :sidskey:`ListLength` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`. If :sidskey:`PointList` is specified, then :sidskey:`ListLength` is the number of indices in the list of points. In this situation, :sidskey:`ListLength` becomes a user input along with the indices of the list :sidskey:`PointList`. By user we mean the application code that is generating the CGNS database.

.. c:function:: FUNCTION DataSize()

   :return value: one-dimensional ``int`` array of length :sidskey:`IndexDimension`
   :dependencies: :sidskey:`IndexDimension`, :sidskey:`VertexSize[]`, :sidskey:`CellSize[]`, :sidskey:`GridLocation`, :sidskey:`Rind`, :sidskey:`ListLength[]`

   The function :sidskey:`DataSize[]` is the size of flow solution data arrays. If :sidskey:`Rind` is absent then :sidskey:`DataSize` represents only the core points; it will be the same as :sidskey:`VertexSize` or :sidskey:`CellSize` depending on :sidskey:`GridLocation`. The definition of the function :sidskey:`DataSize[]` is as follows:

   .. code-block:: sids

     if (PointRange/PointList is present) then
       {
       DataSize[] = ListLength[] ;
       }
     else if (Rind is absent) then
       {
       if (GridLocation = Vertex) or (GridLocation is absent)
         {
         DataSize[] = VertexSize[] ;
         }
       else if (GridLocation = CellCenter) then
         {
         DataSize[] = CellSize[] ;
         }
       }
     else if (Rind is present) then
       {
       if (GridLocation = Vertex) or (GridLocation is absent) then
         {
         DataSize[] = VertexSize[] + [a + b,...] ;
         }
       else if (GridLocation = CellCenter)
         {
         DataSize[] = CellSize[] + [a + b,...] ;
         }
       }

   where :code:`RindPlanes = [a,b,...]` (see the :sidsref:`Rind_t` structure for the definition of :sidskey:`RindPlanes`).

Flow Solution Example
^^^^^^^^^^^^^^^^^^^^^

 This section contains an example of the flow solution entity, including the designation of grid location and rind planes and data-normalization mechanisms.

Example - Flow Solution
~~~~~~~~~~~~~~~~~~~~~~~

Conservation-equation variables (:math:`\rho, \rho U, \rho V \text{ and } \rho e_0`) for a 2-D grid of size :math:`11 \times 5`. The flowfield is cell-centered with two planes of rind data. The density, momentum and stagnation energy (:math:`\rho e_0`) data is nondimensionalized with respect to a freestream reference state whose quantities are dimensional. The freestream density and pressure are used for normalization; these values are :math:`1.226\,kg/m^3` and :math:`1.0132 \times 10^5\,N/m^2` (standard atmosphere conditions). The data-name identifier conventions for the conservation-equation variables are :sidskey:`Density`, :sidskey:`MomentumX`, :sidskey:`MomentumY` and :sidskey:`EnergyStagnationDensity`.

.. code-block:: sids

  !  CellDimension = 2
  !  IndexDimension = 2
  !  VertexSize = [11,5]
  !  CellSize = [10,4]
  FlowSolution_t<2, [11,5], [10,4]> FlowExample =
    {{
    GridLocation_t GridLocation = CellCenter ;

    Rind_t<2> Rind =
      {{
      int[4] RindPlanes = [2,2,2,2] ;
      }} ;

    DataClass_t DataClass = NormalizedByDimensional ;

    DimensionalUnits_t DimensionalUnits =
      {{
      MassUnits        = Kilogram ;
      LengthUnits      = Meter ;
      TimeUnits        = Second ;
      TemperatureUnits = TemperatureUnitsNull ;
      AngleUnits       = AngleUnitsNull ;
      }} ;

    !  DataType = real
    !  Dimension = 2
    !  DataSize = CellSize + [4,4] = [14,8]
    DataArray_t<real, 2, [14,8]> Density =
      {{
      Data(real, 2, [14,8]) = ((rho(i,j), i=-1,12), j=-1,6) ;

      DataConversion_t DataConversion =
        {{
        ConversionScale  = 1.226 ;
        ConversionOffset = 0 ;
        }} ;

      DimensionalExponents_t DimensionalExponents =
        {{
        MassExponent        = +1 ;
        LengthExponent      = -3 ;
        TimeExponent        =  0 ;
        TemperatureExponent =  0 ;
        AngleExponent       =  0 ;
        }} ;
      }} ;

    DataArray_t<real, 2, [14,8]> MomentumX =
      {{
      Data(real, 2, [14,8]) = ((rho_u(i,j), i=-1,12), j=-1,6) ;

      DataConversion_t DataConversion =
        {{
        ConversionScale  = 352.446 ;
        ConversionOffset = 0 ;
        }} ;
      }} ;

    DataArray_t<real, 2, [14,8]> MomentumY =
      {{
      Data(real, 2, [14,8]) = ((rho_v(i,j), i=-1,12), j=-1,6) ;

      DataConversion_t DataConversion =
        {{
        ConversionScale  = 352.446 ;
        ConversionOffset = 0 ;
        }} ;
      }} ;

    DataArray_t<real, 2, [14,8]> EnergyStagnationDensity =
      {{
      Data(real, 2, [14,8]) = ((rho_e0(i,j), i=-1,12), j=-1,6) ;

      DataConversion_t DataConversion =
        {{
        ConversionScale  = 1.0132e+05 ;
        ConversionOffset = 0 ;
        }} ;
      }} ;
    }} ;

The value of :sidskey:`GridLocation` indicates the data is at cell centers, and the value of :sidskey:`RindPlanes` specifies two rind planes on each face of the zone. The resulting value of the structure function :sidskey:`DataSize` is the number of cells plus four in each coordinate direction; this value is passed to each of the :sidskey:`DataArray_t` entities.

Since the data are all nondimensional and normalized by dimensional reference quantities, this information is stated in :sidskey:`DataClass` and :sidskey:`DimensionalUnits` at the :sidskey:`FlowSolution_t` level rather than attaching the appropriate :sidskey:`DataClass` and :sidskey:`DimensionalUnits` to each :sidskey:`DataArray_t` entity. It could possibly be at even higher levels in the hierarchy. The contents of :sidskey:`DataConversion` are in each case the denominator of the normalization; this is :math:`\rho_\infty` for density, :math:`(p_\infty \rho_\infty)^{1/2}` for momentum, and :math:`p_\infty` for stagnation energy. The dimensional exponents are specified for density. For all the other data, the dimensional exponents are to be inferred from the data-name identifiers.

Note that no information is provided to identify the actual reference state or indicate that it is freestream. This information is not needed for data manipulations involving renormalization or changing the units of the converted raw data.


Zone Subregion Structure Definition: ``ZoneSubRegion_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidsref:`ZoneSubRegion_t` node allows for the ability to give flowfield or other information over a subset of the entire zone in a CGNS file. This subset may be over a portion of a boundary,
or it may be over a portion of the entire field.

.. code-block:: sids

  ZoneSubRegion_t< int IndexDimension, int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                         (o)

    int RegionCellDimension ;                                                  (o/d)

    GridLocation_t GridLocation ;                                              (o/d)

    IndexRange_t<IndexDimension> PointRange ;                                  (r:o:o:o)
    IndexArray_t<IndexDimension, ListLength, int> PointList ;                  (o:r:o:o)
    Descriptor_t BCRegionName ;                                                (o:o:r:o)
    Descriptor_t GridConnectivityRegionName ;                                  (o:o:o:r)

    Rind_t<IndexDimension> Rind;                                               (o/d)

    List( DataArray_t<DataType, 1, ListLength[]> DataArray1 ... DataArrayN ) ; (o)

    FamilyName_t FamilyName ;                                                  (o)

    List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ;         (o)

    DataClass_t DataClass ;                                                    (o)

    DimensionalUnits_t DimensionalUnits ;                                      (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;          (o)
    } ;

.. note::
    1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown;
       users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ZoneSubRegion_t` and shall not include the names :sidskey:`RegionCellDimension`, :sidskey:`Rind`, :sidskey:`PointRange`, :sidskey:`PointList`, :sidskey:`BCRegionName`, :sidskey:`GridConnectivityRegionName`, :sidskey:`FamilyName`, :sidskey:`DataClass` or :sidskey:`DimensionalUnits`.
    2. :sidskey:`RegionCellDimension` must be equal to or less than the cell dimension for the zone. If absent, then its default value is :sidskey:`CellDimension`.
    3. :sidskey:`GridLocation` has a default value of :sidskey:`Vertex` if absent. Permissible values of :sidskey:`GridLocation` are determined by :sidskey:`RegionCellDimension` (see below). All data within a given instance of :sidskey:`ZoneSubRegion_t` must reside at the same grid location.
    4. The extent of the region and distribution of its data is specified by one of :sidskey:`PointRange`, :sidskey:`PointList`, :sidskey:`BCRegionName`, or :sidskey:`GridConnectivityRegionName`. One and only one of these must be specified.

The extent of the subregion and the distribution of data within that subregion is determined by :sidskey:`RegionCellDimension`, :sidskey:`GridLocation`, and one of :sidskey:`PointRange/List`, :sidskey:`BCRegionName` or :sidskey:`GridConnectivityRegionName`. For a 3-D subregion (:sidskey:`RegionCellDimension` = 3), data can be located at vertices, edges, face centers or cell centers. For a 2-D subregion (:sidskey:`RegionCellDimension` = 2), data can be located at vertices, edges or cell centers (i.e. area elements). It is anticipated that one of the widest uses for :sidskey:`ZoneSubRegion_t` will be to store specific boundary-only information. For example, in a 3-D simulation, one may wish to store additional data on surfaces. In this case, the :sidskey:`RegionCellDimension` would be set to 2.

:sidskey:`PointRange/List` refer to vertices, edges, faces or cell centers, depending on the values of :sidskey:`RegionCellDimension` and :sidskey:`GridLocation`. Note that it is both the dimensionality of the zone (:sidskey:`CellDimension`) as well as the dimensionality of the subregion (:sidskey:`RegionCellDimension`), that determines the types of elements permissible in :sidskey:`PointRange/List`. The following table shows these relations.

.. table::
  :width: 300px
  :align: center

  +---------------+---------------------+---------------------------------------------------------------+
  |               |                     |                        GridLocation                           |
  | CellDimension | RegionCellDimension +----------+------------+-------------+-------------------------+
  |               |                     |  Vertex  | EdgeCenter |\*FaceCenter |       CellCenter        |
  +===============+=====================+==========+============+=============+=========================+
  |       1       |          1          | vertices |     \-     |      \-     | cells (line elements)   |
  +---------------+---------------------+----------+------------+-------------+-------------------------+
  |       2       |          1          | vertices |    edges   |      \-     |           \-            |
  +---------------+---------------------+----------+------------+-------------+-------------------------+
  |       2       |          2          | vertices |    edges   |      \-     | cells (area elements)   |
  +---------------+---------------------+----------+------------+-------------+-------------------------+
  |       3       |          1          | vertices |    edges   |      \-     |           \-            |
  +---------------+---------------------+----------+------------+-------------+-------------------------+
  |       3       |          2          | vertices |    edges   |    faces    |           \-            |
  +---------------+---------------------+----------+------------+-------------+-------------------------+
  |       3       |          3          | vertices |    edges   |    faces    | cells (volume elements) |
  +---------------+---------------------+----------+------------+-------------+-------------------------+

.. note::
  In the table, **\*FaceCenter** stands for the possible types: :sidskey:`IFaceCenter`, :sidskey:`JFaceCenter`, :sidskey:`KFaceCenter`, or :sidskey:`FaceCenter`.

For both structured and unstructured grids, :sidskey:`GridLocation = Vertex` means that :sidskey:`PointRange/List` refers to vertex indices. For structured grids, edges, faces and cell centers are indexed using the minimum of the connecting vertex indices, as described in the section :ref:`Structured Grid Notation and Indexing Conventions <structgrid>`. For unstructured grids, edges, faces and cell centers are indexed using their element numbering, as defined in the :sidsref:`Elements_t` data structures.

If the vertices or elements of the subregion are continuously numbered, then :sidskey:`PointRange` may be used. Otherwise, :sidskey:`PointList` should be used to list the vertices/elements. Alternatively, if the data locations and range of the subregion coincide with an existing BC region or zone-to-zone GridConnectivity region, then :sidskey:`BCRegionName` or :sidskey:`GridConnectivityRegionName` may be used. :sidskey:`BCRegionName` is a string giving the name of an existing :sidsref:`BC_t` node of the current zone. :sidskey:`GridConnectivityRegionName` is a string giving the name of an existing :sidsref:`GridConnectivity1to1_t` or :sidsref:`GridConnectivity_t` node of the current zone. The name referred to should be unambiguous.

Consistent with :sidsref:`FlowSolution_t`, the subregion's solution data is stored in the list of :sidsref:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity contains a single quantity. Standardized data-name identifiers for solution quantities are described in the section :ref:`Conventions for Data-Name Identifiers`. As noted above, all solution data within a given subregion must reside at the same grid location.

:sidsref:`DataClass` defines the default class for data contained in the :sidskey:`DataArray_t` entities. For dimensional flow solution data, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules <precedence>`.

:sidskey:`ZoneSubRegion_t` requires the structure function :sidsref:`ListLength[]`, which is used to specify the number of data points (e.g. vertices, cell centers, face centers, edge centers) corresponding to the given :sidskey:`PointRange/List`. If :sidskey:`PointRange` is specified, then :sidskey:`ListLength` is obtained from the number of points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`. If :sidskey:`PointList` is specified, then :sidskey:`ListLength` is the number of indices in the list of points. In this situation, :sidskey:`ListLength` becomes a user input along with the indices of the list :sidskey:`PointList`. By *user* we mean the application code that is generating the CGNS database.

:sidsref:`Rind` is an optional field that indicates the number of rind planes (for structured grids) or rind points (for unstructured grids). If :sidskey:`Rind` is absent, then the :sidskey:`DataArray_t` structure entities contain only core data of length :sidskey:`ListLength`, as defined for this region. If :sidskey:`Rind` is present, it will provide information on the number of rind elements, in addition to the :sidskey:`ListLength`, that are contained in the :sidskey:`DataArray_t` structures. The bottom line is that :sidskey:`Rind` simply adds a specified number to :sidskey:`ListLength`, as used by the :sidskey:`DataArray_t` structures.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored.

There may be multiple instances of :sidskey:`ZoneSubRegion_t` in a given zone. These may simply be multiple regions defined for a single solution, or they may be associated with different times / different solutions in a time-dependent simulation (in which case :sidsref:`ZoneIterativeData_t` should be used to associate them).

All :sidskey:`FamilyName` and :sidskey:`AdditionalFamilyName` entries should respect the rules defined in :ref:`Base Level Families <BaseLevelFamilies>` and :sidsref:`Zone_t`.


Zone Subregion Examples
^^^^^^^^^^^^^^^^^^^^^^^

This section contains four examples of Zone Subregions, including the use of :sidskey:`PointList`, :sidskey:`PointRange` and :sidskey:`BCRegionName`.

Example - Volume Subregion for a Structured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For this example, it is assumed that a 1-zone 3-D structured grid exists of size (\ :math:`197\times97\times33`). Inside of this zone, the user wishes to output a special subset region of interior data (say, temperature and kinematic viscosity) at the specific cell-center locations :math:`i = 121-149`, :math:`j = 17-45`, :math:`k = 21-23`. Even though this same data may possibly exist under :sidskey:`FlowSolution_t` (which holds the flowfield data for the entire zone), this particular location may represent a special region of interest where the user wants to focus attention or output different types of flowfield variables or user-defined data. Note that for structured grids, the location list always references grid nodes; in this case with :sidskey:`GridLocation = Cellcenter` the cell centers are indexed by the minimum :math:`i`, :math:`j`, and :math:`k` indices of the connecting vertices.

Under :sidskey:`Zone_t`:

.. code-block:: sids

     ZoneSubRegion_t<3,3> Region1 =
       {{
       GridLocation_t GridLocation = CellCenter ;
       int RegionCellDimension = 3;
       IndexRange_t<3> PointRange =
         {{
         int[3] Begin = [121,17,21];
         int[3] End = [149,45,21];
         }};

       ! ListLength = (149-121+1)*(45-17+1)*(23-21+1) = 29*29*3 = 2523
       DataArray_t<real,1,2523> Temperature =
         {{
         Data(real,1,2523) = temperature at the cell centers specified
         }} ;
       DataArray_t<real,1,2523> ViscosityKinematic =
         {{
         Data(real,1,2523) = kinematic viscosity at the cell centers specified
         }} ;
       }} ; ! end Region1

Example - Volume Subregion for an Unstructured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example is like the previous one, except it is for an unstructured zone. Inside of this zone, the user wishes to output a special subset region of data (say, temperature and kinematic viscosity) at a specific list of 2523 element cell-center locations, located somewhere within the (larger) field of elements. Recall that when :sidskey:`GridLocation` is anything other than :sidskey:`Vertex` in conjunction with unstructured grids, then the location list represents element numbers and not grid node numbers.

Under :sidskey:`Zone_t`:

.. code-block:: sids

     ZoneSubRegion_t<1,3> Region1 =
       {{
       GridLocation_t GridLocation = CellCenter ;
       int RegionCellDimension = 3;
       IndexArray_t<1,2523,int> PointList =
         {{
         int[1] ElementList = list of 3-D element numbers where region data given
         }} ;

       ! ListLength = length of the element list = 2523
       DataArray_t<real,1,2523> Temperature =
         {{
         Data(real,1,2523) = temperature at the element cell centers specified
         }} ;
       DataArray_t<real,1,2523> ViscosityKinematic =
         {{
         Data(real,1,2523) = kinematic viscosity at the element cell centers specified
         }} ;
       }} ; ! end Region1

Example - Surface Subregion for an Unstructured Grid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, boundary data is output on a 2-D surface subregion of a 3-D problem. Because this is data on a topologically 2-D boundary (in a 3-D simulation), :sidskey:`RegionCellDimension` is set to 2. :sidskey:`GridLocation` is specified as :sidskey:`FaceCenter`. Recall that when :sidskey:`GridLocation` is anything other than :sidskey:`Vertex` in conjunction with unstructured grids, then the location list represents element numbers and not grid node numbers. Thus, the :sidskey:`PointList/Range` indicates particular surface elements (or boundary elements) that need to have been defined in the file under their own :sidskey:`Elements_t` node(s), separate from the 3-D volume elements that make up the grid. In this case, we assume that the surface element numbers at which we are outputting data are 5568 through 5592 inclusive. Because the numbers occur in sequential order, we can make use of :sidskey:`PointRange`.

Under :sidskey:`Zone_t`:

.. code-block:: sids

     ZoneSubRegion_t<1,3> Region1 =
       {{
       GridLocation_t GridLocation = FaceCenter ;
       int RegionCellDimension = 2;
       IndexArray_t<1,25,int> PointRange =
         {{
         int[1] Begin = [5568];
         int[1] End = [5592];
         }} ;

       ! ListLength = length of the element list = 25
       DataArray_t<real,1,25> Temperature =
         {{
         Data(real,1,25) = temperature at the specific face element locations specified
         }} ;
       DataArray_t<real,1,25> ViscosityKinematic =
         {{
         Data(real,1,25) = kinematic viscosity at the specific face element locations specified
         }} ;
       }} ; ! end Region1

Example - Surface Subregion Utilizing BC Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, boundary data is output at the same locations where the BCs are specified in a particular :sidskey:`BC_t` node (in this case the :sidskey:`ListLength` is 25). Note that because this is data on a topologically 2-D boundary (in a 3-D simulation), :sidskey:`RegionCellDimension` is set to 2. :sidskey:`GridLocation` is not specified, because it is inherited from the :sidskey:`BC_t` node along with the :sidskey:`ListLength`.

Under :sidskey:`Zone_t`:

.. code-block:: sids

     ZoneSubRegion_t<1,3> Region1 =
       {{
       int RegionCellDimension = 2;
       Descriptor_t BCRegionName = "name of a ZoneBC/BC_t node" ;

       ! ListLength = length of the point/element list from BC_t = 25
       DataArray_t<real,1,25> Temperature =
         {{
         Data(real,1,25) = temperature at the specific BC locations specified
         }} ;
       DataArray_t<real,1,25> ViscosityKinematic =
         {{
         Data(real,1,25) = kinematic viscosity at the specific BC locations specified
         }} ;
       }} ; ! end Region1


.. last line
