.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _SIDS-connectivity:

Multizone Interface Connectivity
================================

This section defines structures for describing multizone interface connectivity for :ref:`1-to-1 abutting, mismatched abutting, and overset type interfaces <interfaces>`.
All interface connectivity information pertaining to a given zone is grouped together in a :sidsref:`ZoneGridConnectivity_t` structure entity; this in turn is contained in a :ref:`zone structure entity <Zone_t>`.

Before presentation of the structure definitions, a few design features require comment.
All indices used to describe interfaces are the dimensionality (:sidskey:`IndexDimension`) of the grid, even when they are used to describe lower-dimensional zonal boundaries for abutting interfaces. The alternative for structured zones that was not chosen is to use lower-dimensional indices for lower-dimensional interfaces (e.g., for a 3-D grid, use two-dimensional indices for describing grid planes that are interfaces). Both alternatives offer trade-offs. The lower-dimensional indices require cyclic notation conventions and additional identification of face location; whereas, full-dimensional indices result in one redundant index component when describing points along a grid plane. We decided that full-dimensional indices would be more usable and less error prone in actual implementation.

A major consequence of this decision is that connectivity information for describing mismatched abutting interfaces and overset interfaces can be merged into a single structure, :sidsref:`GridConnectivity_t`.
In fact, this single structure type can be used to describe all zonal interfaces.

A second design choice was to duplicate all 1-to-1 abutting interface information within the CGNS database. It is possible to describe a given 1-to-1 interface with a single set of connectivity data. In contrast, mismatched and overset interfaces require different connectivity information when the roles of receiver and donor zones are interchanged. Therefore, a given mismatched or overset interface requires two sets of connectivity data within the database. The decision to force two sets of connectivity data (one contained in each of the :sidskey:`Zone_t` entities for the two adjacent zones)for each 1-to-1 interface makes the connectivity structures for all interface types look and function similarly. It also fits better with the zone-by-zone hierarchy chosen for the CGNS database. The minor penalty in data duplication was deemed worth the advantages gained.

.. note::

  It is a CGNS design intent that a given zone boundary segment or location should at most be defined (or covered) by either a boundary condition or a multizone interface connectivity, but not by both.


Zonal Connectivity Structure Definition: ``ZoneGridConnectivity_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All multizone interface grid connectivity information pertaining to a given zone is contained in the :sidskey:`ZoneGridConnectivity_t` structure.
This includes abutting interfaces (1-to-1 and general mismatched), overset-grid interfaces, and overset-grid holes.

