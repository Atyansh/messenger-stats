# Configurable options
FILENAME = 'message_1.json'
PRINT_STATS = True
GENERATE_WORDCLOUD = False

# keys
ACTOR = 'actor'
AUDIO_FILES = 'audio_files'
CONTENT = 'content'
FILES = 'files'
GIFS = 'gifs'
MESSAGES = 'messages'
PHOTOS = 'photos'
REACTIONS = 'reactions'
REACTION = 'reaction'
SENDER = 'sender_name'
STICKER = 'sticker'
TIMESTAMP_MS = 'timestamp_ms'
TYPE = 'type'
VIDEOS = 'videos'

# types
CALL = 'Call'
GENERIC = 'Generic'
SHARE = 'Share'


# Total
TOTAL = 'Total'


# easier iteration
DATA_SET = set([
    AUDIO_FILES,
    CONTENT,
    FILES,
    GIFS,
    PHOTOS,
    STICKER,
    VIDEOS
])

PLURAL_DATA = set([
    AUDIO_FILES,
    FILES,
    GIFS,
    PHOTOS,
    VIDEOS
])


# wordcloud
WIDTH = 2000
HEIGHT = 1000
MIN_WORD_LENGTH = 6
