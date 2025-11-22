def lista_codwa(x):
    lista=[]
    for i in range(x):
        lista.append(i)
    lista_2 = lista[::2]
    print(lista_2)
lista_codwa(10)