from catalogapp.engine.templates import urls, path
from catalogapp.engine import calculations

entity = {
    # 'catalogs': {
    #     'entity': 'catalogs',
    #     'subentity': None,
    #     'url': urls['catalogs'],
    #     'filter': filters['empty'],
    #     'path': path['catalogs'],
    #     'filters_type': 'empty',
    #     'entities_type': 'root',
    #     'timestamp': False
    #     },
    'vendors': {       
        'url': urls['vendors'],
        'path': path['vendors'],
        'calculation_type': calculations.load_offset_total,
        'timestamp': False
        },
    # 'suppliers': {
    #     'entity': 'suppliers',
    #     'subentity': None,
    #     'url': urls['catalog_entity'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity'],
    #     'filters_type': 'offset',
    #     'entities_type': 'entity',
    #     'timestamp': False
    #     },
    # 'categories': {
    #     'entity': 'categories',
    #     'subentity': None,
    #     'url': urls['catalog_entity'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity'],
    #     'filters_type': 'offset',
    #     'entities_type': 'entity',
    #     'timestamp': False
    #     },
    # 'pricing-profiles': {
    #     'entity': 'pricing-profiles',
    #     'subentity': None,
    #     'url': urls['catalog_entity'],
    #     'filter': filters['offset'],
    #     'path': path['catalog_entity'],
    #     'filters_type': 'offset',
    #     'entities_type': 'entity',
    #     'timestamp': False
    #     },
    # 'models': {
    #     'entity': 'models',
    #     'subentity': None,
    #     'url': urls['catalog_entity'],
    #     'filter': filters['startid'],
    #     'path': path['catalog_entity_timestamp'],
    #     'filters_type': 'startid',
    #     'entities_type': 'entity',
    #     'timestamp': True
    #     },
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