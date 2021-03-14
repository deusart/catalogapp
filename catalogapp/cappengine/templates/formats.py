def dictionary(json_line, catalog_id):
    data = {}
    json_line['catalogId'] = catalog_id
    data[json_line['id']] = json_line
    return data

def model(json_line, catalog_id):
    entity = {}
    entity_line = {}

    if 'id' in json_line.keys():
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = json_line['id']
        entity_line['name'] = json_line['name']
        if 'article' in json_line.keys():
            entity_line['article'] = json_line['article']
        if 'color' in json_line.keys():    
            entity_line['color'] = json_line['color']
        if 'ean' in json_line.keys():
            entity_line['ean'] = json_line['ean']
        if 'externalId' in json_line.keys():
            entity_line['externalId'] = json_line['externalId']
        if 'vendor' in json_line.keys():
            entity_line['vendor'] = json_line['vendor']
        if 'category' in json_line.keys():
            entity_line['category'] = json_line['category']
        entity[entity_line['id']] = entity_line
     
    return entity