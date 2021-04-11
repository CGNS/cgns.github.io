.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _SupportExamples:
   
Examples
========

These files are distributed as a service to help CGNS users test their own implementations.
They are submitted by users "as is" and are **not certified by anyone except the sender to be CGNS compliant**. 

If you have any questions about these data files, please contact the person listed in the table. The CGNS Committee is not able to provide technical support for the data files listed on this webpage. 

Please send any CGNS data files (along with a graphic file if possible) or the URL of the datafiles which you would like to share with the CGNS users community to: cgnstalk@lists.nasa.gov .
 
Note that most of the files on this page are very old.


Structured Grid
---------------

Constricting channel
^^^^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Marc Poinot <marc.poinot@safrangroup.com>`_
      - Jan.25.16
      - Jan.25.16

  .. image:: ../../example_cgns_files/ConstrictingChannel/constrictingchannel.png
     :width: 200px

  :Description: Structured, 12 block, 3-D constricting channel, with example use of Family_t for BCs
  :Data File (ADF): :download:`sqnz_s.adf.cgns.gz<../../example_cgns_files/ConstrictingChannel/sqnz_s.adf.cgns.gz>` (< 1Mb)
  :Data File (HDF): :download:`sqnz_s.hdf.cgns.gz<../../example_cgns_files/ConstrictingChannel/sqnz_s.hdf.cgns.gz>` (< 1Mb)


Axisymmetric bump
^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Chris Rumsey <c.l.rumsey@nasa.gov>`_
      - Apr.14.00
      - Feb.03.14

  .. image:: ../../example_cgns_files/Chris/bump.gif
     :width: 200px

  :Description: Structured, 1 block, quasi-3D axisymmetric bump (2 planes) , with cell centered solution
  :Data File (ADF): :download:`bump.cgns.gz<../../example_cgns_files/Chris/bump.cgns.gz>` (6.4Mb)
  :Data File (HDF): :download:`bump_hdf5.cgns.gz<../../example_cgns_files/Chris/bump_hdf5.cgns.gz>` (6.4Mb)

2D Multielement airfoil
^^^^^^^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Chris Rumsey <c.l.rumsey@nasa.gov>`_
      - Apr.14.00
      - Feb.03.14

  .. image:: ../../example_cgns_files/Chris/multi.gif
     :width: 200px

  :Description: Structured, 4 blocks, 2D (2 planes in third dimension) multielement airfoil, with cell centered solution
  :Data File (ADF): :download:`multi.cgns.gz<../../example_cgns_files/Chris/multi.cgns.gz>` (2.3Mb)
  :Data File (HDF): :download:`multi_hdf5.cgns.gz<../../example_cgns_files/Chris/multi_hdf5.cgns.gz>` (2.3Mb)
    

3D Delta Wing
^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Chris Rumsey <c.l.rumsey@nasa.gov>`_
      - Apr.14.00
      - Jul.24.07

  .. image:: ../../example_cgns_files/Chris/delta.gif
     :width: 200px

  :Description: Structured, 1 block, 3-D Delta Wing, with cell centered solution - see also :file:`delta_vertex.cgns.gz` with solution at vertices
  :Data File: :download:`delta.cgns.gz<../../example_cgns_files/Chris/delta.cgns.gz>` (8.1Mb)

Wing Vertex solution
^^^^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Chris Rumsey <c.l.rumsey@nasa.gov>`_
      - Jul.23.07
      - Jul.23.07

  .. image:: ../../example_cgns_files/Chris/delta.gif
     :width: 200px

  :Description: Structured, 1 block, 3-D Delta Wing, with solution at vertices - see also :file:`delta.cgns.gz` with cell-center solution
  :Data File: :download:`delta_vertex.cgns.gz<../../example_cgns_files/Chris/delta_vertex.cgns.gz>` (3.1Mb)

Overset Airfoil 1
^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Herb Schilling <hschilling@nasa.gov>`_
      - Feb.23.07
      - Feb.23.07

  .. image:: ../../example_cgns_files/Overset/oversetnasa1.gif
     :width: 200px

  :Description: Structured, 3 block, 2D (1 plane in third dimension) airfoil with combination 1-to-1 and overset connectivity, no solution included
  :Data File: :download:`oversetnasa1.cgns.gz<../../example_cgns_files/Overset/oversetnasa1.cgns.gz>` (181Kb)

Overset Airfoil 2
^^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Herb Schilling <hschilling@nasa.gov>`_
      - Feb.23.07
      - Feb.23.07

  .. image:: ../../example_cgns_files/Overset/oversetnasa2.gif
     :width: 200px

  :Description: Structured, 5 block, 2D (1 plane in third dimension) airfoil with combination 1-to-1 and overset connectivity, no solution included
  :Data File: :download:`oversetnasa2.cgns.gz<../../example_cgns_files/Overset/oversetnasa2.cgns.gz>` (191Kb)

DLR-F6 Wing body
^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Chris Rumsey <c.l.rumsey@nasa.gov>`_
      - Feb.09.07
      - Feb.09.07

  .. image:: ../../example_cgns_files/DLR-F6/dlr-f6.gif
     :width: 200px

  :Description: Structured, 26 block, DLR-F6 wing-body (includes several degenerate lines), no solution included
  :Data File: :download:`dlr-f6.coar.cgns.gz<../../example_cgns_files/DLR-F6/dlr-f6.coar.cgns.gz>` (55.5Mb)

