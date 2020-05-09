def convertString(_strGiven):
    AryToEuro = 0.00024
    EuroToAry = 4168.79

    _elems = _strGiven.split()
    _value = int(_elems[1])
    if _elems[0] == "EA":
        return _value * EuroToAry
    elif _elems[0] == "AE":
        return _value * AryToEuro
    else:
        print("Wrong string entered")


print("**** Episode 3 ****")
strGiven = str(input("Veuillez saisir une chaine de conversion (exemple : EA 8 ou AE 4000) :"))
typeGiven = strGiven.split()
if typeGiven[0] == "EA":
    print(typeGiven[1], "Euros become", convertString(strGiven), "AryArys")
elif typeGiven[0] == "AE":
    print(typeGiven[1], "AryArys become", convertString(strGiven), "Euros")
