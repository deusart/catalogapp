from catalogapp import cappengine
from config import settings
from catalogapp import catalogs as capp
from catalogapp import modified

debug = cappengine.Debug(settings.OUTPUT)
engine = cappengine.CatalogEngine(debug.trace, settings)
engine.get_template = cappengine.get_template
engine.get_ids = cappengine.get_ids

catalogs = capp.Catalogs(engine)
vendors = capp.Dictionaries(engine, catalogs, 'vendors')
categories = capp.Dictionaries(engine, catalogs, 'categories')
suppliers = capp.Dictionaries(engine, catalogs, 'suppliers')
pricing_profiles = capp.Dictionaries(engine, catalogs, 'pricing_profiles')

models = capp.Models(engine, catalogs, 'models')
suppliers_prices = capp.Prices(engine, catalogs, 'suppliers_prices')
pricing_profiles_prices = capp.Prices(engine, catalogs, 'pricing_profiles_prices')

categories_details = capp.CategoiesDetails(engine, catalogs, 'categories_details')

modified = modified.Modified(engine, catalogs, 'modified')


def show_response(url, filters=''):
    print(engine.get_response(url, filters))
    