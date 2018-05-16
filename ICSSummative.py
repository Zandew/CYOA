'''File name: Summative
Author: Rayton Lin & Andrew Xue
Teachers: Mr.Saleem
Date created:May 9th,2018
Date modified: May 9th,2018
Python Version: 3.6
'''
import time
import random
import sys

class pokemon():

    def __init__(self, name, hp, attack, type):
        self.maxhp = hp
        self.name = name
        self.hp = hp
        self.maxattack = attack
        self.type = type

    @property
    def minattack(self):
        return round(self.maxattack*0.7)
        
    def levelup(self):
        print ('{} leveled up!'.format(self.name))
        print ('You have gained 5 stat points! ')
        health = int(input("How many stats do you want to allocate into HP?"))
        while health<0 or health>5:
            print('This is not a valid increase in health!')
            health = int(input("How many stats do you want to allocate into HP?"))
        print(5-health,'points were allocated into attack. ')
        self.hp += health
        self.maxattack += 5-health
        
    def heal(self):
        self.hp = self.maxhp

gameinfo1 = ['Welcome to the game!', 'The objective of this game is to defeat\
the boss and escape the locked room.', 'You have to escape by battling pokemon.\
If you beat all the guards, you can face the boss!', 'Each pokemon has health and attack stats. The attack stat is split up\
between minimum and maximum attack stats. The minimum attack \
stat is 0.7 times the maximum attack stat. When you level up, you get 5 stat points to \
allocate between health and attack.', 'Each pokemon is of a different type. There are grass,fire and water kinds.\
Grass is super effective on water, water is super effective on fire and fire is \
super effective on grass! There are also pokemon with no type that are only super \
effective against other pokemon with no type. Type super effectiveness \
increases damage!']

gameinfo2 = ['You have waken up in a room with no apparent exit other than two doors','You have no idea what \
has happened, only that you were on your way to the prestigeous Pokemon Academy for \
your first day of middle school with your very first pokemon.', 'Now, you appear to be in a locked room and only have that \
pokemon with you to help you escape. While thinking about this situation, you can not help but wonder; why did this happen \
to me? Where do these doors lead? How could I have ever ended up in this situation...']
        
def getstarterpokemon():
    starterpokemonname=input("Enter your pokemon name: ") #Players can choose their pokemon's name
    ptype=0 #arbitrary value to enter the while loop
    types=['fire','water','grass'] #list of all the types to make sure entered type is valid
    while ptype not in types:
        ptype=input("Enter your pokemon's type (fire,water,grass): ").lower()#Players choose their pokemon's type
        if ptype not in types:
            print('Not a valid type! Enter either fire, water or grass exactly.')#If an invalid type, ask for the type again
    starterpokemon=pokemon(starterpokemonname,50,10,ptype)

#Shows what type each type is effective against.
effectivedict = {'water': ['fire'],
                 'fire': ['grass'],
                 'grass': ['water'],
                 'None': ['None'],
                 'psychic': ['fire', 'water', 'grass', 'None']}
    
def is_effective(pokemon1, pokemon2):
    if pokemon2.type in effectivedict[pokemon1.type]:
        return True
    return False
    
def attack(pokemon1, pokemon2):
    attack = random.randint(pokemon1.minattack, pokemon1.maxattack)
    if is_effective(pokemon1, pokemon2):
        attack += 2
    pokemon2.hp = pokemon2.hp-attack
    print (pokemon1.name, 'has attacked', pokemon2.name, 'for', attack, 'damage')
    if pokemon2.hp<0:
        print (pokemon1.name, 'has knocked out', pokemon2.name)
        return False
    
def battle(pokemon1, pokemon2):
    if is_effective(pokemon1, pokemon2):
        print ('{} has a type advantage over {}!'.format(pokemon1.name, pokemon2.name))
    elif is_effective(pokemon2, pokemon1):
        print ('{} has a type advantage over {}!'.format(pokemon2.name, pokemon1.name))
    x = True
    while x !=False:
        x = attack(pokemon1, pokemon2)
        if x==False:
            pokemon1.levelup()
            return True
            break
        x = attack(pokemon2, pokemon1)
        if x==False:
            print ('{} fainted!'.format(starterpokemon.name))
            print ( "YOU LOSE")
            sys.exit()

wild1 = pokemon('Bidoof', random.randint(30, 40), 8,'None')
wild2 = pokemon('Poliwag', random.randint(40, 45), 7, 'water')
wild3 = pokemon('Magikarp', random.randint(30, 35), 5, 'water')
wild4 = pokemon('Growlithe', random.randint(45, 50), 8, 'fire')
wild5 = pokemon('Vulpix', random.randint(40, 50), 7, 'fire')
wild6 = pokemon('Oddish', random.randint(30, 45), 6, 'grass')
wild7 = pokemon('Tangela', random.randint(40, 50), 7, 'grass')
guard1 = pokemon('Vaporeon', 45, 10, 'water')
guard2 = pokemon('Leafeon', 40, 11, 'grass')
guard3 = pokemon('Flareon', 45, 11, 'fire')
boss = pokemon('Meowth', 55, 14, 'psychic')

