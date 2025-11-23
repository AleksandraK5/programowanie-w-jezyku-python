def lista_parzyste(x):
    for i in x:
         if i % 2 == 0:
           print(i)
lista = list(range(0,10))
lista_parzyste(lista)