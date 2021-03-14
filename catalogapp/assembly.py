from catalogapp import cappengine
from config import settings
from catalogapp import catalogs as capp

debug = cappengine.Debug(settings.OUTPUT)
engine = cappengine.CatalogEngine(debug.trace, settings)
engine.get_template = cappengine.get_template
catalogs = capp.Catalogs(engine)
vendors = capp.Dictionaries(engine, catalogs, 'vendors')
categories = capp.Dictionaries(engine, catalogs, 'categories')
suppliers = capp.Dictionaries(engine, catalogs, 'suppliers')
pricing_profiles = capp.Dictionaries(engine, catalogs, 'pricing_profiles')

models = capp.Models(engine, catalogs, 'models')

# from catalogapp import catalogs as capp

# engine =  capp.engine
# catalogs = capp.Catalogs()
# vendors = capp.Entity('vendors', catalogs)

# def show_response(url, limit=None):
#     if limit is None:
#         print(engine.get_response(url))
#     else:
#         print(engine.get_response(url, limit=limit))

