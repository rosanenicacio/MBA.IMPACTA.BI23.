#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Trabalho - Calculadora V2
#Por Rosane Ananias - 04/05/2021 - 14:23
#MBA Impacta - Business Analytics & Big Data 

#*REGRAS DE NEGÓCIO*

# A Calculadora precisa estar em uma função.
# A função precisa obrigatoriamente receber 3 parametros: 
#1. primeiro valor
#2. segundo valor
#3. operação.
#soma, subtracao, multiplicacao, divisao, expoente.


def calculadora():
    operacao = input('''
Por favor, escolha a operação a ser realizada:
+ se for adição
- se for subtração
* se for multiplicação
/ se for divisão
** se for calcular o exponecial de um número
''')
    
    num_1 = int(input('Digite o primeiro numero: '))
    num_2 = int(input('Digite o segundo numero: '))

    if operacao == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operacao == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operacao == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operacao == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
            
    elif operacao == '**':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 ** num_2)

    else:
        print('Você não digitou uma operação válida, por favor, informe novamente!')
    

        # chamada da funcao novamente para que o usuário decida se quer continuar ou não
    novamente()

def novamente():
    calc_novamente = (input('''
Gostaria de efetuar outro cálculo?
Por favor, caso a resposta seja "SIM" digite S se for NÃO, digite N.
'''))

    if calc_novamente.upper() == "S":
        calculadora()
    elif calc_novamente.upper() == "N":
        print('Obrigada!')
    else:
        novamente()

calculadora()


# In[ ]:


#Trabalho - Calculadora V1#
#Por Rosane Ananias - 03/05/2021 - 22:52#
#MBA Impacta - Business Analytics & Big Data #

#*REGRAS DE NEGÓCIO*#

#calculadora precisa estar em uma função.
# A função precisa obrigatoriamente receber 3 parametros: 
#1. primeiro valor
#2. segundo valor
#3. operação.
#soma, subtracao, multiplicacao, divisao, expoente.#


def soma():
    x = float(input("Digite o primeiro numero:  "))
    y = float(input("Digite o segundo numero:"))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Digite o primeiro numero:  "))
    y = float(input("Digite o segundo numero: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Digite o primeiro numero: "))
    y = float(input("Digite o segundo numero:"))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Digite o primeiro numero: "))
    y = float(input("Digite o segundo numero: "))
    print("Divisao: ",x/y)

def expoente():
    x = float(input("Digite o primeiro numero: "))
    y = float(input("Digite o segundo numero: "))
    print("Expoente: ",x**y,"\n""\n" "Escolha a opção")
    
opcao=1

while opcao:
    print("\n""0. Sair")
    print("\n""1. Somar")
    print("\n""2. Subtrair")
    print("\n""3. Multiplicação")
    print("\n""4. Divisão ")
    print("\n""5. Expoente""\n")

    opcao = int(input("\n""Escolha a sua opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
    if(opcao==5):
        expoente()


# In[ ]:




