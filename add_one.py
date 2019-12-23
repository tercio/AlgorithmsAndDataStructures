# [1,2,3]
# [1,3,9]
# [9,9,9]

def add_one (alist):

    new_list = list(alist)

    if len(alist) == 0 or alist == []:
        return alist

    carry = 1
    for i,item in reversed(list(enumerate(alist))):
        sum = alist[i] + carry
        if sum % 10 == 0:
            new_list[i] = 0
            carry = 1
        else:
            new_list[i] = sum % 10
            carry = 0

    if carry == 1:
        new_list.insert(0,1)


    return new_list


if __name__ == "__main__":

    print ("[1,2,3]: ", add_one([1,2,3]))
    print ("[1,3,9]: ", add_one([1,3,9]))
    print ("[9,9,9]: ", add_one([9,9,9]))
    print ("[9]    : ", add_one([9]))
    print ("[]     : ", add_one([]))
