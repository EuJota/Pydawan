# -*- coding: utf-8 -*- [Define a utilização de alguns caracteres especiais, como ~, ^, etc.]

'''
Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
'''
#incializacao de variaveis
num_1 = 0
num_2 = 0

#coloquei os input como float para o caso do usuario inserir valores nao inteiros
num_1 = float(input("Informe o primeiro número: "))
num_2 = float(input("Informe o segundo número: "))

#condicional ifelse para verificar o maior dos valores
if num_1>num_2:
    print("O maior é: ",num_1)
else:
    print("O maior é: ",num_2)
        