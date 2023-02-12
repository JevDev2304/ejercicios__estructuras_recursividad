listaejemplo = [1, 3 , 7 , "Juanes", 19, 24]
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
def fibonacci(sucesion):
    if sucesion == 0:
        return 0
    if sucesion == 1:
        return 1
    else:
        return fibonacci(sucesion-2)+fibonacci(sucesion-1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   imprimirunoan(10)
   imprimirelementolista(listaejemplo)
   resultado = factorial(14)
   print("El resultado de la  función factorial de 14 es "+ str(resultado))
   resultadofibonacci = fibonacci(4)
   print("El resultado de la  función fibonacci en la cuarta sucesion es " + str(resultadofibonacci))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
