---
# try also 'default' to start simple
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: images/cover.png
# some information about your slides, markdown enabled
title: Method Course Tools for Scientific Computing
info: false
author: Gert-Ludwig Ingold
# apply any unocss classes to the current slide
# class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# https://sli.dev/guide/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/guide/syntax#mdc-syntax
mdc: true
#
aspectRatio: 16/9
---

# Method Course
# Tools for Scientific Computing
### Gert-Ludwig Ingold

<div class="pt-12">
  <div>
  <carbon-logo-github /> <a href="https://github.com/gertingold/tools4scicomp">https://github.com/gertingold/tools4scicomp</a>
  </div>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

<style>
h1{ color: white; }
</style>

---

# Topics

* Version control with Git
* Testing of code
* Scientific computing with NumPy and SciPy
* Run-time analysics
* Documentation of code
* Aspects of parallel computing

<br>

* any suggestions or wishes from the audience?

<!--
Here is another comment.
-->

---
layout: gli-two-cols-header
---

# How does the method course work?

::left::

### Where and when

* lecture: 2 hours  
  Monday, 8h15 – 9h45, S-448
* practical work: 4 hours    
  Monday, 14h – 17h, S-448  

<br>

### What can be earned

* a lot of useful knowledge, but also:
* 6 credit points
* Master Materials Science and Engineering
  - Methods in Materials Science
* Master Physics
  - physics elective area

::right::

### Practical work

* programming project
* carried out in small groups of two or three persons
* extends typically over the full semester
* includes all aspects taught in the course like the use of
  version control, writing of unit tests, documentation, ...
* in order to earn credit points: the project repository including
  source code, tests etc. and the documentation have to be handed in
  by the end of the semester
  
---
layout: section
---

# Version control with Git

---

# Why do we need version control?

#### Software is developed iteratively
- code is added
- errors are fixed
- code is improved or refactored

<br>

#### <carbon-arrow-right /> It is important to keep a version history.
- apparent improvements  might turn out to lead to non-functional code
- it might be important to know whether certain numerical results were affected by an error
- design decisions can be documented

<br>

#### Why not simply keep one or more backup copies?
- naming can become unsystematic very easily
- for larger projects seeing all backup copies is distracting
- differences between versions are not easily accessible

---

# Short history of version control systems

<div class="grid grid-cols-[10%_1fr] gap-4">
  <div>1972</div><div>SCCS (source code control system)</div>
  <div>1982</div><div>RCS (revision control system)</div>
  <div>1990</div><div>CVS (concurrent versions system)</div>
  <div>1990</div><div>CVS (concurrent versions system)</div>
  <div>2000</div><div>Subversion</div>
  <div>2005</div><div><span style="color: #aa0000;">Git</span>, Mercurial, Bazaar</div>
</div>

<br>

Git is a very popular version control system, in particular for the development of
open-source software. This makes code of scientific libraries like NumPy or SciPy easily
accessible for inspection.

The university hosts its own GitLab instance: `git.rz.uni-augsburg.de`

---
layout: quote
---

## *Why the name Git?*
<br>

<div class="grid grid-cols-[4%_1fr] gap-4">
<div><carbon-quotes class="text-3xl"/></div><div>
It's the British slang term for stupid, despicable person ― arse. 
   The joke "I name all my projects for myself, first Linux, then git"
   was just too good to pass up. But it is also short, easy-to-say, and
   type on a standard keyboard. And reasonably unique and not any standard
   command, which is unusual.
  </div></div>
 
 <br>
 
 <div style="text-align: right">
 Linus Torvalds <a href="https://www.wired.com/2012/02/github-2/"><carbon-launch /></a>
 </div>

---

# Collaborative software development

#### How are versions shared among developers?
  - centralized version control systems, e.g. Subversion  
    at each moment in time the server contains well-defined revision of the code
  - distributed version control systems, e.g. Git  
    different computers may have different versions

<br>

#### What if developers work in parallel, what should be done in case of conflicts?
  - need to handle merge conflicts

<br>

While parallel editing of text like in Overleaf or Google docs may make sense, code needs a consistent
version to allow e.g. for testing.
  
<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800">
The use of a version control system is no substitute for project management and  for attributing tasks to developers.
</div>

---

# Centralized version control systems

<br>

<img src="images/cvcs.png" style="width: 60%; margin: auto">

<br>

* sequential revisions of project states encompassing all files present at a certain moment
* an internet connection to the server is needed in order to record changes and create a new revision

---

# Distributed version control system

<br>

<img src="images/dvcs.png" style="width: 70%; margin: auto">

<br>

* there is no longer a global squential numbering
* instead files and commits, i.e. sets of files, are characterized by hash values
  depending on the content
* histories of different users may differ
* users can create new versions without internet connection favoring atomic commits

<br>

* How is collaboration possible in a distributed setup while respecting access permissions?

---

# Distributed version control system with central server

In practice, there is a central server through which users exchange their versions.

<br>

<img src="images/dvcs-github.png" style="width: 50%; margin: auto">
