def load_offset(get_data, output, limit=10000):
    result = []  
    filter = 0      
    data = get_data(filter)

    while len(data) >= limit:
        result += data        
        filter += limit
        data = get_data(filter)
    else:
        result += data
        output(result)


def load_startid(get_data, output, limit=10000):
    result = []        
    step = 1 
    filter = 0      
    data = get_data(filter)
    while len(data) >= limit:
        result += data       
        step += 1
        filter = data[limit-1]['id']
        data = get_data(filter)
    else:
        result += data
        output(result)

def load_startid_partition(get_data, output, partition=False, limit=10000):
    result = []        
    step = 1 
    filter = 0      
    data = get_data(filter)
    while len(data) >= limit:
        result += data
        if partition and step % int(partition) == 0:
            output(result)
            step = 1
            result = []
        step += 1
        filter = data[limit-1]['id']
        data = get_data(filter)
    else:
        result += data
        output(result)
