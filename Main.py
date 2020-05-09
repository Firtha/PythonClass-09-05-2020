import numpy as np


def somme(_A, _B, _C):
    return _A + _B + _C


def volumeSphere(_rayon):
    return 4 / 3 * np.pi * pow(_rayon, 3)


def compterMots(_chaine):
    mots = _chaine.split()
    for x in mots:
        nbX = _chaine.count(x)
        print("Le mot", x, "est présent", nbX, "fois dans la chaîne", _chaine)


def est_email(_email):
    _arrobas = 0
    _suffixe = 0
    for x in _email:
        if _arrobas == 1 and _suffixe == 4:
            _suffixe = 0

        if _suffixe == 0 and x == '@':
            _arrobas = 1

        if _arrobas == 1 and x == '.' and _suffixe == 0:
            _suffixe = 1

        if _arrobas == 1 and x == 'c' and _suffixe == 1:
            _suffixe = 2

        if _arrobas == 1 and x == 'o' and _suffixe == 2:
            _suffixe = 3

        if _arrobas == 1 and x == 'm' and _suffixe == 3:
            _suffixe = 4

    if _arrobas == 1 and _suffixe == 4:
        return 1
    else:
        return 0


print("Hello World ! Let's start the work with first question.")

### PREMIER BREAKPOINT
# Exo 1
# print("**** EXERCICE 1 ****")
temps = 6.892
distance = 19.7
vitesse = distance / temps
print("Vitesse de", "%.1f" % vitesse, "unité de distance par unité de temps (unknown).")

# Exo 2
print("**** EXERCICE 2 ****")
nom = str(input("Saisissez un nom :"))
age = int(input("Et un age :"))
print("La personne " + nom + ",", age, "ans, a été saisi.")

# Exo 3
print("**** EXERCICE 3 ****")
floatVal = float(input("Saisissez un nombre flottant :"))
if floatVal < 0:
    print("Error this number should be upper or equal of 0")
else:
    print(np.sqrt(floatVal))

# Exo 4
print("**** EXERCICE 4 ****")
mot1 = str(input("Saisissez un mot :"))
mot2 = str(input("Saisissez un autre mot :"))
if mot1 > mot2:
    print(mot1, "est plus 'gros' que", mot2)
elif mot2 > mot1:
    print(mot2, "est plus 'gros' que", mot1)
else:
    print("Les deux mots", mot1, "sont les mêmes !")
print(mot1, "est représenté par la valeur", id(mot1))
print(mot2, "est représenté par la valeur", id(mot2))

# Exo 5
print("**** EXERCICE 5 ****")
pSeuil = 2.3
vSeuil = 7.41
pCourant = float(input("Saisissez une pression actuelle (nombre flottant) :"))
vCourant = float(input("Saisissez un volume actuel (nombre flottant) :"))
if pCourant > pSeuil and vCourant > pSeuil:
    print("Arrêt immédiat de l'enceinte préssurisée.")
elif pCourant > pSeuil and vCourant <= vSeuil:
    print("Veuillez augmenter le volume de l'enceinte")
elif pCourant <= pSeuil and vCourant > vSeuil:
    print("Veuillez diminuer le vomume de l'enceinte")
else:
    print("Tout va bien pour le moment")

### DEUXIEME BREAKPOINT
# Exo 6
print("**** EXERCICE 6 ****")
mailAddr = str(input("Veuillez saisir une adresse email valide de type .com"))
if est_email(mailAddr) == 1:
    print("Valid email address")
else:
    print("Invalid email address")

# Exo 7
print("**** EXERCICE 7 ****")
for x in range(0, 10):
    print("Bonjour numero", x)

# Exo 8
print("**** EXERCICE 8 ****")
monMot = "ShortWord"
print(monMot, ":")
for x in monMot:
    print(x)

# Exo 9
print("**** EXERCICE 9 ****")
a = 0
b = 10
while a < b:
    print("Value of a is", a)
    a += 1

# Exo 10
print("**** EXERCICE 10 ****")
while b > 0:
    b -= 1
    if (b % 2) == 1:
        print("Value of b is", b)

# Exo 11
print("**** EXERCICE 11 ****")
value = int(input("Veuillez saisir une valeur comprise entre 1 et 10 :"))
while not (1 <= value <= 10):
    value = int(input("Veuillez saisir une valeur comprise entre 1 et 10 :"))

# Exo 12
print("**** EXERCICE 12 ****")
maChaine = "ChaqueCaractere"
print(maChaine, ":")
for x in maChaine:
    print(x)

print("Liste de 3 element :")
maListe = ["elem1", "elem2", "elem3"]
for x in maListe:
    print(x)

# Exo 13
print("**** EXERCICE 13 ****")
for x in range(1, 15):
    if (x % 3) == 0:
        print(x)

# Exo 14
print("**** EXERCICE 14 ****")
value = 1
while value < 15:
    if (value % 2) == 0:
        print(value)
    value += 1

for x in range(1, 15):
    if (x % 2) == 0:
        print(x)

