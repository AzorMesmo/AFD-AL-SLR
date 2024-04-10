import numpy


def generate(header, dict_tokens):
    dict_gr = dict()
    t_first = True
    last = 0

    file = open('input.txt', 'r')
    lines = file.readlines()

    dict_productions = dict()
    width = len(dict_tokens) + 1
    new_transition = 0

    row = [new_transition]
    for i in range(width - 1):
        row.append('Ø')
    new_transition += 1
    header = numpy.append(header, numpy.matrix(row), axis=0)

    for line in lines:
        line = line.strip()

        if not line:
            t_first = True
            dict_gr = dict()
            continue

        if line[0] != '{':  # Token
            first = True
            for token in line:
                if not first:
                    row = [new_transition]

                    for i in range(dict_tokens[token] - 1):
                        row.append('Ø')

                    row.append(new_transition + 1)

                    for i in range(width - len(row)):
                        row.append('Ø')

                    new_transition += 1
                    header = numpy.append(header, numpy.matrix(row), axis=0)
                else:
                    if header[1, dict_tokens[token]] == 'Ø':
                        header[1, dict_tokens[token]] = new_transition
                    else:
                        header[1, dict_tokens[token]] = f'{header[1, dict_tokens[token]]}|{new_transition}'
                    first = False

            row = [f'*{new_transition}']
            for i in range(width - 1):
                row.append('Ø')
            dict_productions[line] = new_transition
            new_transition += 1
            header = numpy.append(header, numpy.matrix(row), axis=0)

        else:  # GR
            first = True
            line = line.split('|')
            origin = 0
            dict_productions['variavel'] = -1
            for transition in line:
                if t_first:
                    origin = transition[1:-1]
                    last = transition[1:-1]
                    dict_gr[origin] = 0
                    t_first = False
                    first = False
                    continue
                if first:
                    origin = transition[1:-1]
                    first = False
                    continue

                if transition == '&':
                    header[dict_gr[origin] + 1, 0] = f'*{header[dict_gr[origin] + 1, 0]}'
                else:
                    temp = transition.split('{')

                    if temp[1][:-1] not in dict_gr.keys():
                        last = temp[1][:-1]
                        if new_transition in dict_gr.values():
                            new_transition += 1
                        dict_gr[temp[1][:-1]] = new_transition
                        row = [new_transition]
                        for i in range(width - 1):
                            row.append('Ø')
                        header = numpy.append(header, numpy.matrix(row), axis=0)
                        new_transition += 1

                    if header[dict_gr[origin] + 1, dict_tokens[temp[0]]] == 'Ø':
                        header[dict_gr[origin] + 1, dict_tokens[temp[0]]] = dict_gr[temp[1][:-1]]
                    else:
                        header[dict_gr[origin] + 1, dict_tokens[temp[0]]] = \
                            f'{header[dict_gr[origin] + 1, dict_tokens[temp[0]]]}|{dict_gr[temp[1][:-1]]}'
            if dict_productions['variavel'] == -1:
                dict_productions['variavel'] = dict_gr[last]
            else:
                dict_productions['variavel'] = f'{dict_productions['variavel']}|{dict_gr[last] + 1}'

    file.close()

    return header, dict_productions
