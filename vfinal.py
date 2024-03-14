import csv
from math import *
# coding : utf-8
"""
HENNI Abderrezek
ROUX Pierre
MALBERT Lilian

https://github.com/p3rxs/Choixpeau-LAP

Ce programme est un choipeaux magique, on lui donne des caractéristiques de profile cible, et grâce à un algorithme des k 
plus proches voisins, il sera capable de leur assigner une maison et de donner ses 5 plus proches voisins.

"""

personnages_a_tester = [{"Courage": 9, "Ambition": 2, "Intelligence": 8, "Good": 9}, {"Courage": 6, "Ambition": 7, "Intelligence": 9, "Good": 7}, {"Courage": 3, "Ambition": 8, "Intelligence": 6, "Good": 3}, {"Courage": 2, "Ambition": 3, "Intelligence": 7, "Good": 8}, {"Courage": 3, "Ambition": 4, "Intelligence": 8, "Good": 8}]
k = 5
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


def fusion_table(tabl1, tabl2):
    '''
    rôle : fusionner les données brutes de deux fichiers CSV vers une liste
    entrée : chemin et nom des fichiers csv à traiter
    sortie : liste fusionnée
    '''
    poudlard = []
    for poudlard_character in tabl1:
        for kaggle_character in tabl2:
            if poudlard_character['Name'] == kaggle_character['Name']:
                poudlard_character.update(kaggle_character)
                poudlard.append(poudlard_character)
    return poudlard

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
        if compteur < k :
            k_plus_proche_voisins.append(persos)
            compteur += 1
    return k_plus_proche_voisins

def maison_des_voisins(voisins):
    '''
    rôle : chercher les maisons des 5 plus proche voisins du profil cible
    entrée : liste contenant les 5 plus proche voisins
    sortie : liste des maisons triée de la plus nombreuse à la moin nombreuse
    '''

    liste_maison = [["Gryffindor", 0], ["Slytherin", 0], ["Ravenclaw", 0], ["Hufflepuff", 0]]
    list_maison_proche = []
    for voisin in voisins:
        list_maison_proche.append(voisin['House'])
    for maison in list_maison_proche:
        if maison == "Gryffindor":
            liste_maison[0][1] += 1
        elif maison == "Slytherin":
            liste_maison[1][1] += 1
        elif maison ==  "Ravenclaw":
            liste_maison[2][1] += 1
        elif maison == "Hufflepuff":
            liste_maison[3][1] += 1
    liste_maison.sort(key=lambda x: x[1], reverse=True)
    return liste_maison


def teste_perso_voisins(liste_de_poudlard, perso):
    """
    rôle : attribuer la maison majoritaire au profil cible et tester et résoudre le cas d'égalité si il y en a un
    entrée : liste contenant les 5 plus proche voisins
             le profile cible (dico)
    sortie : liste des 5 plus proches voisins
             le profile cible avec sa maison de rajouter(dico)
    """
    liste_de_poudlard = k_proche_voisins(mesure_de_distance(liste_de_poudlard, perso))
    liste_maison = maison_des_voisins(liste_de_poudlard)
    if liste_maison[0][1] == liste_maison[1][1]:
        if liste_de_poudlard[0]["House"] == liste_maison[0][1] or liste_de_poudlard[0]["House"] == liste_maison[1][1]:
            perso["Maison"] = liste_de_poudlard[0]["House"]
        else:
            perso["Maison"] = liste_de_poudlard[1]["House"]
    else:
        perso["Maison"] = liste_maison[0][0]
    return liste_de_poudlard, perso

def affichage_des_voisins(perso, liste_de_poudlard):
    """
    rôle : afficher les caractéristiques, la maison, et, les noms, les maison, et les distances des 5 plus proche voisins
    entrée : liste des 5 plus proches voisins
             le profile cible avec sa maison de rajouter(dico)
    """
    print(f"Ce personnage a un courage de \033[92m{perso['Courage']}\033[0m, une ambition de \033[92m{perso['Ambition']}\033[0m, une intelligence de \033[92m{perso['Intelligence']}\033[0m, une tendance à la bonté de \033[92m{perso['Good']}\033[0m,\nIl irait bien chez les \033[91m{perso['Maison']}\033[0m")
    print(f'Ses 5 plus proche voisins sont: ')
    for voisin in liste_de_poudlard[:k]:
        print(f"\033[93m{voisin['Name']}, {voisin['House']}, {voisin['Distance']}\033[0m")
    print("\n")

"""

for perso in personnages_a_tester:
    table, perso_avec_maison = teste_perso_voisins(poudlard_characters,perso)
    affichage_des_voisins(perso_avec_maison, table)

    <button id="button1"></button>
        <script type="text/python">  
            from code import *
            from browser import document, html
            def affichage(ev):
                document["aaa"].textContent = questions
            document["button1"].bind("click", affichage)
        </script>
        <p id="aaa">coucou</p>
        document["aaa"].textContent = questions
"""