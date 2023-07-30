% Hechos
    carretera(cordoba,granada).
    carretera(cordoba,jaen).
    carretera(cordoba,malaga).
    carretera(cordoba,sevilla).
    carretera(sevilla,cadiz).
    carretera(sevilla,huelva).
    carretera(sevilla,malaga).
% Reglas
    conectado(Origen,Destino):- 
        carretera(Origen, Destino).
        !. % cut operator
    conectado(Origen,Destino):-  
        carretera(Origen,Intermedio), conectado(Intermedio,Destino).

main :- print("inicio-carreteras").

/* Ejemplos de consultas

Como hemos usado el operador !, podríamos ejecutar: 

    ?- conectado(sevilla,cadiz).        Pulsando "enter" 
    true.

    ?- trace, conectado(sevilla,cadiz).
    Call: (11) conectado(sevilla, cadiz) ? creep
    Call: (12) carretera(sevilla, cadiz) ? creep
    Exit: (12) carretera(sevilla, cadiz) ? creep
    Exit: (11) conectado(sevilla, cadiz) ? creep
    true.

Si no hubiéramos usado el operador !, como en "1-inicio-carreteras.pl"

    ?- conectado(sevilla,cadiz).        Pulsando "enter" 2 veces
    true .

    ?- conectado(sevilla,cadiz).        Pulsando ; tras cada solución
    true ;
    false.

    ?- trace, conectado(sevilla,cadiz).
    Call: (11) conectado(sevilla, cadiz) ? creep
    Call: (12) carretera(sevilla, cadiz) ? creep
    Exit: (12) carretera(sevilla, cadiz) ? creep
    Exit: (11) conectado(sevilla, cadiz) ? creep
    true ;
    Redo: (11) conectado(sevilla, cadiz) ? creep
    Call: (12) carretera(sevilla, _14506) ? creep
    Exit: (12) carretera(sevilla, cadiz) ? creep
    Call: (12) conectado(cadiz, cadiz) ? creep
    Call: (13) carretera(cadiz, cadiz) ? creep
    Fail: (13) carretera(cadiz, cadiz) ? creep
    Redo: (12) conectado(cadiz, cadiz) ? creep
    Call: (13) carretera(cadiz, _19368) ? creep
    Fail: (13) carretera(cadiz, _19368) ? creep
    Fail: (12) conectado(cadiz, cadiz) ? creep
    Redo: (12) carretera(sevilla, _14506) ? creep
    Exit: (12) carretera(sevilla, huelva) ? creep
    Call: (12) conectado(huelva, cadiz) ? creep
    Call: (13) carretera(huelva, cadiz) ? creep
    Fail: (13) carretera(huelva, cadiz) ? creep
    Redo: (12) conectado(huelva, cadiz) ? creep
    Call: (13) carretera(huelva, _26660) ? creep
    Fail: (13) carretera(huelva, _26660) ? creep
    Fail: (12) conectado(huelva, cadiz) ? creep
    Redo: (12) carretera(sevilla, _14506) ? creep
    Exit: (12) carretera(sevilla, malaga) ? creep
    Call: (12) conectado(malaga, cadiz) ? creep
    Call: (13) carretera(malaga, cadiz) ? creep
    Fail: (13) carretera(malaga, cadiz) ? creep
    Redo: (12) conectado(malaga, cadiz) ? creep
    Call: (13) carretera(malaga, _2456) ? creep
    Fail: (13) carretera(malaga, _2456) ? creep
    Fail: (12) conectado(malaga, cadiz) ? creep
    Fail: (11) conectado(sevilla, cadiz) ? creep
    false.

*/