.. code-block:: sids

  ZoneGridConnectivity_t< int IndexDimension, int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( GridConnectivity1to1_t<IndexDimension>
          GridConnectivity1to11 ... GridConnectivity1to1N ) ;          (o)

    List( GridConnectivity_t<IndexDimension, CellDimension>
          GridConnectivity1 ... GridConnectivityN ) ;                  (o)

    List( OversetHoles_t<IndexDimension> 
          OversetHoles1 ... OversetHolesN ) ;                          (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

   Default names for the :sidsref:`Descriptor_t`, :sidsref:`GridConnectivity1to1_t`, :sidsref:`GridConnectivity_t`, :sidsref:`OversetHoles_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of ZoneGridConnectivity_t.

   All lists within the :sidskey:`ZoneGridConnectivity_t` structure may be empty. 

:sidskey:`ZoneGridConnectivity_t` requires two structure parameters, :sidskey:`IndexDimension`, which is passed onto all connectivity substructures, and :sidskey:`CellDimension`, which is passed to :sidsref:`GridConnectivity_t` only.

Connectivity information for 1-to-1 or matched multizone interfaces is contained in the :sidsref:`GridConnectivity1to1_t` structure.
Abutting and overset connectivity is contained in the :sidsref:`GridConnectivity_t` structure, and overset-grid holes are identified in the :sidsref:`OversetHoles_t` structure.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 


1-to-1 Interface Connectivity Structure Definition: ``GridConnectivity1to1_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GridConnectivity1to1_t` only applies to structured zones interfacing with structured donors and whose interface is a logically rectangular region.
It contains connectivity information for a multizone interface patch that is abutting with 1-to-1 matching between adjacent zone indices (also referred to as :math:`C^{0}` connectivity).
An interface patch is the subrange of the face of a zone that touches one and only one other zone.
This structure identifies the subrange of indices for the two adjacent zones that make up the interface and gives an index transformation from one zone to the other.
It also identifies the name of the adjacent zone.

All the interface patches for a given zone are contained in the :sidskey:`ZoneGridConnectivity_t` entity for that zone.
If a face of a zone touches several other zones (say *N*), then *N* different instances of the :sidskey:`GridConnectivity1to1_t` structure must be included in the zone to describe each separate interface patch.
This convention requires that a single interface patch be described twice in the database - once for each adjacent zone.

.. code-block:: sids

  GridConnectivity1to1_t< int IndexDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    int[IndexDimension] Transform ;                                    (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (r)
    IndexRange_t<IndexDimension> PointRangeDonor ;                     (r)

    Identifier(Zone_t) ZoneDonorName ;                                 (r)

    GridConnectivityProperty_t GridConnectivityProperty ;              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;

.. note::

    #. Default names for the :sidskey:`Descriptor_t` and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`GridConnectivity1to1_t` and shall not include the names :sidskey:`GridConnectivityProperty`, :sidskey:`PointRange`, :sidskey:`PointRangeDonor`, :sidskey:`Transform`, or :sidskey:`Ordinal`.
    
    #. If Transform is absent, then its default value is :code:`[+1,+2,+3]`.
    
    #. :sidskey:`ZoneDonorName` must be equated to a 32 character maximum zone identifier within the current CGNS database (i.e., it must be equal to one of the :sidskey:`Zone_t` identifiers contained in the current :sidskey:`CGNSBase_t` entity) or to a 65 character maximum zone identifier in another base of the same CGNS tree; in that case the :sidskey:`ZoneDonorName` string has the pattern base/zone, **only one single "/" character is allowed**, and neither basename nor zonename should be empty. :sidskey:`ZoneDonorName` should also not be empty.
    
    #. Beginning indices of :sidskey:`PointRange` and :sidskey:`PointRangeDonor` must coincide (i.e., must be the same physical point); ending indices of :sidskey:`PointRange` and :sidskey:`PointRangeDonor` must also coincide.
    
    #. Elements of :sidskey:`Transform` must be signed integers in the range :sidskey:`-IndexDimension, ..., +IndexDimension`; element magnitudes may not be repeated. In 3-D allowed elements are 0, ±1, ±2, ±3. 

:sidskey:`PointRange` contains the subrange of indices that makes up the interface patch in the current zone (i.e., that :sidskey:`Zone_t` entity that contains the given instance of :sidskey:`GridConnectivity1to1_t`).
:sidskey:`PointRangeDonor` contains the interface patch subrange of indices for the adjacent zone (whose identifier is given by :sidskey:`ZoneDonorName`).
By convention the indices contained in :sidskey:`PointRange` and :sidskey:`PointRangeDonor` refer to vertices.

:sidskey:`Transform` contains a short-hand notation for the transformation matrix describing the relation between indices of the two adjacent zones.
The transformation matrix itself has rank :sidskey:`IndexDimension` and contains elements :math:`+1`, :math:`−1` and :math:`0`; it is orthonormal and its inverse is its transpose.
The transformation matrix (:code:`T`) works as follows: If :code:`Index1` and :code:`Index2` are the indices of a given point on the interface, where :code:`Index1` is in the current zone and :code:`Index2` is in the adjacent zone, then their relationship is,

.. code-block::

   Index2 = T.(Index1 - Begin1) + Begin2 

   Index1 = Transpose[T].(Index2 - Begin2) + Begin1 

where the :code:`"."` notation indicates matrix-vector multiply. :code:`Begin1` and :code:`End1` are the subrange indices contained in :sidskey:`PointRange`, and :code:`Begin2` and :code:`End2` are the subrange indices contained in :sidskey:`PointRangeDonor`.

The short-hand notation used in :sidskey:`Transform` is as follows: Each element shows the image in the adjacent zone's face of a positive index increment in the current zone's face. The first element is the image of a positive increment in *i*; the second element is the image of an increment in *j*; and the third (in 3-D) is the image of an increment in *k* on the current zone's face. For 3-D, the transformation matrix :code:`T` is constructed from :code:`Transform` :math:`= [\pm a, \pm b, \pm c]` as follows:

.. math::

    T  = 
    \begin{bmatrix} 
    sgn(a) del(a-1) & sgn(b) del(b-1) & sgn(c) del(c-1) \\
    sgn(a) del(a-2) & sgn(b) del(b-2) & sgn(c) del(c-2) \\
    sgn(a) del(a-3) & sgn(b) del(b-3) & sgn(c) del(c-3) \\
    \end{bmatrix}


where :math:`sgn(x) \equiv +1 \text{ if } x ≥ 0\text{, and } -1 \text{ if } x < 0`, and :math:`del(x−y) \equiv +1 \text{ if } |x| = |y|\text{, and } 0 \text{ otherwise}`.

For example, :code:`Transform = [−2, +3, +1]` gives the transformation matrix,


.. math::

    T  = 
    \begin{bmatrix} 
    0 & 0 & +1 \\
    -1 & 0 & 0 \\
    0 & +1 & 0 \\
    \end{bmatrix}

For establishing relationships between adjacent and current zone indices lying on the interface itself, one of the elements of :sidskey:`Transform` is superfluous since one component of both interface indices remains constant.
It is therefore acceptable to set that element of :sidskey:`Transform` to zero.

If the transformation matrix is used for continuation of computational coordinates into the adjacent zone (e.g., to find the location of a rind point in the adjacent zone), then all elements of :sidskey:`Transform` are needed.
If the above mentioned superfluous element is set to zero, it can be easily regenerated from :sidskey:`PointRange` and :sidskey:`PointRangeDonor` and the grid sizes of the two zones.
This is done by determining the faces represented by :sidskey:`PointRange` and :sidskey:`PointRangeDonor` (i.e., *i*-min, *i*-max, *j*-min, etc.).
If one is a minimum face and the other a maximum face, then the sign of the missing element in :sidskey:`Transform` is :code:`"+"`, and the value of the missing element in the transformation matrix (:code:`T`) is +1.
If the faces are both minimums or are both maximums, the sign is :code:`"−"`. Next, the position and magnitude of the element in :sidskey:`Transform`, and hence the row and column in the transformation matrix, is given by the combinations of *i*, *j* and *k* faces for the two.
For example, if :sidskey:`PointRange` represents a *j*-min or *j*-max face and :sidskey:`PointRangeDonor` represents an *i*-min or *i*-max face, then the missing element's position in :sidskey:`Transform` is 2 and its magnitude is 1 (i.e., :math:`\text{Transform } = [*, \pm 1, *]`).

Note also that the transform matrix and the two index pairs overspecify the interface patch.
For example, :code:`End2` can be obtained from :code:`Transform`, :code:`Begin1`, :code:`End1` and :code:`Begin2`.

A :sidsref:`GridConnectivityProperty_t` data structure may be used to record special properties associated with particular connectivity patches, such as a periodic interface, or an interface where data is to be averaged in some way.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

:sidskey:`Ordinal` is user-defined and has no restrictions on the values that it can contain. It is included for backward compatibility to assist implementation of the CGNS system into applications whose I/O depends heavily on the numbering of zone interfaces.
Since there are no restrictions on the values contained in :sidskey:`Ordinal` (or that :sidskey:`Ordinal` is even provided), there is no guarantee that the interfaces in an existing CGNS database will have sequential values from 1 to N without holes or repetitions. Use of :sidskey:`Ordinal` is discouraged and is on a user-beware basis.


1-to-1 Interface Connectivity Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section contains two examples of structure entities for describing the connectivity for structured-zone 1-to-1 abutting multizone interfaces. The Structured Two-Zone Flat Plate Example contains additional examples of 1-to-1 interfaces.

Example - 1-to-1 Abutting of Complete Faces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two zones have the same orientation; zone 1 is :math:`9 \times 17 \times 11` and zone 2 is :math:`9 \times 17 \times 21`.
The *k*-max face of zone 1 abuts the *k*-min face of zone 2. Contained in the structure entities of zone 1 is the following interface structure:

.. code-block:: sids

  GridConnectivity1to1_t<3> Zone1/ZoneGridConnectivity/KMax =
    {{
    int[3] Transform = [1,2,3] ;
    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1,1,11] ;
      int[3] End   = [9,17,11] ;
      }} ;
    IndexRange_t<3> PointRangeDonor =
      {{
      int[3] Begin = [1,1,1] ; 
      int[3] End   = [9,17,1] ;
      }} ;
    Identifier(Zone_t) ZoneDonorName = Zone2 ;
    }} ;

