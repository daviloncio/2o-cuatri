lista_decr = [1,2,3]
dic_pasos_clave = {1:100,2:200,3:300}

for i in range(len(lista_decr)):
    lista_decr[i] = dic_pasos_clave[lista_decr[i]]


print(dic_pasos_clave)
print(lista_decr)