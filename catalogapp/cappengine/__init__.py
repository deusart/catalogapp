from catalogapp.cappengine.engine import CatalogEngine
from catalogapp.cappengine.utils.debug import Debug
from catalogapp.cappengine.entities import entity as defaults

def get_template(entity, template):
    return defaults[entity][template]