Contained in the structure entities of zone 2 is the following:

.. code-block:: sids

  GridConnectivity1to1_t<3> Zone2/ZoneGridConnectivity/KMin =
    {{
    int[3] Transform = [1,2,3] ;
    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1,1,1] ; 
      int[3] End   = [9,17,1] ;
      }} ;
    IndexRange_t<3> PointRangeDonor =
      {{
      int[3] Begin = [1,1,11] ;
      int[3] End   = [9,17,11] ;
      }} ;
    Identifier(Zone_t) ZoneDonorName = Zone1 ;
    }} ;

This example assumes zones 1 and 2 have the identifiers :code:`Zone1` and :code:`Zone2`, respectively.


Example - 1-to-1 Abutting, Complete Face to a Subset of a Face
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../../images/sids/figs/cnct_1to1.gif
   :width: 600px
   :align: center
   :alt: Two abutting zones, with 1-to-1 abutting of a complete face to a subset of a face

   *Example Interface for 1-to-1 Connectivity*


The above figure shows a more complex 1-to-1 abutting interface, where the entire *j*-max face of zone 2 coincides with a subset of the *i*-max face of zone 1.
This situation would result in the following connectivity structures:

.. code-block:: sids

  GridConnectivity1to1_t<3> Zone1/ZoneGridConnectivity/IMax =
    {{
    int[3] Transform = [-2,-1,-3] ;
    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [17,3,1] ;
      int[3] End   = [17,9,5] ;
      }} ;
    IndexRange_t<3> PointRangeDonor =
      {{
      int[3] Begin = [7,9,5] ; 
      int[3] End   = [1,9,1] ;
      }} ;
    Identifier(Zone_t) ZoneDonorName = Zone2 ;
    }} ;

  GridConnectivity1to1_t<3> Zone2/ZoneGridConnectivity/JMax =
    {{
    int[3] Transform = [-2,-1,-3] ;
    IndexRange_t<3> PointRange =
      {{
      int[3] Begin = [1,9,1] ;
      int[3] End   = [7,9,5] ;
      }} ;
    IndexRange_t<3> PointRangeDonor =
      {{
      int[3] Begin = [17,9,5] ; 
      int[3] End   = [17,3,1] ;
      }} ;
    Identifier(Zone_t) ZoneDonorName = Zone1 ;
    }} ;

This example also assumes zones 1 and 2 have the identifiers :code:`Zone1` and :code:`Zone2`, respectively.
Note that the index transformation matrix for both this and the previous examples is symmetric; hence, the value of :sidskey:`Transform` is identical for both members of the interface pair.
In general this will not always be the case.


