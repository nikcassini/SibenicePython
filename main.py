import wordList

# Základní proměnné
win = False
wordGuess = wordList.getWord()
wordRevealed = wordGuess

# Zašifrovat slovo, aby nebyly vidět písmenka
x = 0
while (x < len(wordGuess)):
    wordRevealed[x] = "_"