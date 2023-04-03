import random 

class LinkedList:

    
    #--------------- nested _Node class 
    class _Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        
        __slots__ = '_data', '_next'   # streamline memory usage
        
        def __init__(self, e):
            self._data = e
            self._next = None
            
    #------- LinkedList methods  ---------------------------------------
    
    def __init__(self) :
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty (self):
        return self._size == 0
    
    def add_first (self, e):
        newest = self._Node(e)     # create new node instance storing reference to element e
        newest._next = self._head  # set new node’s next to reference the old head node
        self._head = newest        # set variablehead to reference the new node
        self._size += 1            # increment the node count
        
        # Speccial case: only one node in the list
        if self._size == 1:
            self._tail = self._head
        
    def add_last(self, e):
        if self.is_empty():
            self.add_first(e)
            return
        
        newest = self._Node(e)  # create new node instance storing reference to element e
        self._tail._next = newest  # set old last node's next to reference the newest
        self._tail = newest        # set variable tail to reference the new node
        self._size += 1            # increment the node count
        
    def delete_first(self):
        if self.is_empty():
            raise Exception('The list is empty')
        
        data = self._head._data            # capture tha data storaged at tha first node
        self._head = self._head._next      # make head point to next node (or None)
        self._size -= 1                    # decrement the node count
    
        # Special case: Empty list
        if self.is_empty():
            self._tail = None
        
        return data
    
    def delete_last (self):
        '''cost O(n)'''
        
        # Less than one node in the list
        if self._size <= 1:
            return self.delete_first()
        
        # Traverse the list to stop BEFORE the last node
        auxiliar = self._head
        while auxiliar._next._next != None: 
            auxiliar = auxiliar._next
        
        data = auxiliar._next._data    # capture tha data storaged at tha first node
        self._tail = auxiliar          # set the node referenced by auxiliar the new last
        self._tail._next = None        # set the next of the last node 
        self._size -= 1                # decremet 
        
        return data
    
    def first(self):
        if self.is_empty():
            raise Exception('The list is empty')
        return self._head._data 

    def last(self):
        if self.is_empty():
            raise Exception('The list is empty')
        return self._tail._data 
    
    def __len__(self):
        '''Return the number of elements in the list'''
        return self._size
        
    def __iter__(self):
        '''Permite que la lista enlazada sea un objeto iterable. Coste O(n)'''
        auxiliar = self._head
        while auxiliar != None:
            yield auxiliar._data
            auxiliar = auxiliar._next
    
    def __str__(self): 
        str_ = ''
        for elem in self:
            str_ += str(elem) + ''
            
        str_ += ''
        return str_


class Edge:
    def __init__(self, from_, to_, weight = None):
        self._from = from_
        self._to = to_
        self._weight = weight
    def endpoints(self):
        return (self._from, self._to, self._weight)
    def __str__(self) -> str:
        
        return f'({self._from},{self._to},{self._weight})'


class Vertex:
    def __init__(self, vertex): 
        
        self._attributes = {'key' : vertex,
        'd' : 0, # discover time DFS  #supongo que modificaremos estos valores a la hora de hacer el set_attribute para cambiar el color.
        'f' : 0, # finalization DFS
        'degree' : 0, # vertex degree
        'color' : 'WHITE', # to mark nodes
        'parent' : None } # to the dfs-tree+
        self._adyacents = list()
    def adyacent(self,vertex):
        self._adyacents.append(vertex)
    def get_attribute(self, name):
        '''Returns the attribute name of the vertex
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys():
            return self._attributes[name]
        raise TypeError("There is not such attribute")

    def set_attribute(self, name, value):
        '''Set the attribute name of the vertex to value
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys():
            self._attributes[name] = value 
        else:
            raise TypeError("There is not such attribute")
    def get_adyacents(self):  #SUPONGO QUE ESTE MÉTODO TAMBIÉN HABRÁ QUE QUITARLO
        '''Returns a geneartor over the outcoming adyacent vertices'''
        for element in self._adyacents:
            yield element
    def __str__(self):
        v = ' [' + str(self._attributes['key']) + ','
        v += ' atributos: ' + str(self._attributes )+ '] '
        return v
        
