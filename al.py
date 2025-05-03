import numpy


def generate(afd):
    # Dicionário Vazio Inicial -> Cabeçalho (Nenhuma Transição)
    al = [dict()]
    # Posição, (Index), Dos Estados -> {Estado: Linha Da Matriz} -> Linha Da Matriz = Posição Da Lista No AL)
    states_position = dict()
    # Percorre As Linhas Da Matriz (Para Popular O Dicionário Acima)
    for row in range(afd.shape[0]):
        # Percorre As Colunas Da Matriz
        for column in range(afd.shape[1]):
            # Se É A Primeira Coluna (Index De Estados)
            if column == 0:
                states_position[str(afd[row, column]).strip('@')] = row
    # Cria O Analizador Léxico (Lista De Dicionários)
    # Percorre As Linhas Da Matriz
    for row in range(afd.shape[0]):
        # Ignora O Cabeçalho
        if row == 0:
            continue
        state_transitions = dict()
        # Percorre As Colunas Da Matriz
        for column in range(afd.shape[1]):
            # Ignora O Index
            if column == 0:
                continue
            # Adiciona A Transição
            state_transitions[str(afd[0, column])] = states_position[afd[row, column]]
        # Salva O Dicionário De Transições Por Estado
        al.append(state_transitions)
    return al


def process(al, final_states, string):
    current_state = 1
    tape = ''
    # Percorre A String De Entrada
    for token in string:
        tape += token

    return tape
