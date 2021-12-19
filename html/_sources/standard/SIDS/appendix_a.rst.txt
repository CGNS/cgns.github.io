.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. default-domain:: sids

.. role:: sidskey(code)

.. role:: sidsref(code)


.. _dataname:

Appendix A: Conventions for Data-Name Identifiers
=================================================

Identifiers or names can be attached to :sidskey:`DataArray_t` entities to identify and describe the quantity being stored.
To facilitate communication between different application codes, we propose to establish a set of standardized data-name identifiers with fairly precise definitions.
For any identifier in this set, the associated data should be unambiguously understood. In essence, this section proposes standardized terminology for labeling CFD-related data, including grid coordinates, flow solution, turbulence model quantities, nondimensional governing parameters, boundary condition quantities, and forces and moments.

We use the convention that all standardized identifiers denote scalar quantities; this is consistent with the intended use of the :sidskey:`DataArray_t` structure type to describe an array of scalars.
For quantities that are vectors, such as velocity, their components are listed.

Included with the lists of standard data-name identifiers are the fundamental units of dimensions associated with that quantity.
The following notation is used for the fundamental units: :math:`M` is mass, :math:`L` is length, :math:`T` is time, :math:`\Theta` is temperature, :math:`\alpha` is angle, and :math:`I` is electric current.
These fundamental units are directly associated with the elements of the :sidskey:`DimensionalExponents_t` structure.
For example, a quantity that has dimensions :math:`ML/T` corresponds to :sidskey:`MassExponent = +1`, :sidskey:`LengthExponent = +1`, and :sidskey:`TimeExponent = -1`.

Unless otherwise noted, all quantities in the following sections denote floating-point data types, and the appropriate :sidskey:`DataType` structure parameter for :sidskey:`DataArray_t` is :code:`real`.


A1 Coordinate Systems
^^^^^^^^^^^^^^^^^^^^^

Coordinate systems for identifying physical location are as follows:

.. table::
  :widths: 30 30 40

  =============  ========================== ===================================================================
   System         3-D                        2-D
  =============  ========================== ===================================================================
   Cartesian      :math:`(x,y,z)`            :math:`(x,y)` or :math:`(x,z)` or :math:`(y,z)`
   Cylindrical    :math:`(r,\theta,z)`       :math:`(r,\theta)`
   Spherical      :math:`(r,\theta,\phi)`	
   Auxiliary      :math:`(\xi,\eta,\zeta)`   :math:`(\xi,\eta)` or :math:`(\xi,\zeta)` or :math:`(\eta,\zeta)`
  =============  ========================== ===================================================================


Associated with these coordinate systems are the following unit vector conventions:

.. table::
  :widths: 33 33 33

  ==========================================   ==================================================== ==================================================
  :math:`x`-direction: :math:`\mathbf{e}_x`     :math:`r`-direction: :math:`\mathbf{e}_r`           :math:`\xi`-direction: :math:`\mathbf{e}_\xi`
  :math:`y`-direction: :math:`\mathbf{e}_y`     :math:`\theta`-direction: :math:`\mathbf{e}_\theta` :math:`\eta`-direction: :math:`\mathbf{e}_\eta`
  :math:`z`-direction: :math:`\mathbf{e}_z`     :math:`\phi`-direction: :math:`\mathbf{e}_\phi`     :math:`\zeta`-direction: :math:`\mathbf{e}_\zeta`
  ==========================================   ==================================================== ==================================================

Note that :math:`\mathbf{e}_r`, :math:`\mathbf{e}_\theta` and :math:`\mathbf{e}_\phi` are functions of position.


We envision that one of the "standard" coordinate systems (Cartesian, cylindrical or spherical) will be used within a zone (or perhaps the entire database) to define grid coordinates and other related data.
The auxiliary coordinates will be used for special quantities, including forces and moments, which may not be defined in the same coordinate system as the rest of the data.
When auxiliary coordinates are used, a transformation must also be provided to uniquely define them.
For example, the transform from Cartesian to orthogonal auxiliary coordinates is,

.. math::
  
  \begin{pmatrix} \hat{e}_\xi \\ \hat{e}_\eta\\ \hat{e}_\zeta \end{pmatrix} = T \begin{pmatrix} \hat{e}_x \\ \hat{e}_y \\ \hat{e}_z \end{pmatrix}


where :math:`T` is an orthonormal matrix (:math:`2\times2` in 2-D and :math:`3\times3` in 3-D).

In addition, normal and tangential coordinates are often used to define boundary conditions and data related to surfaces. The normal coordinate is identified as :math:`n` with the unit vector :math:`\mathbf{e}_n`.

The data-name identifiers defined for coordinate systems are listed in the following table. All represent real :sidskey:`DataTypes`, except for :sidskey:`ElementConnectivity` and :sidskey:`ParentData`, which are integer.

.. table:: **Data-Name Identifiers for Coordinate Systems**

  +-----------------------------------+-----------------------------------------------------+----------------+
  |Data-Name Identifier               | Description                                         | Units          |
  +===================================+=====================================================+================+
  |:sidskey:`CoordinateX`             | :math:`x`                                           | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateY`             | :math:`y`                                           | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateZ`             | :math:`z`                                           | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateR`             | :math:`r`                                           | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateTheta`         | :math:`\theta`                                      | :math:`\alpha` |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinatePhi`           | :math:`\phi`                                        | :math:`\alpha` |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |                                                                                                          |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateNormal`        | Coordinate in direction of :math:`\mathbf{e}_n`     | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateTangential`    | Tangential coordinate (2-D only)                    | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |                                                                                                          |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateXi`            | :math:`\xi`                                         | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateEta`           | :math:`\eta`                                        | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateZeta`          | :math:`\zeta`                                       | :math:`L`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |                                                                                                          |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`CoordinateTransform`     | Transformation matrix (:math:`\mathbf{T}`)          | :math:`-`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |                                                                                                          |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`InterpolantsDonor`       | Interpolation factors                               | :math:`-`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |                                                                                                          |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`ElementConnectivity`     | Nodes making up an element                          | :math:`-`      |
  +-----------------------------------+-----------------------------------------------------+----------------+
  |:sidskey:`ParentData`              | Element parent identification                       | :math:`-`      |
  +-----------------------------------+-----------------------------------------------------+----------------+


A2 Flowfield Solution
^^^^^^^^^^^^^^^^^^^^^

