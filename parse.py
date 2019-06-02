import json
import pprint
from person import Person
from constants import *

pp = pprint.PrettyPrinter()
rows = json.loads(open(FILENAME, 'r').read())

total = Person(TOTAL)

participants = {
    TOTAL: total
}

for row in rows[MESSAGES]:
    name = str(row[SENDER])
    if name not in participants:
        participants[name] = Person(name)

    participant = participants[name]
    participant.counts[row[TYPE]] += 1

    total.counts[row[TYPE]] += 1

    if CONTENT in row:
        participant.counts[CONTENT] += 1
        total.counts[CONTENT] += 1
    if PHOTOS in row:
        participant.counts[PHOTOS] += len(row[PHOTOS])
        total.counts[PHOTOS] += len(row[PHOTOS])

pp.pprint(participants)
