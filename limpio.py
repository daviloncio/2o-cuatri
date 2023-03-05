
import numpy as np
import random 
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression




#función multiplicación matrices

def multiplicar(a:np.array,b:np.array):
    def multiplicar_listas(l1,l2):
        a_sumar=[]
        for i in range(len(l1)):
            a_sumar.append(l1[i]*l2[i])
        return sum(a_sumar)
    filas_a,columnas_a=np.shape(a)
    filas_b,columnas_b=np.shape(b)
   
    if columnas_a!=columnas_b:
        raise KeyError('las matrices no se pueden multiplicar')
    l=[]
    for x in range(filas_a):
        l.append([])
    for i in range(filas_a):  #por cada fila de a hay una columna de b SIEMPRE,sino no podríamos multiplicar las matrices
        for e in range(columnas_b):
            l[i].append(multiplicar_listas(a[i],b[:,e]))
    return np.array(l)

movimientos = 0

#3A Hanoi
def hanoi_moves(n, t1="t1", t2="t2", t3="t3"):

    global movimientos
    if n == 1:
        movimientos += 1
    else:
        hanoi_moves(n - 1, t1, t3, t2)
        movimientos +=1
        hanoi_moves(n - 1, t2, t1, t3)

import math
#3-B: fibonacci
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    

def fibonacci_iterativo(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for h in range(n-1):
        c = a+b
        a = b
        b = c
    return c

#funciones insert sort

def insert_sort(t: np.array):
    for i in range(1, len(t)):
        j = i
        a = t[i]
        while j > 0 and t[j-1] > a:
            t[j] = t[j-1]
            j -= 1
            t[j] = a
a=np.array([8,7,2,1,3,4,5,9,1,2])

def insert_sort1(t: np.array, ini: int, fin: int):
    if ini == fin:
        return t
    elif fin<0:
        fin=len(t)+fin #por si se nos introduce un índice final negativo, lo convertimos a positivo
    

    for i in range(ini,fin):
        j = i
        a = t[i]
        while ini < j  and t[j-1] > a:
            t[j] = t[j-1]
            j -= 1
            t[j] = a
    return t
#print(insert_sort1(a,0,-3))

def ave_time_insert_sort(n_permutations: int,size_ini:int,size_fin:int,step:int) -> np.array:
    
    list_tiempos_medias = []
    tamaño_array = []
    
    for e in range(size_ini,size_fin,step):
        
        tamaño_array.append(e)
        hacer_media_tiempos = []
        
        for i in range(n_permutations):
            
            creamos_permutación = np.random.permutation(e)  
            inicio=time.time()
            insert_sort(creamos_permutación)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            hacer_media_tiempos.append(tiempo_ejecucion)
        
        result = sum(hacer_media_tiempos)/n_permutations
        list_tiempos_medias.append(result)
        
    result = dict(zip(tamaño_array,list_tiempos_medias) )
       
 
    
def worst_time_insert_sort(size_ini:int,size_fin:int,step:int) -> np.array:

    tamaño_array = []
    list_tiempos = []
    for e in range(size_ini,size_fin,step):
        
        tamaño_array.append(e)
        
        list_mayor_a_menor = []
        for i in reversed(range(1,e)):
            list_mayor_a_menor.append(i)  #de esta forma, el insertsort tendrá que hacer el mayor número de comparaciones posible.

        inicio=time.time()
        insert_sort(list_mayor_a_menor)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        list_tiempos.append(tiempo_ejecucion)
    print(list_tiempos)
    result = dict(zip(tamaño_array,list_tiempos) )
    print(result)
       