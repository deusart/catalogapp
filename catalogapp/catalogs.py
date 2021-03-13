from catalogapp.engine import engine
from catalogapp.engine import debug
from catalogapp.engine import templates
# from catalogapp.engine import format
from catalogapp.base import Entity
# from catalogapp.engine import calculations
import datetime

class Catalogs(object):
    def __init__(self):
        url = templates.urls['catalogs']
        self.catalogs = engine.get_response(url)
        catalogs = {}
        for item in  self.catalogs:
            catalogs[item['name']] = item ['id']        
        self.ids = tuple(catalogs.values())
        self.names = catalogs
        debug.trace('Entity catalogs created.','System')

    def store(self):
        engine.save_json('', self.catalogs, 'catalogs')
    
    def info(self):
        print(self.names)
