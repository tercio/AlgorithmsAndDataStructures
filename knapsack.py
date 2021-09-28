
lookup = {}
    
def knapsack(w,v,n,W):

    global lookup

    if W < 0:
        return -5000

    if n < 0 or W == 0:
        return 0

    key = "%s|%s"% (n,W)

    if key not in lookup:

        # Temos dois subproblemas:
        # ========================

        # o item atual deve ser incluido no ks e depois recur no item anterior
        include = v[n] + knapsack(w,v,n - 1,W - w[n])

        # o item atual NAO entra no ks e faço o recur no item atual
        exclude = knapsack(w,v,n-1,W)

        lookup[key] = max(include,exclude)
    
    return lookup[key]



w = [3,2,5,1]
v = [1,4,2,6]
W = 10

# w = [10,20,30]
# v = [60,100,120]
# W = 50

n = len(w)

print (knapsack(w,v,n-1,W))
#print (lookup)