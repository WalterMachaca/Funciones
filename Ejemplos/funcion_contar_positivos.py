def contar_positivos(lista):
    contador=0
    for numero in lista:
        if numero>0:
            contador=contador+1
    return contador
lista1=[-3,2,-1,8,3,5,6,4,8,5,652,65,35,84,75,-2,0,35,5]
print(contar_positivos(lista1))
 
