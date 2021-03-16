from catalogapp.base import Entity

class Models(Entity):
    def _init_custom(self):
        self.partition = 20

class Deleted(Entity):
    def _init_defaults(self):
        pass

        # create specific methods for models offset
    def output(self, result):
        self.data += self.engine.get_ids(result)

    def request(self, filter_input=0):
        filters = self.filter_template % (filter_input)        
        response = self.engine.get_response(self.url, filters) 
        if isinstance(response, dict):
            response = [response,]
        return response

    def store(self, date_offset=None): # need to be updated to offset
        self.entities = {}

        self.url_template = self.get_template('models_deleted', 'url')
        self.filter_template = self.get_template('models_deleted', 'filter')
        self.path_template = self.get_template('models_deleted', 'path')
        self.calculation = self.get_template('models_deleted', 'calculation')

        for catalog_id in self.catalogs.ids:                
            self.url = self.url_template % (catalog_id)
            self.path = self.path_template % (catalog_id)
            self.data = []
            self.calculation(self)
            self.data = list(dict.fromkeys(self.data))
            self.engine.save_json(self.path, self.data, 'models_deleted', 'False')
            self.entities[catalog_id] = list(self.data)
        
