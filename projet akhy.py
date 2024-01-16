import csv
from math import *

with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters_tab = [{key : value.replace('\xa0', ' ') for key, value in element.items()} for element in reader]

print(characters_tab)


with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characteristics_tab = [{key : value for key, value in element.items()} for element in reader]

print(characteristics_tab)

poudlard_characters = []

for poudlard_character in characteristics_tab:
    for kaggle_character in characters_tab:
        if poudlard_character['Name'] == kaggle_character['Name']:
            poudlard_character.update(kaggle_character)
            poudlard_characters.append(poudlard_character)

print(poudlard_characters)
# rajouter un "k" = 5 pour connaitre les 5 plus proche voinsins
charactere_test = {"Courage": 9, "Ambition": 2, "Intelligence": 8, "Good": 9}
for perso in poudlard_characters:
    chemin_cas_plus_proche = sqrt(((int(perso["Courage"]) - charactere_test["Courage"])**2) + (((int(perso["Ambition"]) - charactere_test["Ambition"])**2)) + (((int(perso["Intelligence"]) - charactere_test["Intelligence"])**2)) + (((int(perso["Good"]) - charactere_test["Good"])**2)))
print(chemin_cas_plus_proche)