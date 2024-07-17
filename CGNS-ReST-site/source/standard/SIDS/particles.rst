
.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)



Particle Data
-------------

This section defines structure types for describing the particle data.

Particle Zone Structure Definition: :sidskey:`ParticleZone_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :sidskey:`ParticleZone_t` structure contains all information pertinent to an individual set of particles.

.. code-block:: sids

 ParticleZone_t< PhysicalDimension > :=
   {

   int ParticleSize ;                                                 (r)

   List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

   List( ParticleCoordinate<ParticleSize>
         ParticleCoordinates MovedParticles1 ... MovedParticlesN ) ;  (o)

   FamilyName_t FamilyName ;                                          (o)

   List( AdditionalFamilyName_t AddFamilyName1 ... AddFamilyNameN ) ; (o)

   List( ParticleSolution_t<ParticleSize>
         ParticleSolution1 ... ParticleSolutionN ) ;                  (o)

   List( IntegralData_t IntegralData1 ... IntegralDataN ) ;           (o)

   ParticleIterativeData_t<NumberOfSteps> ParticleIterativeData ;     (o)

   ReferenceState_t ReferenceState ;                                  (o)

   DataClass_t DataClass ;                                            (o)

   DimensionalUnits_t DimensionalUnits ;                              (o)

   ParticleEquationSet_t ParticleEquationSet ;                        (o)

   List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
   } ;


.. note::

   1. Default names for the :sidskey:`Descriptor_t`, :sidskey:`ParticleCoordinates_t`, :sidskey:`ParticleSolution_t`, :sidskey:`IntegralData_t`, and :sidskey:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleZone_t` and shall not include the names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`, :sidskey:`FamilyName`, :sidskey:`FlowEquationSet`, :sidskey:`ParticleCoordinates`, :sidskey:`ParticleSolution`, :sidskey:`ParticleIterativeData`, and :sidskey:`ReferenceState`.
   2. The original particle coordinates should have the name :sidskey:`ParticleCoordinates`. Default names for the remaining entities in the :sidskey:`ParticleCoordinates_t` list are as shown; users may choose other legitimate names, subject to, the restrictions listed in the previous note.
   3. There may be multiple :sidskey:`ParticleZone_t` per base. This allows users to create different groups of particles. :sidskey:`FamilyName_t` and :sidskey:`AdditionalFamilyName_t` nodes can be used to discern each :sidskey:`ParticleZone_t` node.
   4. :sidskey:`ParticleSize` is the only required field within the :sidskey:`ParticleZone_t` structure.

:sidskey:`ParticleZone_t` requires the parameter :sidskey:`PhysicalDimension`. :sidskey:`ParticleSize` corresponds to the number of particles in the :sidskey:`ParticleZone_t`. :sidskey:`ParticleSize` identifies the size of the particle-size arrays and is passed on to the particle coordinates and particle solution.

The :sidskey:`ParticleCoordinates_t` structure contains the physical coordinates of the center of each particle in the :sidskey:`ParticleZone_t`. The original particle coordinates are contained in :sidskey:`ParticleCoordinates`. Additional :sidskey:`ParticleCoordinates_t` data structures are allowed, to store particles at multiple time steps or iterations.

:sidskey:`FamilyName` identifies to which family particles belongs. Where multiple families are desired, :sidskey:`AdditionalFamilyName` nodes may be used to specify them. Both :sidskey:`FamilyName` and :sidskey:`AdditionalFamilyName` should refer to a :sidskey:`CGNSBase_t` level :sidskey:`Family_t`, in the parent base of the :sidskey:`ParticleZone_t` or in another sibling base (see :ref:`Base Level Families`).

Particle-solution quantities are contained in the list of :sidskey:`ParticleSolution_t` structures.
Multiple :sidskey:`ParticleSolution_t` structures can be provided to store
particle-solution data at multiple time steps or iterations.

Miscellaneous :sidsref:`ParticleZone_t`-specific global data is contained
in the list of :sidsref:`IntegralData_t` structures.

The particle-based :sidsref:`DataArray_t` vectors in :sidsref:`ParticleSolution_t` can correspond to a subset of particles defined in :sidsref:`ParticleCoordinates_t` through the use of a :sidsref:`PointRange` or :sidsref:`PointList`. Unless a :sidsref:`PointList` is defined, particle-based :sidsref:`DataArray_t` vectors in :sidsref:`ParticleSolution_t` must use the same ordering as those defined in :sidsref:`ParticleCoordinates_t`.

The :sidsref:`ParticleIterativeData_t` data structure may be used to record pointers to particle data at multiple time steps or iterations.

Reference-state data specific to an individual zone is contained in the :sidsref:`ReferenceState` structure.

:sidsref:`DataClass` defines the particle default for the class of data contained in the :sidsref:`ParticleZone_t` and its substructures. If a :sidsref:`ParticleZone_t` contains dimensional data, :sidsref:`DimensionalUnits` may be used to describe the system of dimensional units employed. :sidsref:`ReferenceState`, and :sidsref:`ParticleEquationSet` have special function in the hierarchy. They are applicable throughout a given particle zone, but their precedence may be superseded by local entities contained in the particle zone's substructures. If any of these entities are present within a given instance of :sidsref:`ParticleZone_t`, they take precedence over the corresponding global entities contained in database's :sidsref:`CGNSBase_t` entity. These precedence rules are further discussed in the section on :ref:`Precedence Rules and Scope Within the Hierarchy <precedence>`.

:sidsref:`DataClass` and :sidsref:`DimensionalUnits` have special function in the hierarchy. They are applicable throughout a given :sidsref:`ParticleZone_t`, but their precedence may be superseded by local entities contained in the :sidsref:`ParticleZone_t`'s substructures. If any of these entities are present within a given instance of :sidsref:`ParticleZone_t`, they take precedence over the corresponding global entities contained in the database's :sidsref:`ParticleZone_t` or :sidsref:`CGNSBase_t` entity. These precedence rules are further discussed in the section on :ref:`Precedence Rules and Scope Within the Hierarchy<precedence>`.

The :sidsref:`UserDefinedData_t` data structure allows arbitrary user-defined data to be stored in :sidsref:`Descriptor_t` and :sidsref:`DataArray_t` children without the restrictions or implicit meanings imposed on these node types at other node locations.

Particle Coordinates Structure Definition: :sidsref:`ParticleCoordinates_t`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The physical coordinates of the particle centers are described by the
:sidsref:`ParticleCoordinates_t` structure. This structure contains a list for the data arrays of the individual components of the position vector.

.. code-block:: sids

  ParticleCoordinates_t< int ParticleSize, int PhysicalDimension> :=
    {
    DataArray_t<DataType,PhysicalDimension, 2> BoundingBox ;           (o)

    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    List( DataArray_t<DataType, ParticleSize>
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;


.. note::

   1. Default names for the :sidsref:`Descriptor_t`, :sidsref:`DataArray_t`, and :sidsref:`UserDefinedData_t` lists are as shown; users may choose other legitimate names. Legitimate names must be unique within a given instance of :sidskey:`ParticleCoordinates_t` and shall not include the names :sidskey:`DataClass`, or :sidskey:`DimensionalUnits`.
   2. There are no required fields for :sidsref:`ParticleCoordinates_t`.
   3. The structure parameter :sidsref:`DataType` must be consistent with the data stored in the :sidsref:`DataArray_t` substructures.

:sidskey:`ParticleCoordinates_t` requires one structure parameters:  :sidskey:`ParticleSize`, which is the number of particles in the :sidsref:`ParticleZone_t` node.

The particle coordinates data is stored in the list of :sidsref:`DataArray_t` entities; each :sidskey:`DataArray_t` structure entity may contain a single component of the position vector (e.g., three separate :sidskey:`DataArray_t` entities are used for x, y, and z).

Standardized data-name identifiers for the particle coordinates are
described in :ref:`Conventions for Data-Name Identifiers<convention>`.

:sidsref:`DataClass` defines the default class for data contained in the :sidsref:`DataArray_t` entities. For dimensional grid coordinates, :sidsref:`DimensionalUnits` may be used to describe the system of units employed. If present, these two entities take precedence over the corresponding entities at higher levels of the CGNS hierarchy, following the standard :ref:`precedence rules<precedence>`. An example that uses these particle-coordinate defaults is shown under :ref:`Particle Coordinates Examples<_particle_coordinates_example>`.


.. _particle_coordinates_example:

Example - Particle Coordinates for a 3-D Case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example show how to set the particle coordinate in the case where :sidskey:`ParticleSize` is 15.

.. code-block:: sids

  !  ParticleSize = 15
  ParticleCoordinates_t&lt;15&gt; ParticleCoordinates =
    {{

    ! DataType = real
    ! ParticleSize = 15
    DataArray_t&lt;real, 1, 15&gt; CoordinateX =
      {{
      Data(real, 1, 15) = (x(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; CoordinateY =
      {{
      Data(real, 1, 15) = (y(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; CoordinateZ =
      {{
      Data(real, 1, 15) = (z(i), i=1,15) ;
      }} ;
    }} ;
</pre>


<a name="ParticleSolution"></a>
<h3>13.3 Particle Solution Structure Definition: :sidskey:`ParticleSolution_t`</h3>

<p>
The solution on each particle within a given :sidskey:`ParticleZone_t` is described by the
:sidskey:`ParticleSolution_t` structure.
This structure contains a list for the data arrays of the individual
solution variables. Particle solutions are implicitly defined at particle centers,
and correspond to the solution for the entire particle.

<pre>
  ParticleSolution_t&lt; int ParticleSize&gt; :=
    {
    List( Descriptor_t Descriptor1 ... DescriptorN ) ;                 (o)

    IndexRange PointRange ;                                            (o)
    IndexArray&lt;DataSize[], int&gt; PointList ;                            (o)

    List( DataArray_t&lt;DataType, DataSize[]&gt;
          DataArray1 ... DataArrayN ) ;                                (o)

    DataClass_t DataClass ;                                            (o)

    DimensionalUnits_t DimensionalUnits ;                              (o)

    List( UserDefinedData_t UserDefinedData1 ... UserDefinedDataN ) ;  (o)
    } ;
</pre>

<i>Notes</i>

<ol>
<li> Default names for the
     <a href="build.html#Descriptor">:sidskey:`Descriptor_t`</a>,
     <a href="data.html#DataArray">:sidskey:`DataArray_t`</a>, and
     <a href="misc.html#UserDefinedData">:sidskey:`UserDefinedData_t`</a>
     lists are as shown; users may choose other legitimate names.
     Legitimate names must be unique within a given instance
     of :sidskey:`ParticleSolution_t` and shall not include the
     names :sidskey:`DataClass`, :sidskey:`DimensionalUnits`,
     :sidskey:`PointList` or :sidskey:`PointRange`.
<li> There are no required fields for :sidskey:`ParticleSolution_t`.
<li> Both of the fields :sidskey:`PointList` and :sidskey:`PointRange` are
     optional. Only one of these two fields may be specified.
<li> The structure parameter :sidskey:`DataType` must be consistent with
     the data stored in the
     <a href="data.html#DataArray">:sidskey:`DataArray_t`</a>
     structure entities; :sidskey:`DataType` is
     :sidskey:`real` for all particle-solution identifiers defined in
     the section <a href="dataname.html">Conventions for Data-Name
     Identifiers</a>.
<li> Indexing of data within the
     <a href="data.html#DataArray">:sidskey:`DataArray_t`</a> structure
     must be consistent with coordonates defined in the <a href="#ParticleCoordinates">:sidskey:`ParticleCoordinates_t`</a>.
</ol>

<p>
The particle solution data is stored in the list of
<a href="data.html#DataArray">:sidskey:`DataArray_t`</a> entities; each
:sidskey:`DataArray_t` structure entity may contain a single component of
the solution vector.
Standardized data-name identifiers for the particle-solution quantities are
described in the section <a href="dataname.html">Conventions for Data-Name
Identifiers</a>.

<p>
<a href="build.html#DataClass">:sidskey:`DataClass`</a> defines the default
class for data contained in the
<a href="data.html#DataArray">:sidskey:`DataArray_t`</a> entities.
For dimensional particle solution data,
<a href="build.html#DimensionalUnits">:sidskey:`DimensionalUnits`</a> may be
used to describe the system of units employed.
If present, these two entities take precedence over the corresponding
entities at higher levels of the CGNS hierarchy, following the
standard <a href="cgnsbase.html#precedence">precedence rules</a>.

<p>
The <a href="misc.html#UserDefinedData">:sidskey:`UserDefinedData_t`</a>
data structure allows arbitrary user-defined data to be stored in
:sidskey:`Descriptor_t` and :sidskey:`DataArray_t` children without the
restrictions or implicit meanings imposed on these node types at other
node locations.

<a name="DataSize_particle"></a>
<h4>FUNCTION :sidskey:`DataSize[]`:</h4>

return value: :sidskey:`int`
<br>
dependencies: :sidskey:`PointRange`, :sidskey:`PointList`

<p>
:sidskey:`ParticleSolution_t` requires the structure function :sidskey:`DataSize`,
which is used to specify the number of entities corresponding
to a given :sidskey:`PointRange` or :sidskey:`PointList`. This will therefore be the
size of the ParticleSolution data arrays. If :sidskey:`PointRange` is
specified, then :sidskey:`DataSize` is obtained from the number of points
(inclusive) between the beginning and ending indices of :sidskey:`PointRange`.
If :sidskey:`PointList` is specified, then :sidskey:`DataSize` is the number of
indices in the list of points. In this situation, :sidskey:`DataSize` becomes
a user input along with the indices of the list :sidskey:`PointList`. By <i>user</i>
we mean the application code that is generating the CGNS database.

<a name="ParticleSolutionExample"></a>
<h4>Example - Particle Solution</h4>
<pre>
  ParticleSolution_t&lt;15&gt; ParticleSolution =
    {{

    ! DataType = real
    ! ParticleSize = 15

    DataArray_t&lt;real, 1, 15&gt; Radius =
      {{
      Data(real, 1, 15) = (r(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; Temperature =
      {{
      Data(real, 1, 15) = (T(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; VelocityX =
      {{
      Data(real, 1, 15) = (u(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; VelocityY =
      {{
      Data(real, 1, 15) = (v(i), i=1,15) ;
      }} ;

    DataArray_t&lt;real, 1, 15&gt; VelocityZ =
      {{
      Data(real, 1, 15) = (z(i), i=1,15) ;
      }} ;
    }} ;
</pre>


















