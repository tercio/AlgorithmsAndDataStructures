
#pagina 421 do Introduction to Algorithms

def greedy_activity_selector(s,f):
    
    a = []
    n = len(s)
    k = 0 # esse será a primeira atividade, já que se espera que estão em ordem crescente de término (array f)
    a.append((s[k],f[k])) # primeira tarefa então, como dito acima, é a primeira da lista!
    

    for m in range (k+1,n): # começa a testar a próxima, ou seja, k+1

        # o m é o ponteiro, ou index, que testa a próxima posição
        # aqui, precisamos qual a próxima tarefa (m em s[m]), cujo inicio, é maior ou igual à tarefa atual (k f[k])
        if s[m] >= f[k]:
            a.append((s[m],f[m])) # insere na lista de tarefas
            k = m  # atualiza o ponteiro ou index da tarefa atual

    return a

s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]

print (greedy_activity_selector(s,f))

