
    
def a(v):
    """
    >>> a('que')
    que
    >>> a(1)
    Traceback (most recent call last):
      File "c:/Users/juanj/OneDrive/Documentos/2� cuatri/repositorio1/pruebas.py", line 19, in <module>
        a(1)
      File "c:/Users/juanj/OneDrive/Documentos/2� cuatri/repositorio1/pruebas.py", line 11, in a
        raise TypeError('se esperaba un string')
    TypeError: se esperaba un string"""
    if type(v) != str:
        raise TypeError('se esperaba un string')
    x=print(v)
    return x
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

    