### TROISIEME BREAKPOINT
# Exo 15
print("**** EXERCICE 15 ****")
maListe = [17, 38, 10, 25, 72]
maListe.sort()
for x in maListe:
    print(x)

print("On ajoute 12 a la liste")
maListe.append(12)
for x in maListe:
    print(x)

print("On inverse la liste")
maListe.reverse()
currIndex = 0
index17 = 0
for x in maListe:
    print(x)
    if x == 17:
        index17 = currIndex
    currIndex += 1

print("17 est a la position", index17)

print("Sans la valeur 38")
maListe.remove(38)
for x in maListe:
    print(x)

print("2e au 3e element")
maSousListe = maListe[1:3]
for x in maSousListe:
    print(x)

print("1er au 2e element")
maSousListe = maListe[0:2]
for x in maSousListe:
    print(x)

print("3e au dernier element")
maSousListe = maListe[2:len(maListe)]
for x in maSousListe:
    print(x)

print("Tous les elements")
maSousListe = maListe[0:len(maListe)]
for x in maSousListe:
    print(x)

# Exo 16
print("**** EXERCICE 16 ****")
maChaine = "ruojnoB"
print("Chaine initiale :", maChaine)
newChaine = ""
for x in range(len(maChaine) - 1, -1, -1):
    newChaine = newChaine + maChaine[x]

print("Chaine finale :", newChaine)

# Exo 17
print("**** EXERCICE 17 ****")
maChaineInvalide = "Bonjour"
maChaineValide = "okko"
print("Sur la chaine invalide ", maChaineInvalide)
isOk = 1
for x in range(0, len(maChaineInvalide)):
    if maChaineInvalide[x] != maChaineInvalide[len(maChaineInvalide) - 1 - x]:
        isOk = 0
if isOk == 1:
    print("La chaine", maChaineInvalide, "est un palindrome")
else:
    print("La chaine", maChaineInvalide, "n'est pas un palindrome")
print("Sur la chaine valide ", maChaineValide)
isOk = 1
for x in range(0, len(maChaineValide)):
    if maChaineValide[x] != maChaineValide[len(maChaineValide) - 1 - x]:
        isOk = 0
if isOk == 1:
    print("La chaine", maChaineValide, "est un palindrome")
else:
    print("La chaine", maChaineValide, "n'est pas un palindrome")

# Exo 18
print("**** EXERCICE 18 ****")
monEmail = "salutToi@email.com"
arrobas = 0
startCount = 0
nbCharAfterPoint = 0
for x in monEmail:
    if startCount == 1:
        nbCharAfterPoint += 1
    if x == '@':
        arrobas = 1
    if arrobas == 1 and x == '.':
        startCount = 1

if nbCharAfterPoint == 3:
    print("L'adresse email", monEmail, "possède bien 3 caractères après son .")
else:
    print("L'adresse email", monEmail, "ne possède pas 3 caractères après son .")

# Exo 19
print("**** EXERCICE 19 ****")
truc = []
machin = [0.0, 0.0, 0.0, 0.0, 0.0]
print("Affichage de truc :")
for x in truc:
    print(x)

print("Affichage de machin :")
for x in machin:
    print(x)

# Exo 20
print("**** EXERCICE 20 ****")
print("0 à 3 :")
for x in range(0, 4):
    print(x)

print("4 à 7 :")
for x in range(4, 8):
    print(x)

print("2 à 8 avec un pas de 2 :")
for x in range(2, 9, 2):
    print(x)

chose = [0, 1, 2, 3, 4, 5]
print("Appartenance de 3 :", chose.index(3))
try:
    print("Appartenance de 6 :", chose.index(6))
except:
    print("Error in retrieving the index 6 of list 'chose' : Index out of range.")

### Quatrième Breakpoint
# Exo 21
print("**** EXERCICE 21 ****")
x = int(input("Veuillez saisir un nombre (assez petit c'est mieux):"))
file = open("record.txt", "w+")
stringList = []
for y in range(0, x):
    currStr = str(input("Veuillez saisir une chaine :"))
    stringList.append(currStr)

for y in stringList:
    file.write(y + "\n")

file.close()

# Exo 22
print("**** EXERCICE 22 ****")
file = open("record.txt", "r")
content = file.readlines()
for x in content:
    if len(x) > 0:
        if est_email(x.rstrip("\n")) == 1:
            print(x, "is a valid email address")
        else:
            print(x, "is an invalid email address")

file.close()

# Exo 23
print("**** EXERCICE 23 ****")
strGiven = str(input("Veuillez saisir une chaine :"))
compterMots(strGiven)

# Exo 24
print("**** EXERCICE 24 ****")
rayonGiven = float(input("Veuillez saisir un rayon (flottant) :"))
print("Le volume de la sphere est", volumeSphere(rayonGiven))

# Exo 25
print("**** EXERCICE 25 ****")
myTuple = (4, 6, 10)
print("La somme du tuple 4, 6, 10 est", somme(*myTuple))
