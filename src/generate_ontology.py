import os
from owlready2 import *

cdo_onto = get_ontology("https://onto.colossi.network/cdo")
cdo = cdo_onto.get_namespace("https://onto.colossi.network/cdo#")

from .Models.classes import *

def initialize_database():
    TMP_DIR = './output/'
    _ = os.makedirs(TMP_DIR) if not os.path.exists(TMP_DIR) else None
    owl_file = f'{TMP_DIR}cdo-ontology.owl'
    cdo.save(owl_file)

if __name__ == '__main__':
    initialize_database()