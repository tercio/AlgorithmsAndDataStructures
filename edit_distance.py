
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
 

#s1 = "saturday"
#s2 = "monday"
#s1 = "Rua Adele Zarzur"
#s2 = "R. Adele Zarzur"
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