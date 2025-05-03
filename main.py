# Símbolos De Controle
# '[' Representa O Inicio Do Nome De Um Estado
# ']' Representa O Final Do Nome De Um Estado
# '|' Representa A Divisão Entre Transições De Um Estado
# '&' Representa ε
# '#', '@' São Utilizados Na Lógica Do Programa
# Obs.: As Gramáticas Devem Ser Escritas Antes Das Palavras
# Obs.: GRs Devem Possuir Pelo Menos Dois Estados e Seguir O Padrão De Escrita Dos Exemplos À Seguir
# Obs.: Além Disso GRs Terminando Com Símbolos Terminais Ao Invés De & (Exemplo: [S]|a|b) Não São Suportadas
#
# [ARITHMETIC_OPERATORS] <- Label (Nome Dos Tokens Identificados)
# [S]|+[A]|-[A]|*[A]|/[A] <- [Nome Da Regra]|PRODUÇÃO[Estado]|PRODUÇÃO[Estado]|...
# [A]|& <- Toda GR Deve Possuir & (Para Construção Do Estado Final)
#
# [ASSIGNMENT_COMPARISON_OPERATORS]
# [S]|=[A]|>[A]|<[A]
# [A]|=[B]|&
# [B]|&
#
# [VARIABLES]
# [S]|a[A]|e[A]|i[A]|o[A]|u[A]
# [A]|a[A]|e[A]|i[A]|o[A]|u[A]|&

import header
import afnd
import afd
import errors
import pandas

# Cria O Cabeçalho (Lista Com Todos Os Tokens)
header, symbol_position = header.generate()
# Cria O Autômato Finito Não Determinístico
afnd, final_states = afnd.generate(header, symbol_position)
# Cria O Autômato Finito Determinístico
afd, final_states = afd.generate(afnd, header, symbol_position, final_states)
# Cria O Estado De Erro E Suas Transições
afd, final_states = errors.generate(afd, final_states)
# Gera O Arquivo .csv Do AFD
afnd_csv = pandas.DataFrame(afd)
afnd_csv.to_csv("afd.csv")

print('\n', final_states)
print('\n', afd)
