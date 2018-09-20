************************
Version Control with Git
************************

Why version control?
====================

A program is rarely written in one go but rather evolves through a number of
stages where the code is improved, for example by fixing errors or improving its
functionality. In this process, it is generally a good idea to keep old
versions. Occasionally, one has an apparently good idea of how to improve a
program, only to find out somewhat later that it was not such a good idea after
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

.. _cvcs-vs-dvcs:

Centralized and distributed version control systems
===================================================

Often software is developed by a team. For the sake of illustration let us
think of a number of authors working jointly on a text. In fact, scientific
manuscripts are often written in (La)TeX which can be viewed as a specialized
programming language. Obviously, there exists a probability that persons
working in parallel on the text will make incompatible changes. Inevitably, at
some point the question arises which version should actually be accepted. We
will encounter such situations later as so-called merge conflicts.

Early version control systems like RCS avoided such conflicts by a locking
technique. In order to change the text or code, it was necessary to first
lock the corresponding file, thus preventing other persons from modifying the
same file at the same time. Unfortunately, this technique tends to impede
parallel development. For our example of manuscript, it is perfectly fine
if several persons work in parallel on different sections. Therefore, locking
has been found not to be a good idea and it is not substitute for communication
between team members about who is doing what.

More modern version control systems are designed to favor collaboration within
a team. There exist two different approaches: centralized version control
systems on the one hand and distributed version control systems on the other
hand. The version control system Git which we are going to discuss in more
detail in this chapter is a distributed version control system. In order to
better understand some of its aspects, it is useful to contrast it with a
centralized version control system like Subversion.

.. _cvcs:
.. figure:: img/cvcs.*
   :width: 30em
   :align: center

   A centralized version control system contains a well defined set of
   files at any given moment in time which can be referred to by a
   sequential revision number.


More modern version control systems are designed to favor collaboration within
a team. There exist two different approaches: centralized version control
systems on the one hand and distributed version control systems on the other
hand. The version control system Git which we are going to discuss in more
detail in this chapter is a distributed version control system. In order to
better understand some of its aspects, it is useful to contrast it with a
centralized version control system like Subversion.

The basic structure of a centralized version control system is depicted in the
left part of :numref:`cvcs`. One or more developers, referred to as clients
here, exchange code versions via the internet with a central server. At any
moment of time, the server contains a definite set of files, i.e. a revision
which is numbered sequentially as indicated in the right part of :numref:`cvcs`.
From one revision to the next, files can change or remain unchanged and files
can be added or removed. The prize to pay for this simple sequential history 
is that an internet connection and a working server is needed in order to
create a new revision. A developer cannot create new revisions of the code
while working off-line, an important drawback of centralized version control
systems.

.. _dvcs:
.. figure:: img/dvcs.*
   :width: 30em
   :align: center

   In a distributed version control system each user keeps file versions in
   a local repository and exchanges versions with other repositories when
   needed. As a consequence no global sequential history can be defined.

As an alternative, one can use a distributed version control system which
is schematically represented in :numref:`dvcs`. In such a setup, each developer
keeps his or her own versions in a local repository and exchanges files
with other repositories when needed. Due to the local repository, one can
create a new version at any time, even in the absence of an internet connection.
On the other hand, there exist local version histories and the concept of
a global sequential revision numbering scheme does not make sense anymore.
Instead, Git uses hexadecimal hash values to identify versions of individual
files and sets of files, so-called commits, which reflect changes in the
code base. The main point to understand here is that the seemingly natural
sequential numbering scheme cannot work in a distributed version control
system. 

.. _dvcs-github:
.. figure:: img/dvcs-github.*
   :height: 10em
   :align: center

   A typical setup for the distributed version control system Git uses
   a central server to exchange versions between local repositories.

In most cases, a distributed version control system is not implemented
precisely in the way presented in :numref:`dvcs` as it would require
communication between potentially a large number of local repositories. A setup
like the one shown in :numref:`dvcs-github` is typical instead. The important
difference as compared to the centralized version control system displayed in
:numref:`cvcs` consists in the existence of local repositories where individual
developers can manage their code versions even if disconnected with the central
server. The difference is most obvious in the case of a single developer. Then,
a local repository is completely sufficient and there is no need to use another
server.

