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
    >>> infix_to_sufix((A + B) * (C + D)")
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
#print(infix_to_sufix("m*n+(p-q)+r"))

if __name__== " __main__ ":
    import doctest
    doctest.testmod(name=infix_to_sufix)
  
print (infix_to_sufix("(A + B) * (C + D)"))
