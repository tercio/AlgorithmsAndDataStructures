def binary_search(alist,n):

    lower = 0
    upper = len(alist) -1


    while True:
        center = int((upper-lower)/2) + lower
        print ("center: ",center, " lower: ",lower, " upper: ",upper)
        if alist[center] == n:
            return True

        if alist[center] > n:
            upper = center -1
        if alist[center] < n:
            lower = center +1
        if lower > upper:
            return False

if __name__ == "__main__":

    alist = [1,2,3,4,5,6,7,8,9]

    print ("1: ",binary_search(alist,1))
    print ("0: ",binary_search(alist,0))
    print ("9: ",binary_search(alist,9))
    print ("4: ",binary_search(alist,4))
