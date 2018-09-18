************************
Version Control with Git
************************

Why version control?
====================

A program is rarely written in one go but rather evolves through a number of
stages where the code is improved, for example by fixing errors or improving its
functionality. In this process, it is generally a good idea to keep old
versions. Occasionally, one has an apparently good idea of how to improve a
programm, only to find out somewhat later that it was not such a good idea after
all. Without having the original version available, one might have a hard time
going back to it.

Often, old versions are kept in an informal way by inventing filenames to
distinguish different versions. Unless one strictly abides by a naming
convention, sooner or later one will be unable to identify the stage of 
development corresponding to a given file. Things become even more difficult if
more than one developer is involved.

The potential loss of a working program is not the only motivation to keep
a history of program versions. Suppose that a version of the program is used
to compute scientific data and suppose that the program is further developed,
e.g. by adding functionality. One might think that it is unnecessary to keep
the old version. However, imagine that at some point it turns out that the
program contains a mistake resulting in erroneous data. In such a situation,
it may become essential to know whether the data obtained previously are
affected by the mistake or not. Do the data have to be discarded or can continue
to use them? If the version of the code used obtain the data is documented, this
question can be decided. Otherwise, one probably could not trust the old data
anymore.

Another reason of keeping the history of a program is to document its evolution.
The motivation for design decisions can be made transparent and even bad
decisions could be kept for further reference. In a scenario where code is
developed by several or even a large number of people, it might be desirable to
know who is to be praised or blamed for a certain piece of code. Version control
systems often support collaborative development by providing tools to discuss
code before accepting the associated changes and by the possibility of easily
going back to an older version. In this way, trying out new ideas can be
encouraged.

A version control system storing the history of a software project is clearly
an invaluable tool. This insight is anything but new and indeed as early as in
the 1970s, a first version control system, SCCS (short for source code control
system), was developed. Later systems in wide use include RCS (revision control
system) and CVS  (concurrent versions system), both developed in the last century,
Subversion developed around the turn of the century and more recent systems
like Git, Mercurial and Bazaar.

Here, we will discuss the version control system Git created by Linus Torvalds
in 2005. Its original purpose was to serve in the development of the Linux
kernel. In order to make certain aspects of Git better understandable and to
highlight some of its advantages, we will consider in the following section
in some more detail different approaches to version control.

Centralized and distributed version control systems
===================================================



