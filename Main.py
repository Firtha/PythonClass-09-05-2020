import numpy as np

print("Hello World ! Let's start the work with first question.")

### PREMIER BREAKPOINT
# Exo 1
print("**** EXERCICE 1 ****")
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
    print(mot1,"est plus 'gros' que", mot2)
elif mot2 > mot1:
    print(mot2, "est plus 'gros' que", mot1)
else:
    print("Les deux mots", mot1,"sont les mêmes !")
print(mot1,"est représenté par la valeur",id(mot1))
print(mot2,"est représenté par la valeur",id(mot2))

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
strLength = len(mailAddr)
arrobas = 0
suffixe = 0
for x in mailAddr:
    if arrobas == 1 and suffixe == 4:
        suffixe = 0

    if suffixe == 0 and x == '@':
        arrobas = 1

    if arrobas == 1 and x == '.' and suffixe == 0:
        suffixe = 1

    if arrobas == 1 and x == 'c' and suffixe == 1:
        suffixe = 2

    if arrobas == 1 and x == 'o' and suffixe == 2:
        suffixe = 3

    if arrobas == 1 and x == 'm' and suffixe == 3:
        suffixe = 4

if arrobas == 1 and suffixe == 4:
    print("Valid email address")
else:
    print("Invalid email address")

# Exo 7
print("**** EXERCICE 7 ****")
for x in range(0,10):
    print("Bonjour numero",x)

# Exo 8
print("**** EXERCICE 8 ****")
monMot = "ShortWord"
print(monMot,":")
for x in monMot:
    print(x)

# Exo 9
print("**** EXERCICE 9 ****")
a = 0
b = 10
while a < b:
    print("Value of a is",a)
    a += 1

# Exo 10
print("**** EXERCICE 10 ****")
while b > 0:
    b -= 1
    if (b % 2) == 1:
        print("Value of b is",b)

# Exo 11
print("**** EXERCICE 11 ****")
value = int(input("Veuillez saisir une valeur comprise entre 1 et 10 :"))
while not(1 <= value <= 10):
    value = int(input("Veuillez saisir une valeur comprise entre 1 et 10 :"))

# Exo 12
print("**** EXERCICE 12 ****")
maChaine = "ChaqueCaractere"
print(maChaine,":")
for x in maChaine:
    print(x)

print("Liste de 3 element :")
maListe = ["elem1", "elem2", "elem3"]
for x in maListe:
    print(x)

# Exo 13
print("**** EXERCICE 13 ****")
for x in range(1,15):
    if (x % 3) == 0:
        print(x)

# Exo 14
print("**** EXERCICE 14 ****")
value = 1
while value < 15:
    if (value % 2) == 0:
        print(value)
    value += 1

for x in range(1,15):
    if (x % 2) == 0:
        print(x)

### TROISIEME BREAKPOINT
# Exo 15
