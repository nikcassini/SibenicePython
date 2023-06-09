import wordList

# Základní proměnné
play = True
lifes = 10
wordGuess = wordList.getWord()
charactersUsed = []
wordHidden = []

# Zašifrovat slovo, aby nebyly vidět písmenka
x = 0
while (x < len(wordGuess)):
    wordHidden.append("_")
    x += 1

# Hraje se do té doby, dokud není slovo uhádnuté a/nebo dokud má hráč životy.
while (play == True):
    # Vypsat slovo, životy a již uhádnuté a neuhádnuté znaky
    x = 0
    characters = ""
    while (x < len(charactersUsed)):
        characters += charactersUsed[x] + ", "
        x += 1
    print("Životy:", lifes)
    print("Použité znaky:", characters)
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
        charactersUsed.append(guess)

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
