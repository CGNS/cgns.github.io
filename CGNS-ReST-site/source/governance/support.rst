.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _support:
   
Support
=======

Discussion list
---------------

This is a mailman system, if you want to join you have
`to register on this page <https://lists.nasa.gov/mailman/listinfo/cgnstalk/>`_

Doc is built using :term:`Sphinx`

Doc Conventions for these CGNS web pages
----------------------------------------

.. code-block:: rest

   Top level header
   ================

   Second level
   ------------

   Third level
   ^^^^^^^^^^^

   Fourth level
   ~~~~~~~~~~~~


The index is generated, you just have to mention an index entry in the text.
For example, if you wan to add a reference to *boundary condition* in the index,
you add:

.. code-block:: rest

   :index:`Reference-state` data is useful for situations
   where :index:`boundary-condition`
   is not provided, and flow solvers are free to enforce any
   appropriate boundary condition equations. 

You note in this example we also add an index for the *reference-state*.
We have now an entry *boundary-condition* and an entry *reference-state*.

We can use a similar to add two entries at the same time. In that case you
have an entry *boundary-condition* in the index at *reference-state* and 
vice-versa.

.. code-block:: rest

   Reference-state data is useful for situations
   where :index:`index entries <pair: boundary-condition; reference-state>`
   is not provided, and flow solvers are free to enforce any
   appropriate boundary condition equations. 

.. last line
