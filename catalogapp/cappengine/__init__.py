from catalogapp.cappengine.engine import CatalogEngine
from catalogapp.cappengine.utils.debug import Debug
from catalogapp.cappengine.entities import entity as defaults

def get_template(entity, template):
    return defaults[entity][template]

def get_ids(json_list):
    data = []
    if len(json_list) > 0:
        for item in json_list:
            data.append(item['id'])
    return data