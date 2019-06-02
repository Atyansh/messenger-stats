from constants import *

class Person:
    
    def __init__(self, name):
        self.name = name
        self.counts = {
            GENERIC: 0,
            SHARE: 0,
            CALL: 0,
            CONTENT: 0,
            PHOTOS: 0
        }

    def __repr__(self):
        return str(self.counts)
