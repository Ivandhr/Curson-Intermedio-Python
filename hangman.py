import random, os


def read():
    with open('./files/data.txt', 'r', encoding="latin-1") as f:
        words = [line.strip('\n') for line in f]
        dict_words = {key:value for key, value in enumerate(words)}
        return dict_words

def normalized(s):
    replacement = (('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'))    
    for a, b in replacement:
        s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
        
def run():
    os.system('cls')
    dict_words = read()
    # print(dict_words)
    random_word = dict_words.get(random.randint(1, len(dict_words) + 1))
    print(random_word)
    normal_word = normalized(random_word)
    print(normal_word)


if __name__ == '__main__':
    run()