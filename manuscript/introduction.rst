************
Introduction
************

The daily routine in scientific work is characterized by careful checks and detailed
documentation. Experimentalists calibrate their apparatuses and note all relevant aspects
of an experiment in a lab book, either on paper or digitally. Theorists check their
calculations and consider limiting cases to ensure the correctness of their results.
On the other hand, it can frequently be observed that not the same standards are applied
to scientific computational work, even though appropriate tools exist. Furthermore, knowledge
of these tools can be an important asset when looking for a job outside of academia.

The present lecture notes cover a number of tools useful in scientific
computing. In view of the aspects just discussed, we specifically mention the
use of a version control system like Git introduced in :numref:`Chapter %s
<version_control>`, testing of code discussed in :numref:`Chapter %s
<testing>`, and the documentation of code covered in :numref:`Chapter %s
<documenting>`.  The discussion of the version control system Git is completely
independent of the specific programming language used. On the other hand, the
tools covered in the chapter on testing – doctests and the ``pytest`` package – 
are specific to the programming language Python. However, the basic ideas should
be transferable to other programming languages. For the purpose of documentation, we
introduce the Sphinx documentation generator. Despite its origin as a tool to generate
the Python documentation, it is very flexible and can be used also for other programming
languages. In fact, even the present lecture notes where produced with Sphinx.

The other chapters are concerned more with the performance of programs. This is an
important issue when using Python as a programming language. Python has gained a significant
popularity in scientific computing despite its reputation of not being the fastest 
language. However, there exist a variety of approaches to bring Python up to speed.
One possibility is the use of scientific numerical libraries like NumPy and SciPy which
are discussed in :numref:`Chapter %s <scientific_libraries>`. This chapter is rather
specific to Python apart from the aspect of illustrating the use of numerical libraries.

:numref:`Chapter %s <profiling>` is devoted to the run-time analysis of code
with the aim of identifying the most time-consuming parts of a program. Here
again, the tools are specific to Python but the concepts can be applied to
other languages as well. Finally, :numref:`Chapter %s <parallel_computing>`
gives a brief introduction to aspects of parallel computing in Python. In view
of the existence of the global interpreter lock, this discussion is rather specific
to Python. In addition, possibilities offered by just-in-time compilers to increase
the performance of programs are highlighted.

These lecture notes present material covered in a one-semester method course
*Tools for scientific computing* taught at the Universität Augsburg consisting
of a two-hour lecture and four-hour practical work per week. The material is
thus intended for a total of 30 hours of lectures.

The sources of the lecture notes are publicly available on Github at 
https://github.com/gertingold/tools4scicomp. Suggestions for improvements
through Github issues or pull request are welcome.