wildlist = [wild1, wild2, wild3, wild4, wild5, wild6, wild7]
guardlist = [guard1, guard2, guard3]
dialoguelist = ['I am sure you must be wondering why you have been sent here. \
Well I, Guardone cannot give you the answer. If you feel that you must escape, \
then you will have to defeat my Vaporeon with your own skill!', 'Impressive \
beating his Vaporeon. However I, Guardtwo cannot let you go. My Leafeon shall \
send you back!', 'YOU HAVE SOME NERVE TRYING TO BEAT US! DO YOU REALLY THINK \
WE WILL JUST BACK DOWN TO A FIGHT? WELL I, GUARDTHREE WILL BURN YOUR POKEMON \
WITH MY FLAREON! THAT POKEMON OF YOURS IS VERY IMPORTANT TO US, BUT IF YOU \
DO NOT BACK OFF WE WILL HAVE NO CHOICE!']
bossdialogue=['Jessie: I’m sure you are wondering why you were brought here. To show respect for your skill, \
we shall explain.','James: That pokemon of yours has a very special ability that we, Team Rocket would like to have. \
That ability is being able to grow exponentially fast through the use of pokemon battles.','Meowth: You have the only other \
pokemon than me that has this ability. We absolutely cannot let you have it.','Jessie:Your friends, they have no idea what has \
happened to you. Your family as well. They would never believe you anyways, so do not try to defy us. You have barely known that \
pokemon anyways, so if you do not mind, we will take that pokemon by force.']
endingdialogue=['Jessie: So you have beaten us... That must be a true testament of your skill.','James: It appears like we will \
have to let you go for now, but know that there are much more dangerous groups out there targeting your pokemon and its ability.'\
,'Meowth: You must continue to get stronger. I can tell that your pokemon knows this as well. We have the resources to help you \
train but know that we are being targeted by some very dangerous organizations as well. Our deal is that we will help you train \
your pokemon in exchange for helping protect us. Is that a deal?','THE END']

def room1():#Where you can level up your pokemon, then you go into the guard room.
    print('Here you can level up your pokemon if you win a battle.')
    wildencounter()
    print ('You come across a huge hole and the only ways to get across are to walk over an old \
    bridge or to walk around the hole')
    print ('Do you take the bridge or walk around the hole?')
    command = input().lower()
    if 'bridge' in command:
         print ('While you are taking the bridge, the bridge collapses, you fall down the hole and find a wild pokemon!!')
         wildencounter()
         print ('Luckily there is a ladder going up the hole, you take the ladder and reach the other side')
         
    else:
         print ('You crossed the hole safely!')
    pokecenter()
    guardroom()        
        
def room2():#Where you can level up your pokemon
    print('Here you can level up your pokemon if you win a battle.')
    wildencounter()
    print ('Looks like this room is a dead end!')
    print('You arrived back at the starting room!')
    startingroom()
       
def startingroom(): #This is the first room players end up in
    command=input('Both rooms look like they contain wild pokemon. Turn left or right?: ')
    if 'left' in command:
        room1()
    elif 'right' in command:
        room2()
    else:
        print('Please enter a valid direction!')
        startingroom()
        
def pokecenter():
    command = input('It looks like there is a Pokemon Center nearby, do you want to heal your pokemon?').lower()
    if 'yes' in command:
    	print ('Hello, and welcome to the Pokémon Center. We will heal your pokemon to full health.')
    	starterpokemon.heal()
    	print ('Please come again!')
        
def guardroom():
    print('This is the guard room! You have to face 3 pokemon back to back!')
    guardbattle()
    pokecenter()
    bossbattle()

def wildencounter():
    index = random.randint(0, 6)
    wild = wildlist[index]
    print ('A wild {} appeared!'.format(wild.name))
    battle(starterpokemon, wild)

def guardbattle():
    for guard, dialogue in zip(guardlist, dialoguelist):
        print (dialogue)
        battle(starterpokemon, guard)

def endingscene():
    for dialogue in endingdialogue:
        print(dialogue)
        time.sleep(2.5)
    sys.exit()        
        
def bossbattle():
    for dialogue in bossdialogue:
        print (dialogue)
        time.sleep(2.5)
    battle(starterpokemon, boss)
    endingscene()
    
def main():
    for dialogue in gameinfo1:
        print (dialogue)
        time.sleep(5)
    getstarterpokemon()
    for dialogue in gameinfo2:
        print (dialogue)
        time.sleep(3)
    startingroom()
    
main()
