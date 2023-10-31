# License

EUPL 1.2

We have distilled the most crucial license specifics to make your adoption seamless: [see here for details](https://github.com/THCLab/licensing).

# Overview

Repository helding ontologies


### Installation
1. Install conda

2. Run `conda env create -f requirements.yml`

3. Run `conda activate PyCDO`

### Ontology File Generation

The repository uses OwlReady2 to design and create the ontology. 

#### Design Ontology
Ontology design is in two files:
- file were classes are defined: [src/Models/classes.py](src/Models/classes.py)

- file were properties are defined: [src/Models/properties.py](src/Models/properties.py)

The following command uses thse defintoins to generate the .OWL file:

1. `cd ontology`

1. Run `python -m src.generate_ontology`

1. Review output in [output/cdo-ontology.owl](output/cdo-ontology.owl)

1. Use Protege to generate a Turle (.ttl) file from the .owl file, such as [output/cdo-ontology.ttl](output/cdo-ontology.ttl).