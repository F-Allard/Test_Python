# Evolution d'une épidémie dans la ville

import os

nb_total = int(input("Saisissez un nombre d'habitants: "))			# l'utilisateur saisie un nombre d'habitants
nb_malade = 1														# nombre de personne victime de l'épidémie
i = 1																# correspond au jour depuis l'épidémie

while nb_total < 1:
	print("Cette valeur est incorrecte")
	nb_total = int(input("Saisissez un nombre d'habitants: "))

while nb_malade < nb_total:
	i = i + 1
	nb_malade = nb_malade + 3

print(i)

os.system("pause")