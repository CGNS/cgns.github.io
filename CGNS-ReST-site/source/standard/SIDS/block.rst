.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)

.. _StandardBlockStructure:

Building Block Structure Definition
+++++++++++++++++++++++++++++++++++

This section defines and describes low-level structures types that are used in the definition of more complex structures within the hierarchy. 

Definition ``DataClass_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`DataClass_t` is an enumeration type that identifies the class of a given piece of data.

.. code-block:: sids

  DataClass_t := Enumeration( 
    DataClassNull, 
    DataClassUserDefined,
    Dimensional,
    NormalizedByDimensional,
    NormalizedByUnknownDimensional,
    NondimensionalParameter,
    DimensionlessConstant ) ;

These classes divide data into different categories depending on dimensional units or normalization associated with the data.
:sidskey:`Dimensional` specifies dimensional data. :sidskey:`NormalizedByDimensional` specifies nondimensional data that is normalized by dimensional reference quantities.
In contrast, :sidskey:`NormalizedByUnknownDimensional` specifies nondimensional data typically found in completely nondimensional databases, where all field and reference data is nondimensional.
:sidskey:`NondimensionalParameter` specifies nondimensional parameters such as Mach number and lift coefficient.
Constants such as :math:`π` are designated by :sidskey:`DimensionlessConstant`.
The distinction between these different classes is further discussed in :ref:`Data-Array Structure Definition<StandardDataArrayStruct>`.

Definition ``Descriptor_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`Descriptor_t` is a documentation or annotation structure that contains a character string.
Characters allowed within the string include newlines, tabs and other special characters; this potentially allows for unlimited documentation inclusion within the database.
For example, a single :sidskey:`Descriptor_t` structure could be used to "swallow" an entire ASCII file.
In the hierarchical structures defined in the next sections, each allows for the inclusion of multiple :sidskey:`Descriptor_t` substructures.
Conventions could be made for names of often-used :sidskey:`Descriptor_t` structure entities, such as *ReadMe* or *YouReallyWantToReadMeFirst*.

.. code-block:: sids

  Descriptor_t :=
    {
    Data(char, 1, string_length) ;                       (r)
    } ;

where :sidskey:`string_length` is the length of the character string. 

Definition ``DimensionalUnits_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`DimensionalUnits_t` describes the system of units used to measure dimensional data. It is composed of a set of enumeration types that define the units for mass, length, time, temperature, angle, electric current, substance amount, and luminous intensity.

.. code-block:: sids

  MassUnits_t              := Enumeration( MassUnitsNull, MassUnitsUserDefined,
                                           Kilogram, Gram, Slug, PoundMass ) ;

  LengthUnits_t            := Enumeration( LengthUnitsNull, LengthUnitsUserDefined,
                                           Meter, Centimeter, Millimeter, Foot,
                                           Inch ) ;

  TimeUnits_t              := Enumeration( TimeUnitsNull, TimeUnitsUserDefined,
                                           Second ) ;

  TemperatureUnits_t       := Enumeration( TemperatureUnitsNull,
                                           TemperatureUnitsUserDefined, Kelvin,
                                           Celsius, Rankine, Fahrenheit ) ;

  AngleUnits_t             := Enumeration( AngleUnitsNull, AngleUnitsUserDefined,
                                           Degree, Radian ) ;

  ElectricCurrentUnits_t   := Enumeration( ElectricCurrentUnitsNull,
                                           ElectricCurrentUnitsUserDefined, Ampere,
                                           Abampere, Statampere, Edison, auCurrent ) ;

  SubstanceAmountUnits_t   := Enumeration( SubstanceAmountUnitsNull,
                                           SubstanceAmountUnitsUserDefined, Mole,
                                           Entities, StandardCubicFoot,
                                           StandardCubicMeter ) ;

  LuminousIntensityUnits_t := Enumeration( LuminousIntensityUnitsNull,
                                           LuminousIntensityUnitsUserDefined,
                                           Candela, Candle, Carcel, Hefner, Violle ) ;

  DimensionalUnits_t :=
    {
    MassUnits_t        MassUnits ;                                     (r)
    LengthUnits_t      LengthUnits ;                                   (r)
    TimeUnits_t        TimeUnits ;                                     (r)
    TemperatureUnits_t TemperatureUnits ;                              (r)
    AngleUnits_t       AngleUnits ;                                    (r)

    AdditionalUnits_t :=                                               (o)
      {
      ElectricCurrentUnits_t   ElectricCurrentUnits ;                  (r)
      SubstanceAmountUnits_t   SubstanceAmountUnits ;                  (r)
      LuminousIntensityUnits_t LuminousIntensityUnits ;                (r)
      }
    } ;

The International System (**SI**) uses the following units. 

.. table::
  :widths: 70 30

  =====================  ==========
  Physical Quantity	      Unit
  =====================  ==========
   Mass                   Kilogram
   Length                 Meter
   Time                   Second
   Temperature            Kelvin
   Angle                  Radian
   Electric Current       Ampere
   Substance Amount       Mole
   Luminous Intensity     Candela
  =====================  ==========

For an entity of type :sidskey:`DimensionalUnits_t`, if all the elements of that entity have the value :sidskey:`Null` (i.e., :sidskey:`MassUnits` = :sidskey:`MassUnitsNull`, etc.), this is equivalent to stating that the data described by the entity is nondimensionsal.

Definition ``DimensionalExponents_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`DimensionalExponents_t` describes the dimensionality of data by defining the exponents associated with each of the fundamental units.

