class Authorization:
    
    def __init__(self, apiKey:str =None):
        self.auth = apiKey

    def get_auth(self) -> str:
        return self.auth
    
    def set_auth(self, apiKey: str) -> None:
        self.auth = apiKey
