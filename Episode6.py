def get_firstValue(strGiven):
    strGiven = strGiven.rstrip('\n')
    _elems = strGiven.split()
    _x = _elems[0]
    _x = _x.rstrip("cm")
    _x = int(_x)
    return _x


def file_check(_fileName):
    try:
        open(fileName, "r")
        return 1
    except:
        return 0


fileName = str(input("Veuillez saisir le nom d'un fichier (episode6.txt existant) : "))

if file_check(fileName) == 1:
    file = open(fileName, "r")

    maCollection = file.readlines()
    for x in range(0, len(maCollection) - 1):
        firstValue = get_firstValue(maCollection[x].rstrip("\n"))
        secondValue = get_firstValue(maCollection[x + 1].rstrip("\n"))
        if firstValue < secondValue:
            print("Ligne", x,": OUI")
        else:
            print("Ligne", x,": NON")

    file.close()
else:
    print("Fichier non trouvé.")