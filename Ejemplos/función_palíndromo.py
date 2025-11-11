def es_palíndromo(palabra):
    palabra=palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra==palabra_invertida:
        return "Es palíndromo"
    else:
        return "No es palíndromo"
print(es_palíndromo("REConocer"))
print(es_palíndromo("hola"))
