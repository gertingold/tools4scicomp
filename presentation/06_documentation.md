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

### examples:

<div class="grid grid-cols-[50%_1fr] gap-8"><div>

```rst
Markup of lists
===============

The following is a bullet-point list:

* first item
* second item
```

</div><div>

<h1>Markup of lists</h1>
<p>The following is a bullet-point list:</p>
<ul>
 <li>first item</li>
 <li>second item</li>
</ul>

</div></div>

<div class="grid grid-cols-[50%_1fr] gap-8"><div>

```rst
Text can be *emphasized*, usually as italics, or even
**strongly emphasized**, usually as boldface. It is also
possible to insert ``inline literals`` which will usually
be represented as monospaced text.

This is another paragraph showing how to embed an inline
literal while suppressing the surrounding blanks:
re\ ``structured``\ Text.
```

</div><div>

Text can be <em>emphasized</em>, usually as italics, or even <strong>strongly emphasized</strong>,
usually as boldface. It is also possible to insert <code>inline literals</code> which
will usually be represented as monospaced text.

This is another paragraph showing how to embed an inline literal while
suppressing the surrounding blanks: re<code>structured</code>Text.

</div></div>
