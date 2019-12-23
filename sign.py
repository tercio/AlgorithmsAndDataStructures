
#with open('dictionary.txt',"r") as fd:
    #data= fd.read().splitlines()

#for word in data:
#    print ("".join(sorted(word))," ",word)

with open('dictionary.txt',"r") as fd:
    for word in fd:
        word = word.rstrip("\n")
        print ("".join(sorted(word))," ",word)
