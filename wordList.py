import random
words = ['les', 'pes', 'strom', 'koza', 'prase', 'lízátko', 'žirafa', 'nevěsta', 'žába', 'číslo', 'včelka', 'plevel', 'prsten', 'prodavač', 'peníze', 'ibišek', 'pojem', 'broskev', 'humr', 'pastelky', 'hlavonožec', 'matice', 'produkt', 'vlk', 'tchýně', 'knížka', 'pěvec', 'lotus', 'podzemí', 'mír', 'minimum', 'osel', 'záhada', 'návod', 'večerka', 'blůza', 'jaguár', 'kočka', 'zlomek', 'překážka', 'léky', 'čočka', 'sklář', 'lékárnice', 'rámus', 'plachta', 'cvičebna', 'kryt', 'symbol', 'náprstek', 'přátelé', 'podnik', 'provaz', 'vypínač', 'pití', 'žádost', 'balada', 'vstupenka', 'luk', 'bažina', 'letiště', 'modelína', 'pirát', 'investice', 'kapičky', 'vazba', 'císař', 'chobot', 'brusle', 'železo', 'odpornost', 'kulomet', 'pendrek', 'princezna', 'houbička', 'pšenice', 'kouzelník', 'tiskopis', 'pot', 'zedník', 'opasek', 'zinek', 'vykřičník', 'generátor', 'figura', 'plán', 'plotna', 'botanika', 'sorbet', 'koště', 'oheň']

randomWordsID = 0
wordReturn = ""

def getWord():
    randomWordsID = random.randint(0, len(words) -1)
    wordReturn = list(words[randomWordsID])

    return wordReturn