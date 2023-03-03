

def suma(a,b):
    """
    Test the suma function
    >>> suma(0,1)
    1
    
    """
    return a+b

def decimal_to_base_rec (num:int, base:int)->str:
    
    """
    Test the decimal_to_base_rec function
    >>> decimal_to_base_rec(19,2)
    '11001'
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

###---EJERCICIO 6
#poner el caso error fuera de la recursión

def from_prefix_to_infix(expr:str, oper=['+','-','*','/','^']):
    primer_caracter=expr[0]
    resto_expr=expr[1:]
    segundo_caracter=expr[1]

    if primer_caracter in oper:
        formando_expr,index = from_prefix_to_infix(resto_expr)
        if expr[index+2] in oper: #vuelta a la recursión, hay un operador después de primer_caracter, dos posiciones delante.
            formando_expr=formando_expr+'('+expr[index]+primer_caracter+from_prefix_to_infix(expr[index+1:])[0]+')'
            
        else:
            formando_expr='('+formando_expr+primer_caracter+expr[index+1]+')'

    else: #caso excepción
        index = 0
        principio_expr=''
        return principio_expr,index
    index += 1
    return formando_expr,index

    
print(from_prefix_to_infix('+/*ABAC'))