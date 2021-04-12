.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _support:
   
Support
=======

The CGNS community can help you to understand, use and even participate
to the CGNS standard. There are various means.
As a **user** of the CGNS files and tools,
you can browse the :ref:`web resources <WebResources>`
or ask to the :ref:`CGNS mailing list <SupportCGNSTalk>`.
If you are a **developper** and you want to install the libs, the docs or
the tools you jump to Development support.

.. _SupportCGNSTalk:

Discussion list
---------------

This is a mailman system, if you want to join you have
`to register on this page <https://lists.nasa.gov/mailman/listinfo/cgnstalk/>`_

The mailing list archives are available from 2008 forward from: https://lists.nasa.gov/mailman/private/cgnstalk/ (you may need to sign up to be a member of CGNSTalk in order to view).
For convenience, they are also given below, along with older archives extending back to 2000.

:2000-2020:
  Archives	(Gzipped Text File)

<link to archives>



.. _WebResources:

Web resources
-------------

list here some web sites...


.. _SupportDev:

Development support
-------------------

Building libraries and tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CGNS libs and tools are hosted on Github, the associated documentation
can be found on `this page <http://www.github.com/CGNS/CGNS>`_.

Building the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The documentation is generated from text files. We use **Sphinx** to produce
the web pages from these text files and a set of layout templates.
The template we use for CGNS is a modified version of the **Guzzle** template.
This modified version is released with the doc sources.

First, you have to install the production libs and tools, you have to
make available:

  - Python (v3+)
  - Sphinx (v3.2+) and all its associated libs (see below)
  - guzzle sphinx theme

Jump to the glossary to get more info about :term:`Python` and :term:`Sphinx`.
The *guzzle* theme can be found in the CGNS doc sources.
You can find below an example installation of *guzzle* you have to modify 
to fit your own environment.

.. code-block:: shell

   mkdir /tmp/gz
   cp guzzle_sphinx_theme-master.zip /tmp/gz
   cd /tmp/gz
   unzip guzzle_sphinx_theme-master.zip
   cd guzzle_sphinx_theme-master/
   python setup.py build
   mkdir /tmp/gz/install
   export PYTHONPATH=/tmp/gz/install/lib/python3.7/site-packages/:$PYTHONPATH
   python setup.py install --prefix=/tmp/gz/install

Once you have installed *guzzle*,
make sure the Python .egg file is uncompressed.
For example, on a Unix platform with a *sh* shell:

.. code-block:: shell

   cd /tmp/gz/install/lib/python3.7/site-packages
   unzip guzzle_sphinx_theme-0.7.11-py3.7.egg

Second you run the `build.sh` script, it generates all the stuff and
copies a final/ usable html directory with all required files.
You can copy this directory at any place you want, the directory is
self-contained. 

The equation rendering makes a reference to an external link,
so that you may have issues with the equations if you are not connected
to the public internet.

Documentation editing
^^^^^^^^^^^^^^^^^^^^^

Doc Conventions for these CGNS web pages

header
~~~~~~

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
~~~~~~~~~~~~~

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

External link
~~~~~~~~~~~~~

For an external reference the syntax is:

.. code-block:: rest

   Info can be found on `other site web page < URL to other site page >`_.

Do not miss the trailing underscore.

Block quote
~~~~~~~~~~~

To add a quote in the text, inside a box (this is the default style 
of our template), shift the text block on the right:

.. code-block:: rest

   Generating documentation from source code is possible.

      But code does not explain by itself

      -- C compiler (stdout)

Generating documentation from source code is possible.

   But code does not explain by itself

   -- C compiler (stdout)

Simple Table
~~~~~~~~~~~~

.. cssclass:: table-bordered
	      
+--------+--------+-----------+
| Header | Header with 2 cols |
+========+========+===========+
| CFD    | Data : | **TURB**  |
+--------+  - cfl +-----------+
| CSM::  |  - rms | | K       |
|        |        |   Epsilon |
|  *v1a* |  #. a  | | Spalart |
|  *v2a* |  #. b  | | K-l     |
+--------+--------+-----------+

Admonition
~~~~~~~~~~

A set of special blocks are called *admonitions*. These includes notes,
warnings... their layout, again, is set by the style we use.

.. code-block:: rest

   .. note::

      if you do not read the doc

   .. warning::

      no way you succeed

   .. tip::

      start from first page

.. note::

   if you do not read the doc

.. warning::

   no way you succeed

.. tip::

   start from first page

Image
~~~~~

There are several ways to insert an image. 
The first example adds an image as a new paragraph:

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
~~~~~~~~

Inserting footnotes, citation or any reference can be defined in
several ways:

.. code-block:: rest

   In the text you can add references such as [2]_, [1]_, [CIT2002]_.

   .. [2] In the footnote.
          
   .. [1] A footnote contains body elements, consistently
      indented by at least 3 spaces.

   .. [CIT2002] Just like a footnote, except the label is
      textual.

In the text you can add references such as [2]_, [1]_, [CIT2002]_.

.. [2] In the footnote.
       
.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

.. [CIT2002] Just like a footnote, except the label is
   textual.

.. _CPEXguidelines:

CPEX guidelines
^^^^^^^^^^^^^^^

The CPEX process requires multiple docs.

The CPEX should include the following information:

  - Name(s) and organization(s) of proposer(s)
  - E-mail contact information
  - General description of extension
  - Reason or need for extension
  - A SIDS detailed description of extension using similar documentation style found in the SIDS
  - File Mapping description of Node Attributes, following the prescription given in existing `Node Description Documentation <FMMNodeDescriptions>`
  - Specific example(s) of extension



.. last line