Business Jet
^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Edwin van der Weide <Edwin.vanderWeide@standford.edu>`_
      - July.29.04
      - July.29.04

  
  :Description: Multiblock stuctured grids for a business jet, a wing/body, and a wing/body/nacelle/pylon configuration are available from Stanford.
  :Data File: `Stanford CGNS test files <http://aero-comlab.stanford.edu/vdweide/CGNSFiles/>`_ (link to external site)


Butterfly mesh
^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Diane Poirier <Diane.Poirier@ansys.com>`_
      - Apr.06.00
      - Apr.06.00

  .. image:: ../../example_cgns_files/5blocks/5blocks.gif
     :width: 200px

  :Description: 3D Multiblock Structured Mesh
  :Data File: :download:`5blocks.cgns.gz<../../example_cgns_files/5blocks/5blocks.cgns.gz>` (21Kb)


Unstructured Grid
-----------------

YF-17
^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
      - Revised by
    * - `Bruce Wedan <brucewedan@gmail.com>`_
      - Mar.17.11
      - Feb.03.14
      - `Chris Rumsey <c.l.rumsey@nasa.gov>`_

  .. image:: ../../example_cgns_files/YF-17/yf17.gif
     :width: 200px

  :Description: Unstructured mesh for YF-17 with solution with useful BCs.
  :Data File (ADF): :download:`yf17.cgns.gz<../../example_cgns_files/YF-17/yf17.cgns.gz>` (7.5Mb)
  :Data File (HDF): :download:`yf17_hdf5.cgns.gz<../../example_cgns_files/YF-17/yf17_hdf5.cgns.gz>` (7.5Mb)


Trapped Vortex
^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Marc Poinot <marc.poinot@safrangroup.com>`_
      - Feb.27.20
      -	Feb.27.20

  .. image:: ../../example_cgns_files/TrappedVtx/trappedvtx.png
     :width: 200px

  :Description: Unstructured polygonal mesh of a trapped vortex combustor configuration with Family hierarchy tree (CGNS 4.1 standard).
  :Data File: :download:`trappedvtx_ngon.cgns.gz<../../example_cgns_files/TrappedVtx/trappedvtx_ngon.cgns.gz>` (4.8Mb)

SC10 Blade
^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Andrew McGhee <cgns2007@rpmturbo.com>`_
      - Feb.07.07
      -	Feb.07.07

  .. image:: ../../example_cgns_files/SC10/SC10.gif
     :width: 200px

  :Description: 3-D hexahedral mesh for the Standard Configuration 10 blade (single blade, part of a compressor cascade), with cell centered solution.
  :Data File: :download:`SC10_steady.cgns.gz<../../example_cgns_files/SC10/SC10_steady.cgns.gz>` (34.2Mb)

Heating Coil
^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Richard Hann <Richard.Hann@ansys.com>`_
      - Jul.29.04
      -	Jul.29.04

  .. image:: ../../example_cgns_files/CFX/HeatingCoil.gif
     :width: 200px

  :Description: 2 zone unstructured mixed element mesh of a coil inside a cylinder with solution.
  :Data File: :download:`HeatingCoil.cgns.gz<../../example_cgns_files/CFX/HeatingCoil.cgns.gz>` (2.3Mb)


Static Mixer
^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Richard Hann <Richard.Hann@ansys.com>`_
      - Jul.29.04
      -	Jul.29.04

  .. image:: ../../example_cgns_files/CFX/StaticMixer.gif
     :width: 200px

  :Description: Unstructured mesh of a static mixer with solution.
  :Data File: :download:`StaticMixer.cgns.gz<../../example_cgns_files/CFX/StaticMixer.cgns.gz>` (221Kb)


Piston
^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Richard Hann <Richard.Hann@ansys.com>`_
      - Jul.29.04
      -	Jul.29.04

  .. image:: ../../example_cgns_files/CFX/MovingTransient.gif
     :width: 200px

  :Description: Moving mesh solution of a piston; 20 timesteps (not using the standard BaseIterativeData method, but rather storing each time step in a separate base).
  :Data File: :download:`MovingTransient.cgns.gz<../../example_cgns_files/CFX/MovingTransient.cgns.gz>` (849Kb)

Obstructed Elbow
^^^^^^^^^^^^^^^^

  .. list-table::
    :header-rows: 1

    * - Contact
      - Posted Date
      - Revision Date
    * - `Steve Feldman <stevef@adapco.com>`_
      - Apr.07.00
      -	Apr.07.00

  .. image:: ../../example_cgns_files/AdapcoTut21/tut21.gif
     :width: 200px

  :Description: 3D Flow of Air in Obstructed Elbow:  Unstructured mesh of MIXED element types with cell centered solution, no boundaries or boundary info included.
  :Data File: :download:`tut21.cgns.gz<../../example_cgns_files/AdapcoTut21/tut21.cgns.gz>` (61Kb)


.. last line
