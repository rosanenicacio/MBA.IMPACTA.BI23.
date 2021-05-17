#!/usr/bin/env python
# coding: utf-8

# *LISTA DE EXERCICIOS - ATIVIDADE 2*

# In[ ]:


#Data de Criação 11/05/2021 - 01:12
# Lista de Exercicios - 01
# MBA 
# Rosane Ananias

# 1 Regra: Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,"hum","dois"] 
#A ideia do exercício é:
# *tirar a média de todos os valores contidos na lista, porém para fazer o cálculo
# *precisa remover as strings.

import numpy as np
#funcao para tirar as palavras
def remove_item(my_list,*args):
    deletar = list(args)
    for item in deletar:
        while item in my_list:
            my_list.remove(item)
    return my_list
my_list = [6,7,4,7,8,4,2,5,7,"hum","dois"]
#informando qual item retirar
remove_item(my_list,"hum","dois")
#montando minha lista limpa
my_array = np.array(my_list)
#calculando
#soma
soma = my_array.sum()
l = my_array
#media
avg = numpy.mean(l)
print(my_list)
print(soma)
print(avg)


# In[2]:


#Data de Criação 11/05/2021 01:48
#Lista de exercicios - 02
#MBA
#Rosane Ananias
# 2 crie um método que receba duas matrizes, some os valores total de cada matriz e
#depois multiple o resultado delas e retorne o valor.

def calculaValoresMatriz(m1,m2):
    soma1=0
    soma2=0
    for x in m1:
        soma1+=x
    for x in m2:
        soma2+=x
    valor=soma1*soma2
    print('A soma da matriz 1 é ' + str(soma1))
    print('A soma da matriz 2 é ' + str(soma2))
    print('A multiplicação é ' + str(valor))
    return valor

somamatriz=calculaValoresMatriz([1,3,5,6], [3,4,5,2])
print(somamatriz)


# In[3]:


#Data de Criação 11/05/2021 01:48
#Lista de exercicios - 03
#Rosane Ananias

#3. Criar uma matriz nxm (n = 5, m =7)
#a. faça a matriz transposta desta matriz
#b. somar toda matrix
#c. somar todas as colunas
#d. somar todas as linhas.
#e. retorne o maior valor
#f. retorne o menor valor.

import numpy as np
from numpy import random
#Criar uma matriz nxm (n = 5, m =7)
n=5
m=7
matriz1 = np.random.randint(1,99, (n,m))
print('Matriz')
print(matriz1)
#faça a matriz transposta desta matriz
matriz2=matriz1.T
print('Matriz Transposta')
print(matriz2)
#somar toda matrix
print('Soma todos os valores da Matriz')
print(matriz2.sum())
#somar todas as colunas
print('Soma todos os valores das Colunas')
print(matriz2.sum(axis=0))
#somar todas as linhas.
print('Soma todos os valores das Linhas')
print(matriz2.sum(axis=1))
#retorne o maior valor
print('Retorne o maior valor da Matriz')
print(matriz2.max())
#retorne o menor valor.
print('Retorne o menor valor da Matriz')
print(matriz2.min())


# In[4]:


#Data de Criação 11/05/2021 01:48
#Lista de exercicios - 04
#MBA
#Rosane Ananias

#4. Crie uma matriz nxn (n=5). Agora some essa matriz com a matriz do exercício 3.

n=5
matriz3 = np.random.randint(1,99, (n,n))
print(matriz2.sum()+matriz3.sum()) 


# In[5]:


#Data de Criação 11/05/2021 01:48
#Lista de exercicios - 05
#MBA
#Rosane Ananias

#5. crie um array de números que vai de 0 a 1000.

n=5
matriz4 = np.random.randint(1,1000, (n,n))
print(matriz4)


# In[6]:


#Data de Criação 11/05/2021 01:48
#Lista de exercicios - 06
#MBA
#Rosane Ananias

#Regra: Crie uma matriz só de zeros

# Definindo o tamanho da matrix
n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []
for i in range(n):
    matriz.append([0]*m)
#imprimir em formato de matriz
for i in range(n):
    #impressão da matriz preenchida com zeros
    print(matriz[i])


# In[ ]:




