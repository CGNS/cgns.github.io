
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

