def getFields():
    return ['','Fulano de Tal','Rua Xyz','Sao Paulo']

def processTemplate (template):

    text = ""
    fields = getFields()

    chars = iter(template)
    for char in chars:
        if char != "$":
            text += char
        else:
            char = next(chars)
            if char == "$":
                text += char
            else:
                try:
                    text += fields[int(char)]
                except IndexError as e:
                    text += "<field not found:%s>" % (e)

    return text

if __name__ == "__main__":

    template = """
    Olá $1,

    Seu produto será enviado para $2 - $3

    Obrigado $4!
    """

    print (processTemplate(template))
