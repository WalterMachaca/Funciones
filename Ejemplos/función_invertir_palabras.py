def invertir_palabras(frase):
    palabras=frase.split()
    palabras_invertidas=palabras[::-1]
    frase_invertida=" ".join(palabras_invertidas)
    return frase_invertida
print (invertir_palabras("Las funciones ahorran espacio de memoria en el código"))