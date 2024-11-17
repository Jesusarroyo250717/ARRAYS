#2. Sumar todos los elementos de un array
#Crea un programa que tome una lista de números y calcule la suma de todos sus elementos

numeros=[5,7,5,1,6,9,2,4]
suma=0 #almacena el numero
for i in numeros:
    suma+=i #esta sumando (suma=0) con el 1er numero(5)
print("La suma es: ", suma)