

def getCharKey (telephone_key, place):

    keys = [['0','0','0'],
            ['1','1','1'],
            ['A','B','C'],
            ['D','E','F'],
            ['G','H','I'],
            ['J','K','L'],
            ['M','N','O'],
            ['P','R','S'],
            ['T','U','V'],
            ['W','X','Y']
    ]

    return keys[telephone_key][place-1]


class TelephoneNumbers():

    def __init__ (self,_phoneNum):
        self.phoneNum = _phoneNum
        self.result = len(self.phoneNum)*['']



    def combinations (self):
        self._combinations_(0)

    def _combinations_ (self,curDigit):

        if curDigit == len(self.phoneNum):
            print ("result: ","".join(self.result))
            return
        else:
            for place in range(1,4):
                self.result[curDigit] = getCharKey(phoneNum[curDigit],place)
                self._combinations_(curDigit+1)
                if self.phoneNum[curDigit] == 0 or self.phoneNum[curDigit] == 1:
                    return


if __name__ == "__main__":

    for place in range(1,4):
        print ("Key 0 :",getCharKey(0,place))
    for place in range(1,4):
        print ("Key 2 :",getCharKey(2,place))
    for place in range(1,4):
        print ("Key 4 :",getCharKey(4,place))

    phoneNum = [4,9,7,1,9,2,7]
    tn = TelephoneNumbers(phoneNum)
    print (phoneNum," ",tn.combinations())

    phoneNum = [8,6,6,2,6,6,5]
    tn = TelephoneNumbers(phoneNum)
    print (phoneNum," ",tn.combinations())
