from catalogapp.cappengine.templates import urls
from catalogapp.cappengine.utils import files, http
import datetime
import time
class CatalogEngine(object):
    
    def __init__(self, trace, settings):
        self.trace = trace
        self.token = None
        self.last_timestamp = 0
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
        
        try:
            response = http.get_json(url, self.token)
        except Exception as exeption:
            message = str(exeption).replace("'","")
            self.trace(f'Request error {message}. Empty Return.', 'Error')
            response = []    
        return response

    def save_json(self, path, data, entity, timestamp=False):  
        current_timestamp = int(datetime.datetime.now().timestamp())
        if self.last_timestamp != current_timestamp:
            self.last_timestamp = current_timestamp
        else:
            time.sleep(1)
            self.last_timestamp = current_timestamp

        if len(data) > 0:
            path = f'{self.folder}{path}'
            message = files.directory_exists(path)
            if message is not None:
                self.trace(message)
            self.trace(files.save_json(path, entity.replace('-','_'), data, self.encoding, timestamp), 'Saving')