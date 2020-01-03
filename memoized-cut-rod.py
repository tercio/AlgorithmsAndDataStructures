# Dynamic Programming
# Exemplo do livro Introduction to Algorithms pagina 366

def memoized_cut_rod_aux (p,n,r):
    
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -32000
        for i in range (1,n+1):
            q = max(q,p[i] + memoized_cut_rod_aux(p,n-i,r))
    r[n] = q

    return q

def memoized_cut_rod(p,n):

    r = [-32000] * (n + 1)
    return memoized_cut_rod_aux(p,n,r)




if __name__ == "__main__":

    p = [0,1,5,8,9,10,17,17,20,24,30]

    n = 4
    print("N: ",n," gets a revenue equals to ",memoized_cut_rod(p,n))
