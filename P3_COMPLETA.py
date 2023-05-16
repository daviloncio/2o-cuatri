import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author


from stackarray import Stack

class Tree:
    class Node:
        __slots__ = '_data', '_left', '_right'
        def __init__(self, element,parent = None):
            self._data = element
            self._left = None
            self._right = None
            self._parent = parent
            
    def __init__(self):
        self._root = None
        self._size = 0
    def is_empty(self):
        return self._root == None
    def inorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _inorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                _inorder(node._left,lista)
                
                lista.append(node._data)
                
                if node._right != None:
                    _inorder(node._right,lista)
                    
        _inorder(self._root,result)
        return result
        
    def preorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _preorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                lista.append(node._data)
                
                _preorder(node._left,lista)
                #si tiene nodo hijo derecho
                if node._right != None:
                    _preorder(node._right,lista)
                    
        _preorder(self._root,result)
        return result
    def postorder(self):
        """Returns a list with all nodes. Supports an inorder
        traversal on a view of self. Recursive
        """
        result = []
        def _postorder(node:self.Node,lista):
            if (node._left,node._right) == (None,None):
                lista.append(node._data)
                return 
            else:
                _postorder(node._left,lista)
                #si tiene nodo hijo derecho
                if node._right != None:
                    _postorder(node._right,lista)
                
                lista.append(node._data)
            
        _postorder(self._root,result)
        return result
        pass
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise.
        """
        def _recurse(node, level):
        # Base case
            if node == None:
                return ''
        # General case
            s = ''
            s += _recurse(node._right, level + 1)
            s += "| " * level
            s += str(node._data) + "\n"
            s += _recurse(node._left, level + 1)
            return s
        return _recurse(self._root, 0)
    def num_nodes(self):
        def _num_nodes(node:self.Node):
            if self.is_empty():
                return 0
            else:
                return 1 + _num_nodes(node._left) + _num_nodes(node._right)
        _num_nodes(self._root)
    def mirror(self):
        def _mirror(node):
  
            if node._left == None: #no tendrá hijos
                return
            else:
                _mirror(node._left)
                if node._right != None:  #comprobación de que existe el hijo derecho

                    node._right._data,node._left._data = node._left._data,node._right._data
                    _mirror(node._right)  
                    
        _mirror(self._root) #no devolvemos nada, estamos modificando el árbol
                            #por lo que hacemos un print para comprobar y ya

    def print_path_recursive(self,item):
        '''tree tiene su propio print path como BSTree.Este es recursivo
        el caso base se da al encontrar al elemento.USA EL PARENT'''
        camino=''
        def recursive(node:self.Node,item):
            if node._data == item:
                return f'{node._data}'
            if (node._left,node._right) == (None,None):
                return None
            if node._left != None:
                busco_izq=recursive(node._left,item)
                
            if busco_izq == None and node._right != None: 
                #solo si hay hijo derecho y si no hemos encontrado por la derecha
                busco_der = recursive(node._right,item)
                
                if busco_der != None: #encontramos algo por la derecha
                    busco_der = f'{node._data}->'+busco_der   
                return busco_der #sino devolvemos None
            
            if busco_izq != None: #ha habido suerte por la izq
                busco_izq = f'{node._data}->'+busco_izq 
            return busco_izq #devolvemos None
        print(recursive(self._root,item))

class BSTree(Tree):
    """A link-based binary search tree implementation.
    Non-repeated elements
    """
    class Node:
        '''Node includes attibute parent'''
        __slots__ = '_data', '_left', '_right', '_parent'
        def __init__(self, element, parent = None):
            self._data = element
            self._left = None
            self._right = None
            self._parent = parent # Solo necesario para el borrado en ABdB
    
    def insert(self, item):
        '''Adds item to its proper place in the tree'''
        
        def _insert(node, item):
            '''Assume BSTreee is not empty'''
            if item < node._data:   #nada más llamamos a la función, la primera compraración es con el nodo raíz
                if node._left == None:
                    node._left = self.Node(item,node)
                    
                else:
                    _insert(node._left, item)
            elif item > node._data:
                if node._right == None:
                    node._right = self.Node(item,node)
                else:
                    _insert(node._right, item)
            else:
                return
            """if self.find(item) != None:
            raise Exception('ese número ya está dentro del árbol')"""
        if self.is_empty():
            self._size += 1
            self._root = self.Node(item)
        else:
            _insert(self._root,item)
            self._size += 1

    def find(self, item):
        def _find(x:self.Node, item):
            if x == None:
                return None
            
            if item == x._data:
                return x
            if item < x._data:
                return _find(x._left, item)
            else:
                return _find(x._right,item)
        
        node=_find(self._root,item)
        
        if node != None:
            return node
        return None
    
    def print_path(self,item):
        def _print_path(node:self.Node,item):
            if node == None:
                return 
            if node._data == item:
                s = Stack()
                
                while node._parent != None:
                    s.push(node._data)
                    node = node._parent
                s.push(node._data)
                strng = ""
                strng = strng + str(s.pop())
                
                while s.is_empty() == False:
                    strng = strng + "->" + str(s.pop())
                    
                print (strng)
            else:
                _print_path(node._right,item)
                _print_path(node._left,item)
                          
        _print_path(self._root,item)
    def _successor(self,x):
        '''si tiene hijo derecho,el sucesor será el menor del subárbol
           sino, buscará al primer hijo izquierdo por arriba y cogerá a su padre
           si nos encontramos con la raíz y no hemos dado con un hijo izq devolvemos None'''
        if x._right != None:
            buscar_min= x._right
            while buscar_min._left != None:
                buscar_min = buscar_min._left
            return buscar_min
        
        buscar_hijo_izq = x
        while buscar_hijo_izq._parent != None:
            
            if buscar_hijo_izq._parent._left == buscar_hijo_izq:
                return buscar_hijo_izq._parent
            
            buscar_hijo_izq=buscar_hijo_izq._parent
    def successor(self, item):
        x = self.find(item) # returns the node with item as data
        if x != None:
            y = self._successor(x)
        else:
            y = None
        if y != None:
            return y
        return None
    
    def _transplant(self, u, v):
        if u._parent == None:
            self._root = v
        elif u == u._parent._left:
            u._parent._left = v
        
        else:
            u._parent._right = v
        if v._data != None:
            v._parent = u._parent
    def delete(self, item):
        z = self.find(item)
        if z == None:
            raise TypeError("Given node does not exist.")
        if z._left == None:
            self._transplant(z, z._right)
        elif z._right == None:
            self._transplant(z, z._left)
        else:
            y = self.successor(z._data)
            if y != z._right:
                self._transplant(y, y._right) 
                y._right = z._right
                y._right._parent = y
            self._transplant(z, y)
            y._left = z._left
            y._left._parent = y 
            
  

    


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
            
            try:
                revista=list_records[i]["journal"]
            except:
                revista = None
            try:
                year_publicacion = int(list_records[i]["year"]) #no queremos str para neustro set()
            except:
                year_publicacion = "Unknown"
            
            
            #print(autores)
            for autor in autores:  #en la lista nos podemos encontrar uno o más autores
                ind=autores.index(autor)
                
                #print(f'{autor} en el indice {i}')
                
                author_abdb.insert(Author(autor,i,set(autores[:ind]+autores[ind+1:]),year_publicacion,revista))  
                    
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
            raise ValueError('El autor no se encuentra en la base de datos')
        
        
        return f(author_obj._data,*args, **kwargs)
    
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
            
            #antes solo hacía falta poner node._data + item 
            if item == node._data:
                node._data=node._data + item 
                
            if item < node._data:   #node._data es el objeto autor
                if node._left == None:
                    node._left = self.Node(item,node)
                    
                else:
                    _insert(node._left, item)
            elif item > node._data:
                if node._right == None:
                    node._right = self.Node(item,node)
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
        result= list()
        def _apply_function(node:self.Node,lista,f,*args,**kwargs):
            if (node._left,node._right) == (None,None):
                dic = dict()
                result_func = f(node._data,*args, **kwargs)
                if result_func != None:
                    
                    dic[node._data.get_author()] = result_func
                    lista.append(dic)
                return 
            else:
                dic = dict()
                result_func = f(node._data,*args, **kwargs)
                if result_func != None:
                    
                    dic[node._data.get_author()] = result_func
                    lista.append(dic)
                
                if node._left != None:
                    _apply_function(node._left,lista,f,*args,**kwargs)
                
                if node._right != None:
                    _apply_function(node._right,lista,f,*args,**kwargs)
                    
        _apply_function(self._root,result,f,*args,**kwargs)
        return result
    
class Author:
    '''Información que se guarda en los nodos del árbol'''
    def __init__(self, author, cites = None, colab = None,year=None,journal=None):
        self._key = author # author name:
        self._attrib = dict()
        
        if type(cites)==list: 
            #a la hora de crear un nuevo author con add,podríamos querer introducir una lista de cites
            self._attrib['cites'] = cites
        elif cites or cites==0: # index cite in the db

            self._attrib['cites'] = list()
            self._attrib['cites'].append(cites)
            #print(f'eeeey aqui meti el cite {cites} con {author}')
        else:
            self._attrib['cites'] = list()
        if colab: # conjunto colaboradores
            self._attrib['colab'] = colab
        else:
            self._attrib['colab'] = set()
            
        if type(year)==list:
            self._attrib['year'] = year
        elif year:
            self._attrib['year']= list()
            self._attrib['year'].append(year)
        else:
            self._attrib['year']= list()
            
        if type(journal)==list: 
            self._attrib['journal'] = journal
        elif journal:
            self._attrib['journal']= list()
            self._attrib['journal'].append(journal)
        else:
            self._attrib['journal']= list() 
  
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
    
    def __add__(self,other):
        
        new_cites=self._attrib['cites'] + other.get_attrib('cites')
        new_colab = self._attrib['colab'].union(other.get_attrib('colab'))
        new_year=self._attrib['year'] + other.get_attrib('year')
        new_journal=self._attrib['journal'] + other.get_attrib('journal')
        
        return Author(self._key,new_cites,new_colab,new_year,new_journal)
        
    def __add__antiguo(self, other):
        '''Modifica el diccionario de self._atrib con la información de other.
        Este metodo magico lo vamos a ir usando para poder modificar un nodo y meter más info haciendo []+[aquí iría la referencia del archivo]'''
        self._attrib['cites'] += other.get_attrib('cites') #lo usamos porque es privado
        
        self._attrib['colab'].update(other.get_attrib('colab'))
        
        self._attrib['year'].update(other.get_attrib('year'))
    def __hash__(self):
        pass
    def __str__(self):
        str_ = self._key
        return str_



#MAIN PROGRAM 

db = DB('bibtex.bib') # crea la BB.DD

#print(db._records)

author ='Kondo, Tadashi'
print(f'\nColaboradores del autor: {author}')
print(db.get_author_info(author, Author.get_attrib, 'colab'))
print(f'\nTotal de publicaciones del autor: {author}')
print(len(db.get_author_info(author, Author.get_attrib, 'cites')))

a = 10

def citas_totales(data, a):
    l = data.get_attrib('cites')
    if len(l) > a:
        return l
def autores_2022(data):
    years =data.get_attrib('year')
    if 2022 in years:
        return years
def medias(data,attrib,num_publis:list):
    l = data.get_attrib(attrib)
    num_publis.append(len(l))
def crear_histograma(data,attrib,histograma:dict):
    lista = data.get_attrib(attrib) #la lista podria contener las cites,años o revistas.
    
    for element in lista: 
        if element not in histograma:
            histograma[element]=1
        else:
            histograma[element]+= 1
    return histograma
    

    
print(f"Lista los autores de l base de datos con mas de {a} publicaciones")    
print(db.get_authors_info(citas_totales, a))

print('Lista de los autores de la base de datos que publicaron en 2022')
print(db.get_authors_info(autores_2022))

num_publis=[]
db.get_authors_info(medias,'cites',num_publis)
media_publicaciones_por_autor=sum(num_publis)/len(num_publis)
print('media de publicaciones por autor:',media_publicaciones_por_autor)

num_colabs=[]
db.get_authors_info(medias,'colab',num_colabs)
media_colaboraciones_por_autor=sum(num_colabs)/len(num_colabs)
print('media de colaboraciones por autor:',media_colaboraciones_por_autor)

dict_revistas={}
db.get_authors_info(crear_histograma,'journal',dict_revistas)
#ordenamos el diccionario según los valores de las claves y sacamos las cinco primeras
print('las cinco revistas más famosas:',sorted(dict_revistas,reverse=True)[:5])


dict_year={}
db.get_authors_info(crear_histograma,'year',dict_year)
print('histograma del numero de publicaciones por año:',dict_year)







'''



print(f'\nReferencias del autor: {author}')
print(db.get_author_records(author))
print(f'\nColaboradores del autor: {author}')
print(db.get_author_info(author, Author.get_attrib, 'colab'))
print(f'\nTotal de publicaciones del autor: {author}')
print(len(db.get_author_info(author, Author.get_attrib, 'cites')))
print(f'\nLista con los colaboradores de cada uno de los autores:')
print(db.get_authors_info(Author.get_attrib, 'colab'))
'''