A central server for the use with the version control system Git can be set up
based on Gitlab. Many institutions are running a Gitlab instance
[#gitlab_uaux]_.  In addition, there exists the Github service at `github.com
<https://github.com/>`_. Github is popular among developers of open software
projects for which it provides repositories free of charge. Private
repositories can be obtained at a monthly rate, but there exists also the
possibility to apply for temporary free private repositories for academic use.
In later sections, when discussing collaborative code development with Git, we
will specifically address Gitlab, but the differences to Github are usually
minor.

In the following sections, we will start by explaining the use of Git in a
single-user scenario with a local repository. This knowledge also forms the
basis for work in a multi-developer environment using Gitlab or Github.

Getting help
============

Before starting to explore the version control system Git, it is useful to
know where one can get help. Generally, Git tries to be quite helpful even
on the command line by adding useful hints to its output. As the general structure
of a Git command starts with ``git <command>``, one can ask for help as follows::

   $ git help
   usage: git [--version] [--help] [-C <path>] [-c name=value]
              [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
              [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
              [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
              <command> [<args>]
   
   These are common Git commands used in various situations:
   
   start a working area (see also: git help tutorial)
      clone      Clone a repository into a new directory
      init       Create an empty Git repository or reinitialize an existing one
   
   work on the current change (see also: git help everyday)
      add        Add file contents to the index
      mv         Move or rename a file, a directory, or a symlink
      reset      Reset current HEAD to the specified state
      rm         Remove files from the working tree and from the index
   
   examine the history and state (see also: git help revisions)
      bisect     Use binary search to find the commit that introduced a bug
      grep       Print lines matching a pattern
      log        Show commit logs
      show       Show various types of objects
      status     Show the working tree status
   
   grow, mark and tweak your common history
      branch     List, create, or delete branches
      checkout   Switch branches or restore working tree files
      commit     Record changes to the repository
      diff       Show changes between commits, commit and working tree, etc
      merge      Join two or more development histories together
      rebase     Reapply commits on top of another base tip
      tag        Create, list, delete or verify a tag object signed with GPG
   
   collaborate (see also: git help workflows)
      fetch      Download objects and refs from another repository
      pull       Fetch from and integrate with another repository or a local branch
      push       Update remote refs along with associated objects
   
   'git help -a' and 'git help -g' list available subcommands and some
   concept guides. See 'git help <command>' or 'git help <concept>'
   to read about a specific subcommand or concept.

Information on a specific command is obtained by means of ``git help <command>``.

Furthermore, Git provides a number of guides which can be read in a terminal window.
A list of available guides can easily be obtained::

   $ git help -g
   The common Git guides are:
   
      attributes   Defining attributes per path
      everyday     Everyday Git With 20 Commands Or So
      glossary     A Git glossary
      ignore       Specifies intentionally untracked files to ignore
      modules      Defining submodule properties
      revisions    Specifying revisions and ranges for Git
      tutorial     A tutorial introduction to Git (for version 1.5.1 or newer)
      workflows    An overview of recommended workflows with Git
   
   'git help -a' and 'git help -g' list available subcommands and some
   concept guides. See 'git help <command>' or 'git help <concept>'
   to read about a specific subcommand or concept.

For a detailed discussion of Git, the book *Pro Git* by Scott Chacon and Ben
Straub is highly recommended. Its second edition is available in printed form
`online <https://git-scm.com/book/en/v2>`_ where also a PDF version can be downloaded
freely. By the way, the book *Pro Git* as well as the present lecture notes have
been written under version control with Git.

Setting up a local repository
=============================

The use of a version control system is not limited to large software projects
but makes sense even for small individual projects. A prerequisite is the
installation of the Git software which is freely available for Windows, MacOS
and Unix systems from `git-scm.com <https://git-scm.com/>`_. This Git
installation can be used for all projects to be put under version control and
we assume in the following that Git is already installed on the computer. Even
though some graphical user interfaces exist, we will mostly discuss the use of
Git on the command line.

Putting a new project under version control with Git is easy. Once a directory
exists in which the code will be developed, one initializes the repository by
means of::

   $ git init

Note that the dollar sign represents the command line prompt and should not be
typed. Depending on your operating system setup, the dollar could be replaced by
some other character(s). Initializing a new repository in this way will create a
hidden subdirectory called ``.git`` in the directory where you executed the command.
The directory is hidden to avoid that it is accidentally deleted.

.. attention::

   Never delete the directory ``.git`` unless you really want to. You will
   loose the complete history of your project if you did not backup the project
   directory or synchronized your work with a Gitlab server or Github. Removing
   the project directory will remove the subdirectory ``.git`` as well. 

The newly created directory contains a number of files and subdirectories::

   $ ls -a .git
   .  ..  branches  config  description  HEAD  hooks  info  objects  refs

Refrain from modifying anything here as you might mess up files and in this
way loose parts or all of your work.

After having initialized your project, you should let Git know about your name
and your email address by using the following commands::

   $ git config --global user.name <your name>
   $ git config --global user.email <your email>

where the part in angle brackets has to be replaced by the corresponding
information. Enclose the information, in particular your name, in double quotes
if it contains one or more blanks like in the following example::

   $ git config --global user.name "Gert-Ludwig Ingold"

This information will be used by Git when new or modified files are committed
to the repository in order to document who has made the contribution.

If you have globally defined your name and email address as we did here, you do
not need to repeat this step for each new repository. However, you can overwrite
the global configuration locally. This might be useful if you intend to use
a different email address for a specific project.

There are more aspects of Git which can be configured and which are documented
in `Section 8.1 of the Git documentation <https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration>`_. The presently active configuration can be inspected by means of::

   $ git config --list

For example, you might consider setting ``core.editor`` to your preferred editor.

Basic workflow
==============

.. _addcommit:
.. figure:: img/addcommit.*
   :height: 10em
   :align: center

   The transfer of a file to the repository is a two-step process. First one or
   more files are added to the staging area. In a second step, the files are
   committed to the repository.

A basic step in managing a project under version control is the transfer of one
or more new or modified files to the repository where all versions together
with metainformation about them is kept. What looks like a one-step process is
actually done in Git in two steps. For beginners, this two-step process often
gives rise to confusion. We therefore go through the process by means of an
example and make reference to :numref:`addcommit` where the two-step process is
illustrated. A convenient way to check the status of the project files is the
command ``git status``. When working with Git, you will use this command often
to make sure that everything works as expected or to remind yourself of the status
of the project files.

Suppose that we have just initialized our Git repository as expalined in the 
previous section. Then, Git would report the following status::

   $ git status
   On branch master

   Initial commit

   nothing to commit (create/copy files and use "git add" to track)

The output first tells us that we are on a branch called ``master``. Later, we
will discuss the concept of branches and it will be useful to know this
possibility of finding out the current branch. For the moment, we can ignore
this line. Furthermore, Git informs us that we not committed anything yet so 
that the upcoming commit would be the initial one. However, since we have not
created any files, there is nothing to commit. As promised earlier, Git tries
to be helpful and adds some information about what we could do. Obviously, we
first have to create a file in the project directory.

So let us go ahead and create a very simple Python file:

.. code-block:: python

   print("Hello world!")

Now, the status reflects the fact that a new file ``hello.py``  exists::

   $ git status
   On branch master
   
   Initial commit
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   
           hello.py
   
   nothing added to commit but untracked files present (use "git add" to track)

Git has detected the presence of a new file but it is an untracked file which
will basically be ignored by Git. As we ultimately want to include our small
script ``hello.py`` into our repository, we follow the advice and add the
file. According to :numref:`addcommit` this corresponds to moving the file
to the so-called staging area, a prerequisite to ultimately committing the file
to the repository. Let us also check the status after adding the file::

   $ git add hello.py
   $ git status
   On branch master

   Initial commit

   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)

           new file:   hello.py

Note that Git tells us how we could revert the step of adding a file in case of
need.  Having added a file to the staging area does not mean that this file has
vanished from our working directory. As you can easily check, it is still
there.

At this point it is worth emphasizing that we could collect several files in
the staging area. We could then transfer all files to the repository in one single
commit. Committing the file to the respository would be the next logical step.
However, for the sake of illustration, we want to first modify our script. Our
new script could read

.. code-block:: python

   for n in range(3):
       print("Hello world!")

The status now has changed to::

      $ git status
      On branch master
      
      Initial commit
      
      Changes to be committed:
        (use "git rm --cached <file>..." to unstage)
      
              new file:   hello.py
      
      Changes not staged for commit:
        (use "git add <file>..." to update what will be committed)
        (use "git checkout -- <file>..." to discard changes in working directory)
      
              modified:   hello.py

It reflects the fact that now there are two versions of our script ``hello.py``.
The section "Changes to be committed" lists the file or files in the staging area.
In our example, Git refers to the version which we added, i.e. the script consisting
of just a simple line. This version differs from the file present in our working
directory. This two-line script is listed in the section "Changes not staged for commit".
We could move it to the staging area right away or at a later point in case we want to commit
the two versions of the script separately. Note that the most recent version of the script
is no longer listed as untracked file because a previous version had been added and the
file is tracked now by Git.

Having a file in the staging are, we can now commit it by means of ``git commit``.
Doing so will open an editor allowing to define a commit message describing the 
purpose of the commit. The commit message should consist of a single line with
preferably at most 50 characters. If necessary, one can add an empty line followed
by a longer explanatory text. If a single-line commit message suffices, one can
give the message as a command line argument::

   $ git commit -m 'simple hello world script added'
   [master (root-commit) 39977af] simple hello world script added
    1 file changed, 1 insertion(+)
    create mode 100644 hello.py
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)
 
           modified:   hello.py
 
   no changes added to commit (use "git add" and/or "git commit -a")

Checking the status, we see that our two-line script is still unstaged. We could
add it to the staging area and then commit it. Since Git already tracks this file,
we can carry out this procedure in one single step. However, this is only possible
if we do not wish to commit more than one file::

   $ git commit -a -m 'repetition of hello world implemented'
   [master e18f9ff] repetition of hello world implemented
    1 file changed, 2 insertions(+), 1 deletion(-)
   $ git status
   On branch master
   nothing to commit, working tree clean

Now, we have commited two versions of our script as can easily be verified::

   $ git log
   commit e18f9ff9a7f3962c3085334c2de98435402e8fe4
   Author: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
   Date:   Thu Sep 20 14:29:23 2018 +0200

       repetition of hello world implemented

   commit 39977af84732147e09a0177c1521f4a992f30ee6
   Author: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
   Date:   Thu Sep 20 14:24:09 2018 +0200

       simple hello world script added

As we had discussed in :numref:`cvcs-vs-dvcs` the concept of distributed
version control systems does not allow for sequential revision numbers. Our two
commits can thus not be numbered as commit 1 and commit 2. Instead, commits in
Git are identified by their SHA-1 checksum [#sha1]_. The output above lists the
hashes consisting of 40 hexadecimal digits for the two commits. In practice,
when referring to a commit, it is often sufficient to restrict oneself to the
first 6 or 7 digits which typically characterize the commit in a unique way.
To obtain idea of how sensitive the SHA-1 hash is with respect to small changes,
consider the following examples::

   $ echo Python|sha1sum
   79c4e0b5abbd2f67a369ba6ee0b95438c38eb0cb  -
   $ echo python|sha1sum
   32886514c2621f81e01024aa84d0f829d2ce1fad  -

Now that we know how to commit one or more files, one can raise the question of
how often files should be committed. Generally, the rule is to commit often. A
good strategy is to combine changes in such a way that they form a logical
unit.  This approach is particularly helpful if one has to revert to a previous
version.  If a logical change affects several files, it is easy to revert this
change. If on the other hand, a big commit comprises many logically different
changes, one will have to sort out which changes to revert and which ones to
keep. Therefore, it makes sense to aim at so-called atomic commits where a
commit collects all file changes associated with a minimal logical change
[#add-p]_.  On the other hand, in the initial versions of program development,
it often does not make sense to do atomic commits. The situation may change
though as the development of the code progresses.

At the end of this section on the basic workflow, we point out one issue which
in a sense could already be addressed in the initial setting up of the repository,
but which can motivate only now. Having our previous versions safely stored in
the repository, we might be brave enough to refactor our script by defining a
function to repeatedly printing a given text. Doing so, we end up with two files

.. code-block:: python

   # hello.py
   from repeat import repeated_print

   repeated_print("Hello world!", 3)

and

.. code-block:: python

   # repeat.py
   def repeated_print(text, repetitions):
       for n in range(repetitions):
           print(text)

We verify that the scripts do what they are supposed to do ::

   $ python hello.py
   Hello world!
   Hello world!
   Hello world!

Everything works fine so that we add the two files to the staging area and
check the status before committing. ::

   $ git add hello.py
   $ git add repeat.py
   $ git status
   On branch master
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

           modified:   hello.py
           new file:   repeat.py

   Untracked files:
     (use "git add <file>..." to include in what will be committed)

           __pycache__/

Everything looks fine except for the fact that there is an untracked directory
``__pycache__``. This directory and its content are created during the import of
``repeat.py`` and should not go into the repository. After all, they are automatically
generated when needed. Here, it comes in handy to make use of a ``.gitignore`` file.
Each line in this file contains one entry which defines files to be ignored by Git.
For projects based on Python, Github proposes a ``.gitignore`` file starting with
the following lines::

   # Byte-compiled / optimized / DLL files
   __pycache__/
   *.py[cod]
   *$py.class

Lines starting with # are interpreted as comments. The second line excludes the
directory ``__pycache__`` as well as its content. The star in the last two
lines can replace any number of characters. The third line will exclude all
files ending with ``.pyc``, ``.pyo``, and ``.pyc``. For more details see ``git
help ignore`` and the `collection of gitignore files
<https://github.com/github/gitignore>`_, in particular ``Python.gitignore``.
The ``.gitignore`` file should be put under version control as it might develop
over time.

Working with branches
=====================

Collaborative code development with Gitlab
==========================================

.. _gitlab:
.. figure:: img/gitlab.*
   :width: 30em
   :align: center

   Workflow for collaborative development in a distributed version control system
   with a Gitlab instance as central server.


.. [#gitlab_uaux] The computing center of the University of Augsburg is running
   a Gitlab server at ``git.rz.uni-augsburg.de`` which is accessible to anybody
   in possession of a valid user-ID of the computing center.

.. [#sha1] SHA-1 is a hash checksum which characterizes an object but does not
   allow to reconstruct it. Consisting of 160 bits, it allows for
   :math:`2^{160}\approx 10^{48}` different values.

.. [#add-p] Occasionally, one has made several changes which should be separated
   into different atomic commits. In such a case ``git add -p`` might come in
   handy as it allows to select chunks of code while adding a file to the 
   staging area.
