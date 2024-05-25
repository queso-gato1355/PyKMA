from ..utils import Attribute
from ..utils import Authorization
import requests

class URLManager:
    """ URL Manager class
    This class controlls the API urls.
    Adding attributes and setting base url.
    """
    def __init__(self, base_url:str =None, attributes:Attribute =None, auth:Authorization =None):
        self.base_url = base_url
        self.attributes = attributes
        self.auth = auth
        self.params = {}

    def set_base_url(self, url: str) -> None:
        self.base_url = url
    
    def get_base_url(self) -> str:
        return self.base_url
    
    def set_attribute(self, attr:Attribute) -> None:
        if self.attributes == None or len(self.attributes.get_attributes()) == 0:
            self.attributes = attr
        else:
            self.attributes.add_attributes(attr.get_attributes())
        
    def set_auth(self, auth:Authorization) -> None:
        self.auth = auth
    
    def _to_params(self) -> None:
        self.params = self.attributes.get_attributes()
        self.params["authKey"] = self.auth.get_auth()
    
    def request(self, func=lambda x: x):
        self._to_params()
        return func(requests.get(self.base_url, params=self.params))
        
    