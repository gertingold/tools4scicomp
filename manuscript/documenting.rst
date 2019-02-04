.. _documenting:

*********************
Documentation of code
*********************

Besides writing code and testing it, documenting the code is also an important
task which should not be neglected. In Python, it is a good habit to provide
each function or method with a docstring which might even contain doctests as we
have discussed in :numref:`doctests`. For more complex programs, modules or even
packages, it will not be sufficient to limit the documentation to the doctests.
This chapter will be devoted to the discussion of the documentation tool
*Sphinx* which is commonly employed to document Python project but which can 
be used also to document projects written in other programming languages. Even
the present lecture notes are making use of *Sphinx*.

*Sphinx* is based on the markup language *reStructuredText*. Due to its
unobtrusive syntax the original text can easily be read. At the same time,
the markup is powerful enough to produce nicely laid out output in different
formats, in particular in HTML and LaTeX. The latter can directly be used to
produce the documentation in PDF format.

The value of *Sphinx* for the documentation of software projects relies to a
large extent on its capability to make use of docstrings for inclusion in the
documentation. *Sphinx* thus provides another good reason to supply functions
and methods with docstrings.

In the following, we will first give an introduction to the markup language
*reStructuredText* and then explain some of the more important aspects of how
*Sphinx* can be used to document code. For further information, we refer to
the documentation of *reStructuredText* [#docreST]_ and *Sphinx* [#docSphinx]_.


Markup with reStructuredText
============================

Markup languages are used to annotate text for electronic text processing, for
example in order to specify its meaning. A text could be marked as representing
a section title and a computer program could then represent it accordingly, e.g.
as larger text set in boldface. A widespread markup language is the HyperText
Markup Language HTML used for markup of webpages. A pair of tags ``<LI>`` and
``</LI>`` would indicate in HTML that the enclosed text represents an item in
a list. An example of a markup language commonly found in a scientific context
is LaTeX. Here, ``x`` and ``$x$`` will be typeset differently because the dollar
signs in the second case indicate that the character ``x`` is meant to be a
mathematical variable which usually is typeset in an italic font.

The markup in HTML and LaTeX helps computer programs to interpret the meaning
of the text and to represent it correctly. However, text written in these markup
languages often lacks a good human readability. This is particularly true for the
very flexible extensible markup language XML.

On the other hand, there exist so-called lightweight markup languages like
reStructuredText or Markdown where the latter may come in different variants.
These markup languages are designed in such a way that the meaning of the markup
appears rather natural to a human reader. From the following example written in
reStructuredText

.. code-block:: none

   Markup of lists
   ===============

   The following is a bullet-point list:

   * first item
   * second item

it is pretty clear that the first two lines represent a header title and the
last two lines represent a list. Due to the simplicity of its markup, Markdown
or one of its variants is commonly used in Wikis. Both, texts written in
Markdown or in reStructuredText are frequently used for documentation files in
software projects like README.md or README.rst, respectively, which usually
specify the purpose of the software and give further useful information. In
version control systems like Gitlab, they can be represented in a nice form
in the browser.

The documentation generator *Sphinx* is based on reStructuredText. Therefore, we
will now discuss some of the more important aspects of this markup language.

Within a text, parts can be emphasized or even strongly emphasized by enclosing
them in one or two stars, respectively. Inline literals are enclosed in a pairs
of back-quotes. It is important that these constructs should be delimited by 
characters which could also be used otherwise to delimit words like a whitespace
or a punctuation character. If a whitespace is used but should not appear in the
output, it needs to be escaped by means of a backslash. The text to which the
markup is applied may not start or end with a whitespace. The following example
provides an illustration. ::

   Text can be *emphasized*, usually as italics, or even **strongly emphasized**,
   usually as boldface. It is also possible to insert ``inline literals`` which
   will usually be represented as monospaced text.

   This is another paragraph showing how to embed an inline literal while
   suppressing the surrounding blanks: re\ ``structured``\ Text.

will be represented as [#sphinxLatexRepr]_

   Text can be *emphasized*, usually as italics, or even **strongly emphasized**,
   usually as boldface. It is also possible to insert ``inline literals`` which
   will usually be represented as monospaced text.

   This is another paragraph showing how to embed an inline literal while
   suppressing the surrounding blanks: re\ ``structured``\ Text.

This example also shows that paragraphs are separated by a blank line. On a
higher level, text is sectioned into parts, chapters, sections etc. A hierarchy
is established by adorning titles in a systematic way. To this end, an
underline or an underline together with an overline is added to the corresponding
title. An underline or overline is at least as long as the title and contains only
identical non-alphanumeric printable ASCII characters. It is recommended to choose
among the characters ``= - ` : . ' " ~ ^ _ * + #``. Note that even though in this way
one can define a large number of different sectioning levels, in practice this number
may be limited. For example, in HTML the number of different headings is limited to
six. An example of sectioning of a text could look as follows::

   ============
   Introduction
   ============

   A first section
   ===============

   Here comes some text ...

   A second section
   ================
   More text...

   A subsection
   ------------
   And so on...

As this example indicates, an empty line can be put after a title but this is not
mandatory.

Lists, either as bullet-point lists or as enumerated lists, can easily be obtained
in reStructuredText. In a bullet-point list, the items are indicated by a few characters
including ``* + - •``. If the text if an item runs over several lines, it needs
to be consistently indented. Sublists need to be separated from the surrounding list
by empty lines. The following example illustrates the use of bullet-point lists:

.. code-block:: none

   * This is the text for the first item which runs over several lines. Make
     sure that the text is consistently indented.

     Further paragraphs in an item can be added provided the indentation
     is consistent.
   * second item

     * a subitem

   * third item

This code results in

   * This is the text for the first item which runs over several lines. Make
     sure that the text is consistently indented.

     Further paragraphs in an item can be added provided the indentation
     is consistent.
   * second item

     * A subitem is obtained by indenting the corresponding entry.

   * third item

An enumerated list can be numbered explicitly by numbers, alphabet characters
in uppercase or lowercase, or Roman numerals. It is also possible to autonumber
a list by means of ``#``. The sublist of the second item demonstrates two
aspects. The first subitem specifies that lowercase letters should be used for
enumeration and, in addition, the sublist should start with a letter other than
"a".  Once autonumbering has started, fixing a subsequent label would lead to
the start of a new list.

The following code

.. code-block:: none

   #. first item with automatic numbering
   #. second item

      p. subitem
      #. another subitem

   #. another item

results in

   #. first item with automatic numbering
   #. second item

      p. subitem
      #. another subitem

   #. another item

We have already seen how to produce inline literals which may be useful to
mark for example keywords. To display multiline code, the *code* directive
is appropriate. The following example makes use of the possibility to add
linenumbers.

.. code-block:: none

   .. code:: python

      nmax = 10
      sum = 0
      for n in range(1, nmax+1):
          sum = sum+n**2
      print(nmax, sum)

Since it is indicated that the code is written in Python, the syntax of the
code can be highlighted.

   .. code:: python

      nmax = 10
      sum = 0
      for n in range(1, nmax+1):
          sum = sum+n**2
      print(nmax, sum)

Another possibility to typeset code is the use of two colons. If the colons
follow the preceding text immediately, a single colon will be displayed at the
end of the text::

   The following script displays "hello world" three times::

      for _ in range(3):
          print('Hello world!')

Note the indentation of the code block which indicates which part of the text
should be considered as code. The output is as follows:

   The following script displays "hello world" three times::

      for _ in range(3):
          print('Hello world!')

The colon in the output can be avoided if the colons are separated from the
text by a blank::

   The following script displays "hello world" three times. ::

      for _ in range(3):
          print('Hello world!')

Now, the output looks as follows:

   The following script displays "hello world" three times. ::

      for _ in range(3):
          print('Hello world!')

For scientific applications, one might want to include mathematical
expressions.  This can be done by means of the *math* role (``:math:``) for
inline mathematical expressions and the *math* directive (``math::``) for
displayed mathematical expressions. In both cases, the mathematical expression
is entered in LaTeX format. The following code

.. code-block:: none

   Einstein found the famous formula :math:`E=mc^2` which describes the
   equivalence of energy and mass.

   .. math::

      \int_{-\infty}^\infty \mathrm{d}x \mathrm{e}^{-x^2} = \sqrt{\pi}

will result in the output:

   Einstein found the famous formula :math:`E=mc^2` which describes the
   equivalence of energy and mass.

   .. math::

      \int_{-\infty}^\infty \mathrm{d}x \mathrm{e}^{-x^2} = \sqrt{\pi}

There exists also a directive to include images:

.. code-block:: none

   .. image:: img/example.png
      :width: 100
      :height: 100
      :align: center

The name of the image file to be included needs to be specified. Here, the file
happens to reside in a subdirectory ``img`` of the present directory. We have
also specified the size and the alignment of the figure, resulting in the
following output:

.. image:: img/example.png
      :width: 100
      :height: 100
      :align: center

The ``figure`` directive can be used to add a figure caption. The caption text
needs to be indented to indicate that it belongs to the figure directive.

.. code-block:: none

   .. figure:: img/example.png
      :height: 50
      :width: 100

      A graphics can be distorted by specifying ``height`` and ``width``.

This code results in :numref:`example`, which by means of the *Sphinx* LaTeX builder
is created as a floating object.

.. _example:
.. figure:: img/example.png
   :height: 50
   :width: 100

   A graphics can be distorted by specifying ``height`` and ``width``.

Occasionally, one may want to include a link to a web resource. In a documentation, this
might be desirable to refer to a publication where an algorithm or the theoretical basis
of the code has been described. As an example, we present various ways to link to the
seminal paper by Cooley and Tukey on the fast Fourier transformation. The numbering allows
us to refer more easily to the three different versions and plays no role with respect to
the links.

.. code-block:: none

   #. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation
      of complex Fourier series*,
      `Math. Comput. 19, 297–301 (1965) <https://doi.org/10.2307/2003354>`_

   #. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation
      of complex Fourier series*,
      Math. Comput. **19**, 297–301 (1965) `<https://doi.org/10.2307/2003354>`_

   #. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation
      of complex Fourier series*,
      Math. Comput. **19**, 297–301 (1965) https://doi.org/10.2307/2003354

results in the output

#. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation of complex Fourier series*,
   `Math. Comput. 19, 297–301 (1965) <https://doi.org/10.2307/2003354>`_

#. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation of complex Fourier series*,
   Math. Comput. **19**, 297–301 (1965) `<https://doi.org/10.2307/2003354>`_

#. J. W. Cooley and J. W. Tukey, *An algorithm for the machine calculation of complex Fourier series*,
   Math. Comput. **19**, 297–301 (1965) https://doi.org/10.2307/2003354

The first case represents the most comprehensive way to represent a link. The pair of back apostrophes
encloses the text and the link delimited by a less-than and greater-than sign. The text will be shown
in the output with the link associated with it. The underscore at the very end indicates that this is
an outgoing link. In contrast to the two other variants, the volume number (19) can be set as boldface
as nesting of the markup is not possible. 

The second alternative explicitly displays the URL since no text is given. The same effect is obtained
in the third variant by simply putting a URL which can be recognized as such. 

In addition to external links, reStructuredText also allows to create internal links. An example are
footnotes like in the following example.

.. code-block:: none

   This is some text. [#myfootnote]_ And more text...

   .. [#myfootnote] Some remarks.

It is also possible to refer to titles of chapters or sections. The following example gives an
illustration.

.. code-block:: none

   Introduction
   ============

   This is an introductory chapter.

   Chapter 1
   =========

   As discussed in the `Introduction`_ ...

Here, the text of the link has to agree with the text of the chapter or section.

The discussion of reStructuredText in this section did not attempt to cover all possibilities provided
by this markup language. For more details, it is recommended to consult the
`documentation <http://docutils.sourceforge.net/rst.html>`_.

Sphinx documentation generator
==============================

The *Sphinx* documentation generator was initially created to produce the documentation for
Python. However, it is very flexible and can be employed for many other use cases. In fact,
the present lecture notes were also generated by means of *Sphinx*. As a documentation generator,
*Sphinx* accepts documents written in reStructuredText including a number of extension and
provides builders to convert the input into a variety of output formats, among them HTML and
PDF, where the latter is obtained through LaTeX as an intermediate format. *Sphinx* offers the
interesting possibility to autogenerate the documentation or part of it on the basis of the
docstrings provided by the code being documented.

Setting up a Sphinx project
---------------------------

There is not a unique way to set up a *Sphinx* documentation project. For a unexperienced user of
*Sphinx*, the probably simplest way is to invoke [#sphinxversion]_

.. code-block:: bash

   $ sphinx-quickstart

Remember that the dollar sign represents the command line prompt and should not
be typed. The user will then be asked a number of questions and the answers
will allow *Sphinx* to create the basic setup. For the documentation of a
software project, it makes sense to store all documentation related material in
a subdirectory ``doc``. Then, ``sphinx-quickstart`` should either be run in
this directory or the path to this directory should be given as an argument.

The dialog starts with a question about where to place the build directory
relative to the source directory. The latter would for example be the directory
``doc`` and typically contains a configuration file, reStructuredText files,
and possibly images.  For a larger documentation, these files can be organized
in a subdirectory structure.  These source files will usually be put under
version control. When creating the documentation in an output format, *Sphinx*
puts intermediate files and the output in a special directory to avoid mixing
these files with the source files. There are two ways to do so. A directory named
``build`` can be put in parallel to the ``doc`` directory or the it can be kept
within the ``doc`` directory. Then it will be called ``_build`` where the underscore
indicates its special role. It is not necessary to rerun ``sphinx-quickstart``
if you change your mind. One can instead modify the file ``Makefile`` and/or ``make.bat``
which will be discussed below. It may be useful to add the build directory
to the ``.gitignore`` file, provided a Git repository is used.

*Sphinx* now asks the user to choose between the two alternatives. ``(y/n)`` in
the last line indicates the possible valid answers. ``[n]`` indicates the default
value which can also be chosen by simply hitting the return key. Per default, *Sphinx*
thus chooses to place build files into a directory ``_build`` within the source
directory.

.. code-block:: none

   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   > Separate source and build directories (y/n) [n]:

Often, it makes sense to follow the recommendations of *Sphinx*. Two pieces of information
are however mandatory: the name of the project and the author name(s). The default language
is English, but for example by choosing ``de`` it can be switched to German. This information
is relevant when converting to LaTeX in order to choose the correct hyphenation patterns.

``sphinx-quickstart`` offers also to enable a number of extensions. It is possible to
change one's mind later by adapting the configuration file ``conf.py``.

.. code-block:: none

   > autodoc: automatically insert docstrings from modules (y/n) [n]: 
   > doctest: automatically test code snippets in doctest blocks (y/n) [n]: 
   > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: 
   > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: 
   > coverage: checks for documentation coverage (y/n) [n]: 
   > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
   > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
   > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
   > viewcode: include links to the source code of documented Python objects (y/n) [n]: 
   > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

We briefly comment on a few of the more important extensions. ``autodoc``
should be enabled if one wants to generate documentation from the docstrings
provided in the code being documented by the *Sphinx* project. ``intersphinx``
is useful if one wants to provide links to other projects. It is for example
possible to refer to the NumPy documentation.  ``MathJax`` is a Javascript
package [#mathjax]_ which allows for high-quality typesetting of mathematical
material in HTML. 

Depending on the operating system(s) on which output is generated for the *Sphinx* project,
one typically chooses either the ``Makefile`` for Un*x operating systems or a 
Windows command file for Windows operating systems or even both if more than one operating
system is being used.

.. code-block:: none

   > Create Makefile? (y/n) [y]: 
   > Create Windows command file? (y/n) [y]:

While the conversion to an output format can always be done by means of ``sphinx-build``,
the task is facilitated by a Makefile or command file. On a Un*x system, running one of 
the commands

.. code-block:: none

   $ make html
   $ make latexpdf

in the directory where the Makefile resides is sufficient to obtain HTML output of
PDF output, respectively.

Accepting the default values proposed by *Sphinx*, the content of the source directory
on a Un*x system will typically look as follows:

.. code-block:: none

   doc
   +-- _build
   +-- _static
   +-- _templates
   +-- conf.py
   +-- index.rst
   +-- Makefile

As is indicated by the extension, ``conf.py`` is a Python file which defines the
configuration of the *Sphinx* project. This file can be modified according to the
user's need as long as the Python syntax is respected. ``index.rst`` is the main
source file from which reference to other reStructuredText files can be made. Finally,
``Makefile`` defines what should be done when invoking ``make`` with one of the
targets ``html`` or ``latexpdf`` or any other valid target specified by ``make help``.

Sphinx configuration
--------------------

As already mentioned, the file ``conf.py`` offers the possibility to adapt
*Sphinx* to the needs of the project. Basic information includes the name of
the project and of the author(s) as well as copyright information and version
numbers. It makes sense to create a corresponding version tag in the project
repository.

We have seen that ``sphinx-quickstart`` proposes the use of a number of
extensions which, if selected, will appear in the list ``extensions``. Here,
other extensions may be added.  When generating documentation from docstrings,
the ``napoleon`` extensions is of particular interest. Its usefulness will be
discussed in :numref:`autogeneration`. This extension can be enabled by adding
``sphinx.ext.napoleon`` to the list of extensions.

The configuration file contains section for different output builders. We restrict
ourselves here to HTML output and LaTeX output which can serve to produce a PDF
document. Among the options for the HTML output, probably the most interesting
variable is ``html_theme``. https://www.sphinx-doc.org/en/stable/theming.html lists
a few builtin themes which represent a simple way to change the look and feel of
the HTML output. Third-party themes can be found at https://sphinx-themes.org/ and
there is also the possibility to create one's own customized theme.

If the LaTeX output needs to be customized, the dictionary ``latex_elements`` is the
place to look for. The configuration file created by ``sphinx-quickstart`` provides
a structure which is commented out, but might be useful if one needs to customize certain
aspects. For example, if one wants to typeset for A4 paper and would like to have floats
preferentially placed on the top of the page, one might set the dictionary as follows::

   latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        #
        'papersize': 'a4paper',
   
        # The font size ('10pt', '11pt' or '12pt').
        #
        # 'pointsize': '10pt',
   
        # Additional stuff for the LaTeX preamble.
        #
        # 'preamble': '',
   
        # Latex figure (float) alignment
        #
        'figure_align': 'tbp',
   }

An interesting entry is also ``'preamble'`` where all information can be specified which
would normally go in the preamble of a LaTeX document, i.e. between the ``documentclass``
statement and the ``\begin{document}`` line. Note, however, that the use of backslashes
common in LaTeX documents might require to specify the string as raw string by placing
an ``r`` in front of it. A number of parameters specified by the Sphinx style file can be
modified in an entry with key ``'sphinxsetup'``. If the outline of the box enclosing code
should be removed and a background color different from white should be used, one
might specify::

    'sphinxsetup': '''verbatimwithframe=false,
                      VerbatimColor={named}{AliceBlue},
                   '''

This definition is used for the present document. Details about which
parameters can be changed in this way and about other entries which can be
added to the dictionary ``latex_elements`` can be found in the section `LaTeX
customization <https://www.sphinx-doc.org/en/master/latex.html>`_ of the Sphinx
documentation. Finally, it may be useful to know that in the list ``latex_documents``
several properties of the document are specified like the title and author appearing
on the cover page of the documentation.

.. _autogeneration:

Autogeneration of a documentation
---------------------------------

With *Sphinx* it is possible to autogenerate documentation from docstrings. Before discussing
how docstrings can be formatted for use by *Sphinx*, we make a few general remarks on docstrings.
Recommendations about how a docstring should look like are given in :pep:`257`. [#pep]_ 
We here focus on the keypoints pertinent to docstrings of methods and functions. The first line
of the docstring should be a phrase ending in a period. It should be written as a command like
"do something" instead of a description like "does something". This phrase should not exceed
one line and it should be separated from the rest of the docstring by one empty line. Then,
in particular the arguments of the function or method and the return value(s) should be explained.
Or course, further information deemed useful can be given in addition.

In order to demonstrate the autogeneration of documentation from docstrings, we take as an
example the last script for the quantum carpet discussed in :numref:`profiling`. We have
partially supplied the code with docstrings which now looks as follows::

   from math import sqrt
   import numpy as np
   import matplotlib.pyplot as plt
   from matplotlib import cm
   
   class InfiniteWell:
       """Quantum carpet for infinitely deep potential well.
   
       This class allows to determine the time evolution of an
       initial state in an infinitely deep potential well.
   
       :param func psi0: initial wave function
       :param float width: width of the potential well
       :param int nbase: number of basis states
       :param int nint: number of intervals used in the integration routine
       """
   
       def __init__(self, psi0, width, nbase, nint):
           self.width = width
           self.nbase = nbase
           self.nint = nint
           self.coeffs = trapezoidal(lambda x: psi0(x)*self.eigenfunction(x),
                                     -0.5*self.width, 0.5*self.width, self.nint)
   
       def eigenfunction(self, x):
           """Determine set of eigenfunction values at position ``x``.
   
           The basis set is limited by the number of eigenstates given by 
           ``self.nbase``.
   
           :param x: position at which the eigenfunctions are to be determined
           :type x: float or numpy.ndarray
           :return: array of eigenfunction values
           :rtype: numpy.ndarray
           :raises AssertionError: if the dimension of ``x`` does not equal 1
           """
           assert x.ndim == 1
           normalization = sqrt(2/self.width)
           args = (np.arange(self.nbase)[:, np.newaxis]+1)*np.pi*x/self.width
           result = np.empty((self.nbase, x.size))
           result[0::2, :] = normalization*np.cos(args[0::2])
           result[1::2, :] = normalization*np.sin(args[1::2])
           return result
   
       def psi(self, x, t):
           coeffs = self.coeffs[:, np.newaxis]
           eigenvals = np.arange(self.nbase)[:, np.newaxis]
           tvals = t[:, np.newaxis, np.newaxis]
           psit = np.sum(coeffs * self.eigenfunction(x)
                         * np.exp(-1j*(eigenvals+1)**2*tvals), axis= -2)
           return psit
   
   def trapezoidal(func, a, b, nint):
       delta = (b-a)/nint
       x = np.linspace(a, b, nint+1)
       integrand = func(x)
       integrand[..., 0] = 0.5*integrand[..., 0]
       integrand[..., -1] = 0.5*integrand[..., -1]
       return delta*np.sum(integrand, axis=-1)
   
   def psi0(x):
       """Determine Gaussian wave function.
   
       :param float x: position at which the wave function is determined
       :return: value of wave function at position ``x``
       :rtype: float
       """
       sigma = 0.005
       return np.exp(-x**2/(2*sigma))/(np.pi*sigma)**0.25
   
   if __name__ == '__main__':
       w = InfiniteWell(psi0=psi0, width=2, nbase=100, nint=1000)
       x = np.linspace(-0.5*w.width, 0.5*w.width, 500)
       t = np.linspace(0, np.pi/4, 1000)
       z = np.abs(w.psi(x, t))**2
       z = z/np.max(z)
       plt.rc('text', usetex=True)
       plt.imshow(z.T, cmap=cm.hot)
       plt.xlabel('$t$', fontsize=20)
       plt.ylabel('$x$', fontsize=20)
       plt.show()

In addition to the docstrings, this code makes sure that the last part is not executed
when this script is imported, because in order to access the docstrings, *Sphinx* will
import the script. Execution of the last part in our case will simply cost time but 
in general can have more serious side effects. Note that the script can only be imported,
if it is in the search path defined in the *Sphinx* configuration file. This usually
requires to uncomment the three lines ::

   import os
   import sys
   sys.path.insert(0, os.path.abspath('.'))

and to adjust the argument of ``os.path.abspath`` according to the place where the
script to be imported can be found.

The docstrings are written in reStructuredText and admittedly are not easy to
read. We will discuss a solution to this problem shortly. For the moment,
however, we will keep this form of the docstrings.

Now let us add the following code in one of our reStructuredText files which are part of
the documentation::

   .. automodule:: carpet
      :members:
      :undoc-members:

This code will only function correctly, if the ``autodoc`` extension is loaded, i.e.
the list ``extensions`` in the *Sphinx* configuration file contains the entry ``'sphinx.ext.autodoc'``.
The argument ``carpet`` of the ``automodule`` directive implies that the file ``carpet.py``
will be imported. The autogenerated documentation will list all documented as well as
all undocumented members. The generated output will look as follows:

   class carpet.InfiniteWell(psi0, width, nbase, nint)
   
      Quantum carpet for infinitely deep potential well.
   
      This class allows to determine the time evolution of an initial
      state in an infinitely deep potential well.
   
      Parameters:
         * **psi0** (*func*) -- initial wave function
   
         * **width** (*float*) -- width of the potential well
   
         * **nbase** (*int*) -- number of basis states
   
         * **nint** (*int*) -- number of intervals used in the
           integration routine
   
      eigenfunction(x)
   
         Determine set of eigenfunction values at position *x*.
   
         The basis set is limited by the number of eigenstates given by
         ``self.nbase``.
   
         Parameters:
            **x** (*float or numpy.ndarray*) -- position at which the
            eigenfunctions are to be determined
   
         Returns:
            array of eigenfunction values
   
         Return type:
            numpy.ndarray
   
         Raises:
            ``AssertionError`` -- if the dimension of *x* does not equal
            1
   
      psi(x, t)
   
   carpet.psi0(x)
   
      Determine Gaussian wave function.
   
      Parameters:
         **x** (*float*) -- position at which the wave function is
         determined
   
      Returns:
         value of wave function at position ``x``
   
      Return type:
         float
   
   carpet.trapezoidal(func, a, b, nint)

If the line containing ``:undoc-members:`` were left out in the ``automodule`` directive,
the output would contain only the documented class and methods. The listed methods could
be restricted by giving the appropriate names after ``:members:``.

As already mentioned, the docstrings given above are not particularly easy to read. There
are two standards for docstrings which are handled by *Sphinx*, provided the extension
``napoleon`` is loaded. The list ``extensions`` in the *Sphinx* configuration file then
should contain the string ``'sphinx.ext.napoleon'``. The supported standards for docstrings
are the Google style docstring [#googledocstring]_ and NumPy style docstring [#numpydocstring]_.
We will focus our discussion of these two standards to the method ``eigenfunction`` in the
quantum carpet script.

Applying the NumPy style to the method ``eigenfunction`` would result in ::

   def eigenfunction(self, x):
       """Determine set of eigenfunction values at position `x`.

       The basis set is limited by the number of eigenstates given by 
       ``self.nbase``.

       Parameters
       ----------
       x : float or numpy.ndarray
           position at which the eigenfunctions are to be determined

       Returns
       -------
       numpy.ndarray
           array of eigenfunction values

       Raises
       ------
       AssertionError
           if the dimension of `x` does not equal 1

       """

where we did not repeat the code of the eigenfunction method. This docstring is nicely
formatted in sections. The possible sections are not restricted to the ones used in this
example. A complete list is given in the documentation of the `napoleon preprocessor
<http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_. The output obtained
from this docstring corresponds to the one given before, possibly with minor differences, so
that we do not reproduce it here.

The Google style for docstrings resembles the NumPy style in the sectioning of the
docstring even though the details of the format differ. Our example would take the
following form where we again leave out the code of the method::

   def eigenfunction(self, x):
       """Determine set of eigenfunction values at position `x`.

       The basis set is limited by the number of eigenstates given by 
       ``self.nbase``.

       Args:
           x (float or numpy.ndarray): Position at which the eigenfunctions
               are to be determined.

       Returns:
           numpy.ndarray: Array of eigenfunction values.

       Raises:
           AssertionError: The dimension of `x` does not equal 1.

       """

These examples may serve to get the basic idea of how a documentation can be autogenerated
from docstrings. When working with the *Sphinx* documentation generator, questions are likely
to come up which have not been addressed in this chapter. A complete description can be found
in the extensive online documentation which should be consulted in the case of need.


.. [#docreST] More information on reStructuredText can be found in the documentation
   of the docutils project at `<http://docutils.sourceforge.net/rst.html>`_.
.. [#docSphinx] The *Sphinx* project page can be found at `<https://www.sphinx-doc.org/>`_.
.. [#sphinxLatexRepr] Note that the representation given here and in following examples
       is generated by the LaTeX builder of *Sphinx*. It may look differently if the
       representation is generated otherwise, e.g. with tools like ``rst2html`` or
       ``rst2latex`` provided by ``docutils`` or ``rst2pdf``.
.. [#sphinxversion] The following discussion is based on version 1.8.2 of *Sphinx* but
       should mostly apply to all recent versions of *Sphinx*.
.. [#mathjax] For more information see https://www.mathjax.org/.
.. [#googledocstring] For a complete description see
       https://google.github.io/styleguide/pyguide.html#functions-and-methods and
       https://google.github.io/styleguide/pyguide.html#comments-in-classes.
.. [#numpydocstring] For details see https://numpydoc.readthedocs.io/en/latest/format.html.
.. [#pep] PEP is short for Python Enhancement Proposal.
