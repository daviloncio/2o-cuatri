from edat_busqueda_binaria import BSTree,Tree
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author

#REUSAR DE LOS MÉTODOS DE ARBOL BINARIO LO MÁXIMO POSIBLE
class DB:
    def __init__(self, file):
        self._records = self._read_file(file) # list ofdictionaries
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

        with open(file) as bibtex_file:
            parser = BibTexParser()
            parser.customization = customizations
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
            
            return bib_database.entries

    def _do_author_tree(self, list_records: list):
        ''' Creates an ABdB with the authors. Returns the ABdB'''
        author_abdb = BSTree_Author()
        for element in self._records:
            author_abdb.insert(element["author"])
 
    
    def get_author_records(self, author_:str) -> list: #
        "Returns the author's records"
        pass
    def get_author_info(self, author, f, *args, **kwargs) -> list:
        '''Apply the function f to all nodes
        devuelve el retorno de f
        '''
        pass
    def get_authors_info(self, f, *args, **kwargs):
        '''Apply the function f to all nodes
        '''
        pass
    
    
    
class BSTree_Author(BSTree):
    def insert(self, item):
        '''Adds item to its proper place in the tree. Probablemente haya que modificar el insert
        '''

        def _insert(node, item):
            '''Assume BSTree is not empty'''
            if item < node.data:   #nada más llamamos a la función, la primera compraración es con el nodo raíz
                if node._left == None:
                    node._left = self.Node(Author(item),node)
                    
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
    def apply_function(self, f, *args, **kwargs) -> list:
        '''Recorre el arbol en preorden, aplica la funcion f
        a cada nodo.
        Devuelve una lista. Cada uno de los items de la lista
        es un diccionario cuya clave es la llave del nodo y cuyo
        valor
        almacena el retorno de f sobre el nodo. (Recursiva)
        '''
        pass
    
    
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
        else:
            self._attrib['colab'] = set()
        def get_author(self):
            return self._key
        def get_attrib(self, attrib):
            return self._attrib[attrib]
        def __eq__(self, other):
            if self._key == other._key:
                return True
            return False
        def __gt__(self, other):
            if self._key>other._key:
                return True
            return False
        def __lt__(self, other):
            if self._key<other._key:
                return True
            return False
        def __add__(self, other):
            '''Modifica el diccionario de self._atrib con la información de other.
            Este metodo magico lo vamos a ir usando para poder modificar un nodo y meter más info haciendo []+[aquí iría la referencia del archivo]'''
            self._cites += other.get_attrib["cites"] #lo usamos porque es privado
            pass
        def __hash__(self):
            pass
        def __str__(self):
            str_ = self._key
            return str_

         
db = DB("toy_bibtex.bib")
print(db._records)