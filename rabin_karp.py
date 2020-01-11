class RollingHash ():

    def __init__(self,p = 941, alphasize = 256):
        self.p = p
        self.a = alphasize   
        self.u = 0 
        self.up = 0
        self.x = ""

    def append (self,c):
        self.up = ((self.up % self.p) * self.a + ord(c)) % self.p
        self.x += c
        
    def skip(self,c):
        self.up = ((self.up % self.p) - ord(c) * (self.a**(len(self.x) - 1) % self.p)) % self.p
        self.x = self.x[1:]
        #print (self.x)

    def __call__(self):
        return self.up


if __name__ == "__main__":

    s = "karp"
    rs = RollingHash()

    for c in s:
        rs.append(c) 

    t = "this is an example of rabin karp string sarch algorithm"
    rt = RollingHash()

    for c in t[:len(s)]:
        rt.append(c) 

    if rs() == rt():
        print ("found")
        exit(0)

    for i in range (len(s),len(t)):
        rt.skip(t[i-len(s)])
        rt.append(t[i])
        if rt() == rs():
            print ("-found-")
            exit(0)
    
    print ("not found")

