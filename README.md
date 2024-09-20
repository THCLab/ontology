# License

EUPL 1.2

We have distilled the most crucial license specifics to make your adoption seamless: [see here for details](https://github.com/THCLab/licensing).

# Overview

**Abstract** The Core Data Ontology (CDO) and the Informatics Domain Model represent a transformative approach to computational systems, shifting from traditional node-centric designs to a data-centric paradigm. This paper introduces a framework where data is categorized into four modalities: objects, events, concepts, and actions. This quadrimodal structure enhances data security, semantic interoperability, and scalability across distributed data ecosystems. The CDO offers a comprehensive ontology that supports AI development, role-based access control, and multimodal data management. By focusing on the intrinsic value of data, the Informatics Domain Model redefines system architectures to prioritize data security, provenance, and auditability, addressing vulnerabilities in current models. The paper outlines the methodology for developing the CDO, explores its practical applications in fields such as AI, robotics, and legal compliance, and discusses future directions for scalable, decentralized, and interoperable data ecosystems.

This ontology can be cited as

>*Knowles, P., Gajderowicz, B. and Dougas, K. (2024) “Data-Centric Design: Introducing an Informatics Domain Model and Core Data Ontology for Computational Systems,” In Proceedings of the 10th International Conference on Data Mining & Knowledge Management (DaKM 2024)*

### Installation
1. Install conda

2. Run `conda env create -f requirements.yml`

3. Run `conda activate PyCDO`

### Ontology File Generation

The repository uses OwlReady2 to design and create the ontology. 

#### Design Ontology
Ontology design is contained in one file:
- file were classes and properties are defined: [src/Models/classes.py](src/Models/classes.py)
  
The following command uses thse defintoins to generate the .OWL file:

1. `cd ontology`

1. Run `python -m src.generate_ontology`

1. Review output in [output/cdo-ontology.owl](output/cdo-ontology.owl)

1. Use Protege to generate a Turle (.ttl) file from the .owl file, such as [output/cdo-ontology.ttl](output/cdo-ontology.ttl).
