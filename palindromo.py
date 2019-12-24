from collections import deque

def palindromo(str):

    d = deque()
    d.extend(str)

    isequal = True

    while isequal:
        try:
            if d.popleft() != d.pop():
                return False
        except IndexError as e:
            return True


if __name__ == "__main__":

    str = "teste"
    print (str," : ",palindromo(str))

    str = "radar"
    print (str," : ",palindromo(str))

    str = "toot"
    print (str," : ",palindromo(str))
