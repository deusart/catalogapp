from catalogapp import catalogs
import catalogapp

modified = catalogapp.v1.modified
modified.prepare_entities(0)
modified.store_catalog(2)
# print(len(modified.entities[2]))

# categories_details.prepare_entities()
# categories_details.store()
# catalogapp.v1.vendors.store()
# catalogapp.v1.categories.store()
# catalogapp.v1.suppliers.store()
# catalogapp.v1.pricing_profiles.store()

# catalogapp.v1.show_response('https://catalog.app/api/catalogs/1/models/modified')
# pricing_profiles_prices = catalogapp.v1.pricing_profiles_prices
# pricing_profiles_prices.prepare_entities()
# pricing_profiles_prices.store()
# catalogapp.catalogs.info()
# catalogapp.catalogs.store()
# vendors = catalogapp.vendors
# vendors.store_catalog(2)
# print(vendors.url)
# print(vendors.path)
# from unittests import modules
# modules.run_test()

