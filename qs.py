# versão simplificada de um Quicksort do livro Programming Pearls pág 116-118

def swap(a,m,i):

    tmp = a[m]
    a[m] = a[i]
    a[i] = tmp
    

def partition(a,l,u):
    
    pivot = l  # l é o pivot
    m = l 
    for i in range(pivot+1,u+1):
        if a[i] < a[pivot]:
            m += 1
            swap (a,m,i)

    swap (a,pivot,m)

    return m


def qsort (a,l,u):

    if l >= u:
        return

    m = partition(a,l,u)

    qsort (a,l,m-1)
    qsort (a,m+1,u)



if __name__ == "__main__":

    a = [55,41,59,26,53,58,97,93]

    print ("Original: ",a)
    qsort(a,0,len(a)-1)
    print ("Ordenada: ",a)
