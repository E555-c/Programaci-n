#En este cogigo el usuario puede interactuar con la computadora, ya que le pregunta los datos para saber la area de un trinagulo
#Se definen las 2 variables
#Cuando lo mandamos a imprimir hacemos la operacion con un string para saber la longitud de la operacion 

print("Base de un Triangulo")
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingresa la altura del tirangulo: "))

print("El area del trinagulo es: " + str(base*altura/2))
