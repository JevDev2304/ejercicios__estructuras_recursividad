listaejemplo = [1, 3 , 7 , "Juanes", 19, 24]
listaordenada = [10, 20 ,30 , 40 , 50 , 60, 70 ,80, 90,120, 137, 147, 900, 935400]
#Función recursiva para imprimir los números de 1 hasta n
def imprimirunoan(n):
    if n == 1:
        print(n)
        print("Se acabo la funcion imprimir uno a n \n")
        return True
    else:
        print(n)
        return imprimirunoan(n-1)

#Imprimir todos los elementos de una lista
def imprimirelementolista(lista):
    if len(lista)== 0:
        print("Se acabo la funcion imprimir elemento lista\n")
        return None
    else:
        print(lista[0])
        imprimirelementolista(lista[1:])
#Factorial
def factorial(n):
    if n == 0:
        print("Se acabo la funcion factorial")
        return 1
    elif n == 1 :
        print("Se acabo la funcion factorial")
        return 1
    else:
        return n * factorial(n-1)
#Sucesion de fibonacci
def fibonacci(sucesion):
    if sucesion == 0:
        return 0
    if sucesion == 1:
        return 1
    else:
        return fibonacci(sucesion-2)+fibonacci(sucesion-1)
def contarelementoslista(lista):
    if len(lista) == 0:
        print("Se acabo la funcion contarelementos")
        return 0
    else:
        return 1+contarelementoslista(lista[1:])
#Dada una lista l, diga si un elemento e está en la lista o no. (Recursivo)
def estaelementoenlista(lista,e):
    if lista[0] == e:
        print("El elemento e esta en la lista ")
        return True
    elif lista == []:
        return estaelementoenlista(lista[1:],e)
    else:
        print("El elemento e no esta en la lista")
        return False
def busquedabinaria(listaordenada, valor):
    if (valor>listaordenada[len(listaordenada)//2]):
        eliminar = (len(listaordenada)//2)
        return busquedabinaria(listaordenada[eliminar:],valor)
    elif (valor>listaordenada[len(listaordenada)//2]):
        eliminar = (len(listaordenada)//2)
        return busquedabinaria(listaordenada[:eliminar],valor)
    else:
        print(f"El valor encontrado es  {valor}")
        return True















if __name__ == '__main__':
   imprimirunoan(10)
   imprimirelementolista(listaejemplo)
   resultado = factorial(14)
   print("El resultado de la  función factorial de 14 es "+ str(resultado))
   resultadofibonacci = fibonacci(4)
   print("El resultado de la  función fibonacci en la cuarta sucesion es " + str(resultadofibonacci))
   resultadocontarlista = contarelementoslista(listaejemplo)
   print("El numero de elementos en la lista es " + str(resultadocontarlista))
   estaelementoenlista(listaejemplo,"Juane")
   busquedabinaria(listaordenada,147)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
