import wordList

# Základní proměnné
play = True
lifes = 5
wordGuess = wordList.getWord()

# Zašifrovat slovo, aby nebyly vidět písmenka
wordHidden = []
x = 0
while (x < len(wordGuess)):
    wordHidden.append("_")
    x += 1

# Hraje se do té doby, dokud není slovo uhádnuté a/nebo dokud má hráč životy.
while (play == True):
    # Vypsat slovo, životy a již uhádnuté a neuhádnuté znaky
    print("Životy:", lifes)
    x = 0
    while (x < len(wordGuess)):
        print(wordHidden[x], end=" ")
        x += 1
    print("\n")

    # Nechat hráče hádat a zkontrolovat znak, který hádá
    guess = str(input("Zadejte písmeno: "))
    found = False
    x = 0
    while (x < len(wordGuess)):
        if (wordGuess[x] == guess):
            wordHidden[x] = wordGuess[x]
            found = True
        x += 1

    # Ubrat život, když znak není ve slově
    if (found == False):
        lifes -= 1

    # Zkontrolovat, zda hráč neuhodl slovo nebo zda má ještě hráč životy -> Případně ukončit hru, výhra/prohra, odhalit hádané slovo, vyzvat k další hře.
    x = 0
    wordFinal = ""
    while (x < len(wordGuess)):
        wordFinal += wordGuess[x]
        x += 1

    if (wordHidden == wordGuess):
        play = False
        print("Vyhrál jsi! Hádané slovo bylo:", wordFinal)

    if (lifes == 0):
        play = False
        print("Prohrál jsi! Hádané slovo bylo:", wordFinal)
