DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Python developers using comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print('--------------------------------------')
    print('Python developers using comprehensions')
    print('--------------------------------------')

    for worker in all_python_devs:
        print(worker)

    # Python developers using high order functions
    all_python_dev = list(filter(lambda worker: worker['language'] == 'python', DATA))

    print('--------------------------------------------')
    print('Python developers using high order functions')
    print('--------------------------------------------')
    for worker in all_python_devs:
        print(worker)


    # Platzi workers using comprehensions
    all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print('-----------------------------------')
    print('Platzi workers using comprehensions')
    print('-----------------------------------')

    for worker in all_Platzi_workers:
        print(worker)
    
    # Platzi workers using high order functions
    all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    print('-----------------------------------------')
    print('Platzi workers using high order functions')
    print('-----------------------------------------')

    for worker in all_Platzi_workers:
        print(worker['name'])


    # Adult workers using comprehensions
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print('----------------------------------')
    print('Adult workers using comprehensions')
    print('----------------------------------')

    for worker in adults:
        print(worker)

    # Adult workers using high order functions
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print('----------------------------------------')
    print('Adult workers using high order functions')
    print('----------------------------------------')
    
    for worker in adults:
        print(worker)

    # Old people using high order functions
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    # old_people = list(map(lambda worker: worker['old'], old_people))
    print('-----------------------------------------------------------')
    print('Old people using high order functions; adding new key (old)')
    print('-----------------------------------------------------------')

    for worker in old_people:
        print(f'{worker["name"]}, is an elder person? {worker["old"]}')


    # Old people using comprehension
    old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]

    print('-----------------------------------------------------------')
    print('Old people using comprehension; adding new key (old)')
    print('-----------------------------------------------------------')
    for worker in old_people:
        print(f'{worker["name"]}, is an elder person? {worker["old"]}')
        
if __name__ == '__main__':
    run()