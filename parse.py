import json
import pprint
import re

from person import Person
from constants import *

pp = pprint.PrettyPrinter()
rows = json.loads(open(FILENAME, 'r').read())

total = Person(TOTAL)

participants = {
    TOTAL: total
}

def updateFrequency(content, participant, total):
    def update(word, person):
        if word not in person.word_frequency:
            person.word_frequency[word] = 1
        else:
            person.word_frequency[word] += 1

    words = re.sub(r'[^\w\s]','',content).upper().split()
    for word in words:
        update(word, participant)
        update(word, total)


for row in rows[MESSAGES]:
    name = str(row[SENDER])
    if name not in participants:
        participants[name] = Person(name)

    participant = participants[name]
    participant.counts[TYPE][row[TYPE]] += 1

    total.counts[TYPE][row[TYPE]] += 1
    
    for data in DATA_SET:
        if data in row:
            participant.counts[data] += 1
            total.counts[data] += 1

            if data == CONTENT and row[TYPE] == GENERIC:
                updateFrequency(row[CONTENT], participant, total)

pp.pprint(participants)

# pp.pprint(total.word_frequency)
