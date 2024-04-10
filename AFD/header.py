import numpy


def generate():
    file = open('input.txt', 'r')
    lines = file.readlines()

    dict_line = dict()

    tokens = ['δ']
    new_token = 1

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line[0] != '{':  # Token
            for token in line:
                if token not in tokens:
                    tokens.append(token)
                    dict_line[token] = new_token
                    new_token += 1
        else:  # GR
            is_token = False
            for token in line:
                if is_token:
                    if token not in tokens and token != '&':
                        tokens.append(token)
                        dict_line[token] = new_token
                        new_token += 1
                    is_token = False
                if token == "|":
                    is_token = True

    file.close()
    tokens = numpy.matrix(tokens)

    return tokens, dict_line