.. code-block:: sids

  DimensionalExponents_t :=
    {
    real MassExponent ;                                                (r)
    real LengthExponent ;                                              (r)
    real TimeExponent ;                                                (r)
    real TemperatureExponent ;                                         (r)
    real AngleExponent ;                                               (r)

    AdditionalExponents_t :=                                           (o)
      {
      real ElectricCurrentExponent   ;                                 (r)
      real SubstanceAmountExponent   ;                                 (r)
      real LuminousIntensityExponent ;                                 (r)
      }
    } ;

For example, an instance of :sidskey:`DimensionalExponents_t` that describes velocity is,

.. code-block:: sids

  DimensionalExponents_t =
    {{
    MassExponent        =  0 ;
    LengthExponent      = +1 ;
    TimeExponent        = -1 ;
    TemperatureExponent =  0 ;
    AngleExponent       =  0 ;
    }} ;

Definition ``GridLocation_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`GridLocation_t` identifies locations with respect to the grid; it is an enumeration type.

.. code-block:: sids

  GridLocation_t := Enumeration( 
    GridLocationNull,
    GridLocationUserDefined,
    Vertex,
    CellCenter,
    FaceCenter,
    IFaceCenter,
    JFaceCenter,
    KFaceCenter,
    EdgeCenter ) ;

:sidskey:`Vertex` is coincident with the grid vertices. :sidskey:`CellCenter` is the center of a cell; this is also appropriate for entities associated with cells but not necessarily with a given location in a cell.
For structured zones, :sidskey:`IFaceCenter` is the center of a face in 3-D whose computational normal points in the i direction.
:sidskey:`JFaceCenter` and :sidskey:`KFaceCenter` are similarly defined, again only for structured zones.
:sidskey:`FaceCenter` is the center of a generic face that can point in any coordinate direction.
These are also appropriate for entities associated with a face, but not located at a specific place on the face.
:sidskey:`EdgeCenter` is the center of an edge.
See :ref:`Structured Grid Notation and Indexing Conventions<structgrid>` for descriptions of cells, faces and edges.

All of the entities of type :sidskey:`GridLocation_t` defined in this document use a default value of :sidskey:`Vertex`.

Definition ``IndexArray_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`IndexArray_t` specifies an array of indices.
An argument is included that allows for specifying the data type of each index;
typically the data type will be integer (:code:`int`).
:sidskey:`IndexArray_t` defines an array of indices of size :sidskey:`ArraySize`, where the dimension of each index is :sidskey:`IndexDimension`.

.. code-block:: sids

  IndexArray_t< int IndexDimension, int ArraySize, DataType > :=
    {
    Data( DataType, 2, [IndexDimension,ArraySize] ) ;                  (r)
    } ;


Definition ``IndexRange_t``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:sidskey:`IndexRange_t` specifies the beginning and ending indices of a subrange.
The subrange may describe a portion of a grid line, grid plane, or grid volume.

.. code-block:: sids

  IndexRange_t< int IndexDimension > :=
    {
    int[IndexDimension] Begin ;                                        (r)
    int[IndexDimension] End ;                                          (r)
    } ;

where :sidskey:`Begin` and :sidskey:`End` are the indices of the opposing corners of the subrange.

Definition ``Rind_t``
^^^^^^^^^^^^^^^^^^^^^

:sidskey:`Rind_t` describes the number of :ref:`rind planes <rind_struct>` (for structured grids) or :ref:`rind points and elements <rind_unstruct>` (for unstructured grids) associated with a data array containing grid coordinates, flow-solution data or any other grid-related discrete data.

.. code-block:: sids

  Rind_t< int IndexDimension > :=
    {
    int[2*IndexDimension] RindPlanes ;                                 (r)
    } ;

For structured grids, :sidskey:`RindPlanes` contains the number of rind planes attached to the minimum and maximum faces of a zone. The face corresponding to each index *n* of :sidskey:`RindPlanes` in 3-D is:

  .. table::
    :widths: 50 50

    =========================    =======================
     *n* = 1  -->  i-min          *n* = 2  -->  i-max
     *n* = 3  -->  j-min          *n* = 4  -->  j-max
     *n* = 5  -->  k-min          *n* = 6  -->  k-max
    =========================    =======================


For a 3-D grid whose "core" size is :code:`II×JJ×KK`, a value of :code:`RindPlanes = [a,b,c,d,e,f]` indicates that the range of indices for the grid with rind is:

  .. table::

    ====== ========================
     *i*:  :code:`(1 - a, II + b)`
     *j*:  :code:`(1 - c, JJ + d)`
     *k*:  :code:`(1 - e, KK + f)`
    ====== ========================

For unstructured grids, :sidskey:`RindPlanes` does not actually contain planes, but rather contains the number of rind points or elements.
The points are defined by the grid coordinates rind node, and the elements by the element set rind node.
Note that to maintain consistency with the structured usage of :sidskey:`Rind_t`, :sidskey:`RindPlanes` is still dimensioned :code:`2*IndexDimension` for unstructured grids (and, for unstructured grids, :sidskey:`IndexDimension = 1`).
The first :sidskey:`RindPlanes` value is the number of rind nodes/elements stored before the core data, and the second is the number stored after.
Thus :sidskey:`RindPlanes[2] = {1 2}` would mean there is one rind value before the core data, and two after the core data.
However, it is preferable to write all the rind points or elements at the end of the array; in other words, for unstructured grids :sidskey:`RindPlanes[2]` should be set to :code:`{0 nrind}`, where :code:`nrind` is the number of rind points or elements.

.. last line