class Graph:
    '''Representation of a simple graph using an adjacency list'''
    def __init__(self):
        '''Create an empty directed graph.'''
        self._vertices_count = 0
        self._edges_count = 0
        self._vertices = dict() # Dictionary of vertices
        self._adyacents = dict() # Adyacency list

        
    def add_vertex(self, vertex:str):
        '''Add a node with the given label to the graph.
        Raise a TypeError exception if the vertex already exists
        '''
        if vertex in self._vertices:
            raise TypeError("Vertex already in the graph")
        else:
            self._vertices[vertex] = Vertex(vertex)
            self._vertices_count += 1
            self._adyacents[vertex]=LinkedList()

    def add_edge_from_to(self, v_from, v_to:str, weight = None):
        if v_from == v_to:
            pass
        elif v_from in self._vertices and v_to in self._vertices:
            linkedlist = self._adyacents[v_from]
            if v_from in self._adyacents:               
                self._adyacents[v_from].add_last(Edge(v_from,v_to,weight))
                self._vertices[v_from].adyacent(v_to)   #está mal, en el if y el else hay lo mismo
            else:
                self._adyacents[v_from].add_last(Edge(v_from,v_to,weight))
                self._vertices[v_from].adyacent(v_to)
            self._edges_count += 1
            self._vertices[v_from].set_attribute("degree",(self._vertices[v_from].get_attribute("degree")+1))                     
        else:
            raise TypeError("There is no such vertex")
    def vertices(self):
        '''Return an iterator over the graph vertices.'''
        for vertice in self._vertices():
            yield vertice   
    def neighbors(self, v):
        '''Returns a genearator over the outgoing edges of the vertex v'''
        for vertice in self._vertices[v].get_adyacents():  #puedo usar directamente la función iter, pero esto viene a ser lo mismo
            yield (vertice) #si quitamos str devolverá el objeto
                
#cuestión del profe:devería volver el objeto vértice en si o solo el nombre del vertice?
#al parecer, nos será util para el futuro devolver el objeto, es una cuestion que quiere que tratemos
    def vertices_count(self)-> int:
        '''Returns the number of vertices in the graph'''
        return self._vertices_count
    def edges_count(self)-> int:
        '''Returns the number of edges in the graph'''
        return self._edges_count
    def get_vertices_attribute(self, name):  
        '''name es un parámetro que debe ser un atributo del diccionario que cada vértice tiene.
        devuelve un diccinario de nombres de vértices(clave) y el atributo que queramos(valor)
        '''
        dic = {}
        for nombres_vertices in self._vertices:
            objeto_vertice = self._vertices[nombres_vertices]
            dic[nombres_vertices] = objeto_vertice._attributes[name]
        return dic
    
            
    def set_vertices_attribute(self, name, value = 'WHITE'):  #creo que name solo puede ser key,degree,color o parent
        '''Set name attribute of vertices to a value
        '''   
        for nombres_vertices in self._vertices:
            self._vertices[nombres_vertices].set_attribute(name,value)
            
            
    def get_vertex_attribute(self, v, name):
        '''Returns the attribute of the vertex v
        Raise TypeError exception if there is no such vertex
        '''
        return self._vertices[v].get_attribute(name)

        
    def set_vertex_attribute(self, v, name, value):
        '''
        Set name attributes of a vertex to a value
        Returns the attribute of the vertex v
        '''
        if v in self._vertices:
            self._vertices[v].set_attribute(name,value)

        
    def __str__(self): #cambiar
        '''Returns the string representation of the graph'''
        h='{'
        for vertex in self._vertices.keys():
            h += f'[{vertex}, adj:{str(self._adyacents[vertex])}]'
        h+= '}'
        return h

        


        
#10.3: Busqueda de anchura
"""from stackarray import Stack

def DFS_iter(G: Graph,vertex:int):
    G.set_vertices_attribute("color","WHITE")
    s = Stack()
    s.push(vertex)
    while s.is_empty() == False:
        v = s.pop()
        if G.get_vertex_attribute(v,"color") == "WHITE":
            G.set_vertex_attribute(v,"color","black")

            for w in G.neighbors(v):
                if G.get_vertex_attribute(w,"color")== "WHITE":
                    G.set_vertex_attribute(w,"parent",v)
                    s.push(w)"""
                    
                    


 
