import json
import pprint
import re

from person import Person
from constants import *
from wordcloud import WordCloud

pp = pprint.PrettyPrinter()
rows = json.loads(open(FILENAME, 'r').read())

total = Person(TOTAL)

participants = {
    TOTAL: total
}

def bump(data, count, participant, total):
    participant.counts[data] += count
    total.counts[data] += count

def bumpCounts(data, row, participant, total):
    if data in PLURAL_DATA:
        bump(data, len(row[data]), participant, total)
    else:
        bump(data, 1, participant, total)


def buildContent(content, participant, total):
    def update(word, person):
        if word not in person.word_frequency:
            person.word_frequency[word] = 1
        else:
            person.word_frequency[word] += 1

    filtered = re.sub(r'[^\w\s]','',content).upper()
    words = filtered.split()
    for word in words:
        update(word, participant)
        update(word, total)
        if len(word) >= MIN_WORD_LENGTH:
            participant.content.append(word)
            total.content.append(word)


for row in rows[MESSAGES]:
    name = str(row[SENDER])
    if name not in participants:
        participants[name] = Person(name)

    participant = participants[name]
    participant.counts[TYPE][row[TYPE]] += 1

    total.counts[TYPE][row[TYPE]] += 1
    
    for data in DATA_SET:
        if data in row:
            bumpCounts(data, row, participant, total)

            if data == CONTENT and row[TYPE] == GENERIC:
                buildContent(row[CONTENT], participant, total)

if PRINT_STATS:
    pp.pprint(participants)

if GENERATE_WORDCLOUD:
    for participant in participants.values():
        print participant.name
        content = " ".join(participant.content)
        wordcloud = WordCloud(width=WIDTH, height=HEIGHT).generate(content)
        image = wordcloud.to_image()
        image.show()
