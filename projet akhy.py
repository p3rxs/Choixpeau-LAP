import csv
from math import *
with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters_tab = [{key : value.replace('\xa0', ' ') for key, value in element.items()} for element in reader]



with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characteristics_tab = [{key : value for key, value in element.items()} for element in reader]



poudlard_characters = []

for poudlard_character in characteristics_tab:
    for kaggle_character in characters_tab:
        if poudlard_character['Name'] == kaggle_character['Name']:
            poudlard_character.update(kaggle_character)
            poudlard_characters.append(poudlard_character)

charactere_test = {"Courage": 9, "Ambition": 2, "Intelligence": 8, "Good": 9}
for perso in poudlard_characters:
    distance = sqrt(((int(perso["Courage"]) - charactere_test["Courage"])**2) + (((int(perso["Ambition"]) - charactere_test["Ambition"])**2)) + (((int(perso["Intelligence"]) - charactere_test["Intelligence"])**2)) + (((int(perso["Good"]) - charactere_test["Good"])**2)))
    perso["Distance"] = distance
poudlard_characters.sort(key=lambda x : x["Distance"])

k_plus_proche_voisins = []
compteur = 0
for persos in poudlard_characters:
    if compteur < 5 :
        k_plus_proche_voisins.append(persos)
        compteur += 1
#print(k_plus_proche_voisins)
liste_maison = [["Gryffindor", 0], ["Slytherin", 0], ["Ravenclaw", 0], ["Hufflepuff", 0]]
list_maison_proche = []
for voisin in k_plus_proche_voisins:
    list_maison_proche.append(voisin['House'])

for maison in list_maison_proche:
    if maison == "Gryffindor":
        liste_maison[0][1] += 1
    elif maison == ["Slytherin"]:
        liste_maison[1][1] += 1
    elif maison == "Ravenclaw":
        liste_maison[2][1] += 1
    else:
        liste_maison[3][1] += 1

liste_maison.sort(key=lambda x: x[1], reverse=True)
print(liste_maison)
'''
for maison in list_maison_proche:
    for i in liste_maison:
        for cle, valeur in liste_maison.items():
            if maison == cle:
                valeur += 1
                i += 1
            else:
                i += 1
print(liste_maison)
'''