.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _support:
   
Support
=======

.. _SupportCGNSTalk:

Discussion list
---------------

This is a mailman system, if you want to join you have
`to register on this page <https://lists.nasa.gov/mailman/listinfo/cgnstalk/>`_

Doc is built using :term:`Sphinx`

Doc Conventions for these CGNS web pages
----------------------------------------

header
^^^^^^

.. code-block:: rest

   Top level header
   ================

   Second level
   ------------

   Third level
   ^^^^^^^^^^^

   Fourth level
   ~~~~~~~~~~~~

   Fith level
   ++++++++++

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

Internal link
^^^^^^^^^^^^^

An internal link is composed of its *anchor* (the place in the web site
where you want to go to) and a *reference* (the words wich triggers
the jump to the anchor).

An *anchor* is defined with:

.. code-block:: rest

   .. _ThisIsThePlaceYouWantToJumpTo:

Note the leading underscode and the single colon. The anchor test
should be contiguous and we suggest using the camel case syntax.

The actual link is inserted with:

.. code-block:: rest

   You read this text with your eyes but you
   can also :ref:`click on to jump elsewhere <ThisIsThePlaceYouWantToJumpTo>`.

The anchor in into angular brackets, the clickable text is user defined.   

Block quote
^^^^^^^^^^^

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)


Simple Table
^^^^^^^^^^^^

.. cssclass:: table-bordered
	      
+--------+--------+-----------+
| Header | Header with 2 cols |
+========+========+===========+
| A      | Lists: | **C**     |
+--------+  - aha +-----------+
| B::    |  - yes | | a block |
|        |        |   of text |
|  *hey* |  #. hi | | a break |
+--------+--------+-----------+

Image
^^^^^

There are several ways to insert an image. 
The first example adds an
image as a new paragraph:

.. code-block:: rest

   .. image:: ../path/to/image/file.png
      :width: 200px
      :align: center
	 
The second way is to *inline* the image so that it appears in the text
without creating a new paragraph. You have to declare the image using
a label enclosed with vertical bars:

.. code-block:: rest

   .. |inline_image_label| image:: ../../path/to/image/file.png

Then you refer to thus label in the text where you want the insertion:

.. code-block:: rest

   When you read this text you have an image like |inline_image_label| without
   any break.

.. note::   

   Preferred image formats are ``.png``, ``.jpg``, ``.gif`` or even ``.svg``.

.. note::
   
   Image file path is relative to current doc directory and should refer to
   the ``images`` directory where all images are. It is sometimes a bit
   difficult to find out which is the level of directory you are into. You
   have to go back to the root directory of the doc generation, you add as
   many ``../`` as you entered directories up to your file.
   The root directory is the one where you can see ``conf.py`` or ``source``.

   For example, if you are editing ``source/standard/SIDS/convention.rst``
   an image path should have three backwards items, ``../../..`` which are
   related to ``source/standard/SIDS``.

   Your image in this file has the path: ``../../../images/sids/figs/bar_2.png``
Citation
^^^^^^^^

In the text [2]_, [1]_, [CIT2002]_.

.. [2] In the footnote.
       
.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

.. [CIT2002] Just like a footnote, except the label is
   textual.

.. _Python: http://www.python.org

.. |example| function:: module=xml.xslt class=Processor

.. _example:

The "_example" target above points to this paragraph.

Admonition
^^^^^^^^^^

A set of special blocks are called *admonitions*.

.. note::

   if you do not read the doc

.. warning::

   no way you succeed

.. last line
