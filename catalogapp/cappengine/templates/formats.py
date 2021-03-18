def entity(item, catalog_id):
    data = {}
    item['catalogId'] = catalog_id
    data[item['id']] = item
    return data

def models(item, catalog_id):
    entity = {}
    entity_line = {}

    if 'id' in item.keys():
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = item['id']
        entity_line['name'] = item['name']
        if 'article' in item.keys():
            entity_line['article'] = item['article']
        if 'color' in item.keys():    
            entity_line['color'] = item['color']
        if 'ean' in item.keys():
            entity_line['ean'] = item['ean']
        if 'externalId' in item.keys():
            entity_line['externalId'] = item['externalId']
        if 'vendor' in item.keys():
            entity_line['vendorId'] = item['vendor']['id']
        if 'category' in item.keys():
            entity_line['categoryId'] = item['category']['id']
        entity[entity_line['id']] = entity_line     
    return entity

def models_details(item, catalog_id):
    entity = {}
    entity_line = {}

    if 'id' in item.keys():
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = item['id']      
        if 'competitorPrices' in item.keys():
            entity_line['competitorPrices'] = item['competitorPrices']
        if 'modelToLibraries' in item.keys():    
            entity_line['modelToLibraries'] = item['modelToLibraries']
        if 'propertyValues' in item.keys():
            entity_line['propertyValues'] = item['propertyValues']
        if 'description' in item.keys():
            entity_line['description'] = item['description']
        if 'similarModels' in item.keys():
            entity_line['similarModels'] = item['similarModels']
        entity[entity_line['id']] = entity_line     
    return entity

def suppliers_prices(item, catalog_id, model_id=None):
    entity = {}
    entity_line = {}

    if 'id' in item.keys():
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = item['id']
        entity_line['priceName'] = item['priceName']
        if 'priceArticle' in item.keys():
            entity_line['priceArticle'] = item['priceArticle']
        if 'priceCurrency' in item.keys():
            entity_line['priceCurrency'] = item['priceCurrency']
        if 'minRetailPrice' in item.keys():
            entity_line['minRetailPrice'] = item['minRetailPrice']
        if 'minRetailPriceCurrency' in item.keys():    
            entity_line['minRetailPriceCurrency'] = item['minRetailPriceCurrency']
        if 'inStockAmount' in item.keys():
            entity_line['inStockAmount'] = item['inStockAmount']
        if 'deliveryTime' in item.keys():
            entity_line['deliveryTime'] = item['deliveryTime']
        if 'priceSellerCode' in item.keys():    
            entity_line['priceSellerCode'] = item['priceSellerCode']
        if 'validated' in item.keys():
            entity_line['validated'] = item['validated']
        if 'manuallyValidated' in item.keys():
            entity_line['manuallyValidated'] = item['manuallyValidated']
        if 'suspicious' in item.keys():
            entity_line['suspicious'] = item['suspicious']
        if model_id is None:
            if 'model' in item.keys():
                entity_line['modelId'] = item['model']['id']
        else:
            entity_line['modelId'] = model_id
        if 'supplier' in item.keys():
            entity_line['supplierId'] = item['supplier']['id']

        entity[entity_line['id']] = entity_line
    return entity

def pricing_profiles_prices(item, catalog_id, model_id=None):
    entity = {}
    entity_line = {}

    if 'id' in item.keys():
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = item['id']
        if 'price' in item.keys():
            entity_line['price'] = item['price']
        if 'supplierPrice' in item.keys():
            entity_line['supplierPrice'] = item['supplierPrice']
        if 'deliveryTime' in item.keys():
            entity_line['deliveryTime'] = item['deliveryTime']
        if 'deliveryTownPrice' in item.keys():    
            entity_line['deliveryTownPrice'] = item['deliveryTownPrice']
        if 'deliveryCountryPrice' in item.keys():
            entity_line['deliveryCountryPrice'] = item['deliveryCountryPrice']
        if 'minCompetitorPrice' in item.keys():
            entity_line['minCompetitorPrice'] = item['minCompetitorPrice']
        if 'installmentPrice' in item.keys():    
            entity_line['installmentPrice'] = item['installmentPrice']
        if 'maxInstallmentCost' in item.keys():
            entity_line['maxInstallmentCost'] = item['maxInstallmentCost']
        if 'inStockAmount' in item.keys():
            entity_line['inStockAmount'] = item['inStockAmount']
        if 'minRetailPrice' in item.keys():
            entity_line['minRetailPrice'] = item['minRetailPrice']
        if 'supplierId' in item.keys():
            entity_line['supplierId'] = item['supplierId']
        if 'exportAttributeId' in item.keys():
            entity_line['exportAttributeId'] = item['exportAttributeId']
        if 'pricingProfile' in item.keys():
            entity_line['pricingProfileId'] = item['pricingProfile']['id']
        if model_id is None:
            if 'model' in item.keys():
                entity_line['modelId'] = item['model']['id']
        else:
            entity_line['modelId'] = model_id

        entity[entity_line['id']] = entity_line
    return entity

def categories_details(item, catalog_id):
    entity = {}
    entity_line = {}

    if 'properties' in item.keys() and (len(item['properties']) > 0 or len(item['propertyGroups']) > 0):
        entity_line['catalogId'] = catalog_id
        entity_line['id'] = item['id']
        if 'properties' in item.keys():
            entity_line['properties'] = item['properties']
        if 'propertyGroups' in item.keys():    
            entity_line['propertyGroups'] = item['propertyGroups']      
        entity[entity_line['id']] = entity_line     
    return entity