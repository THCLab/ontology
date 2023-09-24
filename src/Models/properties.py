from py2graphdb.utils.db_utils import Thing
from owlready2 import default_world, ObjectProperty, DataProperty, rdfs, Thing 

from py2graphdb.config import config as CONFIG
gproj = default_world.get_ontology(CONFIG.NM)

with gproj:
    class hasName(DataProperty):
        rdfs.comment = ["User name"]
        range = [str]

    class hasDescription(DataProperty):
        rdfs.comment = ["User address"]
        range = [str]
    class hasAddress(DataProperty):
        rdfs.comment = ["User address"]
        range = [str]

    class hasOneURI(ObjectProperty):
        rdfs.comment = ["Desc for the object"]
        range = [Thing]

    class hasListOfURIs(ObjectProperty):
        rdfs.comment = ["Desc for the object"]
        range = [Thing]
    class hasRoles(ObjectProperty):
        rdfs.comment = ["Desc for the object"]
        range = [Thing]
    class roleFor(ObjectProperty):
        rdfs.comment = ["Desc for the object"]
        range = [Thing]
