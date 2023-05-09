import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
from edat_busqueda_binaria import BSTree,Tree

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

        with open(file,'r', encoding='utf-8',errors='ignore') as bibtex_file:
            parser = BibTexParser()
            parser.customization = customizations
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
            
            return bib_database.entries

    def _do_author_tree(self, list_records: list):
        ''' Creates an ABdB with the authors. Returns the ABdB'''
        author_abdb = BSTree_Author()
        
        for i in range(len(list_records)):
            autores=list_records[i]["author"]
            #print(autores)
            for autor in autores:  #en la lista nos podemos encontrar uno o más autores
                ind=autores.index(autor)
                #print(f'{autor} en el indice {i}')
                print(i,autor)
                author_abdb.insert(Author(autor,i,set(autores[:ind]+autores[ind+1:])))  
                    
        return author_abdb
 
    
    def get_author_records(self, author_:str) -> list: #recorremos el arbol binario
        "Returns the author's records"
        nodo_del_autor = self._authors_tree.find(Author( author_))
        if type(nodo_del_autor) == None:
            return None
        cites=nodo_del_autor.get_attrib('cites')
        publicaciones_del_autor=[]
        
        for cita in cites:
            publicaciones_del_autor.append(self._records[cita])
        return publicaciones_del_autor
        
    def get_author_info(self, author:str, f, *args, **kwargs):
        '''Apply the function f to the author with key = author'''
        #hago find autor es str y lo hago sobre el nodo que devuelve find
        #la funcion tiene que devolver lo que deuvleva la función
        author_obj= self._authors_tree.find(Author(author))
        
        if type(author_obj) == None:
            raise ValueError('jcnqooidcjoihouh')
        
        
        return f(author_obj,*args, **kwargs)
    
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
            if item == node._data:
                cites = 'cites'
                #print(f'hacemos add a {node._data.get_attrib(cites)} sumando {item.get_attrib(cites)}')
                node._data + item 
                
            if item < node._data:   #node._data es el objeto autor
                if node._left == None:
                    node._left = self.Node(item,node)
                    
                else:
                    _insert(node._left, item)
            elif item > node._data:
                if node._right == None:
                    colab = 'colab'
                    #print (f'creamos nodo con el autor {item.get_author()} y con colaboradores {item.get_attrib(colab)}')
                    node._right = self.Node(item,node)
                else:
                    _insert(node._right, item)
            else:
                return
        if self.is_empty():
            self._size += 1
            colab = 'colab'
            #print(f'creamos nodo con el autor {item.get_author()} y con colaboradores {item.get_attrib(colab)}')
            self._root = self.Node(item)
        else:
            _insert(self._root,item)
            self._size += 1
            

    '''def find(self, item): 
        
        def _find(x:self.Node, item):
            if x == None:
                return None
            
            if item == x._data.get_author():
                return x
            if item < x._data.get_author():
                return _find(x._left, item)
            else:
                return _find(x._right,item)
            
        node=_find(self._root,item)
        
        if node != None:
            return node._data
        return None    '''
    
    def apply_function(self, f, *args, **kwargs) -> list:
        '''Recorre el arbol en preorden, aplica la funcion f
        a cada nodo.
        Devuelve una lista. Cada uno de los items de la lista
        es un diccionario cuya clave es la llave del nodo y cuyo
        valor
        almacena el retorno de f sobre el nodo. (Recursiva)
            '''
        result= list()
        def _apply_function(node:self.Node,lista,f,*args,**kwargs):
            if (node._left,node._right) == (None,None):
                dic = dict()
                dic[node._data.get_author()] =f(node._data,*args, **kwargs)
                lista.append(dic)
                return 
            else:
                dic = dict()
                dic[node._data.get_author()] =f(node._data,*args, **kwargs)
                lista.append(dic)
                _apply_function(node._left,lista,f,*args,**kwargs)
                
                if node._right != None:
                    _apply_function(node._right,lista,f,*args,**kwargs)
                    
        _apply_function(self._root,result,f,*args,**kwargs)
        return result
    
class Author:
    '''Información que se guarda en los nodos del árbol'''
    def __init__(self, author, cites = None, colab = None):
        self._key = author # author name:
        self._attrib = dict()
        if cites or cites==0: # index cite in the db

            self._attrib['cites'] = list()
            self._attrib['cites'].append(cites)
            print(f'eeeey aqui meti el cite {cites} con {author}')
        else:
            self._attrib['cites'] = list()
        if colab: # conjunto colaboradores
            self._attrib['colab'] = colab
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
        self._attrib['cites'] += other.get_attrib('cites') #lo usamos porque es privado
        
        self._attrib['colab'].update(other.get_attrib('colab'))
        
    def __hash__(self):
        pass
    def __str__(self):
        str_ = self._key
        return str_



#MAIN PROGRAM 

db = DB('bibtex.bib') # crea la BB.DD
print(db._records)
#print(db._records)


author ='Clavito, Pablito'
print(f'\nReferencias del autor: {author}')
print(db.get_author_records(author))
print(f'\nColaboradores del autor: {author}')
print(db.get_author_info(author, Author.get_attrib, 'colab'))
print(f'\nTotal de publicaciones del autor: {author}')
print(len(db.get_author_info(author, Author.get_attrib, 'cites')))
print(f'\nLista con los colaboradores de cada uno de los autores:')
print(db.get_authors_info(Author.get_attrib, 'colab'))