General Interface Connectivity Structure Definition: ``GridConnectivity_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GridConnectivity_t` contains connectivity information for generalized multizone interfaces, and may be used for any mix of structured and unstructured zones. Its purpose is to describe mismatched-abutting and overset interfaces, but can also be used for 1-to-1 abutting interfaces.

For abutting interfaces that are not 1-to-1, also referred to as patched or mismatched, an interface patch is the subrange of the face of a zone that touches one and only one other zone.
This structure identifies the subrange of indices (or array of indices) that make up the interface and gives their image in the adjacent (donor) zone.
It also identifies the name of the adjacent zone. If a given face of a zone touches several (say *N*) adjacent zones, then *N* different instances of :sidskey:`GridConnectivity_t` are needed to describe all the interfaces.
For a single abutting interface, two instances of :sidskey:`GridConnectivity_t` are needed in the database - one for each adjacent zone.

For overset interfaces, this structure identifies the fringe points of a given zone that lie in one and only one other zone.
If the fringe points of a zone lie in several (say *N*) overlapping zones, then *N* different instances of :sidskey:`GridConnectivity_t` are needed to describe the overlaps.
It is possible with overset grids that a single fringe point may actually lie in several overlapping zones (though in typical usage, linkage to only one of the overlapping zones is kept).
There is no restriction against a given fringe point being contained within multiple instances of :sidskey:`GridConnectivity_t`; therefore, this structure allows the description of a single fringe point lying in several overlapping zones.

.. code-block:: sids

  GridConnectivityType_t := Enumeration(
    GridConnectivityTypeNull,
    GridConnectivityTypeUserDefined,
    Overset,
    Abutting,
    Abutting1to1 ) ;

  GridConnectivity_t< int IndexDimension, int CellDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridConnectivityType_t GridConnectivityType ;                      (o/d)

    GridLocation_t GridLocation ;                                      (o/d)

    IndexRange_t<IndexDimension> PointRange ;                          (o:r)
    IndexArray_t<IndexDimension, PointListSize, int>  PointList ;      (r:o)
    IndexArray_t<IndexDimension, PointListSize, int>  PointListDonor ; (o)
    IndexArray_t<IndexDimension, PointListSize, int>  CellListDonor ;  (o)

    Identifier(Zone_t) ZoneDonorName ;                                 (r)

    DataArray_t <real, 2, [CellDimension, PointListSize]>
       InterpolantsDonor                                               (o)

    GridConnectivityProperty_t GridConnectivityProperty ;              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)

    int Ordinal ;                                                      (o)
    } ;

.. note::

    #. Default names for the :sidskey:`Descriptor_t` and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`GridConnectivity_t` and shall not include the names :sidskey:`CellListDonor`, :sidskey:`GridConnectivityProperty`, :sidskey:`GridConnectivityType`, :sidskey:`GridLocation`, :sidskey:`InterpolantsDonor`, :sidskey:`Ordinal`, :sidskey:`PointList`, :sidskey:`PointListDonor`, or :sidskey:`PointRange`.

    #. :sidskey:`ZoneDonorName` must be equated to a 32 character maximum zone identifier within the current CGNS database (i.e., it must be equal to one of the :sidskey:`Zone_t` identifiers contained in the current :sidskey:`CGNSBase_t` entity) or to a 65 character maximum zone identifier in another base of the same CGNS tree; in that case the :sidskey:`ZoneDonorName` string has the pattern *base/zone*, only one single "/" character is allowed, and neither basename nor zonename should be empty. :sidskey:`ZoneDonorName` should also not be empty.

    #. If :sidskey:`GridConnectivityType` is absent, then its default value is :sidskey:`Overset`.

    #. For :sidskey:`Abutting` or :sidskey:`Abutting1to1` interfaces, :sidskey:`GridLocation` can be either :sidskey:`Vertex` or :sidskey:`FaceCenter`. When :sidskey:`GridLocation` is set to :sidskey:`Vertex`, then :sidskey:`PointList` or :sidskey:`PointRange` refer to node indices, for both structured and unstructured grids. When :sidskey:`GridLocation` is set to :sidskey:`FaceCenter`, then :sidskey:`PointList` or :sidskey:`PointRange` refer to face elements. Face elements are indexed using different methods depending if the zone is structured or unstructured. For a structured zone, face elements are indexed using the minimum of the connecting vertex indices, as described in the section :ref:`Structured Grid Notation and Indexing Conventions <structgrid>`. For an unstructured zone, face elements are indexed using their element numbering, as defined in the :sidskey:`Elements_t` data structures. For :sidskey:`Overset` interfaces, :sidskey:`GridLocation` can be either :sidskey:`Vertex` or :sidskey:`CellCenter`, allowing the description of the overlap region in the receiver zone to be consistent with the grid location used for storing the flow solution. If :sidskey:`GridLocation` is absent, then its default value is :sidskey:`Vertex`.

    #. One of :sidskey:`PointRange` and :sidskey:`PointList` must be specified, but not both.

    #. If :sidskey:`PointRange` is specified, then an index ordering convention is needed to map receiver-zone grid points to donor-zone grid points. FORTRAN multidimensional array ordering is used.

    #. If :sidskey:`GridConnectivityType` is :sidskey:`Abutting1to1` or :sidskey:`Abutting`, then :sidskey:`PointRange` or :sidskey:`PointList` must define points associated with a face subrange (if the zone is structured, all points must be in a single computational grid plane); the donor-zone grid locations defined by :sidskey:`PointListDonor` or :sidskey:`CellListDonor` must also be associated with a face subrange.

    #. If donor information is given, either :sidskey:`PointListDonor` alone, or :sidskey:`CellListDonor` with or without :sidskey:`InterpolantsDonor`, must be used. The use of :sidskey:`PointListDonor` is restricted to :sidskey:`Abutting1to1`, whereas :sidskey:`CellListDonor` can be used for any interface type.

    #. Thus, for a :sidskey:`GridConnectivityType` that is not :sidskey:`Abutting1to1`, there are three allowable levels of description concerning the connectivity information: (a) full, giving :sidskey:`ZoneDonorName` with :sidskey:`CellListDonor` plus :sidskey:`InterpolantsDonor`; (b) partial, giving :sidskey:`ZoneDonorName` with :sidskey:`CellListDonor` but no :sidskey:`InterpolantsDonor`; or (c) minimal, giving :sidskey:`ZoneDonorName` only. 

The type of multizone interface connectivity may be :sidskey:`Overset`, :sidskey:`Abutting`, or :sidskey:`Abutting1to1`. :sidskey:`Overset` refers to zones that overlap; for a 3-D configuration the overlap is a 3-D region. :sidskey:`Abutting` refers to zones that abut or touch, but do not overlap (other than the vertices and faces that make up the interface).
:sidskey:`Abutting1to1` is a special case of abutting interfaces where grid lines are continuous across the interface and all vertices on the interface are shared by the two adjacent zones.

The interface grid points within the receiver zone may be specified by :sidskey:`PointRange` if they constitute a logically rectangular region (e.g., an abutting interface where an entire face of the receiver zone abuts with a part of a face of the donor zone).
In all other cases, :sidskey:`PointList` should be used to list the receiver-zone grid points making up the interface.
For a structured-to-structured interface, all indices in :sidskey:`PointRange` or :sidskey:`PointList` should have one index element in common (see note 7).

:sidsref:`GridLocation` identifies the location of indices within the receiver zone described by :sidskey:`PointRange` or :sidskey:`PointList`.
It also identifies the location of indices defined by :sidskey:`PointListDonor` in the donor zone. :sidskey:`GridLocation` does not apply to :sidskey:`CellListDonor` or :sidskey:`InterpolantsDonor`.
The :sidskey:`CellListDonor` is always an index or indices that define a particular cell or element, while the :sidskey:`InterpolantsDonor` defines an interpolation value relative to the cell/element vertices.
In other words, when using :sidskey:`InterpolantsDonor`, the interpolants are always given with respect to the vertices of the donor zone.
:sidskey:`InterpolantsDonor` is currently only defined for structured grids and certain basic unstructured grid element types.

For structured grids, the interpolant value is given along each index direction, depending on the location within the cell.
For example, if the point is located within the cell at a position 75% in the *i*-direction, 41% in the *j*-direction, and 20% in the *k*-direction, then :sidskey:`InterpolantsDonor` values :math:`(r, s, t)` would be :code:`(0.75, 0.41, 0.20)`.

The interpolation function is a linear combination of the *x*, *y*, and *z* values at the surrounding nodes:

.. math::

   d = \sum_{i=1}^{N} W_{i} \cdot d_{i}

where :math:`d` is the :math:`x`, :math:`y`, or :math:`z` value at an interior point in the cell, :math:`d_{i}` is the :math:`x`, :math:`y`, or :math:`z` value at node *i*, and :math:`W_{i}` is a weight at node *i*.
The weights are functions of the parametric variables :math:`r`, :math:`s`, and :math:`t` (corresponding with the *i*, *j*, and *k* directions, respectively), which vary from 0 to 1, inclusively.
For structured grids in 3-D, :math:`N = 8`. Note that for skewed, non-parallel grids, it is not always easy to determine the interpolants geometrically, and it may be necessary to solve an inverse problem using the interpolation function.

.. list-table::

  * - .. figure:: ../../../images/sids/figs/cnct_struct.gif
        :width: 300px
        :align: center
        :alt: Structured grid cell

    - .. math::

        W_{i,j,k} &= (1 − r) (1 − s) (1 − t) \\
        W_{i+1,j,k} &= r (1 − s) (1 − t) \\
        W_{i,j+1,k} &= (1 − r) s (1 − t) \\
        W_{i,j,k+1} &= (1 − r)(1 − s) t \\
        W_{i+1,j+1,k} &= r s (1 − t) \\
        W_{i+1,j,k+1} &= r (1 − s) t \\
        W_{i,j+1,k+1} &= (1 − r) s t \\
        W_{i+1,j+1,k+1} &= r s t

For unstructured grids, :sidskey:`InterpolantsDonor` is defined only for the basic linear element types: :sidskey:`BAR_2`, :sidskey:`TRI_3`, :sidskey:`QUAD_4`, :sidskey:`TETRA_4`, :sidskey:`PYRA_5`, :sidskey:`PENTA_6`, and :sidskey:`HEXA_8`.
The directionality for the :math:`r`, :math:`s`, and :math:`t` interpolants for the basic element types is defined as follows.

.. list-table:: ``BAR_2``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_bar2.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid line element

    - .. math::

        W_{1} &= 1 − r \\
        W_{2} &= r

.. list-table:: ``TRI_3``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_tri3.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid triangular element

    - .. math::

        W_{1} &= 1 − r - s \\
        W_{2} &= r \\
        W_{3} &= s


.. list-table:: ``QUAD_4``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_quad4.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid quadrilateral element

    - .. math::

        W_{1} &= (1 − r) (1 - s) \\
        W_{2} &= r (1 - s)\\
        W_{3} &= r s \\
        W_{4} &= (1 - r) s


.. list-table:: ``TETRA_4``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_tetra4.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid tetrahedral element

    - .. math::

        W_{1} &= 1 − r - s - t \\
        W_{2} &= r \\
        W_{3} &= s \\
        W_{4} &= t

.. list-table:: ``PYRA_5``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_pyra5.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid pyramid element

    - .. math::

        W_{1} &= (1 − r)(1 - s)(1 - t) \\
        W_{2} &= r (1 - s)(1 - t)\\
        W_{3} &= r s (1 - t) \\
        W_{4} &= (1 - r) s (1 - t) \\
        W_{5} &= t


.. list-table:: ``PENTA_6``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_penta6.gif
        :width: 260px
        :align: center
        :alt: Unstructured grid pentahedral element

    - .. math::

        W_{1} &= (1 − r − s)(1 − t) \\
        W_{2} &= r (1 - s)\\
        W_{3} &= s (1 - t) \\
        W_{4} &= (1 - r - s) t \\
        W_{5} &= r t \\
        W_{6} &= s t


.. list-table:: ``HEXA_8``

  * - .. figure:: ../../../images/sids/figs/cnct_unst_hexa8.gif
        :width: 280px
        :align: center
        :alt: Unstructured grid hexahedral element

    - .. math::

        W_{1} &= (1 − r)(1 − s)(1 − t) \\
        W_{2} &= r (1 − s)(1 − t)\\
        W_{3} &= r s (1 − t) \\
        W_{4} &= (1 − r) s (1 − t) \\
        W_{5} &= (1 − r) (1 − s) t \\
        W_{6} &= r (1 − s) t \\
        W_{7} &= r s t \\
        W_{8} &= (1 − r) s t


:sidskey:`PointListDonor` may only be used when the interface is :sidskey:`Abutting1to1`.
It contains the images of all the receiver-zone interface points in the donor zone. If the zone is structured, all indices in :sidskey:`PointListDonor` should have one index element in common.

For mismatched or overset interfaces, the zone connectivity donor information, when given, is defined using either the :sidskey:`CellListDonor` alone, or the combination of :sidskey:`CellListDonor` and :sidskey:`InterpolantsDonor`.
:sidskey:`CellListDonor` contains the list of donor cells or elements in which each node of the receiver zone can be located.
:sidskey:`InterpolantsDonor` contains the interpolation factors to locate the receiver nodes in the donor cells.
:sidskey:`InterpolantsDonor` may be thought of as bi- or tri-linear interpolants (depending on :sidskey:`CellDimension`) in the cell of the donor zone.

A :sidskey:`GridConnectivityProperty_t` data structure may be used to record special properties associated with particular connectivity patches, such as a periodic interface, or an interface where data is to be averaged in some way.

The :sidskey:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

:sidskey:`Ordinal` is user-defined and has no restrictions on the values that it can contain.
It is included for backward compatibility to assist implementation of the CGNS system into applications whose I/O depends heavily on the numbering of zone interfaces.
Since there are no restrictions on the values contained in :sidskey:`Ordinal` (or that :sidskey:`Ordinal` is even provided), there is no guarantee that the interfaces for a given zone in an existing CGNS database will have sequential values from 1 to N without holes or repetitions.
Use of :sidskey:`Ordinal` is discouraged and is on a user-beware basis.

.. c:function:: FUNCTION PointListSize()

   :return value: ``int``
   :dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

   :sidskey:`PointListDonor`, :sidskey:`CellListDonor`, and :sidskey:`InterpolantsDonor` require the function :sidskey:`PointListSize`, to identify the length of the array. If :sidskey:`PointRange` is specified by :sidskey:`GridConnectivity_t`, then :sidskey:`PointListSize` is obtained from the number of grid points (inclusive) between the beginning and ending indices of :sidskey:`PointRange`.
   If :sidskey:`PointList` is specified by :sidskey:`GridConnectivity_t`, then :sidskey:`PointListSize` is actually a user input during creation of the database; it is the length of the array :sidskey:`PointList` whose elements are also user inputs (by "user" we mean the application code that is generating the CGNS database).

   By definition, the :sidskey:`PointList` and :sidskey:`PointListDonor` arrays have the same size, and this size should be stored along with the arrays in their respective :sidskey:`IndexArray_t` structures.
   :sidskey:`PointListSize` was chosen to be a structure function, rather than a separate element of :sidskey:`GridConnectivity_t` for the following reasons: first, it is redundant if :sidskey:`PointRange` is specified; and second, it leads to redundant storage if :sidskey:`PointList` is specified, since the value of :sidskey:`PointListSize` is also stored within the :sidskey:`PointList` structure.

   This situation has somewhat of a precedent within the SIDS definitions. The structure :sidskey:`Descriptor_t` contains a string of unspecified length. Yet in actual implementation, the (string) length is a function of the descriptor string itself and should be stored along with the string.

General Interface Connectivity Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example - Structured Abutting Zones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Say that you have a three-dimensional structured grid. Assume that at the interface between two zones you have the following situation.

.. figure:: ../../../images/sids/figs/cnct_example1.gif
   :width: 490px
   :align: center
   :alt: Cell faces at interface between two structured zones

   *Example Interface for Generalized Connectivity, Structured Grids*

In this particular example, the patching occurs on a "plane". 
In other words, the two cells in 3-D have faces that abut in a 2-D sense.
It is these faces that we are picturing here. The solid quadrilateral is the donor cell face, and the dashed quadrilateral is the position of the receiving cell face relative to the donor cell.
Note that since this is a 2-D-type of abutting case, one of the indices (in this case *i* = 20, which represents :code:`imax`) of the donor cell is constant.
For this example, the point R of the receiver cell is located within the donor cell pictured, and we wish to give the :sidskey:`CellListDonor` and :sidskey:`InterpolantsDonor` for it.

Because this is a structured grid, the :sidskey:`CellListDonor` in this case is given by

.. code-block:: sids

   CellListDonor = (19, 10, 2)

Here, we are using the :ref:`Structured Grid Notation and Indexing Conventions <structgrid>` that say cell centers, face centers, and edge centers are indexed by the minimum *i*, *j*, and *k* indices of the connecting vertices.

The :sidskey:`InterpolantsDonor` defines an interpolation value relative to the cell/element vertices.
In this case, say that the point R is located 0.75 along the *j*-index direction and 0.45 along the *k*-index direction.
(It also lies on the *i* = 20, or :code:`imax` face.) Thus, in this example:

.. code-block:: sids

   InterpolantsDonor = (1.0, 0.75, 0.45) 

Note that if the donor zone was instead located on an *i* = 1 (:code:`imin` face), then the :sidskey:`CellListDonor` would be :code:`(1, 10, 2)` and the :sidskey:`InterpolantsDonor` would be :code:`(0.0, 0.75, 0.45)`. 


Example - Unstructured Abutting Zones, HEXA_8 Donor Cell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a second example, assume that you have the same setup as before, but now with a three-dimensional unstructured grid. In this case, we no longer have a 3-D array of indices defining coordinate directions. Instead, we simply have a 1-D list of indices as well as a list of volume (and possibly face) elements composed of those indices. In this example we again are assuming the two zones abut in a 2-D sense. We now have the choice of describing the donor in terms of its volume element or its boundary (face) element, if available. Here in this example, we use the volume element.

.. figure:: ../../../images/sids/figs/cnct_example2.gif
   :width: 490px
   :align: center
   :alt: Cell faces at interface between two unstructured zones

   *Example Interface for Generalized Connectivity, Unstructured Grids with HEXA_8 Donor Cell*

The :sidskey:`HEXA_8` volume element has been appropriately numbered, using the Unstructured Grid Element Numbering Conventions. In this example, it is the 1-2-3-4 face of the volumetric element that is abutting with the other zone (but it could be any of its six faces)

The :sidskey:`CellListDonor` in this case is simply given by

.. code-block:: sids

   CellListDonor = (238)

Using the convention established above for :sidskey:`HEXA_8` elements, the :sidskey:`InterpolantsDonor` would be

.. code-block:: sids

   InterpolantsDonor = (0.75, 0.55, 0.0)


Example - Unstructured Abutting Zones, TRI_3 Donor Cell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a third example, assume that you have two zones in a three-dimensional unstructured grid with triangles and quadrilaterals at its boundaries. Here the current zone (made up of quadrilateral faces) is abutting the donor zone (made up of triangular faces) in a 2-D sense.
We again have the choice of describing the donor in terms of its volume element or its boundary (face) element. Here in this example, we use the face element.

.. figure:: ../../../images/sids/figs/cnct_example3.gif
   :width: 390px
   :align: center
   :alt: Cell faces at interface between two unstructured zones

   *Example Interface for Generalized Connectivity, Unstructured Grids with TRI_3 Donor Cell*


The :sidskey:`CellListDonor` in this case is simply given by

.. code-block:: sids

   CellListDonor = (1893)

Using the convention established above for :sidskey:`TRI_3` elements, the :sidskey:`InterpolantsDonor` would be:

.. code-block:: sids

   InterpolantsDonor = (0.34, 0.61)

In this case the third dimension of the :sidskey:`InterpolantsDonor` (although present) is not used, because by default the interpolation is only two-dimensional in the 2-D plane of the donor face.


Grid Connectivity Property Structure Definition: ``GridConnectivityProperty_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GridConnectivityProperty_t` allows the recording of special properties associated with particular connectivity patches.
At the current time, only two properties (:sidskey:`Periodic_t` and :sidskey:`AverageInterface_t`) are included, but extensions involving other properties may be implemented as additional nodes under :sidskey:`GridConnectivityProperty_t` in the future.

