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

list_maison_proche = []
for voisin in k_plus_proche_voisins:
    list_maison_proche.append(voisin['House'])
print(list_maison_proche) 
for maison in list_maison_proche:
    if maison == list_maison_proche(0):
        maison_majoritaire = maison
    else:
        if maison == maison_majoritaire:
            