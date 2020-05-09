import numpy as np

print("Hello World ! Let's start the work with first question.")

### PREMIER BREAKPOINT
# Exo 1
temps = 6.892
distance = 19.7
vitesse = distance / temps
print("Vitesse de", "%.1f" % vitesse, "unité de distance par unité de temps (unknown).")

# Exo 2
nom = str(input("Saisissez un nom :"))
age = int(input("Et un age :"))
print("La personne " + nom + ",", age, "ans, a été saisi.")

# Exo 3
floatVal = float(input("Saisissez un nombre flottant :"))
if floatVal < 0:
    print("Error this number should be upper or equal of 0")
else:
    print(np.sqrt(floatVal))

# Exo 4
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
