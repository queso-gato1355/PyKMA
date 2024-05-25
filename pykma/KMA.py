from .utils.auth import Authorization
from .utils.attribute import Attribute
from .utils.kmaurl import URLManager
from .utils.table import Table

# Low-level
class KMA:
    
    def __init__(self, authkey: str):
        self.auth = Authorization(authkey)
        
    def set_auth(self, auth: Authorization):
        self.auth = auth
    
    def custom_request(self, url: URLManager, attr:Attribute, func=lambda x: x):
        url.set_auth(self.auth)
        url.set_attribute(attr)
        return func(url.request())
    
    def typ01_request(self, url: URLManager, attr=None):
        if attr is None:
            attr = Attribute()
        if isinstance(attr, dict):
            attr = Attribute(attr)
        if not attr.is_attribute("help") or attr.get_attribute("help") != 1:
            attr.add_attribute("help", 1)
            
        def toTable(req):
            if (req.status_code != 200):
                raise Exception("Error: " + str(req.status_code) + " " + req.json()["result"]["message"])
            myTable = Table(req.text)
            return myTable
            
        request = self.custom_request(url, attr, func=toTable)
        return request
            
        