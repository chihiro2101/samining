Ocarina AADL toolset  |docs|
====================

Latest release: |release|

Citable Reference: |zenodo|

::

  @software{ocarina_v2021_1,
   author       = {OpenAADL},
   title        = {OpenAADL/ocarina: 2021.1},
   month        = sep,
   year         = 2021,
   version      = {v2021.1},
   doi          = {10.5281/zenodo.5459517},
   url          = {https://doi.org/10.5281/zenodo.5459517}
  }

About:
------

Ocarina is an AADL model processor, it acts as a "compiler" for AADL models.

As a front-end, it supports

* AADLv2 language from `AS5506C standard <http://standards.sae.org/as5506c/>`_,
* the Behavioral annex from `AS5506/1 standard <http://standards.sae.org/as5506/a/>`_
* the ARINC653 and the EMV2 annexes from `AS5506/1A standard <http://standards.sae.org/as5506/1a/>`_

As a back-end, it supports

* Code generation towards the AADL runtime `PolyORB-HI/Ada <https://github.com/OpenAADL/polyorb-hi-ada>`_ and `PolyORB-HI/C <https://github.com/OpenAADL/polyorb-hi-c>`_, and ARINC653 compliant APEX, following recommendations from `AS5506/2 standard <http://standards.sae.org/as5506/2/>`_
* WCET analysis, using `Bound-T <http://bound-t.com>`_
* Scheduling analysis, using `Cheddar <http://beru.univ-brest.fr/~singhoff/cheddar/>`_ and `MAST <http://mast.unican.es>`_
* Model checking, using Petri Net `Tina <http://projects.laas.fr/tina//>`_, and `LNT <http://cadp.inria.fr>`_
* Constraint analysis, using the REAL annex language

It can be integrated with the `AADLib <https://github.com/OpenAADL/AADLib>`_ library of AADL components.

It can also be embedded in AADL editors: in `OSATE <http://osate.org>`_ using the `OSATE2 plugin <https://github.com/OpenAADL/osate2-ocarina>`_, and `AADL Inspector <http://www.ellidiss.fr/public/wiki/wiki/inspector>`_ or advanced system processing suite like `TASTE by the European Space Agency <https://www.taste.tools>`_

Installation:
-------------

Refer to the  `ocarina-build <https://github.com/openaadl/ocarina-build>`_ companion project for details.

Q&A:
----

+----------------------------------+---------------+
| Build status GitHub actions      ||github|       |
+----------------------------------+---------------+
| Code coverage                    | |coverage|    |
+----------------------------------+---------------+
| CII Best practice                | |cii|         |
+----------------------------------+---------------+

.. |github| image:: https://github.com/OpenAADL/ocarina/workflows/Ocarina/badge.svg
  :target: https://github.com/OpenAADL/ocarina/actions?query=workflow%3AOcarina

.. |docs| image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: http://ocarina.readthedocs.org/

.. |coverage| image:: https://codecov.io/github/OpenAADL/ocarina/coverage.svg?branch=master
  :target: https://codecov.io/gh/OpenAADL/ocarina
  :alt: Code Coverage

.. |release| image:: https://img.shields.io/github/release/OpenAADL/ocarina.svg
  :target: https://github.com/OpenAADL/ocarina/releases
  :alt: GitHub Releases

.. |cii| image:: https://bestpractices.coreinfrastructure.org/projects/1019/badge
  :target: https://bestpractices.coreinfrastructure.org/projects/1019
  :alt: CII Best practice
  
.. |zenodo| image:: https://zenodo.org/badge/7610156.svg
   :target: https://zenodo.org/badge/latestdoi/7610156
  
