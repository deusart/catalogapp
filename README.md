# catalogapp
Project for data extraction  into json

Modules needed to be installed:
pip install urllib3
pip install requests

module description
- main.py - space to run module
-- core - support module with common functions and objects
--- http.py - module with request functions
---- get_json(url, headers)
---- get_token(url, headers, credentials)