This section describes data-name identifiers for typical Navier-Stokes solution variables. The list is obviously incomplete, but should suffice for initial implementation of the CGNS system. The variables listed in this section are dimensional or raw quantities; nondimensional parameters and coefficients based on these variables are discussed in the section :ref:`Nondimensional Parameters <dataname-nondim>.

We use fairly universal notation for state variables. Static quantities are measured with the fluid at speed: static density (:math:`\rho`), static pressure (:math:`p`), static temperature (:math:`T`), static internal energy per unit mass (:math:`e`), static enthalpy per unit mass (:math:`h`), entropy (:math:`s`), and static speed of sound (:math:`c`).
We also approximate the true entropy by the function :math:`s_{app} = p / \rho^{\gamma}` (this assumes an ideal gas).
The velocity is :math:`\mathbf{q} = u \mathbf{e}_x + v \mathbf{e}_y + w \mathbf{e}_z`, with magnitude :math:`q = ( \mathbf{q} \cdot  \mathbf{q})^{1/2}`.
Stagnation quantities are obtained by bringing the fluid isentropically to rest; these are identified by a subscript "0". The term "total" is also used to refer to stagnation quantities.

Conservation variables are density, momentum (:math:`\rho \mathbf{q} = \rho u \mathbf{e}_x + \rho v \mathbf{e}_y + \rho w \mathbf{e}_z`), and stagnation energy per unit volume (:math:`\rho e_{0}`).

For :ref:`rotating coordinate systems <RotatingCoordinates>`, :math:`u`, :math:`v`, and :math:`w` are the :math:`x`, :math:`y`, and :math:`z` components of the velocity vector in the inertial frame; :math:`\mathbf{\omega}` is the rotation rate vector; :math:`\mathbf{R}` is a vector from the center of rotation to the point of interest; and :math:`\mathbf{w}_r = \mathbf{\omega} \times \mathbf{R}` is the rotational velocity vector of the rotating frame of reference, with components :math:`w_{rx}`, :math:`w_{ry}`, and :math:`w_{rz}`.

Molecular diffusion and heat transfer introduce the molecular viscosity (:math:`\mu`), kinematic viscosity (:math:`\nu`) and thermal conductivity coefficient (:math:`k`). These are obtained from the state variables through auxiliary correlations.
For a perfect gas, :math:`\mu` and :math:`k` are functions of static temperature only.

The Navier-Stokes equations involve the strain tensor (:math:`\bar{\bar{S}}`) and the shear-stress tensor (:math:`\bar{\bar{\tau}}`). Using indicial notation, the 3-D Cartesian components of the strain tensor are,

.. math::

  \bar{\bar{S}}_{ij} = \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right)


and the stress tensor is,

.. math::

  \bar{\bar{\tau}}_{ij} = \mu \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right) + \lambda \frac{\partial u_k}{\partial x_k}



where :math:`(x_1,x_2,x_3) = (x,y,z)` and :math:`(u_1,u_2,u_3) = (u,v,w)`.
The bulk viscosity is usually approximated as :math:`\lambda = − 2 \mu /3`.

Reynolds averaging of the Navier-Stokes equations introduce Reynolds stresses (:math:`−\rho(u′v′)_{ave}`, etc.) and turbulent heat flux terms (:math:`−\rho(u′e′)_{ave}, etc.), where primed quantities are instantaneous fluctuations.
These quantities are obtained from auxiliary turbulence closure models. Reynolds-stress models formulate transport equations for the Reynolds stresses directly; whereas, eddy-viscosity models correlate the Reynolds stresses with the mean strain rate,

.. math::

  −(u′v′)_{ave} = \nu_t (\partial u/\partial y + \partial v/\partial x)

where :math:`\nu_t` is the kinematic eddy viscosity. The eddy viscosity is either correlated to mean flow quantities by algebraic models or by auxiliary transport models.
An example two-equation turbulence transport model is the :math:`k`-:math:`\epsilon` model, where transport equations are formulated for the turbulent kinetic energy (:math:`k = [(u′u′)_{ave} + (v′v′)_{ave} + (w′w′)_{ave}] / 2`) and turbulent dissipation (:math:`\epsilon`).

Skin friction evaluated at a surface is the dot product of the shear stress tensor with the surface normal:

.. math::

       \overrightarrow{\tau} = \bar{\bar{\tau}} \cdot \hat{n}

Note that skin friction is a vector.

The data-name identifiers defined for flow solution quantities are listed below.

Note that for some vector quantities, like momentum, the table only explicitly lists data-name identifiers for the :math:`x`, :math:`y`, and :math:`z` components, and for the magnitude.
It should be understood, however, that for any vector quantity with a standardized data name ":sidskey:`Vector`", the following standardized data names are also defined:

.. table::

  ============================  ===========================================
  :sidskey:`VectorX`            :math:`x`-component of vector
  :sidskey:`VectorY`            :math:`y`-component of vector
  :sidskey:`VectorZ`            :math:`z`-component of vector
  :sidskey:`VectorR`            Radial component of vector
  :sidskey:`VectorTheta`        :math:`\theta`-component of vector
  :sidskey:`VectorPhi`          :math:`\phi`-component of vector
  :sidskey:`VectorMagnitude`    Magnitude of vector
  :sidskey:`VectorNormal`       Normal component of vector
  :sidskey:`VectorTangential`   Tangential component of vector (2-D only)
  ============================  ===========================================

Also note that some data-name identifiers used with multi-species flows include the variable string *Symbol*, which represents either the chemical symbol for a species, or a defined name for a mixture.
See the section describing the :sidskey:`ChemicalKineticsModel` :ref:`data structure <ChemicalKineticsModel>` for examples and a table of defined names.

