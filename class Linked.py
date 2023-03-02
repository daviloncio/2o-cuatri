class LinkedVertex:
    def __init__(self, vertex):
        self._adyacents = {} # store the labels of its adyacent vertices
        self._attributes = {'key' : vertex,
                'degree' : 0, # vertex degree
                'color' : 'WHITE', # to mark nodes
                'parent' : None } # to the dfs-tree
    def add_adyacent(self,v,weight):
        
        if type(v) == LinkedVertex():
            self._adyacents[v]=weight
            valor=self._attributes['degree']
            self._attributes['degree']=valor+1
        else:
            raise TypeError("there is no vertex named" + v)

    def get_attribute(self, name):
        '''Returns the attribute name of the vertex
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes:
            return self._attributes[name]
        else:
            raise TypeError("There is not such attribute")
    def set_attribute(self, name, value = None):
        '''Set the attribute name of the vertex to value
        Raise TypeError exception if there is no such attribute
        '''
        pass
    def get_adyacents(self):
        '''Returns a geneartor over the outcoming adyacent vertices'''
        pass
    def __str__(self):
        v = '[' + str(self._attributes['key']) + ','
        v += ' adj: ' + str(self._adyacents) + ']'
        return v
    

class Graph:
    def __init__(self):
        '''Create an empty directed graph.'''
        self._vertices_count = 0
        self._edges_count = 0
        self._vertices = dict() # Dictionary of vertices
    def add_vertex(self, vertex):
        '''Add a node with the given label to the graph.
        Raise a TypeError exception if the vertex already exists
        '''
        if vertex in self._vertices:
            raise TypeError("Vertex already in the graph")
        else:
            self._vertices[vertex]=LinkedVertex(vertex)
            self._vertices_count += 1

    def add_edge_from_to(self, v_from, v_to, weight = None):
        if type(v_from) and type(v_to) == LinkedVertex():
            v_from.add_adyacent(v_to,weight)
            self._edges_count += 1
        else:
            raise TypeError("There is no such vertex")
    def vertices(self):
        '''Return an iterator over the graph vertices.'''
        for vertice in self._vertices:
            print(vertice)
        pass
    def neighbors(self, v):
        '''Returns a genearator over the outgoing edges of the vertex v'''
        if type(v) != LinkedVertex:
            raise TypeError('there is not such vertex')
        
        
        
        pass
    def vertices_count(self):
        '''Returns the number of vertices in the graph'''
        return self._vertices_count
    def edges_count(self):
        '''Returns the number of edges in the graph'''
        return self._edges_count
    def get_vertices_attribute(self, name):  #debe devolver un diccionario con clave(nombre vertice) y valor debe ser otro diccionario
        '''Get vertices attribute from graph
            Returns:
            Dictionary of attributes keyed by vertex name.  '''
        return self._vertices
    def set_vertices_attribute(self, name, value = 'WHITE'):
        '''Set name attribute of vertices to a value
        '''
        #modificar el atributo??
        pass