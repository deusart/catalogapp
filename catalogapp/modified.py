from catalogapp.base import Entity
import datetime

class Modified(Entity):    
    def _init_defaults(self):
        self.url_template = self.get_template(self.entity, 'url')
        self.filter_template = self.get_template(self.entity, 'filter')
        self.url_models_template = self.get_template('models_details', 'url')

        self.calculation_models = self.get_template('models_details', 'calculation')
        self.calculation_modified = self.get_template(self.entity, 'calculation')

        self.format_models = self.get_template('models', 'format')
        self.format_models_details = self.get_template('models_details', 'format')
        self.format_suppliers_prices = self.get_template('suppliers_prices', 'format')
        self.format_pricing_profiles_prices = self.get_template('pricing_profiles_prices', 'format')
        self.path_models = self.get_template('models', 'path')
        self.path_models_details = self.get_template('models_details', 'path')
        self.path_suppliers_prices = self.get_template('suppliers_prices', 'path')
        self.path_pricing_profiles_prices = self.get_template('pricing_profiles_prices', 'path')
        self.result = []

    # create specific methods for models offset
    def output(self, result):
        self.data += self.engine.get_ids(result)

    def request(self, filter_input=0):
        filters = self.filter_template % (filter_input, self.date_from)    
        response = self.engine.get_response(self.url, filters) 
        if isinstance(response, dict):
            response = [response,]
        return response

    def prepare_entities(self, date_offset=None): # need to be updated to offset
        if date_offset is None:
           self.date_from = str(datetime.datetime.now().date() + datetime.timedelta(days = -1))
        else:
           self.date_from = str(datetime.datetime.now().date() + datetime.timedelta(days = -date_offset))
        self.entities = {}

        for catalog_id in self.catalogs.ids:                
            self.url = self.url_template % (catalog_id)
            self.data = []
            self.calculation_modified(self)
            self.data = list(dict.fromkeys( self.data))
            self.entities[catalog_id] = list(self.data)

    def store_catalog(self, catalog_id):
        models = {}
        models_details = {}
        suppliers_prices  = {}
        pricing_profiles_prices = {}

        path_models = self.path_models % (catalog_id)
        path_models_details = self.path_models_details % (catalog_id)
        path_suppliers_prices = self.path_suppliers_prices % (catalog_id)
        path_pricing_profiles_prices = self.path_pricing_profiles_prices % (catalog_id)

        while len(self.entities[catalog_id])>0:
            entity_id = self.entities[catalog_id].pop()
            url_models = self.url_models_template % (catalog_id, entity_id)
            response = self.engine.get_response(url_models)            

            # message = f'Left {len(self.entities[catalog_id])} items. '
            # message += f'Buffer (models {len(models)} items) '
            # message += f'(models_details {len(models_details)} items) '
            # message += f'(suppliers_prices {len(suppliers_prices)} items) '
            # message += f'(pricing_profiles_prices {len(pricing_profiles_prices)} items). '

            # self.trace(message)

            models.update(self.format_models(response, catalog_id))
            models_details.update(self.format_models_details(response, catalog_id))

            if 'supplierPrices' in response.keys():
                for supplier_price in response['supplierPrices']:
                    suppliers_prices.update(self.format_suppliers_prices(supplier_price, catalog_id, entity_id))
            
            if 'profilePrices' in response.keys():
                for pricing_profiles_price in response['profilePrices']:
                    pricing_profiles_prices.update(self.format_pricing_profiles_prices(pricing_profiles_price, catalog_id, entity_id))

           
            if len(models) > 250:
                self.engine.save_json(path_models, models, 'models', True)
                models = {}
            if len(models_details) > 250:
                self.engine.save_json(path_models_details, models_details, 'models_details', True)
                models_details = {}
            if len(suppliers_prices) > 250:
                self.engine.save_json(path_suppliers_prices, suppliers_prices, 'suppliers_prices', True)               
                suppliers_prices  = {}                
            if len(pricing_profiles_prices) > 250:
                self.engine.save_json(path_pricing_profiles_prices, pricing_profiles_prices, 'pricing_profiles_prices', True)
                pricing_profiles_prices = {}

        self.engine.save_json(path_models, models, 'models', True)
        self.engine.save_json(path_models_details, models_details, 'models_details', True)
        self.engine.save_json(path_suppliers_prices, suppliers_prices, 'suppliers_prices', True)               
        self.engine.save_json(path_pricing_profiles_prices, pricing_profiles_prices, 'pricing_profiles_prices', True)