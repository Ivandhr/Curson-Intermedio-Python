def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print()
    print(f'La lista de cuadrados es = {squares}')

    # Reto: crear, con un list comprehension, una lista de 
    # todos los múltiplos de 4 que a la vez también son 
    # múltiplos de 6 y de 9, hasta 5 dígitos.
    challege = [i for i in range(1, 100000) if i % 4 == 0 if i % 6 == 0 if i % 9 == 0 
                if len(str(i)) < 6]
    
    print()
    print(f'La lista del reto es = {challege}')
    print()

if __name__ == '__main__':
    run()

