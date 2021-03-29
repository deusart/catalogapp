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
        else:
            entity_line['article'] = ""  

        if 'color' in item.keys():    
            entity_line['color'] = item['color']
        else:
            entity_line['color'] = ""

        if 'ean' in item.keys():
            entity_line['ean'] = item['ean']
        else:
            entity_line['ean'] = ""

        if 'externalId' in item.keys():
            entity_line['externalId'] = item['externalId']
        else:
            entity_line['externalId'] = ""
            
        if 'vendor' in item.keys():
            entity_line['vendorId'] = item['vendor']['id']
        else:
            entity_line['vendorId'] = ""

        if 'category' in item.keys():
            entity_line['categoryId'] = item['category']['id']
        else:
            entity_line['categoryId'] = ""
            
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
        else:
            entity_line['competitorPrices'] = [] 
        if 'modelToLibraries' in item.keys():    
            entity_line['modelToLibraries'] = item['modelToLibraries']
        else:
            entity_line['modelToLibraries'] = [] 
        if 'propertyValues' in item.keys():
            entity_line['propertyValues'] = item['propertyValues']
        else:
            entity_line['propertyValues'] = [] 
        if 'description' in item.keys():
            entity_line['description'] = item['description']
        else:
            entity_line['description'] = {}
        if 'similarModels' in item.keys():
            entity_line['similarModels'] = item['similarModels']
        else:
            entity_line['similarModels'] = {}
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
        else:
            entity_line['priceArticle'] = ""

        if 'priceCurrency' in item.keys():
            entity_line['priceCurrency'] = item['priceCurrency']
        else:
            entity_line['priceCurrency'] = ""

        if 'minRetailPrice' in item.keys():
            entity_line['minRetailPrice'] = item['minRetailPrice']
        else:
            entity_line['minRetailPrice'] = ""

        if 'minRetailPriceCurrency' in item.keys():    
            entity_line['minRetailPriceCurrency'] = item['minRetailPriceCurrency']
        else:
            entity_line['minRetailPriceCurrency'] = ""

        if 'inStockAmount' in item.keys():
            entity_line['inStockAmount'] = item['inStockAmount']
        else:
            entity_line['inStockAmount'] = ""

        if 'deliveryTime' in item.keys():
            entity_line['deliveryTime'] = item['deliveryTime']
        else:
            entity_line['deliveryTime'] = ""

        if 'priceSellerCode' in item.keys():    
            entity_line['priceSellerCode'] = item['priceSellerCode']
        else:
            entity_line['priceSellerCode'] = ""

        if 'validated' in item.keys():
            entity_line['validated'] = item['validated']
        else:
            entity_line['validated'] = ""

        if 'manuallyValidated' in item.keys():
            entity_line['manuallyValidated'] = item['manuallyValidated']
        else:
            entity_line['manuallyValidated'] = ""

        if 'suspicious' in item.keys():
            entity_line['suspicious'] = item['suspicious']
        else:
            entity_line['suspicious'] = ""

        if model_id is None:
            if 'model' in item.keys():
                entity_line['modelId'] = item['model']['id']
        else:
            entity_line['modelId'] = model_id

        if 'supplier' in item.keys():
            entity_line['supplierId'] = item['supplier']['id']
        else:
            entity_line['supplierId'] = ""

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
        else:
            entity_line['price'] = ""

        if 'supplierPrice' in item.keys():
            entity_line['supplierPrice'] = item['supplierPrice']
        else:
            entity_line['supplierPrice'] = ""

        if 'deliveryTime' in item.keys():
            entity_line['deliveryTime'] = item['deliveryTime']
        else:
            entity_line['deliveryTime'] = ""

        if 'deliveryTownPrice' in item.keys():    
            entity_line['deliveryTownPrice'] = item['deliveryTownPrice']
        else:
            entity_line['deliveryTownPrice'] = ""

        if 'deliveryCountryPrice' in item.keys():
            entity_line['deliveryCountryPrice'] = item['deliveryCountryPrice']
        else:
            entity_line['deliveryCountryPrice'] = ""

        if 'minCompetitorPrice' in item.keys():
            entity_line['minCompetitorPrice'] = item['minCompetitorPrice']
        else:
            entity_line['minCompetitorPrice'] = ""

        if 'installmentPrice' in item.keys():    
            entity_line['installmentPrice'] = item['installmentPrice']
        else:
            entity_line['installmentPrice'] = ""

        if 'maxInstallmentCost' in item.keys():
            entity_line['maxInstallmentCost'] = item['maxInstallmentCost']
        else:
            entity_line['maxInstallmentCost'] = ""

        if 'inStockAmount' in item.keys():
            entity_line['inStockAmount'] = item['inStockAmount']
        else:
            entity_line['inStockAmount'] = ""

        if 'minRetailPrice' in item.keys():
            entity_line['minRetailPrice'] = item['minRetailPrice']
        else:
            entity_line['minRetailPrice'] = ""

        if 'supplierId' in item.keys():
            entity_line['supplierId'] = item['supplierId']
        else:
            entity_line['supplierId'] = ""

        if 'exportAttributeId' in item.keys():
            entity_line['exportAttributeId'] = item['exportAttributeId']
        else:
            entity_line['exportAttributeId'] = ""

        if 'pricingProfile' in item.keys():
            entity_line['pricingProfileId'] = item['pricingProfile']['id']
        else:
            entity_line['pricingProfileId'] = ""

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
        else:
            entity_line['properties'] = []
        if 'propertyGroups' in item.keys():    
            entity_line['propertyGroups'] = item['propertyGroups']  
        else:
            entity_line['propertyGroups'] = []    
        entity[entity_line['id']] = entity_line     
    return entity