.. code-block:: sids

  GridConnectivityProperty_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    Periodic_t Periodic ;                                              (o)
                
    AverageInterface_t AverageInterface ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`GridConnectivityProperty_t` and shall not include the names :sidskey:`Periodic` or :sidskey:`AverageInterface`. 

The :sidskey:`Periodic_t` and :sidskey:`AverageInterface_t` data structures may be used to record properties associated with periodic interfaces, or interfaces where data is to be averaged in some way, respectively.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 

Periodic Interface Structure Definition: ``Periodic_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`Periodic_t` data structure allows data associated with a periodic interface to be recorded.

.. code-block:: sids

  Periodic_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    DataArray_t<real, 1, PhysicalDimension> RotationCenter ;           (r)
    DataArray_t<real, 1, PhysicalDimension> RotationAngle ;            (r)
    DataArray_t<real, 1, PhysicalDimension> Translation ;              (r)

    DataClass_t DataClass ;                                            (o)
                                
    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`Periodic_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`RotationAngle`, :sidskey:`RotationCenter`, or :sidskey:`Translation`. 

:sidskey:`RotationCenter` is the origin for defining the rotation angle between the periodic interfaces. :sidskey:`RotationAngle` defines the angle from the current interface to the connecting interface. If rotating about more than one axis, the rotation is performed first about the x-axis, then the y-axis, then the z-axis. :sidskey:`Translation` defines the translation from the current interface to the connecting interface.

:sidsref:`DataClass` defines the default for the class of data contained in the :sidskey:`DataArray_t` structures. If the data is dimensional, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. If present, these two entities take precedence over all corresponding entities at higher levels of the hierarchy, following the :ref:`standard precedence rules <precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations. 

