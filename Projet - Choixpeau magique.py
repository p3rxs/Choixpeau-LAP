with open("Characters.csv", mode='r', encoding='utf-8') as f:
    character_list = f.readlines()
    
# Necessite un "nettoyage" pour retirer les \n en fin de chaîne
# la méthode strip() supprime les \n en début et fin de chaîne de caractères

for i, chaine in enumerate(character_list):
    character_list[i] = chaine.strip()       
print(character_list)


with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    student_attributes = f.readlines()
    
# Necessite un "nettoyage" pour retirer les \n en fin de chaîne
# la méthode strip() supprime les \n en début et fin de chaîne de caractères

for i, chaine in enumerate(student_attributes):
    student_attributes[i] = chaine.strip()   
    student_attributes[i] = chaine.pop()    
print(student_attributes)