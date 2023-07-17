# def imprimir_mensaje():
#    print("Mensaje Especial")
#    print('Estoy aprendiendo a utilizar funciones')

#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()


def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('Adios')

opcion = int(input('Elije una Opcion (1, 2, 3):'))

if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
else:
    print('Elija una opcion correcta')
