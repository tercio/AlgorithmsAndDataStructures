from queue import PriorityQueue

class Cidade:
    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return "%s" % (self.nome)


class Graph:
    def __init__ (self):
        self.adj = {}

    def __str__(self):
        texto = ""
        for c in self.adj.keys():
            texto += "Cidade: %s\n" % (c)
            for v in self.adj[c]:
                texto += " -> %s : %d km\n" % (v[0],v[1])
            texto += "\n"

        return texto


    def addEdge(self,cidadeA,cidadeB,distancia):
        v = (cidadeB,distancia)
        if cidadeA in self.adj:

            self.adj[cidadeA].append(v)
        else:
            self.adj[cidadeA] = [v]


    def rota(self,cidadeA,cidadeB):
        # dijkstra
        distancia = 0

        pq = PriorityQueue()
        dist = {}

        pq.put((0,cidadeA))
        dist[cidadeA] = 0

        while pq:
            u = pq.get()[1]
            for i in self.adj[u]:
                c = i[0] # proxima cidade
                d = i[1] # distancia para proxima cidade

                if c not in dist or dist[c][1] > dist[u][1] + d:
                    x = dist[u]
                    dist[c] = x + d
                    x = dist[c]
                    pq.put((x,c))



        return distancia



jundiai = Cidade("Jundiai")
campinas = Cidade("Campinas")
itatiba = Cidade("Itatiba")
varzea = Cidade("Varzea")
valinhos = Cidade("Valinhos")
vinhedo = Cidade("Vinhedo")

mapa = Graph()

mapa.addEdge(jundiai,campinas,90)
mapa.addEdge(jundiai,itatiba,40)
mapa.addEdge(itatiba,campinas,55)
# mapa.addEdge(jundiai,varzea,30)
# mapa.addEdge(jundiai,valinhos,60)
# mapa.addEdge(jundiai,vinhedo,40)
# mapa.addEdge(valinhos,campinas,35)
# mapa.addEdge(vinhedo,valinhos,30)
mapa.addEdge(campinas,campinas,0)


#print (mapa)
print ("Distancia: ",mapa.rota(jundiai,campinas))