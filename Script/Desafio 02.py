# Script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem
#com a data formatada.

print('=======DESAFIO 02 ======')

# Solicita o nome do usuário
nome = input('Qual é o seu nome: ')
print('Me informe a sua data de nascimento.')
dia = input('Qual o dia de nascimento: ')
mês = input('Qual o mês de nascimento: ')
ano = input('Qual o ano de nascimento: ')

# Exibe a mensagem completa
print(nome, 'a sua data de nascimento é', dia, 'de', mês, 'de', ano, '. Correto?')
