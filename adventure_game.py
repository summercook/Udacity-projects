import time
import random


def intro():
    global monster
    monster = random.choice(['giant', 'cyclopes', 'ogre', 'dragon'])
    print_sleep('You find yourself in an open field with grass and yellow '
                'wild flowers.')
    print_sleep(f'Rumor has it that a {monster} is to be found somewhere '
                'around here, and has been terrorising the nearby village.')
    print_sleep('In front of you is a house.')
    print_sleep('To your right is a dark cave.')


def knock_or_peer(items):
    print_sleep('Enter 1 to knock on the door of the house.')
    print_sleep('Enter 2 to peer into the cave.')
    response = input('What would you like to do?\n')
    if response == '1':
        monsters(items)
        fight_or_run(items)
    elif response == '2' and 'sword' not in items:
        cave_1st(items)
    elif response == '2' and 'sword' in items:
        cave_2nd(items)
    else:
        invalid_response()
        knock_or_peer(items)


def fight_or_run(items):
    response2 = input('Would you like to (1) fight or (2) run away\n')
    if response2 == '1' and 'sword' not in items:
        fight_dagger()
    elif response2 == '1' and 'sword' in items:
        fight_sword()
    elif response2 == '2':
        print_sleep('You run back into the field. Luckily, you don\'t seem to '
                    'have been followed.')
        knock_or_peer(items)
    else:
        invalid_response()
        fight_or_run(items)


def monsters(items):
    print_sleep('You approach the door of the house.')
    print_sleep('You are about to knock when the door opens and out steps '
                f'a {monster}.\nEep! This is the {monster}\'s house!')
    print_sleep(f'The {monster} attacks you!')
    items.append('monster')


def cave_1st(items):
    print_sleep('You peer cautiously into the cave.')
    print_sleep('It turns out to be only a very small cave.')
    print_sleep('Your eye catches a glint of metal behind a rock.')
    print_sleep('You have found the magical Sword of Ogoroth!')
    print_sleep('You discard your silly old dagger and take the sword '
                'with you.')
    print_sleep('You walk back out to the field.')
    items.append('sword')
    knock_or_peer(items)


def cave_2nd(items):
    print_sleep('You peer cautiously into the cave.')
    print_sleep('You\'ve been here before, and gotten all the good stuff.')
    print_sleep('It\'s just an empty cave now.')
    print_sleep('You walk back out to the field.')
    knock_or_peer(items)


def fight_dagger():
    a = random.randint(0, 3)
    if a == 1:
        print_sleep('You do your best')
        print_sleep(f'But your dagger is no match for the {monster}.')
        print_sleep(f'Just when you are about to be defeated, the {monster} '
                    'falls over dead from a sudden heart attack.')
        print_sleep('You are victorious despite your impetuous behavior.')
        end_or_continue()
    else:
        print_sleep('You do your best')
        print_sleep(f'But your dagger is no match for the {monster}.')
        print_sleep('You have been defeated!')
        end_or_continue()


def fight_sword():
    print_sleep(f'As the {monster} moves to attack, you unsheath your'
                ' new sword.')
    print_sleep('The Sword of Ogoroth shines brightly in your hand as you '
                'brace yourself for the attack.')
    print_sleep(f'But the {monster} takes one look at your shiny new toy and '
                'runs away!')
    print_sleep(f'You have rid the town of the {monster}. You are victorious!')
    end_or_continue()


def end_or_continue():
    print_sleep('Would you like to end the game or continue playing?')
    response = input('Enter 1 to end or 2 to continue\n')
    if response == '1':
        print_sleep('Thanks for playing')
    elif response == '2':
        print_sleep('Great choice!')
        play_game()
    else:
        invalid_response()
        end_or_continue()


def invalid_response():
    print_sleep('I don\'t understand. Enter 1 or 2.')


def print_sleep(message):
    print(message)
    time.sleep(2)


def play_game():
    items = []
    intro()
    knock_or_peer(items)


play_game()
