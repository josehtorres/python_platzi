import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Digite un numero del 1 al 100:'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un Numero mas grande')
        else:
            print('Busca un Numero mas pequeno')
        numero_elegido = int(input('Elije otro numero:'))
    print('!Ganaste!')


if __name__ == '__main__':
    run()

