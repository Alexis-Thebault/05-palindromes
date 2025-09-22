def ispalindrome(p):
    L2 = []
    L1 = []
    LM1 = list(p)
    LM2 = []
    for i in range(len(LM1)):
        if LM1[i] == ' ' or LM1[i] == ',' or LM1[i] == '.' or LM1[i] == '!' or LM1[i] == '?' or LM1[i] == "'" or LM1[i] == '-' or LM1[i] == ':' or LM1[i] == ';':
            LM1[i] = ''
        if LM1[i].isupper():
            LM1[i] = LM1[i].lower()
        if LM1[i] == 'à' or LM1[i] == 'â' or LM1[i] == 'ä':
            LM1[i] = 'a'
        if LM1[i] == 'é' or LM1[i] == 'è' or LM1[i] == 'ê' or LM1[i] == 'ë':
            LM1[i] = 'e'
        if LM1[i] == 'î' or LM1[i] == 'ï':
            LM1[i] = 'i'
        if LM1[i] == 'ô' or LM1[i] == 'ö':
            LM1[i] = 'o'
        if LM1[i] == 'ù' or LM1[i] == 'û' or LM1[i] == 'ü':
            LM1[i] = 'u'
        if LM1[i] == 'ç':
            LM1[i] = 'c'
        if LM1[i] == 'ÿ':  
            LM1[i] = 'y'
        if LM1[i] == 'œ':
            LM1[i] = 'oe'
        if LM1[i] == 'æ':
            LM1[i] = 'ae'
    for i in range (len(LM1)):
        if LM1[i] != '':
            LM2.append(LM1[i])

    for i in range(len(LM2)):
        L1.append(LM2[i])
        L2.append(LM2[len(LM2) - 1 - i])
    if L1 == L2:
        return True

#### Fonction principale


def main():

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie","Eh ! ça va, la vache ?"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()