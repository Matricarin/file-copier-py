class Settings():
    
    def __init__(self):
        self.sources = []
        self.target = ""
        
    def get_settings(self, sources, target):
        self.sources = sources
        self.target = target