from catalogapp import catalogs as capp

engine =  capp.engine
catalogs = capp.Catalogs()
vendors = capp.Entity('vendors', catalogs)

def show_response(url, limit=None):
    if limit is None:
        print(engine.get_response(url))
    else:
        print(engine.get_response(url, limit=limit))


        # if catalog_type == 'dictionaries':
        #     self._set_dictionaries()
        # elif catalog_type == 'models':
        #     self._set_models()
        # elif 'prices' in catalog_type:
        #     self._set_prices(catalog_type)
        # elif catalog_type == 'modified':
        #     self._set_modified()
        # elif catalog_type == 'categories-details':
        #     self._set_categories_details()
        # print('')