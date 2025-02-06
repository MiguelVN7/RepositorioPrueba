nombre = input('Bienvenido al programa de prueba, por favor ingrese su nombre: ')

respuesta = int(input('Hola ' + nombre + ', por favor ingrese 1 si desea continuar o 0 si desea terminar: '))
while(respuesta != 0):
    print('Ha decidido continuar con el programa')
    respuesta = int(input('Por favor ingrese 1 si desea continuar o 0 si desea terminar: '))

print('Ha decidido terminar el programa')
