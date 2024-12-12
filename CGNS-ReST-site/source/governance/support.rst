.. CGNS Documentation files
   See LICENSING/COPYRIGHT at root dir of this documentation sources

.. _support:
   
Support
=======

The CGNS community can help you to understand, use and even participate
to the CGNS standard. There are various means.
As a **user** of the CGNS files and tools,
you can 
ask questions to the :ref:`CGNS Discussion Forum <SupportDiscussionForum>` or
browse the :ref:`web resources <WebResources>`.
If you are a **developer** and you want to install the libs, the docs or
the tools you jump to Development support.

.. _SupportDiscussionForum:

Discussion Forum
----------------

The discussion forum is available on GitHub.com.  You must have an account.
Notifications of new posts are controlled by setting the proper watch notifications for the CGNS/CGNS repository. 

Prior to 2020, there was a CGNSTalk mailing list (connected to NASA) that has since been discontinued.
The CGNSTalk mailing list archives [:download:`GZIPPED TXT FILE<../../cgnstalk_archives/2000-2020.txt.gz>`] are available from 2000 to 2020.

.. _WebResources:

Web resources
-------------

None listed yet.


.. _SupportDev:

Development support
-------------------

Building libraries and tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CGNS libs and tools are hosted on Github; the associated documentation
can be found on `this page <http://www.github.com/CGNS/CGNS>`_.

Building the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The documentation is generated from files found
in `this <https://github.com/CGNS/cgns-modern.github.io>`_ repository. We use
**Sphinx** to produce the web pages from these files.
Additionally, Doxygen and Breathe generate the MLL API documentation from the CGNS
source code. The documentation website should be cloned with the CGNS source submodule
in orrder to generate the Doxygen documentation by using:

.. code-block:: shell

   $ git clone --recurse-submodules https://github.com/CGNS/cgns-modern.github.io.git

The theme we use for CGNS is a custom version of the **Sphinx Book Theme**.
The modifications include specific changes made to the theme, such as color schemes,
layout adjustments, and additional features and is controlled by files in the *_static*
directory.

**STEP 0**
++++++++++++++++++++++++++++++

You have to install the required libs and tools, so you have to
make available:

  - Python (v3+)
  - Sphinx (v3.2+) and all its associated libs (see below)
  - Doxygen (v1.11.0+)
  - Breathe (v4.35.0+)
  - book sphinx theme

To check your configuration, 
open an Unix shell, for example **bash** and run the commands
(do not type the `$` sign which is supposed to be the shell prompt:

.. code-block:: shell

   $ python
   Python 3.9.1 (default, Feb  8 2021, 12:46:16) 
   [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 

If the python version is not 3.x.y or if you do not have python, you
have to install it. On some systems, you would have to type `python3`
to run python instead of only `python` without version number.

Once python 3.x.y is there, go to **STEP 1**.

.. warning::

  Now your python version is 3.x.y and you have to use the **3.x**
  version in all path we mention in next steps. The example are using **3.7**
  and you **should** change these path with your own **3.x** to make it
  work properly.

**STEP 1**
++++++++++++++++++++++++++++++

Using the shell command:

.. code-block:: shell

  $ pip list

verify the following packages are installed:

- Sphinx
- breathe
- sphinx-book-theme

If they are not, then you can install them using the shell command:

.. code-block:: shell

   $ pip install sphinx
   $ pip install sphinx-book-theme
   $ pip install breathe

You may have to install the python packages that they may depend on, in addition to Doxygen.

**STEP 2**
++++++++++++++++++++++++++++++

Congrats! you are now ready to contribute to the CGNS documentation.
We retrieve the last version from the *git* repository.
Go to the directory where you want to produce the documentation,
say for example: ``/my/own/local/doc/directory``

.. code-block:: shell

   cd /my/own/local/doc/directory
   git clone --recurse-submodules https://github.com/CGNS/cgns-modern.github.io.git

.. note::

   You need to have **git** to get the actual documentation source tree.
   We cannot detail here how to install git or how to allow it to access to
   the CGNS repository. If you really are lost, please use CGNS discussion forum.

**STEP 3**
++++++++++++++++++++++++++++++

Everything is ready now, once you are in ``/my/own/local/doc/directory`` 
all sources are in::

  CGNS-ReST-site/
  
Most of the files to be created/edited are **rst** files located in and below CGNS-ReST-site/source/

To produce the documentation, you run::

  cd CGNS-ReST-site
  make html

All doc is generated into CGNS-ReSt-site::

  docs/_build/html/

To check the produced documentation, you open a web browser (*chrome*, 
*firefox*, whatever...) and you open the top page which is ``index.html``
(in this example we are still in the  ``CGNS-ReST-site``)::

  firefox docs/_build/html/index.html

Second you run *make html*, it generates all the stuff and
copies a final/ usable html directory with all required files.
You can copy this directory at any place you want, the directory is
self-contained. 

The equation rendering makes a reference to an external link,
so that you may have issues with the equations if you are not connected
to the public internet.

**STEP 4**
++++++++++++++++++++++++++++++

Now you open your favorite text editor. You follow the documentation
editing recommendations described hereafter and you loop on steps 3 and 4.

**STEP 5**
++++++++++++++++++++++++++++++

You are done with your editing. You commit your changes with a nice
comment and you push it to the repository:

.. code-block:: console

   git add -A
   git commit -m 'update section 4.2.1'
   git push

.. note::

   If some modifications have been applied since you where editing, you have to
   perform a merge by yourself after a ``git pull``

Documentation editing
^^^^^^^^^^^^^^^^^^^^^^

Documenation conventions for these CGNS web pages are as follows:

.. code-block:: rst

  Top level header -- Equal Sign
  =================================

  Second level -- Hyphen
  ---------------------------------
   
  Third level -- Circumflex
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Fourth level -- Tilde
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Fifth level -- Plus Sign
  ++++++++++++++++++++++++++++++

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An internal link is composed of its *anchor* (the place in the web site
where you want to go to) and a *reference* (the words which triggers
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an external reference the syntax is:

.. code-block:: rest

   Info can be found on `other site web page < URL to other site page >`_.

Do not miss the trailing underscore.

Block quote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
---------------------

The CPEX process requires multiple docs.

The CPEX should include the following information:

  - Name(s) and organization(s) of proposer(s)
  - E-mail contact information
  - General description of extension
  - Reason or need for extension
  - A SIDS detailed description of extension using similar documentation style found in the SIDS
  - File Mapping description of Node Attributes, following the prescription given in existing :ref:`Node Description Documentation <FMMNodeDescriptions>`
  - Specific example(s) of extension

.. last line
