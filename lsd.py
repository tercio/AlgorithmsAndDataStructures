
def lsd (aList):

    #for nome,setor in aList:
    #    print ("%s : %s" % (nome,setor))

    count = [0] * len(aList)

    # conta os indices
    for _,setor in aList:
        count [setor+1] += 1
    #print (count)


    # distribui os registros 
    for r in range(0,len(count)-1):
        count [r+1] += count[r]
    #print (count)

    # ordena
    aux = [''] * len(aList)
    for i in range(0,len(aList)):
        aux[ count[ aList[i][1] ] ] = aList[i]
        count[ aList[i][1] ] += 1
    #print (aux)
    
    # remonta aList
    for i in range(0,len(aux)):
        aList[i] = aux[i]



if __name__ == "__main__":

    aList = [('jose',4),('carlos',2),('ana',3),('antonio',5),('bete',1),('joao',4),('maria',3),('pedro',1)]

    lsd(aList)

    print ("--- final ---")
    print (aList)