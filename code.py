
from vfinal import *
table = csv_to_table("question_choixpo.csv")

def liste_element_chercher(table, recherche):
    liste = []
    for ligne in table:
        dico = {}
        for cle, valeur in ligne.items():
            if cle == recherche:
                liste.append(valeur)
    return liste

questions = liste_element_chercher(table, 'question')
reponses1 = liste_element_chercher(table, 'reponse1')
reponses2 = liste_element_chercher(table, 'reponse2')
reponses3 = liste_element_chercher(table, 'reponse3')
courages1 = liste_element_chercher(table, 'courage1')
courages2 = liste_element_chercher(table, 'courage2')
courages3 = liste_element_chercher(table, 'courage3')
ambitions1 = liste_element_chercher(table, 'ambition1')
ambitions2 = liste_element_chercher(table, 'ambition2')
ambitions3 = liste_element_chercher(table, 'ambition3')
intelligences1 = liste_element_chercher(table, 'intelligence1')
intelligences2 = liste_element_chercher(table, 'intelligence2')
intelligences3 = liste_element_chercher(table, 'intelligence3')
goods1 = liste_element_chercher(table, 'good1')
goods2 = liste_element_chercher(table, 'good2')
goods3 = liste_element_chercher(table, 'good3')
print(goods1)