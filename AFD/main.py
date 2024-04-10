# Símbolos De Controle
# { Representa O Inicio Do Nome De Um Estado
# } Representa O Final Do Nome De Um Estado
# | Representa A Divisão Entre Transições De Um Estado
# & Representa ε
# Obs.: Não Há Espaço Da Definção Dos GRs
# Exemplo:
# {S}|a{A}|e{A}|i{A}|o{A}|u{A}
# {A}|a{A}|e{A}|i{A}|o{A}|u{A}|&

import header
import afnd
import afd
import errors
import pandas

header, dict_tokens = header.generate()

afnd, dict_productions = afnd.generate(header, dict_tokens)

afd, dict_productions = afd.generate(afnd, header, dict_tokens, dict_productions)

afd, dict_productions = errors.generate(afd, dict_productions)

pandas.DataFrame(afd).to_csv("afd.csv")

print('\n', dict_productions)
print('\n', afd)
