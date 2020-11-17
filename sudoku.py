# sudoku 
# backtraking

grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def possible (y,x,n):
    global grid

    for i in range(9):
        if grid[i][x] == n:
            return False

    for i in range(9):
        if grid[y][i] == n:
            return False

    # vai testar os sub grupos de 3x3
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False

    return True

#print (possible(0,1,5) )
#print (possible(0,1,3) )
#print (possible(0,1,9) )
#print (possible(0,1,2) )

def solve():

    global grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if possible(i,j,n):
                        grid[i][j] = n
                        solve() # agora com uma celula vazia a menos, chamo o solve novamente
                        grid[i][j] = 0 # backtracking para testar outras possibilidades
                return # a celula é zero! mas nenhuma das 10 possibilidades foi aceita.
                        # chegamos então à um dead-end. Ignora essa tentativa e retorna

    # só cai aqui quando não existe mais nenhum grid vazio, portanto uma solução foi encontrada (se não fosse, teria caido no return acima)
    import numpy as np
    print (np.matrix(grid))
    #input('more?')

solve()


