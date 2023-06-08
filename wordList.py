import random
words = ['les', 'pes', 'strom', 'koza', 'prase', 'lízátko', 'žirafa']

randomWordsID = 0
wordReturn = ""

def getWord():
    randomWordsID = random.randint(0, len(words) -1)
    wordReturn = list(words[randomWordsID])

    return wordReturn