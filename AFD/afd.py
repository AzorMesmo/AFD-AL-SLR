import numpy


def generate(afnd, header, dict_tokens, dict_productions):
    header = numpy.append(header, numpy.matrix(afnd[1]), axis=0)
    transitions_made = ['0']
    dict_transitions = dict()
    width = len(dict_tokens) + 1
    total_rows, current_row = 1, 1

    while True:
        first = True
        for index, value in numpy.ndenumerate(header[current_row]):
            if first:
                first = False
                continue
            if value == 'Ø':
                continue

            if value not in transitions_made:
                if '|' in value:
                    transitions_made.append(value)
                    transitions = value.split('|')

                    rows = []
                    for transition in transitions:
                        dict_transitions[transition] = value
                        rows.append(numpy.matrix(afnd[int(transition) + 1]))

                    row = [value]
                    for i in range(width - 1):
                        row.append('Ø')

                    end = False
                    for row_ in rows:
                        first = True
                        for index_, value_ in numpy.ndenumerate(row_):
                            if first:
                                if '*' in value_:
                                    end = True
                                first = False
                                continue
                            if value_ != 'Ø':
                                if row[index_[1]] == 'Ø':
                                    row[index_[1]] = value_
                                else:
                                    row[index_[1]] = f'{row[index_[1]]}|{value_}'

                    if end:
                        row[0] = f'*{row[0]}'

                    header = numpy.append(header, numpy.matrix(row), axis=0)
                    total_rows += 1
                else:
                    if value not in dict_transitions.keys():
                        transitions_made.append(value)
                        header = numpy.append(header, numpy.matrix(afnd[int(value) + 1]), axis=0)
                        total_rows += 1
                    else:
                        header[current_row, index[1]] = dict_transitions[value]

        if current_row >= total_rows:
            break

        current_row += 1

    br = False
    for i in dict_productions:
        for j in range(header.shape[0] - 1):
            transition = str(header[j + 1, 0]).replace('*', '')
            if br:
                br = False
                break
            if '|' in transition:
                transitions = transition.split('|')
                for k in transitions:
                    if str(dict_productions[i]) == k:
                        dict_productions[i] = j
                        br = True
                        break
            else:
                if str(dict_productions[i]) == transition:
                    dict_productions[i] = j
                    break

    for i in range(header.shape[0] - 1):
        if '*' not in header[i + 1, 0]:
            header[header == header[i + 1, 0]] = f'+{i}'
        else:
            name = header[i + 1, 0]
            header[header == str(name).replace('*', '')] = f'+{i}'
            header[i + 1, 0] = f'*+{i}'
    for index, value in numpy.ndenumerate(header):
        if '+' in value:
            header[index] = str(value).replace('+', '')

    return header, dict_productions
