.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources


.. role:: in
.. role:: out
.. role:: sig-name(code)
   :language: c


.. _MLLEquation:
   
Equation Specification
----------------------

.. list-table::
   :header-rows: 1
   :widths: 2 8

   * -
     - `Flow Equation Set`_ 
   * - ``cg_equationset_write``
     - Write dimensionality of flow equations
   * - ``cg_equationset_read``
     - Read flow equation set info
   * - ``cg_equationset_chemistry_read``
     - Read chemistry equation set info
   * - ``cg_equationset_elecmagn_read``
     - Read electromagnetic equation set info

   
.. list-table::
   :header-rows: 1
   :widths: 2 8
       
   * - 
     - `Governing Equations`_
   * - ``cg_governing_write``
     - Write type of governing equation
   * - ``cg_governing_read``
     - Read type of governing equation
   * - ``cg_diffusion_write``
     - Write flags for diffusion terms
   * - ``cg_diffusion_read``
     - Read flags for diffusion terms 


.. list-table::
   :header-rows: 1
   :widths: 2 8

   * - 
     - `Auxiliary Models`_
   * - ``cg_model_write``
     - Write auxiliary model types
   * - ``cg_model_read``
     - Read auxiliary model types 


Flow Equation Set
^^^^^^^^^^^^^^^^^
Node: FlowEquationSet_t (SIDS, File Mapping) 

Governing Equations
^^^^^^^^^^^^^^^^^^^
Node: GoverningEquations_t (SIDS, File Mapping) 

Auxiliary Models
^^^^^^^^^^^^^^^^

Nodes: GasModel_t (SIDS, File Mapping)
ViscosityModel_t (SIDS, File Mapping)
ThermalConductivityModel_t (SIDS, File Mapping)
TurbulenceClosure_t (SIDS, File Mapping)
TurbulenceModel_t (SIDS, File Mapping)
ThermalRelaxationModel_t (SIDS, File Mapping)
ChemicalKineticsModel_t (SIDS, File Mapping)
EMElectricFieldModel_t (SIDS, File Mapping)
EMMagneticFieldModel_t (SIDS, File Mapping)
EMConductivityModel_t (SIDS, File Mapping)



.. last line