def path_from_to(G:Graph(), v_from, v_to, f):

    if type (G) != Graph:
        raise KeyError("There is no such graph")    
    elif v_from not in G._vertices.keys() or v_from not in G._vertices.keys():
        raise KeyError("Uno de los vertices introducidos no esta presente en el grafo.")
    
    f(G,v_from)
    
    padre_punto = G.get_vertex_attribute(v_to,'parent')
    
    if padre_punto == None:
        print(f'empezamos desde {v_from}, y hacemos el siguiente recorrido:')
    else:
        path_from_to(G,v_from,padre_punto,DFS_iter)
        print(f'de {padre_punto} a {v_to}')




#path_from_to(G,1,5,DFS_iter)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
    
    
#EJERCICIOS 3 Y 4    
    
    

time = 0
def dfs_rec(G:Graph,u):
    global time
    G.set_vertex_attribute(u,"color","gray")
    time += 1
    G.set_vertex_attribute(u,"d",time)
    for w in G.neighbors(u):
        if G.get_vertex_attribute(w,"color")=="white":
            G.set_vertex_attribute(w,"parent",u)
            dfs_rec(G,w)
    time += 1
    G.set_vertex_attribute(u,"f",time)
    G.set_vertex_attribute(u,"color","black")


    
def DFS(G:Graph): 
    '''El algortimo DFS completo e indicando los pasos.El algortimo empieza por el primer vértice que habiamos introducido en el grafo.
    No podemos ordenarle que queremos que empiece por otro vértice. Empezamos poniendo todos los vértices sin padre y con color blanco,
    acaban todos con color negro y con padre(el nodo raíz queda negro pero sin padre).'''
    G.set_vertices_attribute("color", "white") 
    G.set_vertices_attribute("parent","none")

    global time
    time = 0
    for vertice in G._vertices:
        if G.get_vertex_attribute(vertice,"color")=="white":
            dfs_rec(G,vertice)


#EJERCICIO 4

