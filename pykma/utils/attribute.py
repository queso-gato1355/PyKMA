class Attribute:        
    def __init__(self, attributes: dict ={}):
        self.attributes = attributes.copy()
    
    def add_attribute(self, key, value) -> None:
        self.attributes[key] = value
        
    def add_attributes(self, attributes: dict) -> None:
        for key, value in attributes.items():
            self.attributes[key] = value
    
    def get_attribute(self, key: str) -> str:
        return self.attributes[key]

    def remove_attribute(self, key: str) -> str:
        removed = self.attributes[key]
        del self.attributes[key]
        return removed
        
    def is_attribute(self, key: str) -> bool:
        return key in self.attributes
    
    def get_attributes(self) -> dict:
        return self.attributes
    
    def to_string(self) -> str:
        result = "?"
        for i, (key, value) in enumerate(self.attributes.items()):
            if i == 0:
                result += key + "=" + value
            else:
                result += "&" + key + "=" + value
        return result