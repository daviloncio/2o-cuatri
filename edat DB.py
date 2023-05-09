from edat_busqueda_binaria import BSTree,Tree
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author

#REUSAR DE LOS MÉTODOS DE ARBOL BINARIO LO MÁXIMO POSIBLE
class DB:
    def __init__(self, file):
        self._records = self._read_file(file) # list of dictionaries
        self._authors_tree = self._do_author_tree(self._records) #Author's ABdB
        self._file = file
    
    def _read_file(self, file) -> list:
        pass
        def customizations(record):
            pass
            """Use some functions delivered by the library
            :param record: a record
            :returns: -- customized record
            """
            record = author(record)
            return record

        with open(file,encoding="utf-8") as bibtex_file:
            parser = BibTexParser()
            parser.customization = customizations
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
            
            return bib_database.entries

    def _do_author_tree(self, list_records: list):
        ''' Creates an ABdB with the authors. Returns the ABdB'''
        author_abdb = BSTree_Author()
        for i in range(len(self._records)):
            for autor in (self._records[i]["author"]):
                author_abdb.insert(Author(autor,i,set(self._records[i]["author"])))  
        return author_abdb
 
    
    def get_author_records(self, author_:str) -> list: #recorremos el arbol binario
        "Returns the author's records"
        nodo_del_autor = self._authors_tree.find(author_)
        if nodo_del_autor == None:
            return None
        return nodo_del_autor._data.get_attrib('cites')
        
    def get_author_info(self, author, f, *args, **kwargs):
        '''Apply the function f to the author with key = author'''
        #hago find autor es str y lo hago sobre el nodo que devuelve find
        #la funcion tiene que devolver lo que deuvleva la función
        return f(self._authors_tree.find(author), *args, **kwargs)
    
    def get_authors_info(self, f, *args, **kwargs):
        '''Devuelve una lista con el resultado de aplicar la función f
        a todos los autores de la base datos.
        Para ello, se aplica la función f a todos los nodos del árbol
        '''

        return self._authors_tree.apply_function(f,*args,**kwargs)
    
    
    
class BSTree_Author(BSTree):
    def insert(self, item):  #objeto clase author
        '''Adds item to its proper place in the tree. Probablemente haya que modificar el insert
        '''
        
        def _insert(node, item):
            '''Assume BSTree is not empty'''
            if item == None: #esto es de pruebas no se si va
                return
            if item == node._data:
                node._data = node._data + item
            if item < node._data:   #nada más llamamos a la función, la primera compraración es con el nodo raíz
                if node._left._data == None:
                    node._left._data = self.Node(item,node)
                    self._size += 1
                else:
                    _insert(node._left, item)

            elif item > node._data:
                if node._right._data == None:
                    node._right._data = self.Node(item,node)
                    self._size += 1
                else:
                    _insert(node._right, item)
            else:
                return
        if self.is_empty():
            self._size += 1
            self._root = self.Node(item)
        else:
            _insert(self._root,item)
            self._size += 1
    def apply_function(self, f, *args, **kwargs) -> list:
        '''Recorre el arbol en preorden, aplica la funcion f
        a cada nodo.
        Devuelve una lista. Cada uno de los items de la lista
        es un diccionario cuya clave es la llave del nodo y cuyo
        valor
        almacena el retorno de f sobre el nodo. (Recursiva)
        '''
        result=[]
        def _apply_function(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append({node._data.get_author() : f(node, *args, **kwargs)})
                return 
            else:
                lista.append({node._data.get_author() : f(node, *args, **kwargs)})
                _apply_function(node._left,lista)
                #si tiene nodo hijo derecho
                if node._right != None:
                    _apply_function(node._right,lista)
                    
        _apply_function(self._root,result)
        return result
    
    
class Author:
    '''Información que se guarda en los nodos del árbol'''
    def __init__(self, author, cites = None, colab = None):
        self._key = author # author name:
        self._attrib = dict()
        if cites: # index cite in the db
            self._attrib['cites'] = cites
        else:
            self._attrib['cites'] = list()
        if colab: # conjunto colaboradores
            self._attrib['colab'] = colab
            self._attrib['colab'].remove(author)
        else:
            self._attrib['colab'] = set()
    def get_author(self):
        return self._key
    def get_attrib(self, attrib):
        return self._attrib[attrib]
    def __eq__(self, other):       
        if self._key == other.get_author():
            return True
        return False         
    def __gt__(self, other):
        if self._key>other.get_author():
            return True
        return False
    def __lt__(self, other):
        if self._key<other.get_author():
            return True
        return False
    def __add__(self, other):
        '''Modifica el diccionario de self._atrib con la información de other.
        Este metodo magico lo vamos a ir usando para poder modificar un nodo y meter más info haciendo []+[aquí iría la referencia del archivo]'''
        self._attrib["cites"] = self._attrib["cites"] + [other.get_attrib('cites')] #lo usamos porque es privado
        self._attrib["colab"].add(other.get_author())
    def __hash__(self):
        pass
    def __str__(self):
        str_ = self._key
        return str_



#MAIN PROGRAM 

db = DB('toy_bibtex.bib') # crea la BB.DD

print(db._authors_tree)



author = 'Clavito, Pablito'
print(f'\nReferencias del autor: {author}')
print(db.get_author_records(author))
"""
author = 'Clavito, Pablito'
print(f'\nColaboradores del autor: {author}')
print(db.get_author_info(author, Author.get_attrib, 'colab'))
print(f'\nTotal de publicaciones del autor: {author}')
print(len(db.get_author_info(author, Author.get_attrib, 'cites')))
print(f'\nLista con los colaboradores de cada uno de los autores:')
print(db.get_authors_info(Author.get_attrib, 'colab'))"""
