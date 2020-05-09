def get_firstValue(strGiven):
    strGiven = strGiven[2:]
    strGiven = strGiven.rstrip('\n')
    _elems = strGiven.split('\t')
    _x = _elems[0]
    _x = _x.rstrip("cm")
    _x = int(_x)
    return _x


maCollection = ["\b\t80cm\t60cm\n", "\b\t81cm\t51cm\n", "\b\t105cm\t145cm\n"]

for x in range(0, len(maCollection)-1):
    firstValue = get_firstValue(maCollection[x])
    secondValue = get_firstValue(maCollection[x+1])
    if firstValue < secondValue:
        print("Line", x,"has the first value of", firstValue)