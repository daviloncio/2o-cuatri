from stackarray import *
from queue import *
#Se debe tener la clase pila guardada como queue. En caso de no tenerse, sustituir from queue import * por la clase pila de el notebook de teoria
#ejercicio 8


class LinkedVertex:
    def __init__(self, vertex:str):
        self._adyacents = {} # store the labels of its adyacent vertices
        self._attributes = {'key' : vertex,
                'degree' : 0, # vertex degree
                'color' : 'WHITE', # to mark nodes
                'parent' : None } # to the dfs-tree
    def add_adyacent(self,v,weight):
        
        if type(v) == LinkedVertex():
            self._adyacents[v] = weight
            valor = self._attributes['degree']
            self._attributes['degree'] = valor+1
        else:
            raise TypeError("there is no vertex named" + v)
    def exists_adyacent(self, v):
        '''Return True if v is adyacent otherwise return False'''
        if v in self._adyacents:
            return True
        
        return False
    def get_attribute(self, name):
        '''Returns the attribute name of the vertex
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys:
            return self._attributes(name)
        
        raise TypeError("There is not such attribute")

    def set_attribute(self, name, value):
        '''Set the attribute name of the vertex to value
        Raise TypeError exception if there is no such attribute
        '''
        if name in self._attributes.keys:
            self._attributes[name] = value
        else:
            raise TypeError("There is not such attribute")
    def get_adyacents(self):  #??
        '''Returns a geneartor over the outcoming adyacent vertices'''
        for element in self._adyacents:
            yield element
    def __str__(self):
        v = ' [' + str(self._attributes['key']) + ','
        v += ' atributos: ' + str(self._attributes )+ '] '
        return v
    

    
#ejercicio 9s
class Graph:
    def __init__(self):
        '''Create an empty directed graph.'''
        self._vertices_count = 0
        self._edges_count = 0
        self._vertices = dict() # Dictionary of vertices    clave:vertex(str) valor:objeto vértice
    def add_vertex(self, vertex:str):
        '''Add a node with the given label to the graph.
        Raise a TypeError exception if the vertex already exists
        '''
        if vertex in self._vertices:
            raise TypeError("Vertex already in the graph")
        else:
            self._vertices[vertex] = LinkedVertex(vertex)
            self._vertices_count += 1

    def add_edge_from_to(self, v_from: LinkedVertex, v_to: LinkedVertex, weight = None):  #david tio recuerda que un edge es una arista
        if type(v_from) and type(v_to) == LinkedVertex():
            v_from.add_adyacent(v_to,weight)
            self._edges_count += 1
            
        else:
            raise TypeError("There is no such vertex")
    def vertices(self):
        '''Return an iterator over the graph vertices.'''
        for vertice in self._vertices:
            yield vertice
    def neighbors(self, v:LinkedVertex):
        '''Returns a genearator over the outgoing edges of the vertex v'''
        if type(v) != LinkedVertex():
            raise TypeError('there is not such vertex')
        else:
            for vertice in v._adyacents:  #puedo usar directamente la función iter, pero esto viene a ser lo mismo
                yield str(vertice) #si quitamos str devolverá el objeto
                
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
        if name in LinkedVertex()._attributes.keys():
            dic = {}
            for nombres_vertices in self._vertices:
                 
                objeto_vertice = self._vertices[nombres_vertices]
                dic[nombres_vertices] = objeto_vertice._attributes[name]

            return dic
        else:
            raise TypeError('atributo del vértice mal introducido')
            
    def set_vertices_attribute(self, name, value = 'white'):  #creo que name solo puede ser key,degree,color o parent
        '''Set name attribute of vertices to a value
        '''
        if name in LinkedVertex()._attributes.keys():
            
            for nombres_vertices in self._vertices:
                 
                nombres_vertices.set_attribute(name,value)
            
        else:
            raise TypeError('atributo del vértice mal introducido')
            
    def get_vertex_attribute(self, v, name):
        '''Returns the attribute of the vertex v
        Raise TypeError exception if there is no such vertex
        '''
        if v in self._vertices:
            return  v.get_attribute(name)
        else: 
            raise TypeError("There is no such vertex")
        
    def set_vertex_attribute(self, v, name, value):
        '''
        Set name attributes of a vertex to a value
        Returns the attribute of the vertex v
        '''
        if v in self._vertices and  name in LinkedVertex()._attributes.keys():
            
            v.set_attribute(name,value)
        else: 
            raise TypeError("There is no such vertex")
        
    def __str__(self):
        '''Returns the string representation of the graph'''
        g = 'Este grafo esta formado por:\n'
        for i in self._vertices:
            g += str(self._vertices[i])+'\n'
        return g
    
g = Graph()
#EJERCICIO 10
#10.1: Busqueda en profundidad usando la pila

def DFS_iter(G: Graph,vertex: LinkedVertex):
    if type (G) != Graph:
        raise KeyError("There is no such graph")
    elif type(vertex) != LinkedVertex:
        raise KeyError("There is no such vertex")
    else:
        G.set_vertices_attribute("color","white")
        s = Stack()
        s.push(vertex)
        while s.is_empty == False:
            v = s.pop()
            if G.get_vertex_attribute(v,"color") == "white":
                G.set_vertex_attribute(v,"color","black")
                for w in G.neighbors(vertex):
                    if G.get_vertex_attribute(w,"color")== "white":
                        G.set_vertex_attribute(w,"parent",v)
                        s.push(w)

#10.2: Busqueda en profundidad recursivo

def DFS_rec(G: Graph,v: LinkedVertex):
    if type (G) != Graph:
        raise KeyError("There is no such graph")
    elif type(v) != LinkedVertex:
        raise KeyError("There is no such vertex")
    else:
        G.set_vertex_attribute(v,"color","grey")
        for w in G.neighbors(v):
            if G.get_vertex_attribute(w,"color")== "white":
                G.set_vertex_attribute(w,"parent",v)
                DFS_rec(G,w)
        G.set_vertex_attribute(v,"color","black")
        
        
##Si se quiere ejecutar este algoritmo más de una vez, descomentar la siguiente linea
#graph.set_vertices_attribute("color","white") #donde graph es el grafo que sobre el que se desea implementar el alogritmo

      
#10.3: Busqueda de anchura
def BFS(G: Graph,v: LinkedVertex):
    if type (G) != Graph:
        raise KeyError("There is no such graph")
    elif type(v) != LinkedVertex:
        raise KeyError("There is no such vertex")
    else:
        G.set_vertices_attribute("color","white")
        q = Queue()
        q.enqueue(v)
        while q.is_empty == False:
            v.deque
            for w in G.neighbors(v):
                if g.get_vertex_attribute(w,"color")== "white":
                    G.set_vertex_attribute(w,"color","grey")
                    G.set_vertex_attribute(w,"parent",v)
                    q.enqueue(w)
            G.set_vertex_attribute(w,"color","black")
                    
