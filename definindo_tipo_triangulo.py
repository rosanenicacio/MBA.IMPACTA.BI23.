#!/usr/bin/env python
# coding: utf-8

# In[4]:


#digitando as informações
def triangulo():
    a = float(input('Primeiro lado: '))
    b = float(input('Segundo  lado: '))
    c = float(input('Terceiro lado: '))
    
     # regra para valdiar se é triângulo
    if (a + b < c) or (a + c < b) or (b + c < a):
        print('Nao é um triangulo')
    elif (a == b) and (a == c) :
        print('Equilatero')
    elif (a==b) or (a==c) or (b==c):
        print('Isósceles')
    else:
        print('Escaleno')
   


# In[5]:


triangulo()


# In[ ]:




