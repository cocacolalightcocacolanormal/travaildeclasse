# Programme créé par Bénito Ornel Yehouenou
# Programme créé le 26 Octobre 2022
# Combat de monstre

import random

numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
niveau_vie = 20
force_adversaire = random.randint(1, 5)
print("Vous tombez face à un adversaire de difficulté", force_adversaire)

menu = int(input("Que voulez-vous faire ? \n\t 1- Combattre cet adversaire \n\t 2- Contourner cet adversaire et aller ouvrir une autre porte \n\t 3- Afficher les règles du jeu \n\t 4- Quitter la partie"))

if menu == 1:
    numero_combat = +1
    numero_adversaire = +1
    score_de = random.randint(1, 6)
    if score_de >= force_adversaire :
        vie = niveau_vie + score_de
        nombre_victoires = +1
        print("Adversaire :", numero_adversaire ," \n Force de l'adversaire :", force_adversaire ,"\n Niveau de vie de l'usager :", vie ,"\n Combat", numero_combat ,":", nombre_victoires ,"et", nombre_defaites , "\n Lancé du dé :", score_de ,"\n Dernier combat : Victoire")


 