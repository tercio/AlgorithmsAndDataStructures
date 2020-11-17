
memo = {}

def editDistance (s1,s2,m,n):
    global memo

    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m == 0: 
        return n 

    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n == 0: 
        return m 

    key = "%d:%d" % (m,n)
    if key in memo:
        return memo[key]

    if s1[m-1] == s2[n-1]:
        return editDistance(s1,s2,m-1,n-1) # they are the same

    result = 1 + min(editDistance(s1,s2,m-1,n-1), #replace
                        editDistance(s1,s2,m-1,n),#remove
                        editDistance(s1,s2,m,n-1) #insert        
    )

    memo[key] = result
    return result

 
def editDistanceDP(s1,s2,m,n):

    c = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range (n+1):

            if i == 0: # se o i=0, temos os valores restantes de j, ou seja, precisamos inserir todos os caracteres restantes de j
                c[i][j] = j

            elif j == 0: # se o j=0, temos os valores restabntes de i, oposto do acima
                c[i][j] = i

            elif s1[i-1] == s2[j-1]: # mesmo caracter, simplesmente faz a "recursão"
                c[i][j] = c[i-1][j-1]

            else: # valores diferentes, então testa os valores de insert, delete e replace
                c[i][j] = 1 + min(
                    c[i-1][j-1], # replace
                    c[i][j-1],   # insert
                    c[i-1][j]    # delete
                )

    print (c)
    return c[i][j]


#s1 = "saturday"
#s2 = "monday"
s1 = "Rua Adele Zarzur"
s2 = "R. Adele Zarzur"
#s1 = "Rua Adele Santos Zarzur"
#s2 = "R. Adele S. Zarzur"

# no caso acima, poderia fazer o editDistance por palavras, e no caso
# de encontrar uma distância grande, poderia, talvez, ver se é somente
# o caso de uma abreviação. Ex.:
#    s1 = "Santos"
#    s2 = "S."
#   distance = 5
# porem, teoricamente 6 - 5 = 1, ou seja, do tamanho total, a primeira letra é igual
# e temos apenas uma diferença, ou pelo algoritmo, teriamos que inserir 5 letras na segunda
# string, o que faz sentido, já que ela é uma abreviação
# Se fosse algo como Santos e F. a diferença seria ainda maior

print (editDistance(s1,s2,len(s1),len(s2)))
print (editDistanceDP(s1,s2,len(s1),len(s2)))