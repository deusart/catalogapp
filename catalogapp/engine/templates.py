filters = dict (
    empty = '',
    limit = '?limit=%s&',
    offset = '&offset=%s',
    startid = '&startId=%s'
)

urls = dict(
    authorization = 'https://catalog.app/api/authorization',
    catalogs = 'https://catalog.app/api/catalogs',
    vendors = 'https://catalog.app/api/catalogs/%s/vendors',
    categories = 'https://catalog.app/api/catalogs/%s/categories',
    categories_details = 'https://catalog.app/api/catalogs/%s/categories/%s',
    suppliers = 'https://catalog.app/api/catalogs/%s/suppliers',
    suppliers_prices = 'https://catalog.app/api/catalogs/%s/suppliers/%s/prices',
    pricing_profiles = 'https://catalog.app/api/catalogs/%s/pricing-profiles',
    pricing_profiles_prices = 'https://catalog.app/api/catalogs/%s/pricing-profiles/%s/prices',
    models = 'https://catalog.app/api/catalogs/%s/models',
    models_modified = 'https://catalog.app/api/catalogs/%s/models/modified',
    models_deleted = 'https://catalog.app/api/catalogs/%s/models/deleted',
    models_details = 'https://catalog.app/api/catalogs/%s/models/%s/details',
)

path = dict(
    catalogs = '',
    vendors = '%s\\',
    categories = '%s\\',
    categories_details = '%s\\%s\\',
    suppliers = '%s\\',
    suppliers_prices = '%s\\%s\\',
    pricing_profiles = '%s\\',
    pricing_profiles_prices = '%s\\%s\\',
    models = '%s\\%s\\',
    models_modified = '%s\\%s\\',
    models_deleted = '%s\\%s\\',
    models_details = '%s\\%s\\',
)