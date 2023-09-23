
%logica1confallo->relacion trace y arbol de ejecucion
% Hechos
    carretera(cordoba,granada,200).
    carretera(cordoba,jaen,100).
    carretera(cordoba,malaga,150).
    carretera(cordoba,sevilla,140).
    carretera(sevilla,cadiz,200).
    carretera(sevilla,huelva,100).
    carretera(sevilla,malaga,100).

  
% Reglas

%redefinimos esta regla para la funcion distancia



distancia(Origen,Destino,X):-carretera(Origen,Destino,X).
distancia(Origen,Destino,X):-carretera(Destino,Origen,X).
%si no ha funcionado ninguna de las anteriores,entonces las conectan dos carreteras
%sea como sea,pasaremos o por cordoba o por sevilla
distancia(Origen,Destino,X):- %caso pasamos por cordoba
    carretera(cordoba,Origen,Y),carretera(cordoba,Destino,Z),X is Y+Z.

distancia(Origen,Destino,X):-%caso pasamos por sevilla
    carretera(sevilla,Origen,Y),carretera(sevilla,Destino,Z),X is Y+Z.

distancia(Origen,Destino,X):-%caso pasamos por cordoba-sevilla
    carretera(cordoba,sevilla,W),carretera(cordoba,Origen,Y),carretera(sevilla,Destino,Z),X is Y+Z+W.

distancia(Origen,Destino,X):-%caso pasamos por cordoba-sevilla
    carretera(cordoba,sevilla,W),carretera(sevilla,Origen,Y),carretera(cordoba,Destino,Z),X is Y+Z+W.


%A CONTINUACIÓN ESCRIBIMOS LAS REGLAS QUE NOS AYUDARÁN A HACER EL FILTRADO Y 
%ELIMINAR DE DISTANCIAS AQUELLAS DISTANCIAS QUE 
%TENGAN LAS MISMAS CIUDADES DE ORIGEN Y DESTINO

primer_y_segundos_iguales([X,X|_]).

%LA FUNCION EXCLUDE DEJA FUERA AQUELLAS LISTAS QUE CUMPLAN LA ANTERIOR REGLA.


eliminar_iguales(Distancias, ListaFinal):- exclude(primer_y_segundos_iguales,Distancias, ListaFinal).

distancias_sin_filtrado(Origen,Destino,Distancias):- 
findall([Origen,Destino,Distancia], distancia(Origen,Destino,Distancia), Distancias).

distancias_con_filtrado(Origen, Destino, ListaFinal) :-
    distancias_sin_filtrado(Origen, Destino, Distancias),
    eliminar_iguales(Distancias, ListaFinal),
    write(ListaFinal).


main :- print("inicio-carreteras").
