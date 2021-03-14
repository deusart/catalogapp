def dictionary(json_list, catalog_id):
    data = {}
    for item in json_list:
        item['catalogId'] = catalog_id
        data[item['id']] = item
    return data