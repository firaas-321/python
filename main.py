import random
import datetime
import time

# Message d'accueil
print("\n===========================Travail pratique 1 =======================================\n\n")
print("Pour commencer la partie, \n")

# Demande à l'utilisateur d'entrer un choix (Roche, Papier, Ciseau ou exit)
entree_utilisateur = input('Veuillez entrer Roche, Papier, Ciseau ou exit pour sortir: \n ')

# pour enregistrer le moment auquel l’utilisateur fait sont choix
t1 = datetime.datetime.now()

# pour convertir la première lettre de l'entrée utilisateur en minuscules
entree_utilisateur = entree_utilisateur[0].lower()

# Liste des choix possibles de l'ordinateur
list_choix = "Roche", "Papier", "Ciseau"

# L'ordinateur choisit aléatoirement l'un des trois choix
choix_ordi = random.choice(list_choix)

# Pause de 1 seconde(j'ai fais ceci car la machine etait trop rapide,
#les temps de debut et de fin etait exactement identique)
time.sleep(1)

#pour enregistrer le moment auquel l'utilisateur a fait son choix
t2 = datetime.datetime.now()

# Affiche le choix de l'ordinateur
print("L'ordinateur a choisi : ", choix_ordi, "\n")

# quitte le jeux
if entree_utilisateur == 'exit':
    exit()

# affiche le résultat adequat en fonction de l'entré utilisateur
# Roche
if entree_utilisateur == 'r' and choix_ordi == 'Roche':
    print('Roche et {} c\'est le même choix \n '.format(choix_ordi))
elif entree_utilisateur == 'r' and choix_ordi == 'Papier':
    print('L\'ordinateur a gagné, Roche perd contre {}\n '.format(choix_ordi))
elif entree_utilisateur == 'r' and choix_ordi == 'Ciseau':
    print('Félicitations ! Vous avez gagné, Roche gagne contre {}\n'.format(choix_ordi))
# Papier
elif entree_utilisateur == 'p' and choix_ordi == 'Papier':
    print('Papier et {} c\'est le même choix \n '.format(choix_ordi))
elif entree_utilisateur == 'p' and choix_ordi == 'Ciseau':
    print('L\'ordinateur a gagné, Papier perd contre {} \n'.format(choix_ordi))
elif entree_utilisateur == 'p' and choix_ordi == 'Roche':
    print('Félicitations ! Vous avez gagné, Papier gagne contre {}\n'.format(choix_ordi))
# Ciseau
elif entree_utilisateur == 'c' and choix_ordi == 'Ciseau':
    print('Ciseau et {} c\'est le même choix \n '.format(choix_ordi))
elif entree_utilisateur == 'c' and choix_ordi == 'Roche':
    print('L\'ordinateur a gagné, Ciseau perd contre {} \n'.format(choix_ordi))
elif entree_utilisateur == 'c' and choix_ordi == 'Papier':
    print('Félicitations ! Vous avez gagné, Ciseau gagne contre {}\n'.format(choix_ordi))
else:
    print('Vous avez sélectionné une valeur invalide. Veuillez relancer le jeu\n')

# Affiche l'heure de début du jeu
print("Temps de début du jeu : ", t1.strftime("%Hh %Mmin %Ss %f microsecondes"))

# Affiche l'heure de fin du jeu
print("Temps de fin du jeu : ", t2.strftime("%Hh %Mmin %Ss %f microsecondes"))

# la moyenne
dif = t2 - t1
moyenne = t1 + dif / 2

print("Moyenne des deux temps:", moyenne.strftime("%Hh %Mmin %Ss %f microsecondes"))
