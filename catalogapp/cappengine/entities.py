from catalogapp.cappengine.templates import urls, paths, filters, calculations, formats

entity = {
    'catalogs': {
        'url': urls.catalogs,
        'path': paths.catalogs,
        'filter': filters.offset,
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
        'format': formats.model,
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
        'format': formats.entity,
        'timestamp': True
        },

    # 'models-cards': {
    #     'entity': 'models',
    #     'subentity': 'cards',
    #     'url': urls['catalog_entity_id_cards'],
    #     'filter': filters['startid'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },
    # 'models-details': {
    #     'entity': 'models',
    #     'subentity': 'details',
    #     'url': urls['catalog_entity_id_details'],
    #     'filter': filters['startid'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },

    # 'modified': {
    #     'entity': 'models',
    #     'url_modified': urls['catalog_modified'],
    #     'url_models': urls['catalog_entity_id_details'],
    #     'url_models_details': urls['catalog_entity_id_details'],
    #     'filter': filters['startid'],
    #     'filter_modified': filters['fromUtc'],
    #     'path': path['catalog_entity_timestamp'],
    #     'path_models': path['catalog_entity_timestamp'],
    #     'path_models_details': path['catalog_entity_timestamp'],
    #     'timestamp': True
    #     },
    # 'categories-details': {
    #     'entity': 'categories',
    #     'subentity': 'details',
    #     'url': urls['catalog_entity_id'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'offset',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },
    # 'deleted': {
    #     'entity': 'categories',
    #     'subentity': 'details',
    #     'url': urls['catalog_entity_id'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },
}