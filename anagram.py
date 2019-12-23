def isTheSame(s1,s2):

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)



if __name__ == "__main__":

    s1 = "pato"
    s2 = "topa"
    print (s1,s2,isTheSame(s1,s2))

    s1 = "pato"
    s2 = "opa"
    print (s1,s2,isTheSame(s1,s2))
