def divisors(num):
    #divisors = []
    #for i in range(1, num + 1):
    #    if num % i == 0:
    #        divisors.append(i)
    try:
        if num < 0:
            raise ValueError('Debes ingrear un número negativo')
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False
        

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Termino la ejecución del programa')
    except:
        print('Debes ingrear un número.')


if __name__ == '__main__':
    run()