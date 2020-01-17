# Cracking the Coding Interview - pag. 397-398
def sort_anagram (aList):

    anagrams = {}

    for w in aList:
        key = "".join(sorted(w))
        if key in anagrams:
            anagrams[key].append(w)
        else:
            anagrams[key] = [w]
    
    aList.clear()
    for wList in anagrams.values():
        aList.extend(wList)


if __name__ == "__main__":

    aList = ['acre','toca','race','cota','care']

    print (aList)
    sort_anagram(aList)
    print (aList)