def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacía')
        else:
            None
        return string  == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    word = input('Ingrese una palabra: ')
    print(word)
    try:
        print(palindrome(word))
    except TypeError:
        print('Solo se pueden ingresar strings')

        
if __name__ == '__main__':
    run()