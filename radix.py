# Esse algoritmo é baseado no LSD de strings do livro Algorithms 
# Inclusive seria possível deixa-lo mais genérico para que também
# ordenasse strings do mesmo tamanho
# Usa o index counting (o for d in range(0,ndigits) ) para ordenar

def radix_sort (aList,r):
    
    if len(aList) <= 0:
        return

    ndigits = 0
    bigger = max (aList)
    # baseado no maior numero, descobre a qtde de casas decimais
    while bigger > 0:
        ndigits += 1
        bigger //= r

    
    n = len(aList)

    # para cada casa decimal (ndigits !? abaixo)
    for d in range(0,ndigits):

        count = [0] * (r + 1)

        # aqui calculo o bucket baseado no digito atual
        # e onde ele se encaixa exatamente. Lembrando que para
        # a primeira entrada, sempre fazemos +1 para que depois
        # na parte de posicionamento, a conta fique facil
        # ex.: ((8 // (10 ** 0)) % r) = 8  # testando o primeiro digito (unidades)
        # ex.: ((28 // (10 ** 1)) % r) = 2 # testando o segundo digito (dezenas)
        bucket = ((aList[i] // (10 ** d)) % r)
        for i in range(0,n):
            count [(bucket) + 1] += 1
        #print (count)

        # define os indices iniciais de cada bucket
        for c in range(0,r):
            count [c + 1] += count[c]
        #print (count)

        # copia os dados ordenados para a aux
        aux = [0] * n
        for i in range (0,n):
            aux[ count [ (bucket)  ]   ] = aList[i]
            count [ (bucket)  ] += 1

        for i in range(0,n):
            aList[i] = aux[i]


if __name__ == "__main__":

    aList = [8,20,35,12,11,7,66,44,30,18,71]
    print (aList)

    radix_sort(aList,10)

    print (aList)