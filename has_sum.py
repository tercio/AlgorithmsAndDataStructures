# exemplo do video de dicas do Google sobre entrevistas
# https://www.youtube.com/watch?v=XKu_SEDAykw

def has_sum (data,sum):

    comp = set() #complimentary of the current value to make the sum

    for v in data:

        if v in comp:
            return True

        print ("adding ",sum-v," to the set")
        comp.add(sum - v)

    return False

if __name__ == "__main__":

    data = [1,2,4,9]
    sum = 8
    print ("%s has sum %d %s" % (data,sum,has_sum(data,sum)))

    data = [1,2,4,4]
    sum = 8
    print ("%s has sum %d %s" % (data,sum,has_sum(data,sum)))

    data = [1,2,3,4,5,9]
    sum = 8
    print ("%s has sum %d %s" % (data,sum,has_sum(data,sum)))
