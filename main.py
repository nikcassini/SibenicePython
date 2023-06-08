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


while (play == True):
    # Vypsat slovo a nechat hráče hádat
    x = 0
    while (x < len(wordGuess)):
        print(wordHidden[x], end=" ")
        x += 1
    guess = input("Zadejte písmeno: ")

    # Zkontrolovat znak, který hráč hádá
    found = False
    while (x < len(wordGuess)):
        if (guess == wordGuess[x]):
            wordHidden[x] = wordGuess[x]
            found = True
        x += 1
    # Ubrat život, když znak není ve slově
    if (found == False):
        lifes -= 1
        if (lifes == 0):
            play = False