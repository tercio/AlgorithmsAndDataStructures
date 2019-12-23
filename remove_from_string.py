
def remove_from_string(s,remove):

    r = set(remove) # qual seria a diferença de tempo entre o set e um is na propria lista ?

    dst = 0
    for idx,c in enumerate(s):
        if c not in r:
            s = s[:dst] + s[idx:]
            dst += 1

    return s

if __name__ == "__main__":

    s = "teste de string com caracteres para serem removidos"
    remove = "ei"
    print("Removendo os caracteres {!r}\nda string {!r} =\n{}".format(remove,s,remove_from_string(s,remove)))
