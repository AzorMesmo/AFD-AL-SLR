import numpy


def generate(afd, dict_productions):
    last = int(afd[afd.shape[0] - 1, 0].replace('*', '')) + 1
    dict_productions['erro'] = last

    last_f = f'*{last}'
    row = [last_f]

    for i in range(afd.shape[1] - 1):
        row.append('Ø')
    afd = numpy.append(afd, numpy.matrix(row), axis=0)

    for index, value in numpy.ndenumerate(afd):
        if value == 'Ø':
            afd[index] = last

    return afd, dict_productions
