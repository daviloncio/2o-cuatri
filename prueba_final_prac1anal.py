#1: Multiiplicación de matrices
import numpy as np

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


#3-A: Movimientos en Hanoi
movimientos = 0
def hanoi_moves(n, t1="t1", t2="t2", t3="t3"):

    global movimientos
    if n == 1:
        movimientos += 1
    else:
        hanoi_moves(n - 1, t1, t3, t2)
        movimientos +=1
        hanoi_moves(n - 1, t2, t1, t3)

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
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return c



#4: Insert Sort
import numpy as np
def insert_sort(t:np.array):
    for i in range(1,len(t)):
        a1=t[i]
        a3=t[i-1]

        for e in range(i):
            if a1<a3:
            
                t[i-e]=a3
                t[i-e-1]=a1

                a3=t[i-e-2]
            else:
                break
    return t
a=np.array([2,1])
insert_sort(a)