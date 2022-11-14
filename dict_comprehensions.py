def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}             
    print()
    print(f'El diccionario de cubos es = {my_dict}')

    # Reto: crear, con un dictionary comprehension, un diccionario
    # cuyas llaves sean los 1000 primeros números naturales con sus
    # raices cuadradas como valores.
    challege = {i:round(i**0.5,2) for i in range(1, 1001)}

    print()
    print(f'El diccionario del reto es = {challege}')
    print()
if __name__ == '__main__':
    run()