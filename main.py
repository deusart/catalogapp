from catalogapp import catalogs
import catalogapp

categories_details = catalogapp.v1.categories_details
categories_details.prepare_entities()
categories_details.store()
# catalogapp.v1.catalogs.store()
# catalogapp.v1.vendors.store()
# catalogapp.v1.categories.store()
# catalogapp.v1.suppliers.store()
# catalogapp.v1.pricing_profiles.store()

# catalogapp.v1.show_response('https://catalog.app/api/catalogs/2/suppliers/100/prices')
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

