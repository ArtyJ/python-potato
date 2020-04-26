# in, not in

# if __name__ == '__main__':
my_pet = 'dog'
your_pet = 'cat'
animals = ('dog','rabbit','elephant')

if (my_pet in animals):
    print(f"my pet,{my_pet},is in all animals,{animals}")
else:
    print(f'"my pet,{my_pet},is not in all animals,{animals}"')

if (your_pet not in animals):
    print(f'your pet,({your_pet}),is not in all animals,{animals}')
else:
    print(f'your pet,({your_pet}),is in all animals,{animals}')