.. list-table:: **Data-Name Identifiers for Flow Solution Quantities**
  :header-rows: 1
  :widths: 30 64 6

  * - Data-Name Identifier
    - Description
    - Units
  * - :sidskey:`Potential`
    - Potential: :math:`\nabla\phi = q`
    - :math:`L^{2}/T`
  * - :sidskey:`StreamFunction`
    - Stream function (2-D): :math:`\nabla \times \psi = q`
    - :math:`L^{2}/T`
  * -
    -
    -
  * - :sidskey:`Density`
    - Static density (:math:`\rho`)
    - :math:`M/L^{3}`
  * - :sidskey:`Pressure`
    - Static pressure (:math:`p`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`Temperature`
    - Static temperature (:math:`T`)
    - :math:`\Theta`
  * - :sidskey:`EnergyInternal`
    - Static internal energy per unit mass (:math:`e`)
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`Enthalpy`
    - Static enthalpy per unit mass (:math:`h`)
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`Entropy`
    - Entropy (:math:`s`)
    - :math:`M L^{2}/(T^{2} \Theta)`
  * - :sidskey:`EntropyApprox`
    - Approximate entropy (:math:`s_{app} = p / \rho^{\gamma}`)
    - :math:`L^{3\gamma−1}/(M^{\gamma−1} T^{2})`
  * -
    -
    -
  * - :sidskey:`DensityStagnation`
    - Stagnation density (:math:`\rho_0`)
    - :math:`M/L^{3}`
  * - :sidskey:`PressureStagnation`
    - Stagnation pressure (:math:`p_0`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`TemperatureStagnation`
    - Stagnation temperature (:math:`T_0`)
    - :math:`\Theta`
  * - :sidskey:`EnergyStagnation`
    - Stagnation energy per unit mass (:math:`e_0`)
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`EnthalpyStagnation`
    - Stagnation enthalpy per unit mass (:math:`h_0`)
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`EnergyStagnationDensity`
    - Stagnation energy per unit volume (:math:`\rho e_0`)
    - :math:`M/(L T^{2})`
  * -
    -
    -
  * - :sidskey:`VelocityX`
    - x-component of velocity (:math:`u = \mathbf{q} \cdot \mathbf{e}_x`)
    - :math:`L/T`
  * - :sidskey:`VelocityY`
    - y-component of velocity (:math:`v = \mathbf{q} \cdot \mathbf{e}_y`)
    - :math:`L/T`
  * - :sidskey:`VelocityZ`
    - z-component of velocity (:math:`w = \mathbf{q} \cdot \mathbf{e}_z`)
    - :math:`L/T`
  * - :sidskey:`VelocityR`
    - Radial velocity component (:math:`\mathbf{q} \cdot \mathbf{e}_r`)
    - :math:`L/T`
  * - :sidskey:`VelocityTheta`
    - Velocity component in :math:`\theta` direction (:math:`\mathbf{q} \cdot \mathbf{e}_\theta`)
    - :math:`L/T`
  * - :sidskey:`VelocityPhi`
    - Velocity component in :math:`\phi` direction (:math:`\mathbf{q} \cdot \mathbf{e}_\phi`)
    - :math:`L/T`
  * - :sidskey:`VelocityMagnitude`
    - Velocity magnitude (:math:`q = (\mathbf{q} \cdot \mathbf{q})^{1/2}`)
    - :math:`L/T`
  * - :sidskey:`VelocityNormal`
    - Normal velocity component (:math:`\mathbf{q} \cdot \mathbf{n}`)
    - :math:`L/T`
  * - :sidskey:`VelocityTangential`
    - Tangential velocity component (2-D)
    - :math:`L/T`
  * - :sidskey:`VelocitySound`
    - Static speed of sound
    - :math:`L/T`
  * - :sidskey:`VelocitySoundStagnation`
    - Stagnation speed of sound
    - :math:`L/T`
  * -
    -
    -
  * - :sidskey:`MomentumX`
    - x-component of momentum (:math:`\rho u`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`MomentumY`
    - y-component of momentum (:math:`\rho v`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`MomentumZ`
    - z-component of momentum (:math:`\rho w`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`MomentumMagnitude`
    - Magnitude of momentum (:math:`\rho q`)
    - :math:`M/(L^{2}T)`
  * -
    -
    -
  * - :sidskey:`RotatingVelocityX`
    - x-component of velocity, relative to rotating frame (:math:`u_{rx} = u − w_{rx}`)
    - :math:`L/T`
  * - :sidskey:`RotatingVelocityY`
    - y-component of velocity, relative to rotating frame (:math:`u_{ry} = v − w_{ry}`)
    - :math:`L/T`
  * - :sidskey:`RotatingVelocityZ`
    - z-component of velocity, relative to rotating frame (:math:`u_{rz} = w − w_{rz}`)
    - :math:`L/T`
  * - :sidskey:`RotatingMomentumX`
    - x-component of momentum, relative to rotating frame (:math:`\rho u_{rx}`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`RotatingMomentumY`
    - y-component of momentum, relative to rotating frame (:math:`\rho u_{ry}`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`RotatingMomentumZ`
    - z-component of momentum, relative to rotating frame (:math:`\rho u_{rz}`)
    - :math:`M/(L^{2}T)`
  * - :sidskey:`RotatingVelocityMagnitude`
    - Velocity magnitude in rotating frame (:math:`q_r = (u_{rx} + u_{ry} + u_{rz})^{1/2}`)
    - :math:`L/T`
  * - :sidskey:`RotatingPressureStagnation`
    - Stagnation pressure in rotating frame
    - :math:`M/(LT^{2})`
  * - :sidskey:`RotatingEnergyStagnation`
    - Stagnation energy per unit mass in rotating frame (:math:`(e_{0})_r`)
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`RotatingEnergyStagnationDensity`
    - Stagnation energy per unit volume in rotating frame (:math:`\rho (e_{0})_r`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`RotatingEnthalpyStagnation`
    - Stagnation enthalpy per unit mass in rotating frame, rothalpy
    - :math:`L^{2}/T^{2}`
  * - 
    -
    -
  * - :sidskey:`EnergyKinetic`
    - :math:`(u^{2} + v^{2} + w^{2})/2 = q^{2}/2`
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`PressureDynamic`
    - :math:`\rho q^{2}/2`
    - :math:`M/(LT^{2})`
  * - 
    -
    -
  * - :sidskey:`SoundIntensityDB`
    - Sound intensity level in decibels, :math:`10 {log_{10}}(I/I_{ref}) = 20 {log_{10}}(p/p_{ref})`, where :math:`I` is the sound power per unit area, :math:`I_{ref} = 10−12 watts/m^{2}` is the reference sound power per unit area, :math:`p` is the pressure wave amplitude, and :math:`p_{ref} = 2\times10^{−5}\ N/m^{2}` is the reference pressure.
    - :math:`-`
  * - :sidskey:`SoundIntensity`
    - Sound intensity (i.e., sound power per unit area, :math:`I`)
    - :math:`M/T^{3}`
  * - 
    -
    -
  * - :sidskey:`VorticityX`
    - :math:`\omega_x = \partial w/ \partial y − \partial v/ \partial z = \mathbf{\omega} \cdot \mathbf{e}_x`
    - :math:`T^{−1}`
  * - :sidskey:`VorticityY`
    - :math:`\omega_y = \partial u/ \partial z − \partial w/ \partial x = \mathbf{\omega} \cdot \mathbf{e}_y`
    - :math:`T^{−1}`
  * - :sidskey:`VorticityZ`
    - :math:`\omega_z = \partial v/ \partial x − \partial u/ \partial y = \mathbf{\omega} \cdot \mathbf{e}_z`
    - :math:`T^{−1}`
  * - :sidskey:`VorticityMagnitude`
    - :math:`\omega = (\mathbf{\omega} \times \mathbf{\omega})^{1/2}`
    - :math:`T^{−1}`
  * - 
    -
    -
  * - :sidskey:`SkinFrictionX`
    - x-component of skin friction (:math:`\mathbf{\tau} \cdot \mathbf{e}_x`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`SkinFrictionY`
    - y-component of skin friction (:math:`\mathbf{\tau} \cdot \mathbf{e}_y`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`SkinFrictionZ`
    - z-component of skin friction (:math:`\mathbf{\tau} \cdot \mathbf{e}_z`)
    - :math:`M/(LT^{2})`
  * - :sidskey:`SkinFrictionMagnitude`
    - Skin friction magnitude (:math:`(\mathbf{\tau} \times \mathbf{\tau})^{1/2}`)
    - :math:`M/(LT^{2})`
  * - 
    -
    -
  * - :sidskey:`VelocityAngleX`
    - Velocity angle (:math:`arccos(u/q) \in [0, \pi]`)
    - :math:`\alpha`
  * - :sidskey:`VelocityAngleY`
    - :math:`arccos(v/q)`
    - :math:`\alpha`
  * - :sidskey:`VelocityAngleZ`
    - :math:`arccos(w/q)`
    - :math:`\alpha`
  * - 
    -
    -
  * - :sidskey:`VelocityUnitVectorX`
    - x-component of velocity unit vector (:math:`\mathbf{q} \cdot \mathbf{e}_x / q`)
    - :math:`-`
  * - :sidskey:`VelocityUnitVectorY`
    - y-component of velocity unit vector (:math:`\mathbf{q} \cdot \mathbf{e}_y / q`)
    - :math:`-`
  * - :sidskey:`VelocityUnitVectorZ`
    - z-component of velocity unit vector (:math:`\mathbf{q} \cdot \mathbf{e}_z / q`)
    - :math:`-`
  * - 
    -
    -
  * - :sidskey:`MassFlow`
    - Mass flow normal to a plane (:math:`\rho \mathbf{q} \cdot \mathbf{n}`)
    - :math:`M/(L^{2}T)`
  * - 
    -
    -
  * - :sidskey:`ViscosityKinematic`
    - Kinematic viscosity (:math:`\nu = \mu/\rho`)
    - :math:`L^{2}/T`
  * - :sidskey:`ViscosityMolecular`
    - Molecular viscosity (:math:`\mu`)
    - :math:`M/(LT)`
  * - :sidskey:`ViscosityEddyKinematic`
    - Kinematic eddy viscosity (:math:`\nu_t`)
    - :math:`L^{2}/T`
  * - :sidskey:`ViscosityEddy`
    - Eddy viscosity (:math:`\mu_t`)
    - :math:`M/(LT)`
  * - :sidskey:`ThermalConductivity`
    - Thermal conductivity coefficient (:math:`k`)
    - :math:`ML/(T^{3}\Theta)`
  * -  
    -
    -
  * - :sidskey:`PowerLawExponent`
    - Power-law exponent (:math:`n`) in molecular viscosity or thermal conductivity model
    - :math:`-`
  * - :sidskey:`SutherlandLawConstant`
    - Sutherland's Law constant (:math:`T_{s}`) in molecular viscosity or thermal conductivity model
    - :math:`\Theta`
  * - :sidskey:`TemperatureReference`
    - Reference temperature (:math:`T_{ref}`) in molecular viscosity or thermal conductivity model
    - :math:`\Theta`
  * - :sidskey:`ViscosityMolecularReference`
    - Reference viscosity (:math:`\mu_{ref}`) in molecular viscosity model
    - :math:`M/(LT)`
  * - :sidskey:`ThermalConductivityReference`
    - Reference thermal conductivity (:math:`k_{ref}`) in thermal conductivity model
    - :math:`ML/(T^{3}\Theta)`
  * - 
    -
    -
  * - :sidskey:`IdealGasConstant`
    - Ideal gas constant (:math:`R = c_p − c_v`)
    - :math:`L^{2}/(T^{2}\Theta)`
  * - :sidskey:`SpecificHeatPressure`
    - Specific heat at constant pressure (:math:`c_p`)
    - :math:`L^{2}/(T^{2}\Theta)`
  * - :sidskey:`SpecificHeatVolume`
    - Specific heat at constant volume (:math:`c_v`)
    - :math:`L^{2}/(T^{2}\Theta)`
  * - 
    -
    -
  * - :sidskey:`ReynoldsStressXX`
    - Reynolds stress :math:`−\rho (u′u′)_{ave}`
    - :math:`M/(LT^{2})`
  * - :sidskey:`ReynoldsStressXY`
    - Reynolds stress :math:`−\rho (u′v′)_{ave}`
    - :math:`M/(LT^{2})`
  * - :sidskey:`ReynoldsStressXZ`
    - Reynolds stress :math:`−\rho (u′w′)_{ave}`
    - :math:`M/(LT^{2})`
  * - :sidskey:`ReynoldsStressYY`
    - Reynolds stress :math:`−\rho (v′v′)_{ave}`
    - :math:`M/(LT^{2})`
  * - :sidskey:`ReynoldsStressYZ`
    - Reynolds stress :math:`−\rho (v′w′)_{ave}`
    - :math:`M/(LT^{2})`
  * - :sidskey:`ReynoldsStressZZ`
    - Reynolds stress :math:`−\rho (w′w′)_{ave}`
    - :math:`M/(LT^{2})`
  * -
    -
    -
  * - :sidskey:`MolecularWeightSymbol`
    - Molecular weight for species *Symbol*
    - :math:`-`
  * - :sidskey:`HeatOfFormationSymbol`
    - Heat of formation per unit mass for species *Symbol*
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`FuelAirRatio`
    - Fuel/air mass ratio
    - :math:`-`
  * - :sidskey:`ReferenceTemperatureHOF`
    - Reference temperature for the heat of formation
    - :math:`\Theta`
  * - :sidskey:`MassFractionSymbol`
    - Mass of species *Symbol*, divided by total mass
    - :math:`-`
  * - :sidskey:`LaminarViscositySymbol`
    - Laminar viscosity of species *Symbol*
    - :math:`M/(LT)`
  * - :sidskey:`ThermalConductivitySymbol`
    - Thermal conductivity of species *Symbol*
    - :math:`ML/(T^{3}\Theta)`
  * - :sidskey:`EnthalpyEnergyRatio`
    - The ratio :math:`\beta = h / e = \int_{T_{ref}}^{T} c_{p} dT / \int_{T_{ref}}^{T} c_{v} dT` for the mixture
    - :math:`-`
  * - :sidskey:`CompressibilityFactor`
    - The gas constant of the mixture divided by the freestream gas constant, :math:`Z = R / R_{\infty}`
    - :math:`-`
  * - :sidskey:`VibrationalElectronEnergy`
    - Vibrational-electronic excitation energy per unit mass
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`HeatOfFormation`
    - Heat of formation per unit mass for the entire mixture, :math:`H = \sum_{i=1}^{n} Y_i H_i`, where :math:`n` is the number of species, :math:`Y_i` is the mass fraction of species :math:`i`, and :math:`H_i` is the heat of formation for species :math:`i` at the reference temperature :sidskey:`ReferenceTemperatureHOF`. This requires that :sidskey:`ReferenceTemperatureHOF` be specified using the :sidskey:`ChemicalKineticsModel` data structure.
    - :math:`L^{2}/T^{2}`
  * - :sidskey:`VibrationalElectronTemperature`
    - Vibrational electron temperature
    - :math:`\Theta`
  * - :sidskey:`SpeciesDensitySymbol`
    - Density of species *Symbol*
    - :math:`M/L^{3}`
  * - :sidskey:`MoleFractionSymbol`
    - Number of moles of species *Symbol* divided by the total number of moles for all species
    - :math:`-`
  * -
    -
    -
  * - :sidskey:`Voltage`
    - Voltage
    - :math:`ML^{2}/TI`
  * - :sidskey:`ElectricFieldX`
    - *x*-component of electric field vector
    - :math:`ML/TI`
  * - :sidskey:`ElectricFieldY`
    - *y*-component of electric field vector
    - :math:`ML/TI`
  * - :sidskey:`ElectricFieldZ`
    - *z*-component of electric field vector
    - :math:`ML/TI`
  * - :sidskey:`MagneticFieldX`
    - *x*-component of magnetic field vector
    - :math:`I/L`
  * - :sidskey:`MagneticFieldY`
    - *y*-component of magnetic field vector
    - :math:`I/L`
  * - :sidskey:`MagneticFieldZ`
    - *z*-component of magnetic field vector
    - :math:`I/L`
  * - :sidskey:`CurrentDensityX`
    - *x*-component of current density vector
    - :math:`I/L^{2}`
  * - :sidskey:`CurrentDensityY`
    - *y*-component of current density vector
    - :math:`I/L^{2}`
  * - :sidskey:`CurrentDensityZ`
    - *z*-component of current density vector
    - :math:`I/L^{2}`
  * - :sidskey:`ElectricConductivity`
    - Electrical conductivity
    - :math:`ML/T^{3}I^{2}`
  * - :sidskey:`LorentzForceX`
    - *x*-component of Lorentz force vector
    - :math:`ML/T^{2}`
  * - :sidskey:`LorentzForceY`
    - *y*-component of Lorentz force vector
    - :math:`ML/T^{2}`
  * - :sidskey:`LorentzForceZ`
    - *z*-component of Lorentz force vector
    - :math:`ML/T^{2}`
  * - :sidskey:`JouleHeating`
    - Joule heating
    - :math:`ML^{2}/T^{2}`
  * - 
    -
    -
  * - :sidskey:`LengthReference`
    - Reference length :math:`L`
    - :math:`L`
  

A3 Turbulence Model Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists data-name identifiers for typical Reynolds-averaged Navier-Stokes turbulence model variables. Turbulence model solution quantities and model constants present a particularly difficult nomenclature problem - to be precise we need to identify both the variable and the model (and version) that it comes from. The list in the following table falls short in this respect.

.. table:: **Data-Name Identifiers for Typical Turbulence Models**

  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |Data-Name Identifier                  | Description                                                    | Units                |
  +======================================+================================================================+======================+
  |:sidskey:`TurbulentDistance`          | Distance to nearest wall                                       | :math:`L`            |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |                                                                                                                              |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |:sidskey:`TurbulentEnergyKinetic`     | :math:`k = [(u′u′)_{ave} + (v′v′)_{ave} + (w′w′)_{ave}] / 2`   | :math:`L^{2}/T^{2}`  |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |:sidskey:`TurbulentDissipation`       | :math:`\epsilon`                                               | :math:`L^{2}/T^{3}`  |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |:sidskey:`TurbulentDissipationRate`   | :math:`\epsilon/k = \omega`                                    | :math:`T^{−1}`       |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |                                                                                                                              |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |:sidskey:`TurbulentBBReynolds`        | Baldwin-Barth one-equation model :math:`R_T`                   | :math:`-`            |
  +--------------------------------------+----------------------------------------------------------------+----------------------+
  |:sidskey:`TurbulentSANuTilde`         | Spalart-Allmaras one-equation model :math:`\nu_{SA}`           | :math:`L^{2}/T`      |
  +--------------------------------------+----------------------------------------------------------------+----------------------+


A4 Nondimensional Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CFD codes are rich in nondimensional governing parameters, such as Mach number and Reynolds number, and nondimensional flowfield coefficients, such as pressure coefficient.
The problem with these parameters is that the definitions and conditions at which they are evaluated can vary from code to code.
Reynolds number is particularly notorious in this respect.

These parameters have posed a difficult dilemma for us. Either we impose a rigid definition for each and force all database users to abide by it, or we develop some methodology for describing the particular definition that the user is employing.
The first limits applicability and flexibility, and the second adds complexity.
We have opted for the second approach, but we include only enough information about the definition of each parameter to allow for conversion operations.
For example, the Reynolds number includes velocity, length, and kinematic viscosity scales in its definition (i.e., :math:`Re = VLR/\nu`).
The database description of Reynolds number includes these different scales. By providing these "definition components", any code that reads Reynolds number from the database can transform its value to an appropriate internal definition. These definition components are identified by appending a "_" to the data-name identifier of the parameter.

Definitions for nondimensional flowfield coefficients follow: the pressure coefficient is defined as,

.. math::
  
  c_p = (p − p_{ref}) / (\rho_{ref} q^{2}_{ref} / 2)

where :math:`\rho_{ref}q^{2}_{ref} / 2` is the dynamic pressure evaluated at some reference condition, and :math:`p_{ref}` is some reference pressure.
The skin friction coefficient is,

.. math::

  \mathbf{c_f} = \mathbf{\tau} / (\rho_{ref} q^{2}_{ref} / 2)

where :math:`\mathbf{\tau}` is the shear stress or skin friction vector. Usually, :math:`\mathbf{\tau}` is evaluated at the wall surface.

The data-name identifiers defined for nondimensional governing parameters and flowfield coefficients are listed in the following table.

.. table:: **Data-Name Identifiers for Nondimensional Parameters**

  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |Data-Name Identifier                    | Description                                                  | Units                         |
  +========================================+==============================================================+===============================+
  |:sidskey:`Mach`                         | Mach number: :math:`M = q/c`                                 | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Mach_Velocity`                | Velocity scale (:math:`q`)                                   | :math:`L/T`                   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Mach_VelocitySound`           | Speed of sound scale (:math:`c`)                             | :math:`L/T`                   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`RotatingMach`                 | Mach number relative to rotating frame: :math:`M_r = q_r /c` | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  | \                                                                                                                                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Reynolds`                     | Reynolds number: :math:`Re = VL_{R}/\nu`                     | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Reynolds_Velocity`            | Velocity scale (:math:`V`)                                   | :math:`L/T`                   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Reynolds_Length`              | Length scale (:math:`L_R`)                                   | :math:`L`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Reynolds_ViscosityKinematic`  | Kinematic viscosity scale (:math:`\nu`)                      | :math:`L^{2}/T`               |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  | \                                                                                                                                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+ 
  |:sidskey:`Prandtl`                      | Prandtl number: :math:`Pr = \mu c_p/k`                       | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Prandtl_ThermalConductivity`  | Thermal conductivity scale (:math:`k`)                       | :math:`ML/(T^{3}\Theta)`      |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Prandtl_ViscosityMolecular`   | Molecular viscosity scale (:math:`\mu`)                      | :math:`M/(LT)`                |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Prandtl_SpecificHeatPressure` | Specific heat scale (:math:`c_p`)                            | :math:`L^{2}/(T^{2}\Theta)`   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`PrandtlTurbulent`             | Turbulent Prandtl number, :math:`\rho \nu_t c_p/k_t`         | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  | \                                                                                                                                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`SpecificHeatRatio`            | Specific heat ratio: :math:`\gamma = c_p/c_v`                | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`SpecificHeatRatio_Pressure`   | Specific heat at constant pressure (:math:`c_p`)             | :math:`L^{2}/(T^{2}\Theta)`   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`SpecificHeatRatio_Volume`     | Specific heat at constant volume (:math:`c_v`)               | :math:`L^{2}/(T^{2}\Theta)`   |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  | \                                                                                                                                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+ 
  |:sidskey:`CoefPressure`                 | :math:`c_p`                                                  | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`CoefSkinFrictionX`            | :math:`\mathbf{c_f} \cdot \mathbf{e}_x`                      | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`CoefSkinFrictionY`            | :math:`\mathbf{c_f} \cdot \mathbf{e}_y`                      | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`CoefSkinFrictionZ`            | :math:`\mathbf{c_f} \cdot \mathbf{e}_z`                      | :math:`-`                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  | \                                                                                                                                     |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+ 
  |:sidskey:`Coef_PressureDynamic`         | :math:`\rho_{ref} q^{2}_{ref} / 2`                           | :math:`M/(LT^{2})`            |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+
  |:sidskey:`Coef_PressureReference`       | :math:`p_{ref}`                                              | :math:`M/(LT^{2})`            |
  +----------------------------------------+--------------------------------------------------------------+-------------------------------+


A5 Characteristics and Riemann Invariants Based on 1D flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Boundary condition specification for inflow/outflow or farfield boundaries often involves Riemann invariants or characteristics of the linearized inviscid flow equations. For an ideal compressible gas, these are typically defined as follows: Riemann invariants for an isentropic 1-D flow are,

.. math::

  [\partial/\partial t + (u \pm c) \partial/\partial x] [u \pm 2c / (\gamma − 1)] = 0

Characteristic variables for the 3-D Euler equations linearized about a constant mean flow are,

.. math::

  [\partial /\partial t + \Delta_{n} \partial/\partial x] W′_{n}(x,t) = 0  \;\;\;\;\;\; n = 1, 2, ..., 5

where the characteristics and corresponding characteristic variables are

.. table::
  :widths: 50 25 25

  =================   =========================   =========================
   Characteristic      :math:`\Delta_n`            :math:`W'_n`
  =================   =========================   =========================
   Entropy             :math:`u`                   :math:`p′ − \rho′c^{2}`
   Vorticity           :math:`u`                   :math:`v′`
   Vorticity           :math:`u`                   :math:`w′`
   Acoustic            :math:`u \pm c`             :math:`p′ \pm u′ \rho c`
  =================   =========================   =========================

Primed quantities are linearized perturbations, and the remainder are evaluated at the mean flow.
The only non-zero mean-flow velocity component is :math:`u`.
The data-name identifiers defined for Riemann invariants and characteristic variables are listed in the following table.

.. table:: **Data-Name Identifiers for Characteristics and Riemann Invariants**

  +---------------------------------------+-----------------------------------+----------------------+
  |Data-Name Identifier                   | Description                       | Units                |
  +=======================================+===================================+======================+
  |:sidskey:`RiemannInvariantPlus`        | :math:`u + 2c / (\gamma − 1)`     | :math:`L/T`          |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`RiemannInvariantMinus`       | :math:`u − 2c / (\gamma − 1)`     | :math:`L/T`          |
  +---------------------------------------+-----------------------------------+----------------------+
  | \                                                                                                |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`CharacteristicEntropy`       | :math:`p′ − \rho′ c^{2}`          | :math:`M/(L T^{2})`  |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`CharacteristicVorticity1`    | :math:`v′`                        | :math:`L/T`          |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`CharacteristicVorticity2`    | :math:`w′`                        | :math:`L/T`          |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`CharacteristicAcousticPlus`  | :math:`p′ + u′\rho c`             | :math:`M/(L T^{2})`  |
  +---------------------------------------+-----------------------------------+----------------------+
  |:sidskey:`CharacteristicAcousticMinus` | :math:`p′ − u′\rho c`             | :math:`M/(L T^{2})`  |
  +---------------------------------------+-----------------------------------+----------------------+


A6 Forces and Moments
^^^^^^^^^^^^^^^^^^^^^

Conventions for data-name identifiers for forces and moments are defined in this section. Ideally, forces and moments should be attached to geometric components or less ideally to surface grids. Currently, the standard mechanism for storing forces and moments is generally through the :sidsref:`ConvergenceHistory_t` node, either attached to the entire configuration (under :sidsref:`CGNSBase_t`) or attached to a zone (under :sidsref:`Zone_t`).

Given a differential force :math:`f` (i.e., a force per unit area), the force integrated over a surface is,

.. math::

  \mathbf{F} = F_x \mathbf{e}_x + F_y \mathbf{e}_y + F_z \mathbf{e}_z = \int f dA

where :math:`\mathbf{e}_x`, :math:`\mathbf{e}_y` and :math:`\mathbf{e}_z` are the unit vectors in the *x*, *y* and *z* directions, respectively.
The moment about a point :math:`r_{0}` integrated over a surface is,

.. math::

  \mathbf{M} = M_x \mathbf{e}_x + M_y \mathbf{e}_y + M_z \mathbf{e}_z = \int (\mathbf{r} − \mathbf{r}_{0}) \times f dA

Lift and drag components of the integrated force are,

.. math::
    
    L = \mathbf{F} \cdot \mathbf{L}  \;\;\;\;\;\;    D = \mathbf{F} \cdot \mathbf{D}

where :math:`\mathbf{L}` and :math:`\mathbf{D}` are the unit vectors in the positive lift and drag directions, respectively.

Lift, drag and moment are often computed in auxiliary coordinate frames (e.g., wind axes or stability axes).
We introduce the convention that lift, drag and moment are computed in the :math:`(\xi, \eta, \zeta)` coordinate system.
Positive drag is assumed parallel to the :math:`\xi`-direction (i.e., :math:`\mathbf{D} = \mathbf{e}_\xi`); and positive lift is assumed parallel to the :math:`\eta`-direction (i.e., :math:`\mathbf{L} = \mathbf{e}_\eta`).
Thus, forces and moments defined in this auxiliary coordinate system are,

.. math::

  L = \mathbf{F} \cdot \mathbf{e}_{\eta} \;\;\;\;\;\;\; D = \mathbf{F} \cdot \mathbf{e}_\xi
  \\
  \mathbf{M} = M_\xi \mathbf{e}_\xi + M_\eta \mathbf{e}_\eta + M_\zeta \mathbf{e}_\zeta = \int (\mathbf{r} − \mathbf{r}_0) \times f dA

Lift, drag and moment coefficients in 3-D are defined as,

.. math::

  C_{L} = L / (\rho_{ref}q^{2}_{ref}S_{ref} / 2) \;\;\;\;\;\;  C_{D} = D / (\rho_{ref}q^{2}_{ref}S_{ref} / 2)  \;\;\;\;\;\; \mathbf{C_{M}} = \mathbf{M} / (\rho_{ref}q^{2}_{ref}c_{ref}S{ref} / 2)

where :math:`\rho_{ref}q^{2}_{ref} / 2` is a reference dynamic pressure, :math:`S_{ref}` is a reference area, and :math:`c_{ref}` is a reference length.
For a wing, :math:`S_{ref}` is typically the wing area and :math:`c_{ref}` is the mean aerodynamic chord.
In 2-D, the sectional force coefficients are,

.. math::

  c_{l} = L′ / (\rho_{ref}q^{2}_{ref}c_{ref} / 2)  \;\;\;\;\;\;  c_{d} = D′ / (\rho_{ref}q^{2}_{ref}c_{ref} / 2)  \;\;\;\;\;\;  \mathbf{c_m} = \mathbf{M'} / (\rho_{ref}q^{2}_{ref} c^{2}_{ref} / 2)

where the forces are integrated along a contour (e.g., an airfoil cross-section) rather than a surface.

The data-name identifiers and definitions provided for forces and moments and their associated coefficients are listed in the table below. For coefficients, the dynamic pressure and length scales used in the normalization are provided.

.. table:: **Data-Name Identifiers for Forces and Moments**
  :widths: 40 30 20

  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |Data-Name Identifier            |Description                                                                                    | Units              |
  +================================+===============================================================================================+====================+
  |:sidskey:`ForceX`               |:math:`F_x = \mathbf{F} \cdot \mathbf{e}_x`                                                    |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ForceY`               |:math:`F_y = \mathbf{F} \cdot \mathbf{e}_y`                                                    |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ForceZ`               |:math:`F_z = \mathbf{F} \cdot \mathbf{e}_z`                                                    |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ForceR`               |:math:`F_r = \mathbf{F} \cdot \mathbf{e}_r`                                                    |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ForceTheta`           |:math:`F_\theta = \mathbf{F} \cdot \mathbf{e}_\theta`                                          |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ForcePhi`             |:math:`F_\phi = \mathbf{F} \cdot \mathbf{e}_\phi`                                              |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  | \                                                                                                                                                   | 
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Lift`                 |:math:`L` or :math:`L'`                                                                        |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Drag`                 |:math:`D` or :math:`D'`                                                                        |:math:`ML/T^{2}`    |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentX`              |:math:`M_x = \mathbf{M} \cdot \mathbf{e}_x`                                                    |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentY`              |:math:`M_y = \mathbf{M} \cdot \mathbf{e}_y`                                                    |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentZ`              |:math:`M_z = \mathbf{M} \cdot \mathbf{e}_z`                                                    |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentR`              |:math:`M_r = \mathbf{M} \cdot \mathbf{e}_r`                                                    |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentTheta`          |:math:`M_\theta = \mathbf{M} \cdot \mathbf{e}_\theta`                                          |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentPhi`            |:math:`M_\phi = \mathbf{M} \cdot \mathbf{e}_\phi`                                              |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentXi`             |:math:`M_\xi = \mathbf{M} \cdot \mathbf{e}_\xi`                                                |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentEta`            |:math:`M_\eta = \mathbf{M} \cdot \mathbf{e}_\eta`                                              |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`MomentZeta`           |:math:`M_\zeta = \mathbf{M} \cdot \mathbf{e}_\zeta`                                            |:math:`ML^{2}/T^{2}`|
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  | \                                                                                                                                                   | 
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Moment_CenterX`       |:math:`x_0 = \mathbf{r}_0 \cdot \mathbf{e}_x`                                                  |:math:`L`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Moment_CenterY`       |:math:`y_0 = \mathbf{r}_0 \cdot \mathbf{e}_y`                                                  |:math:`L`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Moment_CenterZ`       |:math:`z_0 = \mathbf{r}_0 \cdot \mathbf{e}_z`                                                  |:math:`L`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  | \                                                                                                                                                   | 
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+ 
  |:sidskey:`CoefLift`             |:math:`C_L` or :math:`c_l`                                                                     |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefDrag`             |:math:`C_D` or :math:`c_d`                                                                     |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentX`          |:math:`\mathbf{C_M} \cdot \mathbf{e}_x` or :math:`\mathbf{c_m} \cdot e_x`                      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentY`          |:math:`\mathbf{C_M} \cdot \mathbf{e}_y` or :math:`\mathbf{c_m} \cdot e_y`                      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentZ`          |:math:`\mathbf{C_M} \cdot \mathbf{e}_z` or :math:`\mathbf{c_m} \cdot e_z`                      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentR`          |:math:`\mathbf{C_M} \cdot \mathbf{e}_r` or :math:`\mathbf{c_m} \cdot e_r`                      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentTheta`      |:math:`\mathbf{C_M} \cdot \mathbf{e}_\theta` or :math:`\mathbf{c_m} \cdot \mathbf{e}_\theta`   |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentPhi`        |:math:`\mathbf{C_M} \cdot \mathbf{e}_\phi`  or :math:`\mathbf{c_m} \cdot \mathbf{e}_\phi`      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentXi`         |:math:`\mathbf{C_M} \cdot \mathbf{e}_\xi`   or :math:`\mathbf{c_m} \cdot \mathbf{e}_\xi`       |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentEta`        |:math:`\mathbf{C_M} \cdot \mathbf{e}_\eta`  or :math:`\mathbf{c_m} \cdot \mathbf{e}_\eta`      |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`CoefMomentZeta`       |:math:`\mathbf{C_M} \cdot \mathbf{e}_\zeta` or :math:`\mathbf{c_m} \cdot \mathbf{e}_\zeta`     |:math:`-`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  | \                                                                                                                                                   | 
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+ 
  |:sidskey:`Coef_PressureDynamic` |:math:`\rho_{ref} q^{2}_{ref} / 2`                                                             |:math:`M/(LT^{2})`  |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Coef_Area`            |:math:`S_{ref}`                                                                                |:math:`L^{2}`       |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`Coef_Length`          |:math:`c_{ref}`                                                                                |:math:`L`           |
  +--------------------------------+-----------------------------------------------------------------------------------------------+--------------------+

A7 Time-Dependant flows
^^^^^^^^^^^^^^^^^^^^^^^

Data-name identifiers related to time-dependent flow include those associated with the storage of grid coordinates and flow solutions as a function of time level or iteration. Also included are identifiers for storing information defining both rigid and arbitrary (i.e., deforming) grid motion.

.. table:: **Data-Name Identifiers for Time-Dependent Flow**

  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  | Data-Name Identifier                     |  Data Type        |  Description                                                                                     |  Units             |
  +==========================================+===================+==================================================================================================+====================+
  |                                                                                                                                                                                      |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`TimeValues`                     | :code:`real`      | Time values                                                                                      | :math:`T`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`IterationValues`                | :code:`int`       | Iteration values                                                                                 | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`NumberOfZones`                  | :code:`int`       | Number of zones used for each recorded step                                                      | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`NumberOfFamilies`               | :code:`int`       | Number of families used for each recorded step                                                   | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ZonePointers`                   | :code:`char`      | Names of zones used for each recorded step                                                       | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`FamilyPointers`                 | :code:`char`      | Names of families used for each recorded step                                                    | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |                                                                                                                                                                                      |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`RigidGridMotionPointers`        | :code:`char`      | Names of RigidGridMotion structures used for each recorded step for a zone                       | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`ArbitraryGridMotionPointers`    | :code:`char`      | Names of ArbitraryGridMotion structures used for each recorded step for a zone                   | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridCoordinatesPointers`        | :code:`char`      | Names of GridCoordinates structures used for each recorded step for a zone                       | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`FlowSolutionPointers`           | :code:`char`      | Names of FlowSolution structures used for each recorded step for a zone                          | :math:`-`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |                                                                                                                                                                                      |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`OriginLocation`                 | :code:`real`      | Physical coordinates of the origin before and after a rigid grid motion                          | :math:`L`          |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`RigidRotationAngle`             | :code:`real`      | Rotation angles about each axis of the translated coordinate system for rigid grid motion        | :math:`\alpha`     |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`RigidVelocity`                  | :code:`real`      | Grid velocity vector of the origin translation for rigid grid motion                             | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`RigidRotationRate`              | :code:`real`      | Rotation rate vector about the axis of the translated coordinate system for rigid grid motion    | :math:`\alpha /T`  |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |                                                                                                                                                                                      |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityX`                  | :code:`real`      | :math:`x`-component of grid velocity                                                             | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityY`                  | :code:`real`      | :math:`y`-component of grid velocity                                                             | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityZ`                  | :code:`real`      | :math:`z`-component of grid velocity                                                             | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityR`                  | :code:`real`      | :math:`r`-component of grid velocity                                                             | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityTheta`              | :code:`real`      | :math:`\theta`-component of grid velocity                                                        | :math:`\alpha /T`  |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityPhi`                | :code:`real`      | :math:`\phi`-component of grid velocity                                                          | :math:`\alpha /T`  |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityXi`                 | :code:`real`      | :math:`\xi`-component of grid velocity                                                           | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityEta`                | :code:`real`      | :math:`\eta`-component of grid velocity                                                          | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+
  |:sidskey:`GridVelocityZeta`               | :code:`real`      | :math:`\zeta`-component of grid velocity                                                         | :math:`L/T`        |
  +------------------------------------------+-------------------+--------------------------------------------------------------------------------------------------+--------------------+



.. last line