def Tarjan(G:Graph):
    '''En este código del algoritmo de tarjan se pueden distinguir distintas fases o etapas:
    
        1.Aplicamos DFS en el grafo introducido como parámetro.
        
        2.Debemnos crear el grafo traspuesto del grafo introducido como parámetro( como hemos hecho DFS los vertices tienen padres asignados).
        En nuestro caso lo llamamos traspuesto.
        
        3.Fijándonos en el grafo del parámetro, creamos una lista (lista_decr) con los vértices ordenados por su paso final(paso en el que pasan a negro) de forma decreciente.
        En nuestro caso ejemplo nos queda ['A', 'B', 'E', 'D', 'G', 'C', 'F', 'H', 'I'].
        
        4.Detectamos los vértices que van a ser nodos raíces en los grafos resultantes y aplicamos dfs_rec n veces,
        siendo n el numero de vértices nodos raices y de grafos resultantes. 
        NO podemos aplicar DFS debido a que no podemos ordenar por qué vértice debe empezar el algoritmo, por eso cogemos def_rec.
        
        5.Finalmente , creamos el bosque final y les introducimos los vértices y aristas fijándonos
        en traspuesto después de haber ejecutado dfs_rec en él.
        
        
        
        '''
        
    G.set_vertices_attribute("parent","none")   
    DFS(G)
    
    def graph_traspose(G:Graph)-> Graph:
        
        Tras = Graph()
        for vertice in G._vertices:
            Tras.add_vertex(vertice)

        for v in G._adyacents:
            linkedlist= G._adyacents[v]
            for data in linkedlist:  #data viene a ser los datos que se guardan en los nodos de linkedlist (edges)
                fr, to, weight = data.endpoints()
                Tras.add_edge_from_to(to,fr,weight)

        return Tras

    traspuesto = graph_traspose(G)  
    """
    print('Total edges in the graph:', G.edges_count())
    print('Total vertices in the graph:', G.vertices_count())
    print('Total edges in the graph:', traspuesto.edges_count())
    print('Total vertices in the graph:', traspuesto.vertices_count())
    print(traspuesto.get_vertices_attribute('parent'))
    print(G)
    print(G.get_vertices_attribute('f'))"""
    
    #creamos la lista de vértices con el orden decreciente del paso de los vértices
    dic_pasos_clave={}  
    lista_decr=[]
    #self._adyacents pero con claves y valores al revés
    for v in G._adyacents:
        
        paso=G.get_vertex_attribute(v,'f')
        dic_pasos_clave[paso] = v
        
        lista_decr.append(paso)

    lista_decr.sort(reverse=True)

    for i in range(len(lista_decr)):
        lista_decr[i] = dic_pasos_clave[lista_decr[i]]
 


    traspuesto.set_vertices_attribute('color','white')
    
            

    for v in lista_decr:  #hay que tener en cuenta que cuando empieza este bucle todos los vértices estan en blanco, pero hay un dfs_rec() anidado los vértices de lista_decr vas cambiando de color
                          #cuando se encuentre posteriormente con otro vertice en blanco significará que ese no entró en el anterior dfs_rec. Ese será un nodo raíz de otro grafo.

        if traspuesto.get_vertex_attribute(v,'color') == 'white': #de cumplirse esto, hemos dado con un nodo raiz de un grafo del bosque a devolver
            dfs_rec(traspuesto,v)  #asigna los parents que pronto miraremos
    lista_padres = []
    for v in lista_decr:
        if traspuesto.get_vertex_attribute(v,"parent") == None:
            lista_padres.append(v)

    i = -1
    lista_scc=[]
    for vertice  in lista_decr:
        if vertice not in lista_padres:
            lista_scc[i].append(vertice)
        else:
            i+=1   
            lista_scc.insert(i,[])
            lista_scc[i].insert(i,vertice)

    

    """    for v_padre in bosque_final:  #ahora nos centraremos en llenar estos grafos de sus correspondientes vértices y aristas
        vertices_colocados = [v_padre]

        for i in range(traspuesto.edges_count()): #este bucle es necesario debido a que, sin él, es posible que hicisemos la comprobación de un vértice cuyo padre
                                                  #aun no esté situado,por lo que tenemos que hacer la comprobación más veces.
            
            for v in traspuesto._adyacents:
                
                if traspuesto.get_vertex_attribute(v,'parent') in vertices_colocados:  #solo añadimos el vértice si ya hemos añadido a su padre al grafo resultante
                    v_from = traspuesto.get_vertex_attribute(v,'parent')               #(y por tanto a la lista vertices_colocados).Recordemos que el vértice original ya
                                                                                       #lo habíamos colocado a la hora de crear la instancia del grafo resultante.
                    if v not in bosque_final[v_padre]._adyacents:    
                        
                        bosque_final[v_padre].add_vertex(v)
                        bosque_final[v_padre].add_edge_from_to(v_from,v)  #Una vez dentro los véritces padre e hijo,colocamos arista
                        vertices_colocados.append(v)                      #No tiene peso ya que no lo usamos"""
    return lista_scc                                               #finalmente devolvemos la lista, formada por distintas listas de SCC

def Erdos_renyi(G:Graph,h:int): #recibe un grafo vacío con n vertices
    n = G._vertices_count 
    if h >= n: #calcula la probabilidad de que dos verticces estén conectados.
        p = h/n
    else:
        p = h/n
    for vertice1 in G._vertices:
        for vertice2 in G._vertices:
            if random.random() < p:
                G.add_edge_from_to(vertice1,vertice2)

                
    
if __name__ == '__main__':
    G = Graph()
    H = Graph()
    I = Graph()
    J = Graph()
    for letra in ['A','B','C','D','E','F','G','H','I']:
        G.add_vertex(letra)
        H.add_vertex(letra)
        I.add_vertex(letra)
        J.add_vertex(letra)
    # add edges
    G.add_edge_from_to('A', 'B', 1)
    G.add_edge_from_to('B', 'C', 1)
    G.add_edge_from_to('C', 'F', 1)
    G.add_edge_from_to('F', 'H', 1)
    G.add_edge_from_to('H', 'I', 1)
    G.add_edge_from_to('E', 'D', 1)
    G.add_edge_from_to('E', 'A', 1)
    G.add_edge_from_to('D', 'B', 1)
    G.add_edge_from_to('B', 'E', 1)
    G.add_edge_from_to('G', 'E', 1)
    G.add_edge_from_to('D', 'G', 1)
    G.add_edge_from_to('I', 'F', 1)
    

    bosque_final=Tarjan(G)  #el SCC formado por A,E,G,B,D 
    Erdos_renyi(H,(5))
    Erdos_renyi(I,(1))
    Erdos_renyi(J,(1.5))
    
