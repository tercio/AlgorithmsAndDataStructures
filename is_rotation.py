import os

#  pagina 182 - cracking the coding interview
# Uma rotação é sempre, na verdade, contida na concatenação da primeira

def isRotation (s1,s2):

    if len(s1) == len(s2) and len(s1) > 0:

        s1s1 = s1 + s1
        return s2 in s1s1

    return False


if __name__ == "__main__":

    s1 = "waterbottle"
    s2 = "erbottlewat"
    print ("is %s a rotation of %s ? %s" % (s2,s1,isRotation(s1,s2)))
