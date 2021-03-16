from catalogapp.base import Entity
class Catalogs(object):
    def __init__(self, engine):
        self.trace = engine.trace
        self.engine = engine
        url = engine.get_template('catalogs','url')
        self.catalogs = engine.get_response(url)
        catalogs = {}
        for item in  self.catalogs:
            catalogs[item['name']] = item ['id']        
        self.ids = tuple(catalogs.values())
        self.names = catalogs
        self.trace('Entity catalogs created.','System')

    def store(self):
        self.engine.save_json('', self.catalogs, 'catalogs')
    
    def info(self):
        print(self.names)
class Dictionaries(Entity):
    pass
class Prices(Entity):
    def _init_custom(self):
        self.partition = 3
        self.parent = self.get_template(self.entity, 'parent')        
        self.result = []

    def prepare_entities(self):
        self.entities = {}
        url_template = self.get_template(self.parent, 'url')     
        for catalog_id in self.catalogs.ids:                
            url = url_template % (catalog_id)
            response =  self.engine.get_response((url))
            data = self.engine.get_ids(response)
            self.entities[catalog_id] = tuple(data)
    
    def set_parameters(self, catalog_id, entity_id):
        self.catalog_id = catalog_id
        self.url = self.url_template % (catalog_id, entity_id)
        self.path = self.path_template % (catalog_id)  

    def store_catalog(self, catalog_id):
        for entity_id in self.entities[catalog_id]:
            self.set_parameters(catalog_id, entity_id)
            self.calculation(self)
        self.output(self.result)
        self.result = []
class CategoiesDetails(Entity):    
    def _init_custom(self):
        self.parent = self.get_template(self.entity, 'parent')   
        self.partition = 500     
        self.result = []
    
    def prepare_entities(self): # need to be updated to offset
        self.entities = {}
        url_template = self.get_template(self.parent, 'url')     
        for catalog_id in self.catalogs.ids:                
            url = url_template % (catalog_id)
            response =  self.engine.get_response((url))
            data = self.engine.get_ids(response)
            self.entities[catalog_id] = tuple(data)
    
    def set_parameters(self, catalog_id, entity_id):
        self.catalog_id = catalog_id
        self.url = self.url_template % (catalog_id, entity_id)
        self.path = self.path_template % (catalog_id)
    
    def store_catalog(self, catalog_id):
        for entity_id in self.entities[catalog_id]:
            self.set_parameters(catalog_id, entity_id)
            self.calculation(self)
        self.output(self.result)
        self.result = []
