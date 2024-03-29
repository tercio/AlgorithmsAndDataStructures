def permutations(string, step = 0):

    #print ("\nchamado: ",string,"   step ",step)
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print ("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        #print ("{:*>5}".format(' ') * (step+1),"chamando: ",string_copy,"   step ",step)
        permutations(string_copy, step + 1)


if __name__ == "__main__":

    print (permutations("hat"))
