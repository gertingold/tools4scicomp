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
is LaTeX. Here, ``x`` and ``$x$`` will be typset differently because the dollar
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
or one of its variants is commonly used in Wikis. Both texts written in
Markdown or in reStructuredText are frequently used for documentation files in
software projects like README.md or README.rst, respectively, which usually
specify the purpose of the software and give further useful information. In
version control systems like Gitlab, they can be represented in a nice form
in the browser.

The documentation generator *Sphinx* is based on reStructuredText. Therefore, we
will now discuss some of the more important aspects of this markup language.

::

   Text can be *emphasized*, usually as italics, or even **strongly emphasized**,
   usually as boldface. It is also possible of insert ``inline literals`` which
   will usually be represented as monospaced text.

   This is another paragraph showing how to embed an inline literal while
   suppressing the surrounding blanks: re\ ``structured``\ Text

results in

   Text can be *emphasized*, usually as italics, or even **strongly emphasized**,
   usually as boldface. It is also possible of insert ``inline literals`` which
   will usually be represented as monospaced text.

   This is another paragraph showing how to embed an inline literal while
   suppressing the surrounding blanks: re\ ``structured``\ Text

::

   * first item
   * second item

     * a subitem

   * third item

results in 

   * first item
   * second item

      * a subitem

   * third item

::

   #. first item with automatic numbering
   #. second item

      #. subitem
      #. another subitem

   2. another item forced to be labelled by 2

results in

   #. first item with automatic numbering
   #. second item

      #. subitem
      #. another subitem

   2. another item forced to be labelled by 2

.. [#docreSt] More information on reStructuredText can be found in the documentation
   of the docutils project at `<http://docutils.sourceforge.net/rst.html>`_.
.. [#docSphinx] The *Sphinx* project page can be found at `<https://www.sphinx-doc.org/>`_.
