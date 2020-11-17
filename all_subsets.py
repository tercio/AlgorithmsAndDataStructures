

def all_subsets(aList):

    subset = [''] * len(aList)
    helper (aList,subset,0)

def helper(aList,subset,i):

    if i == len(aList):
        print(subset)
    else:
        # existe sempre duas opções, que são: Incluir ou não incluir o item corrent no subset.
        # as duas chamadas abaixo fazem isso: não inclui e chama recursivamente e a outra, incluir
        # e também chama recursivamente para o próximo item i da lista
        subset[i] = ''
        helper(aList,subset,i+1)
        subset[i] = aList[i]
        helper(aList,subset,i+1)


all_subsets ([1,2,3])