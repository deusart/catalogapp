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
        'format': formats.dictionary,
        'timestamp': False
        },
    'suppliers': {
        'url': urls.suppliers,
        'path': paths.suppliers,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.dictionary,
        'timestamp': False
        },
    'categories': {
        'url': urls.categories,
        'path': paths.categories,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.dictionary,
        'timestamp': False
        },
    'pricing_profiles': {
        'url': urls.pricing_profiles,
        'path': paths.pricing_profiles,
        'filter': filters.offset,
        'calculation': calculations.load_offset,
        'format': formats.dictionary,
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
    # 'suppliers-prices': {
    #     'entity': 'suppliers',
    #     'subentity': 'prices',
    #     'url': urls['catalog_entity_id_prices'],
    #     'filter': filters['startid'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },
    # 'pricing-profiles-prices': {
    #     'entity': 'pricing-profiles',
    #     'subentity': 'prices',
    #     'url': urls['catalog_entity_id_prices'],
    #     'filter': filters['startid'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'subentity',
    #     'timestamp': True
    #     },
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
    # 'categories-details': {
    #     'entity': 'categories',
    #     'subentity': 'details',
    #     'url': urls['catalog_entity_id'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'offset',
    #     'entities_type': 'entity',
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