import time

def print_with_delay(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Short skit
print_with_delay("Hey you're finally awake. Welcome to the world of pokemons \nPlease enter a name to start your journey.")

name = input('Enter your name: ')

if name == 'Amit' or name == 'amit':
    print_with_delay('\nThis character is not allowed to play here.\nHe has abused some cheat power.')
    exit()
else:
    print_with_delay(f'\nWelcome, {name}!')
    time.sleep(2)

menu_greeting = '\nWell then, ' + name + (', today you will be choosing the 3 pokemons y'
                                          'ou will be starting with \nCharmander\nBulbasaur\nSquirtle\n')

print_with_delay(menu_greeting)
your_pokemon_choice = (input('Which pokemon do you want: '))

if your_pokemon_choice == 'charmander' or your_pokemon_choice == 'Charmander':
    your_pokemon = 'Charmander'
    print('You have chosen charmander')
elif your_pokemon_choice == 'bulbasaur' or your_pokemon_choice == 'Bulbasaur':
    your_pokemon = 'Bulbasaur'
    print('You have chosen bulbasaur')
elif your_pokemon_choice == 'squirtle' or your_pokemon_choice == 'Squirtle':
    your_pokemon = 'Squirtle'
    print('You have chosen squirtle')
else:
    print('this isnt a pokemon')
    quit()

print_with_delay('\nSince you have chosen your pokemon you must now do the rest i must go now\n')
print_with_delay('\nI am an mysterious man i will be giving you certain task to reach certain goals for your journey.\nYou must beat several gym trainers in order to aquire all the gym badge you will be needing for.\n')
print_with_delay("\n'randomly someone appeared out of thin air and decided to challenge u!'\n")
print_with_delay('\nDexter: I challenge u to an pokemon battle!\n Dexter has challenged you to an 1v1!\n')
print_with_delay('\nDexter has chosen rattata!\n')

print_with_delay(f'\n{name} you have chosen {your_pokemon} as your pokemon\n')

print_with_delay(f"\n'{your_pokemon} gets the first move!'\n")

number1 = int(input('\nPlease choose a move\n 1.Tackle 2.Scratch \n'))

if number1 == 1:
    print('You have used Tackle')
elif number1 == 2:
    print('You have used Scratch')
else:
    print('you are ded')
    quit()

print_with_delay(f"\nIt was very effective!\n Rattata has used quick attack!\n it wasn't very effective!\nIt is {your_pokemon} turn to attack! ")

number2 = int(input('\nPlease choose a move\n 1.Tackle 2.Scratch \n'))

if number2 == 1:
    print('You have used Tackle')
elif number2 == 2:
    print('You have used Scratch')
else:
    print('you are ded')
    quit()

print_with_delay('\nRattata has been defeated!\n')
print_with_delay(f'\n{your_pokemon} has gained some experience!\n')
print_with_delay("\n'You have Defeated your first challenger and now you are approaching to your 1st gym match'\n")
print_with_delay('\nyou have now made it to your first gym match\n')
print_with_delay('\nShan: So you have came to this gym to challenge me? Well battling me will not be so easy to begin with.\n')
print_with_delay("\n'Shan has used metagross!'\n")
print_with_delay(f'\n{name} has challenged Shan to an 1v1!')
print_with_delay(f'{your_pokemon} will start out!')

number3 = int(input('\nPlease choose a move\n 1.Tackle 2.Scratch \n'))

if number3 == 1:
    print('You have used Tackle')
elif number3 == 2:
    print('You have used Scratch')
else:
    print('you are ded')
    quit()

print_with_delay('\nIt was not effective!\n It is metagross turn!\n')
print_with_delay('\nmetagross has used bullet punch!\n It was effective!')
print_with_delay(f'\nIt is {your_pokemon} turn!')
number4 = int(input('\nPlease choose a move\n 1.Tackle 2.Scratch \n'))

if number4 == 1:
    print('You have used Tackle')
elif number4 == 2:
    print('You have used Scratch')
else:
    print('you are ded')
    quit()

print_with_delay("\nIt wasn't very effective!\n Metagross has used Flash cannon\n")
print_with_delay(f"\nIt was very effective!\n 'Wait {your_pokemon} has learned Giga Impact!'")

number5 = int(input('\nPlease choose a move\n 1.Giga Impact\n'))

if number5 == 1:
    print('You have used Giga Impact!')
else:
    print('game over yeahhhh')
    quit()

print_with_delay('\nThe opponent Metagross has been Defeated!\n')
print_with_delay(f"\nShan: you have defeated me but there are more stronger trainers out there.\n'You have obtained your 1st gym badge!' ")
print_with_delay("\nYou start your journey onward to the next gym battle\n")
print_with_delay(f"'Your {your_pokemon} is evolving!?'")

if your_pokemon == "Charmander":
    your_pokemon = 'Charizard'
    print(f'Charmander has evolved into {your_pokemon}')
elif your_pokemon == 'Bulbasaur':
    your_pokemon = 'Venasaur'
    print(f'Bulbasaur has evolved into {your_pokemon}')
elif your_pokemon == 'Squirtle':
    your_pokemon = 'Blastoise'
    print(f'Squirtle has evolved into {your_pokemon}')
else:
    print('You are in the wrong universe.')


# numba = (input('\nPick which pokemon you want?\n  Charizard , Venasaur , Blastoise: '))
# if numba == 'Charizard' or numba == 'charizard':
#     print(f'Your {your_pokemon} has evolved into Charizard')
# elif numba == 'Venasaur' or numba == 'venasaur':
#     print(f'Your {your_pokemon} has evolved into Venasaur')
# elif numba == 'Blastoise'or numba == 'blastoise':
#     print(f'Your {your_pokemon} has evolved into Blastoise')
# else:
#     print('game over yeahhhh')
#     quit()

print_with_delay(f"\nYour {your_pokemon} is your new pokemon!")
print_with_delay("\nYou have now reached the second gym battle.There you will see Jann the final boss having the last gym badge you need!\n")
print_with_delay(f"\nJann: I see {name} you have arrived here after beating your 1st gym leader. Well i am your final test let see if you can beat me!\n")
print_with_delay(f"\n'Jann has used Groudon!'\n")
print_with_delay(f'{your_pokemon} get the 1st move!')

number6 = int(input(f'\n{your_pokemon} has new moves after evolving!\n 1.Solar beam 2.Stone edge 3.Extreme speed 4.Splash:\n'))

if number6 == 1:
    print('You have used Solar beam!')
elif number6 == 2:
    print('You have used Stone edge!')
elif number6 == 3:
    print('You have used Extreme speed')
elif number6 == 4:
    print('You have used Splash')
else:
    print('You deserve to die!')

print_with_delay("\nIt was very effective!\n")
print_with_delay('\nJann: Groudon mega evolve now!\n')
print_with_delay("\n'The opponent Groudon has mega evolved!'\n")
print_with_delay("\nJann: Primal Groudon use Slam!")
print_with_delay("\n'It was very effective!'\n")
print_with_delay(f"\nIt is {your_pokemon} turn to attack!")\

number7 = int(input(f'\nPlease choose a move.\n 1.Solar beam 2.Stone edge 3.Extreme speed 4.Splash:\n'))

if number7 == 1:
    print('You have used Solar beam!')
elif number7 == 2:
    print('You have used Stone edge!')
elif number7 == 3:
    print('You have used Extreme speed')
elif number7 == 4:
    print('You have used Splash')
else:
    print('You deserve to die!')

print_with_delay("It wasn't very effective ")
print_with_delay("\nJann: Primal Groudon use guillotine!")
print_with_delay("\nIT IS SUPER EFFECTIVE!")
print_with_delay(f"\n{your_pokemon} has 1 hp left.\n{your_pokemon} turn to attack!")

number8 = int(input(f'\n{your_pokemon}has unlocked a new move!.\n 1.KAMEHAMEHA WAVE: \n'))

if number8 == 1:
    print('You have used KAMEHAMEHA WAVE!')
else:
    print('You deserve to die!')
quit()
print_with_delay("\nThe opponent Primal Groudon has been defeated!!!\n")

print_with_delay("\n'You have defeated Jann!'\n")

print_with_delay("You have completed the demo of the game.Thank you for playing!")



