from src.libs.Convert import ascii2str

class Configuration:

    def __init__(self, name=''):
        self.fullname = name
        self.name = ascii2str(name)

    def load(self):
        pass

    def save(self):
        pass

    def new(self, name):
        self.fullname = name
        self.name = ascii2str(name)