Average Interface Structure Definition: ``AverageInterface_t``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :sidskey:`AverageInterface_t` data structure is used when data at the current connectivity interface is to be averaged in some way prior to passing it to a neighboring interface.

.. code-block:: sids

  AverageInterface_t :=
    {
    List( Descriptor_t  Descriptor1 ... DescriptorN ) ;                (o)

    AverageInterfaceType_t AverageInterfaceType                        (r)
                                
    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    Default names for the :sidsref:`Descriptor_t` and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`AverageInterface_t` and shall not include the name :sidskey:`AverageInterfaceType`. 

:sidskey:`AverageInterfaceType_t` is a required enumeration data structure that is used to define the type of averaging to be done.

.. code-block:: sids

  AverageInterfaceType_t := Enumeration(
    AverageInterfaceTypeNull,
    AverageInterfaceTypeUserDefined,
    AverageAll,
    AverageCircumferential,
    AverageRadial,
    AverageI,
    AverageJ,
    AverageK ) ;

:sidskey:`AverageAll` means that the data from the entire current patch is averaged, whereas each of the other choices indicates averaging of the data on the current interface in the indicated direction.
Note that :sidskey:`AverageI`, :sidskey:`AverageJ`, and :sidskey:`AverageK` apply only to structured grids.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

 
Overset Grid Holes Structure Definition: ``OversetHoles_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Grid connectivity for overset grids must also include "holes" within zones, where any solution states are ignored or "turned off", because they are solved for in some other overlapping zone.
The structure :sidskey:`OversetHoles_t` specifies those points within a given zone that make up a hole (or holes), and applies to both structured and unstructured zones. Grid points specified in this structure are equivalent to those with IBLANK=0 in the PLOT3D format.

.. code-block:: sids

  OversetHoles_t< int IndexDimension > :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    GridLocation_t GridLocation ;                                      (o/d)

    List( IndexRange_t<IndexDimension> 
      PointRange, PointRange2 ... PointRangeN ) ;                      (o:r)

    IndexArray_t<IndexDimension, PointListSize, int> PointList ;       (r:o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;

.. note::

    #. Default names for the :sidsref:`Descriptor_t`, :sidsref:`IndexRange_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`OversetHoles_t` and shall not include the names :sidskey:`GridLocation` or :sidskey:`PointList`.
    
    #. If :sidsref:`GridLocation` is absent, then its default value is :sidskey:`Vertex`.
    
    #. One of :sidskey:`PointRange` and :sidskey:`PointList` must be specified, but not both.

The location of grid indices specified in :sidskey:`PointList` and the :sidskey:`PointRange` list is given by :sidsref:`GridLocation`.

The grid points making up a hole within a zone may be specified by :sidskey:`PointRange` if they constitute a logically rectangular region. If the hole points constitute a (small) set of possibly overlapping logically rectangular regions, then they may be specified by the list :sidskey:`PointRange`, :sidskey:`PointRange2`, etc. The more general alternate is to use :sidskey:`PointList` to list all grid points making up the hole(s) within a zone. Note that using multiple :sidskey:`PointRange` specifications may result in a given hole being specified more than once.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

.. c:function:: FUNCTION PointListSize()

   :return value: ``int``
   :dependencies: :sidskey:`PointList`

   :sidskey:`OversetHoles_t` requires one structure function, :sidskey:`PointListSize`, to identify the length of the :sidskey:`PointList` array. :sidskey:`PointListSize` is a user input. (See the discussion on function :ref:`PointListSize <PointListSize_abut>`.)

.. last line
