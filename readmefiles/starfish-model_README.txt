This library is a part of the Starfish project.

# Starfish Model Library
The Starfish Model Library is an open-source library used for data definition, storage, and processing of models in a variety of languages. The library provides the framework to define objects and their relationships as well as perform analysis on those entities. The library is structured in a way that conforms to the OMG MOF v2 Architecture. While this is potentially limiting (not all modeling languages conform to MOF), it is anticipated that langauges which do not conform can be reasonably adapted to fit into the MOF. This limitation is necessary to reap the analytical benefits of the library (such as the use of OCL) and, in general, appears to be consistent with industry trend.

# Conformance
As this library is still in development, this library does *not* currently conform to the OMG MOF specification. However, there are some principles defined for this project:
1. The target for this library is to meet Complete MOF (CMOF) conformance.
2. Development prioritization will focus on Essential MOF (EMOF) conformance.
3. Until this project supports CMOF, the major version number of this library will remain as "0", indicating a pre-release version.

Target versions (and their normative references) are listed below:
* **Meta Object Facility (MOF)**: 2.5.1 ([formal/19-10-01](https://www.omg.org/spec/MOF/2.5.1))
* **XML Metadata Interchange (XMI)**: 2.5.1 ([formal/15-06-07](https://www.omg.org/spec/XMI/2.5.1))
* **Object Constraint Language (OCL)**: 2.4 ([formal/14-02-03](https://www.omg.org/spec/OCL/2.4))


