
from vfinal import *
table = csv_to_table("question_choixpo.csv")


for ligne in table:
    dico = {}
    for element in ligne:
        dico[element] = element[table]
        print(dico)
