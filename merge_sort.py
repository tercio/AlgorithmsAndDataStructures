
def merge_sort(aList):
    helper = [0] * len(aList)
    merge_sort_helper (aList,helper,0,len(aList)-1)
    

def merge_sort_helper (aList,helper,low,high):
    if (low < high):
        middle = (low + high) // 2
        merge_sort_helper (aList,helper,low,middle)
        merge_sort_helper (aList,helper,middle+1,high)

        merge (aList,helper,low,middle,high)
        

def merge (aList,helper,low,middle,high):
    
    #print (helper)
    #print (aList)
    #print (low," ",middle," ",high)
    for i in range(low,high+1):
        helper[i] = aList[i]

    lind = low
    rind = middle + 1
    current = low

    while lind <= middle and rind <= high:
        if helper[lind] <= helper[rind]:
            aList[current] = helper[lind]
            lind += 1
        else:
            aList[current] = helper[rind]
            rind += 1

        current += 1

    # so preciso inserir o left, pois a lista toda aList já contem os mesmos valores de helper
    # portanto, se uso toda o right, só preciso incluir o left depois do middle,
    # porem, se uso todo o right, o left já está lá, ou seja, posso ignorar qualquer valor restante
    # de left pois ele já está posicionado no lugar correto
    remaining = middle - lind
    for i in range(0,remaining + 1):
        aList[current + i] = helper[lind + i]



if __name__ == "__main__":

    aList = [4,7,9,5,2,1,3,4,8]

    print (aList)
    merge_sort(aList)
    print (aList)