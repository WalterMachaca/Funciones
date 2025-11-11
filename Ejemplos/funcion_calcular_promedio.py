def calcular_promedio(lista):
    if len(lista)==0:
        return 0
    suma=sum(lista)
    promedio=suma/len(lista)
    return promedio
print(calcular_promedio([1,2,3,4,5,6,7,8,-5,-6,9]))
print(calcular_promedio([]))
    