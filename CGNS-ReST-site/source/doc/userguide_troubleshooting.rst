.. _DocTroubleshoot:

.. CGNS Troubleshooting

Troubleshooting
---------------

Handling Errors
^^^^^^^^^^^^^^^

The API has an extensive number of checks for errors, relating both to invalid data input as well as SIDS-noncompliance.
However, it is not guaranteed that the API will catch all problems prior to reaching the core level. Even then, additional
errors can arise due to I/O or invalid input. The list of errors that can arise in the CGIO or database manager core
routines may be found in the :ref:`CGIO User's Guide <Error Messages>`. If an error occurs, the message given by API or
core routine should hopefully be descriptive enough to point to the source of the error.

Known Problems
^^^^^^^^^^^^^^

One known problem that can occur, which is not so much a problem as it is a restriction, relates to links. If a user makes
a link from one CGNS file to another, then the linked file *must* have write permission if the user wishes to open the
linking file in ``CG_MODE_MODIFY`` or ``CG_MODE_WRITE`` mode. In other words, opening a CGNS file in 
``CG_MODE_MODIFY`` or ``CG_MODE_WRITE`` mode implies that the entire CGNS hierarchy, including links (since they are
transparent), is accessible in that mode.

.. last line
