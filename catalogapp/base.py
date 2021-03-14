import catalogapp
import catalogapp.cappengine

# debug = cappengine.Debug()
# engine = cappengine.CatalogEngine(debug.trace, settings)

# debug = debug.Debug(settings.OUTPUT)
# engine = CatalogEngine(debug.trace)

# debug = catalogapp.engine.debug
# defaults = catalogapp.engine.defaults
# engine = catalogapp.engine.engine

class Entity(object):

    def __init__(self, engine, catalogs, entity):
        self.trace = engine.trace
        self.engine = engine
        self.get_template = engine.get_template        
        self.entity = entity
        self.catalogs = catalogs        
        self._init_defaults()
        self._init_custom()
        self.trace(f'Entity catalogs.{self.entity} created.','System')
    
    def store(self, catalog_id=None):
        if catalog_id is None:
            for catalog_id in self.catalogs.ids:                
                self.store_catalog(catalog_id)
        else:
            self.store_catalog(catalog_id)
        self.trace(f'Saving entity {self.entity} is completed.\n','System')

    def _init_defaults(self):
        self.url_template = self.get_template(self.entity, 'url')
        self.path_template = self.get_template(self.entity, 'path')
        self.filter_template = self.get_template(self.entity, 'filter')
        self.calculation = self.get_template(self.entity, 'calculation')
        self.format = self.get_template(self.entity, 'format')
        self.timestamp = self.get_template(self.entity, 'timestamp')

    def _init_custom(self):
        pass

    def output(self, result):
        data = {}
        for item in result:
            line = self.format(item, self.catalog_id)
            data.update(line)
        self.engine.save_json(self.path, data, self.entity, self.timestamp)

    def request(self, filter_input=None):
        if filter_input is not None:
            filters = self.filter_template % (filter_input)
        else:
            filters = ''        
        response = self.engine.get_response(self.url, filters) 
        if isinstance(response, dict):
            response = [response,]
        return response

    def set_parameters(self, catalog_id):
        self.catalog_id = catalog_id
        self.url = self.url_template % (catalog_id)
        self.path = self.path_template % (catalog_id)  

    def store_catalog(self, catalog_id):
        self.set_parameters(catalog_id)
        self.calculation(self)

    def store_id(self, catalog_id, entity_id):
        self.set_parameters(catalog_id)
        self.url += f'/{entity_id}'
        response = self.engine.get_response(self.url)
        data = {}
        data['catalogId'] = catalog_id        
        data[response['id']] = response
        self.engine.save_json(self.path, data, self.entity, self.timestamp)