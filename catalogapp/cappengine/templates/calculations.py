def load_offset(entity):
    result = []  
    filter = 0
    limit = entity.engine.limit
    data = entity.request(filter)

    while len(data) >= limit:
        result += data        
        filter += limit
        data = entity.request(filter)
    else:
        result += data
        entity.output(result)

def load_startid(entity):
    result = []
    filter = 0
    limit = entity.engine.limit
    data = entity.request(filter)

    while len(data) >= limit:
        result += data
        filter = data[limit-1]['id']
        data = entity.request(filter)
    else:
        result += data
        entity.output(result)

def load_startid_partition(entity):
    result = []
    step = 1
    filter = 0

    limit = entity.engine.limit
    partition = entity.partition

    data = entity.request(filter)

    while len(data) >= limit:
        result += data
        if partition and step % int(partition) == 0:
            entity.output(result)
            step = 1
            result = []
        step += 1
        filter = data[limit-1]['id']
        data = entity.request(filter)
    else:
        result += data
        entity.output(result)

def load_startid_prices(entity):
    filter = 0

    limit = entity.engine.limit

    data = entity.request(filter)

    while len(data) >= limit:
        entity.result += data
        if len(entity.result) > limit*2:
            entity.output(entity.result)
            entity.result = []
        filter = data[limit-1]['id']
        data = entity.request(filter)
    else:
        entity.result += data
        if len(entity.result) > limit*2:
            entity.output(entity.result)
            entity.result = []

def load_line(entity):    
    data = entity.request()
    limit = entity.engine.limit
    if isinstance(data, dict):
        data = [data,]
    entity.result += data
    if len(entity.result) > entity.partition:
            entity.output(entity.result)
            entity.result = []
   