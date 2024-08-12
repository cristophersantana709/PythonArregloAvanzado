Palabras = ["HOLA","COMO","HOLA","QUIEN","HOLA"]
Palabra_a_contar="HOLA"
contador=0
for palabra in Palabras:
 if palabra == Palabra_a_contar:
    contador += 1
# Mostrar el número de veces que aparece el valor
print(f"El número {Palabra_a_contar} aparece {contador} veces en el arreglo.")