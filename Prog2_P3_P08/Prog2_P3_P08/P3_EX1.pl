%logica1confallo->relacion trace y arbol de ejecucion
% Hechos
carretera(cordoba,granada).
carretera(cordoba,jaen).
carretera(cordoba,malaga).
carretera(cordoba,sevilla). 
carretera(sevilla,cadiz).
carretera(sevilla,huelva).
carretera(sevilla,malaga).
% Reglas
conectado(Origen, Destino) :-
    carretera(Origen, Destino).
conectado(Origen, Destino) :-
    carretera(Destino, Origen).
conectado(Origen, Destino) :-
    \+ carretera(Origen, Destino),
    \+ carretera(Destino, Origen),
    conectado_indirecto(Origen, Destino, [Origen]).


conectado_por(Origen, Destino, Intermedio) :-
    conectado_indirecto(Origen, Destino, [Origen|Intermedio]),
    \+ member(Destino, Intermedio).


conectado_indirecto(Origen, Destino, Visitados) :-
    carretera(Origen, Destino),
    \+ member(Destino, Visitados).

conectado_indirecto(Origen, Destino, Visitados) :-
    carretera(Origen, Intermedio),
    \+ member(Intermedio, Visitados),
    conectado_indirecto(Intermedio, Destino, [Origen | Visitados]).

conectado_indirecto(Origen, Destino, Visitados) :-
    carretera(Intermedio, Origen),
    \+ member(Intermedio, Visitados),
    conectado_indirecto(Intermedio, Destino, [Origen | Visitados]).

ruta(Origen, Destino, Ruta) :-
    ruta_auxiliar(Origen, Destino, [Origen], Ruta).

ruta_auxiliar(Origen, Destino, Visitados, [Origen, Destino]) :-
    carretera(Origen, Destino).

ruta_auxiliar(Origen, Destino, Visitados, [Origen | Ruta]) :-
    carretera(Origen, Intermedio),
    \+ member(Intermedio, Visitados),
    ruta_auxiliar(Intermedio, Destino, [Intermedio | Visitados], Ruta).

