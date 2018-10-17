liste = [79, 75, 73, 12, 39, 74, 45, 21, 65, 15]

j = 1
while j < len(liste):
    i = 0
    while i < j:
        if liste[j] < liste[i]:
            liste.insert(i, liste[j])

        else:
            i = i + 1

    j = j + 1

print(liste)