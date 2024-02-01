import csv
from math import *
perso1 = {"Courage": 9, "Ambition": 2, "Intelligence": 8, "Good": 9}
perso2 = {"Courage": 6, "Ambition": 7, "Intelligence": 9, "Good": 7}
perso3 = {"Courage": 3, "Ambition": 8, "Intelligence": 6, "Good": 3}
perso4 = {"Courage": 2, "Ambition": 3, "Intelligence": 7, "Good": 8}
perso5 = {"Courage": 3, "Ambition": 4, "Intelligence": 8, "Good": 8}

def csv_to_table(csv_file):
    '''
    rôle : extraire les données brutes d'un fichier CSV vers une structure de données de type enregistrement
    entrée : chemin et nom du fichier csv à traiter
    sortie : enregistrement
    '''

    with open(csv_file, mode='r', encoding='utf-8') as f:
        tab = []
        lines = f.readlines()
        key_line = lines[0].strip()
        keys = key_line.split(';')
        for line in lines[1:]:
            line = line.strip()
            values = line.split(';')
            dic = {}
            for i in range(len(keys)):
                dic[keys[i]] = values[i].strip()
            tab.append(dic)
    return tab
poudlard_characters = []


def fusion_table(tabl1, tabl2):
    '''
    rôle : fusionner les données brutes de deux fichiers CSV vers une liste
    entrée : chemin et nom des fichiers csv à traiter
    sortie : liste fusionnée
    '''
    for poudlard_character in tabl1:
        for kaggle_character in tabl2:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard_characters.append(poudlard_character)
    return poudlard_characters
poudlard_characters = fusion_table(csv_to_table("Caracteristiques_des_persos.csv"), csv_to_table("Characters.csv"))


def mesure_de_distance(fusion_de_table, perso_test):
    '''
    rôle : mesurer les distances entre le profil cible et tous les autres profiles
    entrée : liste fusionnée
    sortie : liste fusionnée avec les distances rajouté au personnages
    '''
    for perso in fusion_de_table:
        distance = sqrt(((int(perso["Courage"]) - perso_test["Courage"])**2) + (((int(perso["Ambition"]) - perso_test["Ambition"])**2)) + (((int(perso["Intelligence"]) - perso_test["Intelligence"])**2)) + (((int(perso["Good"]) - perso_test["Good"])**2)))
        perso["Distance"] = distance
    fusion_de_table.sort(key=lambda x : x["Distance"])
    return fusion_de_table


def k_proche_voisins(fusion_de_table):
    '''
    rôle : chercher les 5 plus proche voisin du profil cible
    entrée : liste fusionnéeavec les distances rajouté au personnages
    sortie : liste fusionnée avec les distances rajouté au personnages trié dans l'ordre de distance décroissant(du plus proche au plus éloigner)
    '''
    k_plus_proche_voisins = []
    compteur = 0
    for persos in fusion_de_table:
        if compteur < 5 :
            k_plus_proche_voisins.append(persos)
            compteur += 1
    return k_plus_proche_voisins


def tri_des_voisins(voisins):
    liste_maison = [["Gryffindor", 0], ["Slytherin", 0], ["Ravenclaw", 0], ["Hufflepuff", 0]]
    list_maison_proche = []
    for voisin in voisins:
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
    return liste_maison

liste_maison = tri_des_voisins(poudlard_characters)

def teste_perso_voisins(liste_de_poudlard, perso):
    liste_de_poudlard = mesure_de_distance(liste_de_poudlard, perso)
    k_plus_proche_voisins = k_proche_voisins(liste_de_poudlard)
    liste_maison = tri_des_voisins(k_plus_proche_voisins)
    if liste_maison[0][1] == liste_maison[1][1]:
        perso["Maison"] = k_plus_proche_voisins[0]["House"]
    else:
        perso["Maison"] = liste_maison[0][0]
    return perso

liste_maison = tri_des_voisins(poudlard_characters)

def affichage_des_voisins(perso, liste_de_poudlard):
    print(f"Ce personnage a un courage de {perso['Courage']}, une ambition de {perso['Ambition']}, une intelligence de {perso['Intelligence']}, une tendance à la bonté de {perso['Good']},\nIl irait bien chez les {perso['Maison']}")
    print(f'Ses 5 plus proche voisins sont: ')
    compteur = 0
    for voisin in liste_de_poudlard:
        print(voisin['Name'], voisin['House'], voisin['Distance'])
        if compteur != 5:
            compteur += 1
        else :
            liste_de_poudlard = mesure_de_distance(liste_de_poudlard, perso)
            liste_de_poudlard = k_proche_voisins(liste_de_poudlard)
            return "Voila, au prochains!"

print(affichage_des_voisins(teste_perso_voisins(poudlard_characters, perso1), poudlard_characters))

print(tri_des_voisins(k_proche_voisins(mesure_de_distance(fusion_table(csv_to_table("Caracteristiques_des_persos.csv"), csv_to_table("Characters.csv")), perso2))))

"""
poudlard_characters = mesure_de_distance(poudlard_characters, perso1)
    k_plus_proche_voisins = k_proche_voisins(poudlard_characters)
    liste_maison = tri_des_voisins(k_plus_proche_voisins)
    if liste_maison[0][1] == liste_maison[1][1]:
        perso1["Maison"] = k_plus_proche_voisins[0]["House"]
    else:
        perso1["Maison"] = liste_maison[0][0]
        """