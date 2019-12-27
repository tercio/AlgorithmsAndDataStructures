def sort(arr):

    for i in range(1,len(arr)):
        for j in range (i,0,-1):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            else:
                break

    return arr

if __name__ == "__main__":

    arr = [3,6,8,4,2,5]
    print ("sorting array : ",arr," into: ",sort(arr))

    #import random
    #arr = []
    #for i in range (1,1000001,1):
    #    arr.append(i)
    #random.shuffle(arr)
    #print ("sorting array : ",arr," into: ",sort(arr))
    #print ("sorting array :  into: ",sort(arr))