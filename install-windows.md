# How to install on windows

## Install python

If you do not have python installed please install python 
from https://www.python.org/downloads/ and follow the 
installation instructions.

## Install sphinx

If you do not have sphinx installed please install sphinx.
To check whether open the command line (Windows + R, type 
`cmd`). Now start the python console by typing in `python`.

If the code `import sphinx` does not raise an 
`ModuleNotFoundError` sphinx is installed. You can go on 
with the section *compile the script*.

If `sphinx` is not installed run the code 
`pip install sphinx` (or `conda install sphinx if you have 
python installed via anaconda. To find out if you are using 
conda type `conda list` in the command line. If there is an 
error you are *not* using anaconda).

## Compile the script

Open the command line in the directory of the manuscript 
(`./manuscript`). Now run the following command:

```sphinx-build -M latexpdf . _build```

The compiled .tex file can be found in 
`./manuscript/_build/latex/tools4scicomp.pdf`.