pythonForPlanes
===============

This package is intended as a collection of build routines which will work well for sublime text 2.


Colour Schemes
--------------

Alt All Hallow's Eve
	A modified version of this theme without the grey background for plain tex

Build Scripts
-------------

python_inplace_build

	- Builds the current python package inplace with mingw32 as the compiler and gfortran as the fcompiler
	- Issues:
		- None


python_sphinx
	
	- Builds the sphinx website corresponding the the config file in the current directory
	- Issues:
		- Does not work on linux (maybe a python / sphinx issue)


tec360_macro

	- Executest a tecplot360 macro

LaTeX_dvi
	- Builds the current .tex into a dvi
	- Options located here 'http://users.phys.psu.edu/~collins/software/latexmk-jcc/latexmk-435.txt'

	_note::
		Does not convert the .dvi to a .ps then to a .pdf
