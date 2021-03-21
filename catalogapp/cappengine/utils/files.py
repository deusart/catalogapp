import json
import datetime
import os

def save_json(path, entity, data, encoding='UTF-16', timestamp = False):
    if timestamp:
        entity = f'{entity}_{int(datetime.datetime.now().timestamp())}'
    try:
        with open(f'{path}{entity}.json', 'w', encoding=encoding) as outfile:
            outfile.write(json.dumps(data, ensure_ascii=False))
        return f'File {path}{entity}.json is saved. ({len(data)} Items)'
    except Exception as error:
        return error
        
def directory_exists(path):    
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            return "Creation of the directory %s failed" % path
        else:
            return "Successfully created the directory %s " % path