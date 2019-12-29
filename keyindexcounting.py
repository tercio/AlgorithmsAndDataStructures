#
# Key Index Counting - Example from the Book Algorithms by Robert Sedgwick
# location 12440
#

def keyindexcounting(s):

    N = len(s)
    aux = [''] * N
    R = 5 # sections from 0 to 4 (even though we dont have a student in section 0)
    count = [0] * (R + 1)

    # compute frequency counts
    for name,section in s.items(): 
        count[section + 1] += 1
    print (count)

    # now transform counts into indices
    for r in range (0,R):
        count[r+1] += count[r]
    print (count)

    # Distribute the records in the aux array in the sorted order
    items = list(s.items())
    for i in range(0,N):
        aux[count[items[i][1]]] = items[i]
        # increases the index for this section so next time i+1 will be used
        # in the java version, on the book Algorithms, it seems that it is possible to do this:
        #   aux[count[items[i][1]] ++ ] = items[i]
        count[items[i][1]] += 1 
    print (aux)

    # Copy items back
    s = {}
    for i in range (0,N):
        print (aux[i][0], " = ",aux[i][1])
        s[aux[i][0]] = aux[i][1]

    return s


if __name__ == "__main__":
    students = {
        "Anderson":2,
        "Brown":3,
        "Davis":3,
        "Garcia":4,
        "Harris":1,
        "Jackson":3,
        "Johnson":4,
        "Jones":3,
        "Martin":1,
        "Martinez":2,
        "Miller":2,
        "Moore":1,
        "Robinson":2,
        "Smith":4,
        "Taylor":3,
        "Thomas":4,
        "Thompson":4,
        "White":2,
        "Williams":3,
        "Wilson":4
    }

    print ("Original:")
    print (students)
    students = keyindexcounting(students)
    print ("Sorted:")
    print (students)