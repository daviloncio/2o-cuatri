from stackarray import *
####---EJERCICIO 7  
#poner el caso error fuera de la recursión
def comprobación_infijo(expr:str):
    """esta función nos sirve básicamente para comprobar que lo que hemos obtenido es una expresión infijo.
    De lo contrario, la expresión prefijo recibida no estaría bien formada y devolvemos error.
    
    Recibimos como parámetro la expresión que usará la otra función, donde haremos la recursión
    (la comprobación está fuera de la recursión)
    
    La comprobación se basa en que si el index no tiene como valor final la posición del último elemento
    de la expresión recibida, está mal"""

    def from_prefix_to_infix (expr:str, oper=['+','-','*','/','^'])->str:
        primer_caracter=expr[0]  #en el caso base será siempre un operador
        
        resto_opr=expr[1:]
        if primer_caracter not in oper:
            index=0
            empezamos_result=''
            return empezamos_result,index
        else:
            c,index=from_prefix_to_infix(resto_opr)
            
            if index == 0:  #es decir, si esta es la función predecesora del caso excepción...
                result='('+c+resto_opr[index]+primer_caracter+resto_opr[index+1]+')'
                
            else:
                if resto_opr[index+2] in oper:#si volvemos a encontrarnos con un operador,volvemos a la recursión

                    result=c+primer_caracter+from_prefix_to_infix(resto_opr[index+2:])[0]
                    
                else:
                    result='('+c+primer_caracter+resto_opr[index+2]+')'
                    index=index+1
            index=index+1
            print(index)
            return result,index

    return from_prefix_to_infix('-/AB*cr')[0]
    
comprobación_infijo('-/AB*cr') #como devulve una tupla,pedimos solo el 1er elemento



def decimal_to_base_rec (num:int, base:int)->str:
    
    cociente,resto=divmod(num,base)
    print(cociente,resto)
    
    if cociente >= base:
        cambio_base=decimal_to_base_rec(cociente,base)  
        #con cambio_base recibimos la secuencia de dígitos que hemos obtenido las recusiones anteriores que hemos finalizado
        

    else:
        result=str(resto)+str(cociente) #empezamos a finalizar las funciones de la recursión
        return result
        
    result=str(resto)+cambio_base
    return result
    
decimal_to_base_rec(19,2)

