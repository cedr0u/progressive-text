import time
import os

#var attente correspond au temps entre l'actualisation du text print
#var text correspond au text demandé, (user input terminal)

attente = 0.02
text = input("text à afficher:")
text_afficher = ""
caractere = 0

while not len(text) <= len(text_afficher):
    text_afficher = text_afficher + text[len(text_afficher) + caractere]
    caractere + 1
    print(text_afficher)
    time.sleep(attente)
    os.system('cls')
print(text_afficher)