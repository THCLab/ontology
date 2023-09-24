from py2graphdb.Models.graph_node import GraphNode
from py2graphdb.utils.db_utils import PropertyList, SPARQLDict, resolve_nm_for_dict, Thing
from py2graphdb.utils.db_utils import Thing
from owlready2 import default_world, ObjectProperty, DataProperty, rdfs, Thing 

from py2graphdb.config import config as CONFIG
gproj = default_world.get_ontology(CONFIG.NM)

from .properties import *
import re, os
class User(GraphNode):
    klass = 'gproj.User'
    relations = {
        'name' : {'pred':gproj.hasName, 'cardinality':'one'},
        'addresses' : {'pred':gproj.hasAddress, 'cardinality':'many'},
        'roles' : {'pred':gproj.hasRoles, 'cardinality':'many'},
    }

    def __init__(self, inst_id=None, keep_db_in_synch=False) -> None:
        super().__init__(inst_id=inst_id, keep_db_in_synch=keep_db_in_synch)

        
    from py2graphdb.utils import db_utils
    def_file_path = os.path.dirname(db_utils.__file__) + '/_model_getters_setters_deleters.py'
    imported_code = open(def_file_path).read()
    exec(imported_code)

