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
  
<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
The use of a version control system is no substitute for project management and  for attributing tasks to developers.
    </div>
  </div>
</div>

---

# Centralized version control systems

<br>

<img src="/images/cvcs.png" style="width: 60%; margin: auto">

<br>

* sequential revisions of project states encompassing all files present at a certain moment
* an internet connection to the server is needed in order to record changes and create a new revision

---

# Distributed version control system

<br>

<img src="/images/dvcs.png" style="width: 70%; margin: auto">

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

<div>In practice, even for a distributed version control system there is a central
server through which users exchange their versions.</div>

<br>

<img src="/images/dvcs-github.png" style="width: 40%; margin: auto">

<br>

* exchange of versions between collaborating users via a GitLab server or GitHub
* user does not need to be connected to server in order to commit new versions
* GitLab instances, e.g. `git.rz.uni-augsburg.de`, access via computing center credentials
* GitHub ([github.com](https://github.com))

---

# Git

<div>
  
Webpage:  [git-scm.com](https://git-scm.com)
  
</div>

* Git software for Linux, macOS, Windows
* GUIs, e.g. for Windows: TortoiseGit  
  - IDEs often offer Git integration  
  - we will use Git on the command line
* documentation ([git-scm.com/doc](https://git-scm.com/doc))
  - man pages ([git-scm.com/docs](https://git-scm.com/docs))
  - Pro Git book ([git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)), electronic version free
  - cheat sheets: [training.github.com](https://training.github.com/), [ndpsoftware.com/git-cheatsheet.htm](https://ndpsoftware.com/git-cheatsheet.htm)

---

# Getting help on Git

```console {1|2-}{maxHeight:'450px'}
$ git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

```

---

# Getting help on a subcommand

<div></div>example:

```console {1|2-}{maxHeight:'400px'}
$ git --help init
GIT-INIT(1)                                   Git Manual                                  GIT-INIT(1)

NAME
       git-init - Create an empty Git repository or reinitialize an existing one

SYNOPSIS
       git init [-q | --quiet] [--bare] [--template=<template_directory>]
                 [--separate-git-dir <git dir>] [--object-format=<format>]
                 [-b <branch-name> | --initial-branch=<branch-name>]
                 [--shared[=<permissions>]] [directory]

DESCRIPTION
       This command creates an empty Git repository - basically a .git directory with subdirectories
       for objects, refs/heads, refs/tags, and template files. An initial branch without any commits
       will be created (see the --initial-branch option below for its name).

       If the $GIT_DIR environment variable is set then it specifies a path to use instead of ./.git
       for the base of the repository.

       If the object storage directory is specified via the $GIT_OBJECT_DIRECTORY environment
       variable then the sha1 directories are created underneath - otherwise the default
       $GIT_DIR/objects directory is used.

       Running git init in an existing repository is safe. It will not overwrite things that are
       already there. The primary reason for rerunning git init is to pick up newly added templates
       (or to move the repository to another place if --separate-git-dir is given).

OPTIONS
       -q, --quiet
           Only print error and warning messages; all other output will be suppressed.

       --bare
           Create a bare repository. If GIT_DIR environment is not set, it is set to the current
           working directory.

       --object-format=<format>
           Specify the given object format (hash algorithm) for the repository. The valid values are
           sha1 and (if enabled) sha256.  sha1 is the default.

           THIS OPTION IS EXPERIMENTAL! SHA-256 support is experimental and still in an early stage.
           A SHA-256 repository will in general not be able to share work with "regular" SHA-1
           repositories. It should be assumed that, e.g., Git internal file formats in relation to
           SHA-256 repositories may change in backwards-incompatible ways. Only use
           --object-format=sha256 for testing purposes.

       --template=<template_directory>
           Specify the directory from which templates will be used. (See the "TEMPLATE DIRECTORY"
           section below.)

       --separate-git-dir=<git dir>
           Instead of initializing the repository as a directory to either $GIT_DIR or ./.git/,
           create a text file there containing the path to the actual repository. This file acts as
           filesystem-agnostic Git symbolic link to the repository.

           If this is reinitialization, the repository will be moved to the specified path.

       -b <branch-name>, --initial-branch=<branch-name>
           Use the specified name for the initial branch in the newly created repository. If not
           specified, fall back to the default name (currently master, but this is subject to change
           in the future; the name can be customized via the init.defaultBranch configuration
           variable).

       --shared[=(false|true|umask|group|all|world|everybody|0xxx)]
           Specify that the Git repository is to be shared amongst several users. This allows users
           belonging to the same group to push into that repository. When specified, the config
           variable "core.sharedRepository" is set so that files and directories under $GIT_DIR are
           created with the requested permissions. When not specified, Git will use permissions
           reported by umask(2).

           The option can have the following values, defaulting to group if no value is given:

           umask (or false)
               Use permissions reported by umask(2). The default, when --shared is not specified.

           group (or true)
               Make the repository group-writable, (and g+sx, since the git group may be not the
               primary group of all users). This is used to loosen the permissions of an otherwise
               safe umask(2) value. Note that the umask still applies to the other permission bits
               (e.g. if umask is 0022, using group will not remove read privileges from other
               (non-group) users). See 0xxx for how to exactly specify the repository permissions.

           all (or world or everybody)
               Same as group, but make the repository readable by all users.

           0xxx
               0xxx is an octal number and each file will have mode 0xxx.  0xxx will override users'
               umask(2) value (and not only loosen permissions as group and all does).  0640 will
               create a repository which is group-readable, but not group-writable or accessible to
               others.  0660 will create a repo that is readable and writable to the current user and
               group, but inaccessible to others.

       By default, the configuration flag receive.denyNonFastForwards is enabled in shared
       repositories, so that you cannot force a non fast-forwarding push into it.

       If you provide a directory, the command is run inside it. If this directory does not exist, it
       will be created.
       
TEMPLATE DIRECTORY
       Files and directories in the template directory whose name do not start with a dot will be
       copied to the $GIT_DIR after it is created.

       The template directory will be one of the following (in order):

       •   the argument given with the --template option;

       •   the contents of the $GIT_TEMPLATE_DIR environment variable;

       •   the init.templateDir configuration variable; or

       •   the default template directory: /usr/share/git-core/templates.

       The default template directory includes some directory structure, suggested "exclude patterns"
       (see gitignore(5)), and sample hook files.

       The sample hooks are all disabled by default. To enable one of the sample hooks rename it by
       removing its .sample suffix.

       See githooks(5) for more general info on hook execution.

EXAMPLES
       Start a new Git repository for an existing code base

               $ cd /path/to/my/codebase
               $ git init      (1)
               $ git add .     (2)
               $ git commit    (3)

           1. Create a /path/to/my/codebase/.git directory.
           2. Add all existing files to the index.
           3. Record the pristine state as the first commit in the history.

GIT
       Part of the git(1) suite

Git 2.34.1                                    07/07/2023                                  GIT-INIT(1)


```

---

# Some topical guides on Git

```console {1|2-}{maxHeight:'450px'}
$ git help -g

The Git concept guides are:
   attributes          Defining attributes per path
   cli                 Git command-line interface and conventions
   core-tutorial       A Git core tutorial for developers
   credentials         Providing usernames and passwords to Git
   cvs-migration       Git for CVS users
   diffcore            Tweaking diff output
   everyday            A useful minimum set of commands for Everyday Git
   faq                 Frequently asked questions about using Git
   glossary            A Git Glossary
   hooks               Hooks used by Git
   ignore              Specifies intentionally untracked files to ignore
   mailmap             Map author/committer names and/or E-Mail addresses
   modules             Defining submodule properties
   namespaces          Git namespaces
   remote-helpers      Helper programs to interact with remote repositories
   repository-layout   Git Repository Layout
   revisions           Specifying revisions and ranges for Git
   submodules          Mounting one repository inside another
   tutorial            A tutorial introduction to Git
   tutorial-2          A tutorial introduction to Git: part two
   workflows           An overview of recommended workflows with Git

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

---
layout: gli-two-cols-header
---

# First step: Setting up a local repository

::left::

##### create a new directory for the repository

```console
$ mkdir <myrepo>
$ cd <myrepo>
```

* `<myrepo>` should be replaced by a suitable name
* `mkdir` = **m**a**k**e **dir**ectory
* `cd` = **c**hange **d**irectory

<br>

##### iniitalize the repository
```console
$ git init
```

* a hidden subdirectory `.git` has been created

```console
$ ls -a
.  ..  .git
```

* `ls`: **l**i**s**t content of directory
* option `-a`: do not ignore entries starting with `.`


::right::

#### content of the `.git` directory

```console
$ ls -l .git
total 32
-rw-rw-r-- 1 ingold ingold   23 Apr 12 10:47 HEAD
drwxrwxr-x 2 ingold ingold 4096 Apr 12 10:47 branches
-rw-rw-r-- 1 ingold ingold   92 Apr 12 10:47 config
-rw-rw-r-- 1 ingold ingold   73 Apr 12 10:47 description
drwxrwxr-x 2 ingold ingold 4096 Apr 12 10:47 hooks
drwxrwxr-x 2 ingold ingold 4096 Apr 12 10:47 info
drwxrwxr-x 4 ingold ingold 4096 Apr 12 10:47 objects
drwxrwxr-x 4 ingold ingold 4096 Apr 12 10:47 refs
```

* option `-l`: long listing format

<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800">
  <div class="grid grid-cols-[4%_1fr] gap-10">
    <div><carbon-warning-alt class="text-red-800 text-3xl" /></div>
    <div>
      The directory <code>.git</code> is where the repository lives.
      Do not delete this directory or tamper with it. Otherwise
      your work might be lost.
      <br>
      You have been warned!
    </div>
  </div>
</div>

---

# Personalize your repository

<div></div>
Git records the name of the user committing changes to the code. It therefore needs to know who you are.

This information later can help to find out who introduced a mistake or who added an important piece of code.

```console
$ git config --global user.name <your name>
$ git config --global user.email <your email>
```

* enclose argument in double quotes if it contains whitespace, e.g. the name
* The commands above configure name and email globally, so that this step is only needed once. A local
  configuration per repository is also possible, e.g. if another email address should be used.
* Many aspects of Git can be configured. For details see [chapter 8.1 of the Pro Git book](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).  
  Example: configuration of a default editor
  ```console
  $ git config --global core.editor vim
  ```
* list configuration
  ```console
  $ git config --list
  user.name=Gert-Ludwig Ingold
  user.email=gert.ingold@physik.uni-augsburg.de
  ⋮
  ```
  
---

# Basic workflow in a local repository

<br>

<img src="/images/addcommit.png" style="width: 50%; margin: auto">

<br>

* modifications to several files can be combined in the staging area to a single commit
* a file can exist in different versions at the same time
  - a committed version in the local repository
  - a version staged for going to be committed
  - the version in the working directory which may already contain additional modifications
  - It is possible to move a file from the staging are back to the working directory (see later).

---

# The state of affairs

#### `git status` gives valuable information about the repository.

* On which branch are we?
* status relative to the corresponding remote branch
* files staged for commit including help how to remove files from the staging area
* files in the working directory and known to Git but containing additional modifications
* untracked files

<br>

#### immediately after initialization the status is as follows

```console {1|2|4|6}
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

<v-click>

<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
    Use <code>git status</code> frequently, in particular when unsure whether things are running correctly.
    </div>
  </div>
</div>

</v-click>

---

# A new file

```python
# hello.py
print("Hello world!")
```

<br>

```console {1|6-8}
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

<br>

* there is a new file not known to Git so far
* the file can be added to the staging area by means of `git add`

---

# Adding the file to the staging area

```console
git add hello.py
```

<br>

```console {1|6-8}
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.py

```

<br>

* The file `hello.py` has been added to the staging area and can be committed to the Git
  repository in the next step.
* The file is still present in the working directory.
* Additional files can be added to the staging area in order to commit them together.
* Git tells us how to unstage the file if necessary.

---

# Further modification of the uncommitted file

````md magic-move
```python
# hello.py
print("Hello world!")
```
```python
# hello.py
for n in range(3):
    print("Hello world!")
```
````

<v-click>
```console {1|4|6-8|10-13}
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py
```
</v-click>

<v-after>

* two different versions of the script, one in the working directory, the other one in the staging
  area
* different options:
  - commit first version, add second version and commit it → two commit messages
  - add second version and commit everything → only one commit message

</v-after>

---

# Our first commit

```console
$ git commit -m 'simple hello world script added'
[master (root-commit) 11e2d07] simple hello world script added
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

* argument `-m` contains commit message (preferably less than 50 characters)
* Alternatively, option `-m` can be omitted. Then, an editor will be opened to enter the commit
  message which can consist of a single line or a single line and some additional text separated
  by an empty line.

```console
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

* There exist further changes (the loop) which could now be staged and committed.

---

# Adding and committing

```console
$ git commit -a -m 'repetition of hello world implemented'
[master 52b9aa8] repetition of hello world implemented
 1 file changed, 2 insertions(+), 1 deletion(-)
```

* For a single file, option `-a` adds the file to the staging area and commits it at the same time.

<br>

```console
$ git status
On branch master
nothing to commit, working tree clean
```

* The changes are committed to the repository and presently there is nothing to add to the
  staging area or to commit to the repository.

<br>

#### Basic step

* add changes (or a new file) to the staging area and then commit to the repository
* Changes to several files can be collected in a single commit. This makes particularly sense
  when the changes are logically connected. 

---

# Commit history

```console {1|2-6|8-12}
$ git log
commit 52b9aa80d2441b3d8a7363affbffb9694ee16750 (HEAD -> master)
Author: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
Date:   Fri Apr 12 16:19:41 2024 +0200

    repetition of hello world implemented

commit 11e2d079a65485959e1aa62a0af5d9a5fbebf8d4
Author: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
Date:   Fri Apr 12 16:12:18 2024 +0200

    simple hello world script added
```

* most recent commit at top
* So far, the history is linear, but later there will be parallel branches even for a single user.
  Therefore, there cannot be a counter associated with the commits. Instead, a hash value is used.
* File versions, entire commits, etc. are characterized by a hash value which
  - is used to identify objects and to organize them in the `.git` directory
  - allows to decide easily whether a file has been modified

---

# Secure Hash Algorithm 1 (SHA1)

```console
$ echo Python | sha1sum
79c4e0b5abbd2f67a369ba6ee0b95438c38eb0cb  -
$ echo python | sha1sum
32886514c2621f81e01024aa84d0f829d2ce1fad  -
```

<br>

* Even small differences lead to huge changes in the SHA1 value.
* 160 bits implies 2<sup>160</sup> ≈ 1.46·10<sup>48</sup> different hash values. The same SHA1 value
  for different strings is highly unlikely but not excluded.
* SHA1 has should no longer be used for security-related applications like cryptographic signing.

<br>

* For practical purposes with Git, it is usually sufficient to specify the first 6 or 7 hexadecimal
  digits of the hash value in order to uniquely identify a commit.

---

# How often to commit?

* In a distributed version control system it is possible to commit as often as one wishes
  because no internet connectivity is needed.
  
<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
    <b>atomic commit</b><br>
    collect all modifications associated with one minimal logical change in one commit
    </div>
  </div>
</div>

<br>

* Do not combine different logical changes in a single commit. This might later help to revert well defined changes.
* `git add -p`: The option `-p` is helpful when you want to stage only some of the changes which you have made.
* At the beginning of a project, atomic commits might not be that useful.
* Atomic commits might be more useful for code development but less when a text or a presentation is developped
  in a version control system.
* In the end it is up to you to decide what best suits your needs.

---

# Let us slightly refactor our code

````md magic-move
```python
# hello.py
for n in range(3):
    print("Hello world!")
```
```python
# hello.py
repeated_print("Hello world!", 3)
```
```python
#hello.py
from repeat import repeated_print

repeated_print("Hello world!", 3)
```
````

<v-click>
```python
# repeat.py
def repeated_print(text, repetitions):
    for n in range(repetitions):
        print(text)
```
</v-click>

<br>

<v-click>
Let us check whether the code still works:

```console
$ python hello.py
Hello world!
Hello world!
Hello world!
```
</v-click>

---

# Irrelevant objects appear

```console {all|8,10,11}
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        geändert:       hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        __pycache__/
        repeat.py

no changes added to commit (use "git add" and/or "git commit -a")
```

```console {hide|1|5,8,10}
$ ls -lR
.:
insgesamt 12
-rw-rw-r-- 1 gert gert   69 Apr 13 13:42 hello.py
drwxrwxr-x 2 gert gert 4096 Apr 13 13:42 __pycache__
-rw-rw-r-- 1 gert gert   92 Apr 13 13:42 repeat.py

./__pycache__:
insgesamt 4
-rw-rw-r-- 1 gert gert 393 Apr 13 13:42 repeat.cpython-311.pyc
```

---

# Let Git ignore objects

```console
# .gitignore
__pycache__/
```

```console {hide|all|8,10-11}
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        repeat.py

no changes added to commit (use "git add" and/or "git commit -a")
```

<v-click>

* the directory `__pycache__/` is no longer listed
* wildcards can be used: `*.py[cod]` corresponds to all files with extensions `pyc`, `pyo`, or `pyd`
* put `.gitignore` into version control
* [github.com/github/gitignore](https://github.com/github/gitignore) contains a number of
  `.gitignore` files for different programming languages

</v-click>

---

# What should or should not be committed?

#### to be committed

* all sources which are needed for the project
* this includes information about the software environment, e.g. which library versions
  have been used

<br>

#### not to be committed

* results to not need to be committed, because they can usually be reconstructed
* data of extensive calculations should be stored and backed up separately
* Changes to non-text files like images or PDF files are usually non-local. Therefore
  such files should not be put into version control in most cases as they will take
  a lot of disk space.

---

# The `master` branch 

* So far, we have been working with only one branch.
* This branch was called `master` but the name is not really important. GitHub uses the name `main`
  instead.
* There can be other branches, e.g. to separate production code and development code.
* In addition to local branches, there can be remote branches.

<br>

```console
$ git log --oneline --graph --decorate --all
* 4a97579 (HEAD -> master) .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

* So far, we have a linear history involving only the branch `master`.
* In our working directory, we have commit `4a97579` which is referred to as `HEAD`.

---

# Creating a development branch

```console
$ git branch
* master
```

* We only have one branch and the asterisk indicates that this is the branch on which we are at present.

<br>

* Create a development branch called `dev`. Other names could be used as well to identify the branch.

```console
$ git switch -c dev
Switched to a new branch 'dev'
```

* `switch` switches the branch, `-c` implies creation of a new branch.

```console {all|2}
$ git branch
* dev
  master
```

<br>
Alternative:

```console
$ git branch dev
$ git switch dev
```

---

# Switching back and forth

```console
$ git branch
* dev
  master
```

```console
$ git switch master
Switched to branch »master«
```

```console
$ git branch
  dev
* master
```

```console
$ git switch dev
Switched to branch »dev«
```

```console {all|2}
git log  --oneline --graph --decorate=short --all
* 4a97579 (HEAD -> dev, master) .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

* `HEAD` is now pointing to the `dev` branch.
* Commit `4a97579` belongs both to the `master` branch and the `dev` branch.

---

# Let us do some work in the `dev` branch

````md magic-move
```python
#hello.py
from repeat import repeated_print

repeated_print("Hello world!", 3)
```
```python
# hello.py
from repeat import repeated_print

def hello(name="", repetitions=1):
    if name:
        repeated_print(f"Hello, {name}", repetitions)
    else:
        repeated_print("Hello world!", repetitions)
```
````

```console {hide|all|2,3}
$ git log --oneline --graph --decorate --all
* d5a8fb8 (HEAD -> dev) name as new argument implemented
* 4a97579 (master) .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

<br>

<v-click>

* Commit `d5a8fb8` is on the branch `dev` while master is still at commit `4a97579`.
* So far, the history is still linear.

</v-click>

---

# Switching back and forth

#### `dev` branch

```console {all|2}
$ git branch
* dev
  master
```

```console
$ cat hello.py
from repeat import repeated_print

def hello(name="", repetitions=1):
    if name:
        repeated_print(f"Hello, {name}", repetitions)
    else:
        repeated_print("Hello world!", repetitions)
```

#### `master` branch

```console
$ git switch master
Switched to branch »master«
```
```console
$ cat hello.py
from repeat import repeated_print

repeated_print("Hello world!", 3)
```

---

# Improvement in the `master` branch
  
<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
    Before beginning with your work, make sure that you are in the correct branch:<br>
    <code>git branch</code> or <code>git status</code>
    </div>
  </div>
</div>

```console
$ git branch
  dev
* master
```

<br>

#### add default value to argument `repetitions`

````md magic-move
```python
# repeat.py
def repeated_print(text, repetitions):
    for n in range(repetitions):
        print(text)
```
```python
# repeat.py
def repeated_print(text, repetitions=1):
    for n in range(repetitions):
        print(text)
```
````

<br>

<v-click>

#### commit and go back to the `dev` branch

```console
$ git commit -a -m 'default value for number of repetitions defined'
$ git switch dev
```

</v-click>

---

# Two branches

```console
$ git log --oneline --graph --decorate --all
* 598bbf7 (master) default value for number of repetitions defined
| * d5a8fb8 (HEAD -> dev) name as new argument implemented
|/  
* 4a97579 .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

* The history is no longer linear. We now have changes in two parallel branches.
* We are in the `dev` branch. Therefore, `HEAD` is pointing to `dev`.

---

# Do some more changes to the `hello.py` script

````md magic-move
```python
# hello.py
from repeat import repeated_print

def hello(name="", repetitions=1):
    if name:
        repeated_print(f"Hello, {name}", repetitions)
    else:
        repeated_print("Hello world!", repetitions)
```
```python
# hello.py
from repeat import repeated_print

def hello(name="", repetitions=1):
    if name:
        repeated_print(f"Hello, {name}!", repetitions)
    else:
        repeated_print("Hello world!", repetitions)
```
```python
# hello.py
from repeat import repeated_print

def hello(name="", repetitions=1):
    if name:
        repeated_print(f"Hello, {name}!", repetitions)
    else:
        repeated_print("Hello world!", repetitions)

if __name__ == "__main__":
    hello("Alice", 3)
```
````

<v-clicks at="1">

* add the missing exclamation mark
* add a function call

</v-clicks>

<br>

<v-click>

* What about atomic commits?  
  These two changes are not logically related.

</v-click>

---

# What did we change?

```console {1|all}
$ git diff
diff --git a/hello.py b/hello.py
index 539c294..1240711 100644
--- a/hello.py
+++ b/hello.py
@@ -2,6 +2,9 @@ from repeat import repeated_print
 
 def hello(name="", repetitions=1):
     if name:
-        repeated_print(f"Hello, {name}", repetitions)
+        repeated_print(f"Hello, {name}!", repetitions)
     else:
         repeated_print("Hello world!", repetitions)
+
+if __name__ == "__main__":
+    hello("Alice", 3)
```

* `git diff` helps if you want to know what modifications have been made
* `git diff` works also if more than one file has been modified

---

# `git add -p`

```console
$ git add -p hello.py
diff --git a/hello.py b/hello.py
index 539c294..1240711 100644
--- a/hello.py
+++ b/hello.py
@@ -2,6 +2,9 @@ from repeat import repeated_print
 
 def hello(name="", repetitions=1):
     if name:
-        repeated_print(f"Hello, {name}", repetitions)
+        repeated_print(f"Hello, {name}!", repetitions)
     else:
         repeated_print("Hello world!", repetitions)
+
+if __name__ == "__main__":
+    hello("Alice", 3)
(1/1) Stage this hunk [y,n,q,a,d,s,e,?]?
```

```console {all}{maxHeight:'100px'}
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
s - split the current hunk into smaller hunks
e - manually edit the current hunk
? - print help
```

---

# Split the changes

```console 
(1/1) Stage this hunk [y,n,q,a,d,s,e,?]? s
Split into 2 hunks.
@@ -2,6 +2,6 @@
 
 def hello(name="", repetitions=1):
     if name:
-        repeated_print(f"Hello, {name}", repetitions)
+        repeated_print(f"Hello, {name}!", repetitions)
     else:
         repeated_print("Hello world!", repetitions)
(1/2) Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]? y
@@ -6,2 +6,5 @@
     else:
         repeated_print("Hello world!", repetitions)
+
+if __name__ == "__main__":
+    hello("Alice", 3)
(2/2) Stage this hunk [y,n,q,a,d,K,g,/,e,?]? n
```

* now we can commit the first change
* the other change can be put into a separate commit after a simple `git add`

---

# Merging two branches

```console
$ git log --oneline --graph --decorate --all
* 3915166 (HEAD -> dev) function call added
* 8b7465e exclamation mark added
* d5a8fb8 name as new argument implemented
| * 598bbf7 (master) default value for number of repetitions defined
|/  
* 4a97579 .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

<br>

#### merge `dev` branch into `master` branch

```console
$ git switch master
Switched to branch »master«
```

* switch to the `master` branch first
* now we can merge `dev` into `master`

---

# Merging two branches

```console
$ git merge dev
Merge made by the 'ort' strategy.
 hello.py | 9 ++++++++-
 1 file changed, 8 insertions(+), 1 deletion(-)
```

```console
$ git log --oneline --graph --decorate --all
*   9137444 (HEAD -> master) Merge branch 'dev'
|\  
| * 3915166 (dev) function call added
| * 8b7465e exclamation mark added
| * d5a8fb8 name as new argument implemented
* | 598bbf7 default value for number of repetitions defined
|/  
* 4a97579 .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

* In this case, merging of the two branches could be done cleanly.
* The new version of combines the changes made in the two branches.

---

# Merging

##### common ancestor

```python
# repeat.py 4a97579
def repeated_print(text, repetitions):
    for n in range(repetitions):
        print(text)

```

<br>

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
<h5>version in <code>master</code> branch</h5>

```python
# repeat.py 598bbf7
def repeated_print(text, repetitions=1):
    for n in range(repetitions):
        print(text)
```
</div>
<div>
<h5>version <code>dev</code> branch</h5>

```python
# repeat.py 3915166
def repeated_print(text, repetitions):
    for n in range(repetitions):
        print(text)
```
</div>
</div>

<br>

##### merged version

```python
# repeat.py 9137444
def repeated_print(text, repetitions=1):
    for n in range(repetitions):
        print(text)
```

---

# Deleting a branch

* The branch `dev` can be kept for further development.
* It can also be deleted and a new branch `dev` can be created later.

```console
$ git branch -d dev
Deleted branch dev (was 3915166).
```

* If changes could be lost, the option `-d` is not sufficient to delete the branch.
  Use `-D` if the deletion of the branch is really wanted.

```console
$ git log --oneline --graph --decorate --all
*   9137444 (HEAD -> master) Merge branch 'dev'
|\  
| * 3915166 function call added
| * 8b7465e exclamation mark added
| * d5a8fb8 name as new argument implemented
* | 598bbf7 default value for number of repetitions defined
|/  
* 4a97579 .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

---

# Merge conflicts

* merge conflicts can happen if changes in different branches are inconsistent

<br>

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
<h5>version in <code>master</code> branch</h5>

```python
# repeat.py 6adb4bd
def repeated_print(text, repetitions=1):
    """print text repeatedly

    """
    for n in range(repetitions):
        print(text)
```
</div>
<div>
<h5>version <code>dev</code> branch</h5>

```python
# repeat.py d7f54e0
def repeated_print(text, repetitions):
    """print text several times"""
    for n in range(repetitions):
        print(text)
```
</div>
</div>

<br>

```console
$ git log --oneline --graph --decorate --all
* 6adb4bd (master) doc string added
*   9137444 Merge branch 'dev'
|\  
* | 598bbf7 default value for number of repetitions defined
| | * d7f54e0 (HEAD -> dev) added a doc string
| |/  
| * 3915166 function call added
⋮  ⋮
```

---

# Merge conflicts

```console {all|6,7}
$ git branch
  dev
* master
$ git merge dev
Auto-merging repeat.py
CONFLICT (content): Merge conflict in repeat.py
Automatic merge failed; fix conflicts and then commit the result.
```
<v-click>

* open file(s) with merge conflicts in an editor

</v-click>

<v-after>

```console {all|2-7|7-10}
 # repeat.py
 <<<<<<< HEAD
 def repeated_print(text, repetitions=1):
     """print text repeatedly
 
     """
 =======
 def repeated_print(text, repetitions):
     """print text several times"""
 >>>>>>> dev
     for n in range(repetitions):
         print(text)
```

</v-after>
<v-click>

* edit as needed, then add to staging area and commit

</v-click>

---

# History after resolution of merge conflict

```console
$ git log --oneline --graph --decorate --all
*   ee1bcde (HEAD -> master) Merge branch 'dev'
|\  
| * d7f54e0 (dev) added a doc string
* | 6adb4bd doc string added
* | 9137444 Merge branch 'dev'
|\| 
| * 3915166 function call added
| * 8b7465e exclamation mark added
| * d5a8fb8 name as new argument implemented
* | 598bbf7 default value for number of repetitions defined
|/  
* 4a97579 .gitignore for Python added
* 0c227f4 hello world script refactored
* 52b9aa8 repetition of hello world implemented
* 11e2d07 simple hello world script added
```

* Collaborative development makes merge conflicts more likely.
  
<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
     A good project management can help to avoid merge conflicts. 
    </div>
  </div>
</div>

---

# Collaborative development with GitLab

+ problem: several or even many developers who do not grant access to their computers
+ solution: exchange code via a server (GitLab server or GitHub)

<br>

#### typical scenario with more than one user

<br>

<div class="grid grid-cols-[60%_1fr] gap-8">
 <div><img src="/images/gitlab.png" style="width: 100%; margin: auto"></div>
 <div>

  #### project maintainer

  * public repository `upstream`
  * only needed in a multi-developer scenario

  #### user(s)
  
  * private local Git repository
  * public repository `origin` to make code available to `upstream` repository
 </div>
</div>

---

# Creating a new project on GitLab

<div class="grid grid-cols-[30%_1fr] gap-8">
 <div><img src="/images/gitlab-create-project-1.png" style="width: 100%; margin: auto"></div>
 <div><img src="/images/gitlab-create-project-2.png" style="width: 100%; margin: auto"></div>
</div>

* Create blank project  
  - add a README file to allow for cloning locally
  - do not add a README file to push a local repository
* Create from template  
  sets up a structure for certain application scenarios (not relevant for us
* Import project  
  access via https, http, or git protocol to existing repository necessary

---

# Setting up the project

<div><img src="/images/gitlab-create-project-3.png" style="width: 90%; margin: auto"></div>

<br>

* For the purposes of the method course, make the repository private and add collaborators
  manually.

---

# The initial commit

<div><img src="/images/gitlab-create-project-4.png" style="width: 60%; margin: auto"></div>

<br>

* README file can be edited using markdown syntax (see [commonmark.org/help](https://commonmark.org/help))
* »Code« button lists addresses for cloning via http and ssh protocols
* at the top right, the repository can be forked

---

# Parenthesis on SSH keys: Two protocols

<div><img src="/images/code_urls.png" style="width: 32%; margin: auto;"></div>

<br>

#### Two different protocols
* `http`: hypertext transfer protocol  
  * needs username and password for authentification on the GitLab server 
* `ssh`: secure shell
  * generate an SSH key pair and put *public* key on GitLab server
  * Use *private* key for authentification. A passphrase may be needed to use the private key.
  * secure communication with GitLab server
  * commits can be signed with a SSH key

---

# Parenthesis on SSH keys: Asymmetric key pair

<br>

<div><img src="/images/asymmetric_encryption.png" style="width: 100%; margin: auto;"></div>
<div style="font-size: small;padding-top: 10px;text-align: right;">(adapted from Wikipedia)</div>

* *public* key allows to encrypt message
* decryption requires *private* key

<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800" style="width: 60%;margin: auto;">
  <div class="grid grid-cols-[4%_1fr] gap-10">
    <div><carbon-warning-alt class="text-red-800 text-3xl" /></div>
    <div>
      Distribute the public key, but keep the private key safe!
    </div>
  </div>
</div>

---

# Parenthesis on SSH keys: Key pair generation

* Check first whether you already have a key pair in your directory `$HOME/.ssh`
* If not, generate a key pair. There are different algorithms available. Presently,
  ED25519 is recommended:
  ```console
  $ ssh-keygen -t ed25519
  Generating public/private ed25519 key pair.
  Enter file in which to save the key (/home/ingold/.ssh/id_ed25519): 
  Enter passphrase (empty for no passphrase): 
  Enter same passphrase again: 
  Your identification has been saved in /home/ingold/.ssh/id_ed25519
  Your public key has been saved in /home/ingold/.ssh/id_ed25519.pub
  The key fingerprint is:
  SHA256:9+VBe2dwBxkrPLyErXboCJYIy7SwqBh2HNCCDPX+NT0 ingold@laptop-tp14-1
  The key's randomart image is:
  +--[ED25519 256]--+
  |=oo           oo |
  |.o.o       =  .o |
  |. +..     . B + o|
  |.=.=.. . . + = +.|
  |+.+oo + S E o + +|
  |+..  o o * + o +.|
  |o     . . . . .  |
  |                 |
  |                 |
  +----[SHA256]-----+
  ```

---

# Parenthesis on SSH keys: A key pair

```console
$ ls -l .ssh
total 8
-rw------- 1 ingold ingold 464 Apr 30 15:10 id_ed25519
-rw-r--r-- 1 ingold ingold 102 Apr 30 15:10 id_ed25519.pub
```

* The longer key `id_ed25519` is the *private* key while the shorter key `id_ed25519.pub`
  is the *public* key.
* The public key has the form
  ```console
  $ cat .ssh/id_ed25519.pub
  ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJJ6q/C9VqYciIC45J5wTF2zdkuN4zEIwQGPiiGrSG7B gert.ingold@uni-a.de
  ```

* The private key starts and ends with
  ```console
  -----BEGIN OPENSSH PRIVATE KEY-----
  …
  -----END OPENSSH PRIVATE KEY-----

  ```

* Keep the private key secret.

---

# Parenthesis on SSH keys: Adding public key to GitLab

<div class="grid grid-cols-[1fr_1fr] gap-8">
 <div><img src="/images/add_sshkey_1.png" style="width: 100%; margin: auto"></div>
 <div><img src="/images/add_sshkey_2.png" style="width: 100%; margin: auto"></div>
</div>

<div><img src="/images/add_sshkey_3.png" style="width: 100%; margin: auto"></div>

---

# Parenthesis on SSH keys: Update remote repositories

```console
$ git remote -v
origin  http://gitlab.local:30080/ingold/example.git (fetch)
origin  http://gitlab.local:30080/ingold/example.git (push)
upstream  http://gitlab.local:30080/boss/example.git (fetch)
upstream  http://gitlab.local:30080/boss/example.git (push)
```

```console
$ git remote remove origin
$ git remote add origin git@gitlab.local:30022/boss/example.git
$ git remote remove upstream
$ git remote add upstream git@gitlab.local:30022/ingold/example.git
```

```console
$ git remote -v
origin  git@gitlab.local:30022/ingold/example.git (fetch)
origin  git@gitlab.local:30022/ingold/example.git (push)
upstream  git@gitlab.local:30022/boss/example.git (fetch)
upstream  git@gitlab.local:30022/boss/example.git (push)
```

---

# Parenthesis on SSH keys: `ssh-add`

* Each time the private SSH key is accessed, the passphrase needs
  to be entered. How can this be avoided?
* Use `ssh-add` in order to add keys to the SSH authentication agent.

```console
$ ssh-add -L
The agent has no identities.
```

* option `-L` lists the keys available to the agent

<br>

#### adding an SSH key
```console
$ ssh-add
Enter passphrase for /home/ingold/.ssh/id_ed25519: 
Identity added: /home/ingold/.ssh/id_ed25519 (gert.ingold@uni-a.de)
$ ssh-add -L
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJJ6q/C9VqYciIC45J5wTF2zdkuN4zEIwQGPiiGrSG7B gert.ingold@uni-a.de
```

* After `ssh-add` there is no need anymore to enter the passphrase.
* `ssh-add` needs to be executed again after the next login, if needed


---

# Inviting collaborators

<div class="grid grid-cols-[60%_1fr] gap-8">
<div><img src="/images/gitlab-create-project-5.png" style="width: 100%; margin: auto"></div>
<div><img src="/images/gitlab-create-project-6.png" style="width: 100%; margin: auto"></div>
</div><br>
<div><img src="/images/gitlab-create-project-7.png" style="width: 100%; margin: auto"></div>

---

# The `upstream` repository

<div><img src="/images/gitlab-developer-1.png" style="width: 100%; margin: auto"></div>

<br>

* The repository belonging to Big Boss in this example is usually referred to as `upstream`.
* A user with access to this repository can fork it. This “copy” is usually referred to as
  `origin`.

---

# A reminder of the overall picture

<div><img src="/images/gitlab.png" style="width: 80%; margin: auto"></div>

---

# Forking the repository

<img src="/images/gitlab-developer-2.png" style="width: 80%; margin: auto">

<br>

<img src="/images/gitlab-developer-3.png" style="width: 60%; margin: auto">

---

# Cloning a remote repository

* After forking the `upstream` repository, the repositories `upstream` and `origin` have the
  same content, so that we can clone either one to a local repository.

```console
$ git clone ssh://git@gitlab.local:30022/ingold/example.git
Cloning into 'example'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done
```

<br>

* The repository has been cloned into a subdirectory with the name of the repository. A different
  name could be given as an extra argument.

```console
$ ls -a example
.  ..  .git  README.md
```

---

# Remote repositories

```console
$ cd example
$ git remote -v
origin  ssh://git@gitlab.local:30022/ingold/example.git (fetch)
origin  ssh://git@gitlab.local:30022/ingold/example.git (push)
```

* The option `-v` stands for verbose.
* `origin` is known as a remote branch because we clone the repository from there.
* `upstream` is not yet known to Git, but we can add it as a remote repository.

<br>

```console
$ git remote add upstream ssh://git@gitlab.local:30022/boss/example.git
$ git remote -v
origin  ssh://git@gitlab.local:30022/ingold/example.git (fetch)
origin  ssh://git@gitlab.local:30022/ingold/example.git (push)
upstream        ssh://git@gitlab.local:30022/boss/example.git (fetch)
upstream        ssh://git@gitlab.local:30022/boss/example.git (push)
```
* Additional remote repositories can be declared, if needed.

---

# Make a contribution to the project

```console
$ git switch -c hello
Switched to a new branch 'hello'
```

... editing a script `hello.py` ...

```console
$ ls -a
.  ..  .git  README.md  hello.py
```

... and commit it ...

```console
$ git log --oneline --decorate
51e0462 (HEAD -> hello) hello world script added
af3f1b4 (origin/main, origin/HEAD, main) Initial commit
```

<br>

* so far, the new script exists only in the local repository

---

# Pushing the commit to `origin`

```console
$ git push -u origin hello
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 329 bytes | 329.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: To create a merge request for hello, visit:
remote:   http://gitlab.local:30080/ingold/example/-/merge_requests/new?merge_request%5Bsource_branch%5D=hello
remote:
To ssh://gitlab.local:30022/ingold/example.git
 * [new branch]      hello -> hello
Branch 'hello' set up to track remote branch 'hello' from 'origin'.
```

<br>

* The first time the upstream branch associated with the local branch has to be defined by
  using the option `-u` or `--set-upstream`.
* For later `push` operations from this branch, `git push` will be sufficient.

---

# The state on `origin`

```console
$ git log --oneline --decorate
* 51e0462 (HEAD -> hello, origin/hello) hello world script added
* af3f1b4 (origin/main, origin/HEAD, main) Initial commit
```

* The changes are only present in `hello` and `origin/hello`, but not in `main` and
  `origin/main`
* A request to merge the new commit(s) in the `hello` branch into the `upstream/main`
  branch can be made.

<br>

<img src="/images/gitlab-developer-4.png" style="width: 60%; margin: auto">

---

# Creating a merge request

<img src="/images/gitlab-developer-5a.png" style="width: 80%; margin: auto">


---

# Creating a merge request (continued)

<img src="/images/gitlab-developer-5b.png" style="width: 80%; margin: auto">

---

# A merge request

<div class="grid grid-cols-[60%_1fr] gap-8">
<div><img src="/images/gitlab-developer-6.png" style="width: 100%; margin: auto"></div>
<div>

* Adding more commits before the merging has happened will make them part of the
  merge request.
* This allows for an improvement of the content of the merge request, e.g. through
  discussions with other developers.
* It is possible to ask for explicit approval of the merge request.

</div>
</div>


---

# Ready to merge

<div class="grid grid-cols-[60%_1fr] gap-8">
<div><img src="/images/gitlab-developer-7.png" style="width: 95%; margin: auto"></div>
<div>

* If during the discussion it turns out that the proposed code is not useful, the
  merge request can be closed without merging.
* In such a case, it makes sense to add a comment explaining why the code has not
  been merged.

</div>
</div>

---

# A reminder of the overall picture

<div><img src="/images/gitlab.png" style="width: 80%; margin: auto"></div>

---

# Pull the merged code into the local repository

```console
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

* the new code is still in the `hello` branch, but not in `main`
  <carbon-arrow-right /> update `main` from `upstream`

```console
$ git fetch upstream
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), 248 bytes | 248.00 KiB/s, done.
From ssh://gitlab.local:30022/boss/example 
 * [new branch]      main       -> upstream/main
$ git merge upstream/main       
Updating af3f1b4..da6fdcc       
Fast-forward
 hello.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

* this can also be done in a single step: `git pull upstream main`
* our `main` branch is now consistent with `upstream/main`

---

# Update `origin/main`

```console
$ git log --oneline --graph --decorate --all
*   da6fdcc (HEAD -> main, upstream/main) Merge branch 'hello' into 'main'
|\  
| * 51e0462 (origin/hello, hello) hello world script added
|/  
* af3f1b4 (origin/main, origin/HEAD) Initial commit
```

<br>

* `origin/main` is not yet consistent with `upstream/main` and `main`

<br>

```console
$ git push origin main
Enter passphrase for key '/home/ingold/.ssh/id_ed25519':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 565 bytes | 565.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To ssh://gitlab.local:30022/ingold/example.git
   af3f1b4..da6fdcc  main -> main
```

---

# Cleaning up

```console
$ git log --oneline --decorate --graph
*   da6fdcc (HEAD -> main, upstream/main, origin/main, origin/HEAD) Merge branch 'hello' into 'main'
|\  
| * 51e0462 (hello, origin/hello) hello world script added
|/  
* af3f1b4 Initial commit
```

* Now, `main`, `upstream/main` and `origin/main` point to the same commit.
* The material in `hello` and `origin/hello` is present in the three main branches.
* We can therefore delete the local `hello` branch, but we could also keep it for further
  development.
* `origin/hello` had been removed during the commit, but we could have kept it as well.

<br>

```console
$ git branch -d hello
Deleted branch hello (was 51e0462).
```

* Git would warn us if we want to delete this branch before it has been merged into `main`.

---

# When and why is a clean working directory needed?

* A clean working directory does not contain any changes with respect to `HEAD`.
* When working on a project, a situation may arise where some work has been done but a
  clean working directory is needed because
  * some other work should be done first
  * work in another branch should be done first, e.g. to fix a bug in the production branch  
    problem: Git does not allow to switch to another branch if uncommitted changes are
    present because they might get lost
* There are two options:
  * commit the changes first, but this might be unwanted if the work is not yet complete
  * **stash the changes away**

---
layout: gli-two-cols-header
---

# Trying to leave a dirty working directory

::left::

```console
$ git switch -c dev
Switched to a new branch 'dev'
```

<br>

##### modify `hello.py`
````md magic-move
```python
# hello.py
print("Hello world!")
```
```python
# hello.py
print("Hello world!")
print("Hello world!")
print("Hello world!")
```
````

<v-click>
```console
$ git commit -a -m'repetitive output of message'
[dev e6f467c] repetitive output of message
 1 file changed, 2 insertions(+)
$ git switch main
Switched to branch 'main'
$ git switch dev
Switched to branch 'dev'
```

* leaving a clean working directory is no problem

</v-click>

::right::

<v-click>
```console
$ git branch
* dev
  main
```

<br>

##### modify `hello.py`
````md magic-move
```python
# hello.py
print("Hello world!")
print("Hello world!")
print("Hello world!")
```
```python
# hello.py
for _ in range(3):
    print("Hello world!")
```
````
</v-click>

<v-click>

##### now we do not commit the changes
```console
$ git switch main
error: Your local changes to the following files would be overwritten ↩
by checkout:
        hello.py
Please commit your changes or stash them before you switch branches.
Aborting
```

* a clean working directory is needed, either commit or stash the changes
</v-click>

---
layout: gli-two-cols-header
---

# Stashing changes

::left::

```console
$ git stash
Saved working directory and index state WIP on dev: ↩
e6f467c repetitive output of message
$ git stash list
stash@{0}: WIP on dev: e6f467c repetitive output of message
$ git switch main
Switched to branch 'main'
```

<br>

##### in `main` we still have the first version of our script
```console
$ cat hello.py
print("Hello world!")
```

<br>

##### in `dev` we now get the last committed version
```console
$ git switch dev
Switched to branch 'dev'
$ cat hello.py
print("Hello world!")
print("Hello world!")
print("Hello world!")
```

::right::

```console
$ git stash pop
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in ↩
working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or ↩
"git commit -a")
Dropped refs/stash@{0} (d1fc35f06e65ef6705cafb7f0313f34baf↩
060459)
```

<br>

##### the stash is empty again but we have our work in progress back
```console
$ git stash list
$ cat hello.py
for _ in range(3):
    print("Hello world!")
```

---

# Tagging

```console
$ git tag -a v1 -m 'first production release'
```
```console
$ git show v1
tag v1
Tagger: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
Date:   Tue Apr 23 16:35:10 2024 +0200

first production release

commit 1a55fb0747eebc1dcd01f547e1351bba1359ebec (HEAD -> main, tag: v1, origin/main, origin/HEAD, dev)
Author: Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>
Date:   Tue Apr 23 16:34:12 2024 +0200

    doc string added
```

<br>

* tagging can be useful in order to easily access specific versions
* here we tagged the current `HEAD`

---

# Tagging a commit using its SHA1 value

```console
$ git tag -a v0.1 -m'prerelease version' 60234ed
```
```console
$ git tag
v0.1
v1
```
```console
$ git log --oneline -n2
1a55fb0 (HEAD -> main, tag: v1, origin/main, origin/HEAD, dev) doc string added
60234ed (tag: v0.1) function call added
```

<br>

* the tags are listed together with the other references
* so far, the tags are only known in the local repository but not on the GitLab server

---

# Pushing a tag to the server

```console
$ git push origin v1
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 184 bytes | 184.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
To http://gitlab.local:30080/ingold/myproject.git
 * [new tag]         v1 -> v1
```

<div><img src="/images/gitlab-tag.png" style="width: 70%; margin: auto"></div>

---

# Detached head state

```console
$ git log --oneline
1a55fb0 (HEAD -> main, tag: v1, origin/main, ↩
         origin/HEAD) doc string added
60234ed function call added
f6a49f3 repeated print of text factored out
4a49a85 loop implemented
32e0993 simple hello world script added
3960122 Initial commit
```

* `HEAD` is pointing to (the top of) a branch
* we are interested in the code at a specific commit

```console
$ git checkout f6a49f3
HEAD is now at f6a49f3 repeated print of text factored out
```

```console
$ git log --oneline
f6a49f3 (HEAD) repeated print of text factored out
4a49a85 loop implemented
32e0993 simple hello world script added
3960122 Initial commit
```

* `HEAD` does no longer point to the top of a branch, it is detached

---

# The full Git message

```console
$ git checkout f6a49f3
Note: switching to 'f6a49f3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at f6a49f3 repeated print of text factored out
```

---

# Saving work done in a detached head state

````md magic-move
```python
for _ in range(3):
    print("Hello world!")
```
```python
for _ in range(3):
    print("Hello world! How are you?")
```
````

* a commit was added in the detached head state, let us switch back to the `main` branch

```console
$ git switch main
Warning: you are leaving 1 commit behind, not connected to
any of your branches:

  4e8e665 'how are you' added

If you want to keep it by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> 4e8e665

Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

* the commit is not connected to another branch 
  * either create a new branch before leaving the branch in a detached head state
  * or follow the advice after leaving the branch

---

# Overall picture of the detached head state

<div class="grid grid-cols-[1fr_1fr] gap-20">
<div>

![](/images/detachedhead_1.png)

<br>

![](/images/detachedhead_2.png)

</div>
<div>

![](/images/detachedhead_3.png)

<br>

![](/images/detachedhead_4.png)

</div>
</div>

---

# Rewriting history

<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800" style="width: 85%;margin: auto;">
  <div class="grid grid-cols-[4%_1fr] gap-10">
    <div><carbon-warning-alt class="text-red-800 text-3xl" /></div>
    <div>
      Do not rewrite history in a remote repository as it might result in big problems.
    </div>
  </div>
</div>

<br>

* Rewriting the history in a local repository before pushing to a server is acceptable. 
* Do not feel ashamed to explicitly revert a commit but adding another commit.
* Rewriting the history on a server is highly problematic because other users might have
  already pulled a previous version of the history thus leading to inconsistencies.

<br>

* In the following, we will cover only a few situations, but there exist solutions for
  basically every situation.

---

# Amending the last commit message

#### **Scenario:** One realizes a mistake in the commit message immediately after committing.

````md magic-move
```python
for _ in range(3):
    print("Hello world!")
```
```python
for _ in range(3):
    print("Hello world! How are you?")
```
````

<v-click>

```console
$ git log --oneline
a57c7f6 (HEAD -> main) 'who are you' added
cd59c67 hello world script added
```

* There is a typo in the last commit message which is even misleading.

</v-click>

<br>

<v-click>

#### `--amend` option

```console
$ git commit --amend -m"'How are you?' added"
[main 5bc4331] 'How are you?' added
 Date: Thu May 2 07:41:29 2024 +0200
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```console
$ git log --oneline
5bc4331 (HEAD -> main) 'How are you?' added
cd59c67 hello world script added
```

</v-click>

---

# Removing the last commit

#### **Scenario:** The last commit was not a good idea.

<br>

#### Solution 1: revert commit by adding another commit

```console
$ git log --oneline
5bc4331 'How are you?' added
cd59c67 hello world script added
```

```console
$ git revert HEAD
[main 29f3793] Revert "'How are you?' added"
 1 file changed, 1 insertion(+), 1 deletion(-)
```

```console
$ git log --oneline
29f3793 (HEAD -> main) Revert "'How are you?' added"
5bc4331 'How are you?' added
cd59c67 hello world script added
```

* A new commit has been added and history is not rewritten. Proceeding like this
  is fine even if the previous commit had already been pushed to a remote repository.
* It is also possible to revert other commits by using the corresponding hash value
  as argument.

---

# Removing the last commit

#### **Scenario:** The last commit was not a good idea.

<br>

#### Solution 2: reset to a previous commit

```console
$ git log --oneline
5bc4331 (HEAD -> main) 'How are you?' added
cd59c67 hello world script added
```

```console
$ git reset --hard HEAD^
HEAD is now at cd59c67 hello world script added
```

```console
$ git log --oneline
cd59c67 (HEAD -> main) hello world script added
```

* Now, everything is in the state of the parent of `HEAD`, i.e. `HEAD^`.
* It is also possible to reset to other commits.

<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800" style="width: 85%;margin: auto;">
  <div class="grid grid-cols-[4%_1fr] gap-10">
    <div><carbon-warning-alt class="text-red-800 text-3xl" /></div>
    <div>
      History will be rewritten and changes in the working directory will be lost.
    </div>
  </div>
</div>

---

# Interactive rebase

#### **Scenario:** apply only certain changes in `dev` branch using the `main` branch as base

```console
$ git log --oneline --graph --all
* 014986c (main) headline modified
| * 6147827 (HEAD -> dev) __name__ added to output
| * 766d07e Test output amended
|/  
* 0d079bd Test script added
```

* We want to keep `014986c` and drop `766d07e` instead.
* Then, we want to apply `6147827`.

<br>

* Use an interactive rebase of the `dev` branch on the `main` branch.

```console
$ git branch
* dev
  main
```

```console
$ git branch -i main
```

---

# Interactive rebase

```console {all}{maxHeight:'320px'}
pick 766d07e Test output amended
pick 6147827 __name__ added to output

# Rebase 014986c..6147827 onto 014986c (2 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```

<br>

* We replace `pick` by `drop` in the first line to ignore the commit `766d07e`.
* By means of `reword`, we could modify a commit message.

---

# Interactive rebase

```console
$ git rebase -i main
Auto-merging test.py
CONFLICT (content): Merge conflict in test.py
error: could not apply 6147827... __name__ added to output
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 6147827... __name__ added to output
```

* There is a merge conflict which we need to resolve in the usual way.

```console
$ git add test.py
```

* Now, we can continue the rebase.

```console
$ git rebase --continue
[detached HEAD 19b3f3e] __name__ added to output
 1 file changed, 2 insertions(+)
Successfully rebased and updated refs/heads/dev.
```

---

# Interactive rebase

```console
$ git log --oneline --graph --all
* 19b3f3e (HEAD -> dev) __name__ added to output
* 014986c (main) headline modified
* 0d079bd Test script added
```

* Now, we have a linear history with `19b3f3e` applied on top of `014986c`.
* The commit `__name__ added to output` has a new hash value because certain
  aspects of the commit like its parent and the time of commit have changed.

<br>

* `git rebase` is very powerful and can be applied in many situations.
* But remember: Be careful when rewriting history!
