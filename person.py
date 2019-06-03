from constants import *

class Person:
    
    def __init__(self, name):
        self.name = name
        self.counts = {
            TYPE: {
                CALL: 0,
                GENERIC: 0,
                SHARE: 0,
            },
            AUDIO_FILES: 0,
            CONTENT: 0,
            FILES: 0,
            GIFS: 0,
            PHOTOS: 0,
            STICKER: 0,
            VIDEOS: 0
        }
        self.word_frequency = {}
        self.content = []
        self.filteredContent = []

    def __repr__(self):
        return str(self.counts)
