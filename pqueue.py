
class PriorityQueue:

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.n = 0
        self.data = [0]*self.maxsize
        self.data.append(0)


    def swap(self,i,j):
        t = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = t


    def insert(self,value):
        
        self.n += 1
        self.data[self.n] = value
        i = self.n
        p = i // 2

        while i > 1 and self.data[p] > self.data[i]:
            self.swap(p,i)
            i = p
            p = i // 2

    def removeMin(self):
        i = 1
        c = 2*i
        v = self.data[i]
        self.n -= 1
        self.data[1] = self.data[self.n]

        while c <= self.n:
            if c+1 < self.n and self.data[c+1] < self.data[c]:
                c += 1 # se filho da direita menor que esquerda, usa o da direita (menor)
            if self.data[i] <= self.data[c]:
                break
            self.swap(c,i)                
            i = c
            c = i * 2


        return v

    def __str__(self):
        return str(self.data)



if __name__ == "__main__":

    pq = PriorityQueue(50)

    print ("inserindo valores...")
    pq.insert(18)
    pq.insert(8)
    pq.insert(28)
    pq.insert(3)
    pq.insert(9)
    pq.insert(2)

    #print (pq)

    print ("removeMin: ",pq.removeMin())
    print ("removeMin: ",pq.removeMin())
    print ("removeMin: ",pq.removeMin())

    print ("inserindo valores...")
    pq.insert(1)
    pq.insert(45)

    print ("removeMin: ",pq.removeMin())

