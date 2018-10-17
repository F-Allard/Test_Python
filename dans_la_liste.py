liste = [1, 2, 5, 6, 10]
nb = input("Saisissez un nombre: ")

for i in liste:
    if i == nb:
        save = i
        break
    else:
        print(nb, "n'est pas dans la liste")