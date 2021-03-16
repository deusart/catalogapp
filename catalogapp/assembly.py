from catalogapp import cappengine
from config import settings
from catalogapp import catalogs as capp_catalogs
from catalogapp import modified as capp_modified
from catalogapp import models as capp_models

debug = cappengine.Debug(settings.OUTPUT)
engine = cappengine.CatalogEngine(debug.trace, settings)
engine.get_template = cappengine.get_template
engine.get_ids = cappengine.get_ids

catalogs = capp_catalogs.Catalogs(engine)
vendors = capp_catalogs.Dictionaries(engine, catalogs, 'vendors')
categories = capp_catalogs.Dictionaries(engine, catalogs, 'categories')
suppliers = capp_catalogs.Dictionaries(engine, catalogs, 'suppliers')
pricing_profiles = capp_catalogs.Dictionaries(engine, catalogs, 'pricing_profiles')

models = capp_models.Models(engine, catalogs, 'models')
suppliers_prices = capp_catalogs.Prices(engine, catalogs, 'suppliers_prices')
pricing_profiles_prices = capp_catalogs.Prices(engine, catalogs, 'pricing_profiles_prices')

categories_details = capp_catalogs.CategoiesDetails(engine, catalogs, 'categories_details')
modified = capp_modified.Modified(engine, catalogs, 'modified')

models_deleted = capp_models.Deleted(engine, catalogs, 'models_deleted')

def show_response(url, filters=''):
    print(engine.get_response(url, filters))
    
