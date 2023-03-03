#####-----EJERCICIO 7



"""La función recibe un número decimal entero y una base a la que pasaremos dicho número. Aplicamos recursión hasta que lo que nos quede e el cociente un número
menor que en el resto, en cuyo caso empezaremos a formar el numero que buscamos.Vamos construyéndolo por sus cifras finaes hasta que se acaban ejecutando todas las funciones
que se amontonaron en la pila por la recursión"""



def decimal_to_base_rec (num:int, base:int)->str:
    
    """
    Test the decimal_to_base_rec function
    >>> decimal_to_base_rec(19,2)
    '1100'
    >>> decimal_to_base_rec(7,5)
    '21'
    """
    
    cociente,resto=divmod(num,base)
    
    if cociente >= base:
        cambio_base=decimal_to_base_rec(cociente,base)  
        #con cambio_base recibimos la secuencia de dígitos que hemos obtenido las recusiones anteriores que hemos finalizado
        

    else:
        result=str(resto)+str(cociente) #empezamos a finalizar las funciones de la recursión
        return result
        
    result=str(resto)+cambio_base
    return result

if __name__== " __main__ ":
    import doctest
    doctest.testmod()
    

####---EJERCICIO 6
#poner el caso error fuera de la recursión


"""esta función nos sirve básicamente para comprobar que lo que hemos obtenido es una expresión infijo.
    De lo contrario, la expresión prefijo recibida no estaría bien formada y devolvemos error.
    
    Recibimos como parámetro la expresión que usará la otra función, donde haremos la recursión
    (la comprobación está fuera de la recursión)
    
    La comprobación se basa en que el resultado final del index vienen a ser el número de operadores que nos
    encontramos al principio de la expresión(hay que destacar que, si tenemos un operador que NO está en el principio, 
    volvemos a la recursión pero el index que finalmente se devuelve no le estamos sumando la unidad).Si el index coincide
    con lo explicado significará que se ha ejecutado adecuadamente y que hemos metido una expresión prefija correcta."""

def from_prefix_to_infix(expr:str,oper=['+','-','*','/','^']):
    """
    Test the from_prefix_to_infix function
    >>> from_prefix_to_infix('/*AB+AC')
    ('(A*B)/(A+C)', 2)
    >>> from_prefix_to_infix('+/*ABAC')
    ('(((A*B)/A)+C))', 3)
    >>> from_prefix_to_infix('+^-ABCD')
    ('(((A-B)^C)+D)', 3)
    """
    

    def from_prefix_to_infix_interno (expr:str, oper=['+','-','*','/','^'])->str:
        primer_caracter=expr[0]  #en el caso base será siempre un operador
        
        resto_opr=expr[1:]
        if primer_caracter not in oper:
            index=0
            empezamos_result=''
            return empezamos_result,index
        else:
            build_expresion,index=from_prefix_to_infix_interno(resto_opr)
            
            if index == 0:  #es decir, si justo acabamos de encontrarnos con el caso excepción...
                if resto_opr[1] in oper:
                    pass
                else:
                    result='('+resto_opr[index]+primer_caracter+resto_opr[index+1]+')'
                
            else:
                if resto_opr[index+2] in oper: #si volvemos a encontrarnos con un operador,volvemos a la recursión
                    
                    result=build_expresion+primer_caracter+from_prefix_to_infix_interno(resto_opr[index+2:])[0]
                    
                else:
                    result='('+build_expresion+primer_caracter+resto_opr[index+2]+')'
                    
            index=index+1
            
            return result,index
    result,index=from_prefix_to_infix_interno(expr)
    operadores_principio = 0
    for character in expr:
        
        if character in oper:  #observamos el numero de operadores que hay al principio, y de coincidir con index, se habrá recorrido una expresión prefija correcta
            operadores_principio += 1  
        else:
            break

    if index != operadores_principio:
        
        raise KeyError('se ha introducido una expresión prefijo inválida')
    
    return result,index
            
    
from_prefix_to_infix('/*AB+AC') #como devulve una tupla,pedimos solo el 1er elemento

#####---EJERCICIO 5

from stackarray import *
"""
    Esta función recibe una expresión infija correcta y devuelve su correspondiente expresión sufija. 
    Recibe dos argumentos:
        expr (str): Un string con la exxpresión infijo
        oper (dict): Un diccionario con los tipos de operador permitidos, así como su "peso" que mas tarde servira para tener la expresión correctamente balanceada
    Devuelve:
        expresion_final (str): Devuelve la correspondiente expresion sufija en forma de string.
"""
def infix_to_sufix(expr,oper = ['+', '-', '*', '/', '(', ')', '^'] )->str:
    
    """
    Test the infix_to_sufix function
    >>> infix_to_sufix((A + B) * (C + D))
    A  B+  C  D+*
    """
  
    s=Stack()  
    prioridad = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    expresion_final = '' 
    for c in expr:
        if c not in oper:   #si encuentra un número lo añade directamente a la expresión final 

            expresion_final+= c
        elif c =='(':  

            s.push('(')
        elif c ==')':   #si encuentra un parentesis de cierre vacia la pila añadiendo los correspondientes operadores hasta encontrar su correspondiente apertura
            while s  and s.top() != '(':

                expresion_final+=s.pop()
            s.pop()
        else:   #cuando se encuentra con un operador, va añadiendo los distintos operadores en orden de prioridad
            while s and s.top() !='(' and prioridad[c] <= prioridad[s.top()]:
                expresion_final+=s.pop()
            s.push(c)
    while s:    #al final, vacía la pila, dentro de la cual solo quedan operadores, y los añade al final de la expresión en orden de llegada (LIFO)
        expresion_final+=s.pop()
    return expresion_final

if __name__== " __main__ ":
    import doctest
    doctest.testmod()

