from catalogapp.cappengine.templates import urls, paths, filters, calculations, formats

entity = {
    'catalogs': {
        'url': urls.catalogs,
        'path': paths.catalogs,
        'timestamp': False
        },
    'vendors': {
        'url': urls.vendors,
        'path': paths.vendors,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.entity,
        'timestamp': False
        },
    'suppliers': {
        'url': urls.suppliers,
        'path': paths.suppliers,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.entity,
        'timestamp': False
        },
    'categories': {
        'url': urls.categories,
        'path': paths.categories,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.entity,
        'timestamp': False
        },
    'pricing_profiles': {
        'url': urls.pricing_profiles,
        'path': paths.pricing_profiles,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.entity,
        'timestamp': False
        },
    'models': {
        'url': urls.models,
        'path': paths.models, 
        'filter': filters.startid,
        'calculation': calculations.load_startid_partition,
        'format': formats.models,
        'timestamp': True
        },
    'suppliers_prices': {
        'parent': 'suppliers',
        'url': urls.suppliers_prices,
        'path': paths.suppliers_prices, 
        'filter': filters.startid,
        'calculation': calculations.load_startid_prices,
        'format': formats.suppliers_prices,
        'timestamp': True
        },
    'pricing_profiles_prices': {
        'parent': 'pricing_profiles',
        'url': urls.pricing_profiles_prices,
        'path': paths.pricing_profiles_prices, 
        'filter': filters.startid,
        'calculation': calculations.load_startid_prices,
        'format': formats.pricing_profiles_prices,
        'timestamp': True
        },
    'categories_details': {
        'parent': 'categories',
        'url': urls.categories_details,
        'path': paths.categories_details, 
        'filter': filters.offset,
        'calculation': calculations.load_line,
        'format': formats.categories_details,
        'timestamp': True
        },
    'modified': {
        'parent': 'models',
        'url': urls.models_modified,        
        'filter': filters.offset_fromUtc,
        'calculation': calculations.load_offset,        
        },
    'models_deleted': {
        'parent': 'models',
        'url': urls.models_deleted,
        'path': paths.models_deleted, 
        'filter': filters.offset,
        'calculation': calculations.load_offset,        
        },
    'models_details': {
        'parent': 'models',
        'url': urls.models_details,
        'path': paths.models_details,
        'calculation': calculations.load_line,
        'format': formats.models_details,
        'timestamp': True
        },
}