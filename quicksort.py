import random


class OrdenacaoRapida():
    def quicksort(arr):
        if len(arr) < 2:
            return arr
        else:
            pivo = arr[0]
            menores = [i for i in arr[1:] if i <= pivo]
            maiores = [i for i in arr[1:] if i > pivo]
        return OrdenacaoRapida.quicksort(menores) + [pivo] + OrdenacaoRapida.quicksort(maiores)
    

inicio = 0
maximo = 100
numero_elementos = 10

meu_array = [random.randint(inicio, maximo) for _ in range(numero_elementos)]


print(meu_array)
print(40 * '____')
print(OrdenacaoRapida.quicksort(meu_array))


