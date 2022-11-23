import random
numero_adversaire=0
force_adversaire = random.randint(1,5)
niveau_vie = 20
numero_combat = 0
nombre_victoires=0
nombre_defaites=0

print('Vous tombez face à face avec un adversaire de difficulté', force_adversaire )
#affiche le menu de la partie
menu = int(input('Que voulez-vous faire ? \n\t 1- Combattre cet adversaire \n\t 2- Contourner cet adversaire et aller ouvrir une autre porte \n\t 3- afficher les regles du jeux \n\t 4- quitter la partie'))

if menu == 1: