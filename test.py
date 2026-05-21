print("zweiter Anlauf")

liste = ['H', 'l', 'o', 'a', 'e', 'W', 't', 'l']
gruss = [0, 3, 1, 1, 2]
gruss2 = [5, 4, 7, 6]

wort = "".join(liste[i] for i in gruss)
wort2 = "".join (liste[i] for i in gruss2)

print(wort + ' ' + wort2)