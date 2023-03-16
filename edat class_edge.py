class Edge:
    def __init__(self, from_, to_, weight = None):
        self._from = from_
        self._to = to_
        self._weight = weight
    def endpoints(self):
        return (self._from, self._to, self._weight)
    def __str__(self) -> str:
        
        return f'arista de peso {self._weight} que va desde {self._from} hasta {self._to}'
    
x = Edge(1,2,3)
print(x)

class Vertex:
    def __init__(self, vertex): 
        
        self._attributes = {'key' : vertex,
        'd' : 0, # discover time DFS  #supongo que modificaremos estos valores a la hora de hacer el set_attribute para cambiar el color.
        'f' : 0, # finalization DFS
        'degree' : 0, # vertex degree
        'color' : 'WHITE', # to mark nodes
        'parent' : None } # to the dfs-tree+
        
    def add_adyacent(self,v:str,weight:str=0):
        #ahora los vecinos de los vértices los definimos en la clase Graph, 
        #por lo que creo que hay q devolver en add_adyacent un objeto Edge para guardarlo posteriormente en el diccionario de grafo.
        #Graph.add_edge from_to() accederá a esta función
        arista = Edge(self._attributes['key'],v,weight)
        return arista
    
    def exists_adyacent(self, v):
        '''Return True if v is adyacent otherwise return False'''
        #como coño vamos a revisar sus vecinos si los tenemos guardados en la clase grafo???
        #creo que probable que sea uno de los métodos que hay q eliminar
        if v in self._adyacents:
            return True
        
        return False
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
            self._vertices[vertex] = LinkedVertex(vertex)
            self._vertices_count += 1

    def add_edge_from_to(self, v_from, v_to:str, weight = None):  #david tio recuerda que un edge es una arista
        if v_from in self._vertices and v_to in self._vertices:
            self._vertices[v_from].add_adyacent(v_to,weight)
            self._edges_count += 1
            
            
        else:
            raise TypeError("There is no such vertex")
    def vertices(self):
        '''Return an iterator over the graph vertices.'''
        for vertice in self._vertices():
            yield vertice   
    def neighbors(self, v):
        '''Returns a genearator over the outgoing edges of the vertex v'''
        for vertice in self._vertices[v]._adyacents.keys():  #puedo usar directamente la función iter, pero esto viene a ser lo mismo
            yield (vertice) #si quitamos str devolverá el objeto
                
#cuestión del profe:devería volver el objeto vértice en si o solo el nombre del vertice?
#al parecer, nos será util para el futuro devolver el objeto, es una cuestion que quiere que tratemos
    def vertices_count(self):
        '''Returns the number of vertices in the graph'''
        return self._vertices_count
    def edges_count(self):
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

        
    def __str__(self):
        '''Returns the string representation of the graph'''
        g = 'Este grafo esta formado por:\n'
        for i in self._vertices:
            g += str(self._vertices[i])+'\n'
        return g
        





if __name__ == '__main__':
    G = Graph()


    for i in range(1, 4):
        G.add_vertex(i)
    # add edges
    G.add_edge_from_to(1, 2, 10)
    G.add_edge_from_to(1, 3, 5)
    G.add_edge_from_to(2, 3, 6)
    G.add_edge_from_to(3, 2, 1)
    print('Total edges in the graph:', G.edges_count())
    print('Total vertices in the graph:', G.vertices_count())
    print('\nPrint graph:\n', G)
    atr = 'degree'
    print(f'\n Attribute {atr} of vertices:\n {G.get_vertices_attribute(atr)}')
