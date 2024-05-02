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

<br>

<div class="pt-12">
  <div>
    <carbon-logo-github /> <a href="https://github.com/gertingold/tools4scicomp">https://github.com/gertingold/tools4scicomp</a>
  </div>
  <div>
    <carbon-launch /> <a href="https://gertingold.github.io/tools4scicomp">https://gertingold.github.io/tools4scicomp</a>
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
* Run-time analysis
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
* 8 credit points
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
src: ./02_git.md
---
