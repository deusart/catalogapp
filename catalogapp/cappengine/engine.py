from catalogapp.cappengine.templates import urls
from catalogapp.cappengine.utils import files, http
import time

class CatalogEngine(object):
    
    def __init__(self, trace, settings):
        self.trace = trace
        self.token = None
        self.headers = settings.HEADER
        self.credential = settings.CREDENTIAL
        self.folder = settings.FOLDER
        self.encoding = settings.ENCODING
        self.limit = settings.LIMIT
        self.trace('Engine started.','System')
        self.authorization()
    
    def authorization(self):
        url = urls.authorization
        token = http.get_token(url, self.headers, self.credential)
        self.token = {'Authorization': f'Bearer {token}'}
        self.trace('Bearer token received.', 'System')

    def get_response(self, url='', filters='', limit=None):
        if limit is None:
            limit = self.limit
        url = f'{url}?limit={limit}{filters}'
        return http.get_json(url, self.token)

    def save_json(self, path, data, entity, timestamp=False):  
        time.sleep(1)
        if len(data) > 0:
            path = f'{self.folder}{path}'
            message = files.directory_exists(path)
            if message is not None:
                self.trace(message)
            self.trace(files.save_json(path, entity.replace('-','_'), data, self.encoding, timestamp), 'Saving')