---
layout: section
---

# Documentation of code

---

# Documentation of code

* Ideally, code is written in a way that its meaning is transparent, e.g. by appropriately naming
  variables and functions but also by keeping its structure simple.
* In Python, docstrings are useful to document methods and functions or even a whole script. For
  methods and functions, it is important to state what their purpose is, what the arguments mean
  and which type they should have. Furthermore, the return values should be explained. Necessary
  information on how the method or function works can be put into the docstring in addition to a
  one-line explanation at the beginning.
* Often, a more extensive documentation is necessary which can e.g. be printed or displayed on a
  web page.
* The documentation tool commonly used for Python (but not restricted to this language) is
  [Sphinx](https://www.sphinx-doc.org/) which is based on the markup language
  [reStructuredText](http://docutils.sourceforge.net/rst.html) and can produce output for
  example in LaTeX and PDF or in HTML.

---

# reStructuredText

* reStructuredText is a mark-up language which helps to format text in a simple way. Another
  mark-up language is [Markdown](https://www.markdownguide.org/) which also comes in a [Github
  flavor](https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) used in Gitlab and on GitHub.

<br />

#### examples (rendered by [Online reStructure Editor](https://www.tutorialspoint.com/online_restructure_editor.php)):

<br />

<img src="/images/rst_1.png" style="width: 55%; margin: auto">

<br />

<img src="/images/rst_2.png" style="width: 90%; margin: auto">

---

# Chapters, sections, subsections, …

<img src="/images/rst_3.png" style="width: 65%; margin: auto">

<br />

* For underlining chapters, sections etc., choose from the characters ``= - ` : . ' " ~ ^ _ * + #``.

---

# Bullet-point lists

<img src="/images/rst_4a.png" style="width: 90%; margin: auto">

<br />

<img src="/images/rst_4b.png" style="width: 90%; margin: auto">


---

# Lists with automatic numbering

<img src="/images/rst_5.png" style="width: 100%; margin: auto">

<br />

<img src="/images/rst_6.png" style="width: 100%; margin: auto">

---

# The `code` directive

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```
.. code:: python

   nmax = 10
   sum = 0
   for n in range(1, nmax+1):
       sum = sum+n**2
   print(nmax, sum)
```

</div><div>
<img src="/images/rst_7.png" style="width: 100%; margin: auto">
</div></div>

* with syntax highlighting, here for Python

Alternatives:

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```
The following script displays "hello world" three times::

   for _ in range(3):
       print('Hello world!')
```

</div><div>
<img src="/images/rst_8.png" style="width: 100%; margin: auto">
</div></div>

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```
The following script displays "hello world" three times. ::

   for _ in range(3):
       print('Hello world!')
```

</div><div>
<img src="/images/rst_9.png" style="width: 100%; margin: auto">
</div></div>

* `::` creates a colon unless preceded by a blank

---

# The `math` role

```rst
Einstein found the famous formula :math:`E=mc^2` which describes the
equivalence of energy and mass.

.. math::

   \int_{-\infty}^\infty \mathrm{d}x \mathrm{e}^{-x^2} = \sqrt{\pi}
```

<img src="/images/rst_10.png" style="width: 100%; margin: auto">

<br />

* use LaTeX syntax to display math
* MathJax is used to display math in HTML

---

# `image` and `figure` directive

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```rst
.. image:: img/example.png
   :width: 100
   :height: 100
   :align: center
```

</div><div>
<img src="/images/rst_11.png" style="width: 30%; margin: auto">
</div></div>

<br />

```rst
.. figure:: img/example.png
   :height: 50
   :width: 100

   A graphics can be distorted by specifying ``height`` and ``width``.
```

<br />

<img src="/images/rst_12.png" style="width: 60%; margin: auto">

* `figure` directive allows to add a caption

---

# Links

<img src="/images/rst_13.png" style="width: 100%; margin: auto">

<br />

* In the first version a link enclosed by `<` and `>` is added to a given text. The whole construction
  is delimited by backticks with an underscore at the end.
* In the second version, the text is left out so that it is replaced by the URL.
* This works even without backticks and an underscore if a URL is recognized.

---

# Footnotes and references

<img src="/images/rst_14.png" style="width: 100%; margin: auto">

<br />

* Links, here within the document, end with an underscore. The label starts with `#` and is enclosed in square
  brackets.

<br>

<img src="/images/rst_15.png" style="width: 80%; margin: auto">

<br />

* Here, the label needs to agree with the title and is used to display the link.

---

# More flexible internal references

#### alternative way to implement internal references

```
One possibility is the use of scientific numerical libraries like NumPy and SciPy which
are discussed in :numref:`Chapter %s <scientific_libraries>`. This chapter is rather
specific to Python apart from the aspect of illustrating the use of numerical libraries.

[…]

.. _scientific_libraries:

*****************************************
Scientific computing with NumPy and SciPy
*****************************************
```

<br />

<img src="/images/rst_16.png" style="width: 100%; margin: auto">

<br />

* The `numref` role allows to display the chapter number.
* The label starts with an underscore.

---

# Setting up a Sphinx project

```bash {all|4-5|12|15-17|25|27-30|34-37}{maxHeight:'480px'}
$ sphinx-quickstart
Welcome to the Sphinx 7.3.7 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: 

The project name will occur in several places in the built documentation.
> Project name: Example project
> Author name(s): Gert-Ludwig Ingold
> Project release []: 

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: 

Creating file /home/gli/test/conf.py.
Creating file /home/gli/test/index.rst.
Creating file /home/gli/test/Makefile.
Creating file /home/gli/test/make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file /home/gli/test/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

---

# The Sphinx Makefile

```bash {all|6,16}{maxHeight:'480px'}
$ ls
Makefile  _build  _static  _templates  conf.py  index.rst  make.bat
$ make help
Sphinx v7.3.7
Please use `make target' where target is one of
  html        to make standalone HTML files
  dirhtml     to make HTML files named index.html in directories
  singlehtml  to make a single large HTML file
  pickle      to make pickle files
  json        to make JSON files
  htmlhelp    to make HTML files and an HTML help project
  qthelp      to make HTML files and a qthelp project
  devhelp     to make HTML files and a Devhelp project
  epub        to make an epub
  latex       to make LaTeX files, you can set PAPER=a4 or PAPER=letter
  latexpdf    to make LaTeX and PDF files (default pdflatex)
  latexpdfja  to make LaTeX files and run them through platex/dvipdfmx
  text        to make text files
  man         to make manual pages
  texinfo     to make Texinfo files
  info        to make Texinfo files and run them through makeinfo
  gettext     to make PO message catalogs
  changes     to make an overview of all changed/added/deprecated items
  xml         to make Docutils-native XML files
  pseudoxml   to make pseudoxml-XML files for display purposes
  linkcheck   to check all external links for integrity
  doctest     to run all doctests embedded in the documentation (if enabled)
  coverage    to run coverage check of the documentation (if enabled)
  clean       to remove everything in the build directory
```

---

# Building HTML

```bash {all|6,16}{maxHeight:'480px'}
$ make html
Running Sphinx v7.3.7
making output directory... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 1 source files that are out of date
[…]
build succeeded.

The HTML pages are in _build/html.
```

<br />

<img src="/images/sphinx_example.png" style="width: 80%; margin: auto">

---

# Configuration file `conf.py`

```python {all}{maxHeight:'250px'}
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example project'
copyright = '2024, Gert-Ludwig Ingold'
author = 'Gert-Ludwig Ingold'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
```

<br />

* the configuration file is a Python file
* many more aspects can be configured, e.g. also for the LaTeX builder
* there exists a number of [interesting extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
  which can be added to the list `extensions`

---

# Extensions

<br />

some important examples

* sphinx.ext.autodoc – Include documentation from docstrings
* sphinx.ext.intersphinx – Link to other projects’ documentation
* sphinx.ext.linkcode – Add external links to source code
* sphinx.ext.mathjax – Render math via JavaScript
* sphinx.ext.napoleon – Support for NumPy and Google style docstrings
* sphinx.ext.todo – Support for todo items
* sphinx.ext.viewcode – Add links to highlighted source code

---

# Documentation from docstrings

```bash {6-8|20}{maxHeight:'150px'}
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example project'
copyright = '2024, Gert-Ludwig Ingold'
author = 'Gert-Ludwig Ingold'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
```

* set path correctly so that the script `carpet.py` can be found an imported
* use extensions for creating the documentation from docstrings and for linking to
  the corresponding code

```rst {all|9-11|13-15}{maxHeight:'150px'}
.. Example project documentation master file, created by
   sphinx-quickstart on Wed Jun 12 08:28:41 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Example project's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule:: carpet
   :members:
   :undoc-members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

* `toctree` directive creates table of content
* `automodule` directive creates documentation from docstrings (needs `sphinx.ext.autodoc`)

---

# Sphinx docstring format

```python
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
```

---

# HTML output

<img src="/images/sphinx_carpet.png" style="width: 45%; margin: auto">

---

# Alternative docstring formats – NumPy

```python
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
```

* requires `sphinx.ext.napoleon`

---

# Alternative docstring formats – Google

```python
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
```

* requires `sphinx.ext.napoleon`
