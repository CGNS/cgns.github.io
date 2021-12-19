.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _SupportBuild:
   
Build CGNS code
===============

Note about HDF5
^^^^^^^^^^^^^^^

If building CGNS with an HDF5 version earlier than 1.8, then links will not work when using HDF5 file type.

When using HDF5, it is currently recommended that CGNS be compiled using the newest HDF5 release.

It is recommended to NOT link with HDF5 versions 1.10.0-patch1, 1.10.1 or 1.10.2.


Compilers
^^^^^^^^^

Users should be aware that many new features in CGNS require the use of up-to-date compilers. For example, older FORTRAN compilers that are not FORTRAN 2003 compliant (such as g77) will not work for many CGNS features, and are not recommended or supported.

| When building with PGI and gcc compilers it might be necessary to set the environment variables:
|     FLIBS="-Wl,--no-as-needed -ldl"
|     LIBS="-Wl,--no-as-needed -ldl" 




