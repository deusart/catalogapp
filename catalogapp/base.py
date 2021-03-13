from catalogapp import engine

debug = engine.debug

class Entity(object):

    def __init__(self, entity, catalogs):
        self.entity = entity
        self.catalogs = catalogs        
        self._init_defaults()
        self._init_custom()
        debug.trace(f'Entity catalogs.{self.entity} created.','System')
    
    def store(self, catalog_id=None):        
        if catalog_id is None:
            for catalog_id in self.catalogs.ids:                
                self.store_catalog(catalog_id)
        else:
            self.store_catalog(catalog_id)
        debug.trace(f'Saving entity {self.name} is completed.\n','System')

    def _init_defaults(self):
        self.url = 'sss'

    def _init_custom(self):
        pass
    def _output(self, result):
        pass
    def _request(self, filter_input=None):
        pass
    def show_response(self, url, filters=''):
        pass
    def set_parameters(self, catalog_id):
        pass 
    def _filter(self, data='', filter=''):
        pass
    

        
    def store_catalog(self, catalog_id):
        pass

    def store_id(self, catalog_id, entity_id):
        pass