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

    def __init__(self, name, maxhp, type):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.type = type
        
    def heal(self):
        self.hp = self.maxhp
        
effectivedict = {'water': ['fire'],
                 'fire': ['grass'],
                 'grass': ['water'],
                 'None': ['None'],
                 'psychic': ['fire', 'water', 'grass', 'None']}
    
def is_effective(pokemon1, pokemon2):
    if pokemon2.type in effectivedict[pokemon1.type]:
        return True
    return False    

class basicmove():
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
        
    def __str__(self):
        return self.name
    
class specialmove():
   
    def __init__(self, name, type, amount, pp):
        self.name = name
        self.type = type
        self.amount = amount
        self.maxpp = pp
        self.pp = pp
    def __str__(self):
        return self.name
tackle = basicmove('tackle', 'damage', 7)
heal = specialmove('heal', 'heal', 15, 10)

class wildpokemon(pokemon):

    def __init__(self, name, maxhp, maxattack, type):
        super().__init__(name, maxhp, type)
        self.maxattack = maxattack
        self.hp = maxhp

    @property
    def minattack(self):
        return round(self.maxattack*0.7)

    def attack(self, enemy):
        attack = random.randint(self.minattack, self.maxattack)
        enemy.hp = enemy.hp-attack
        if enemy.hp<=0:
            print ('{} has knocked out {}'.format(self.name, enemy.name))
            return True
        else:
            print ('{} has attacked {} for {} damage'.format(self.name, enemy.name, attack))
            return False
        
class starter_pokemon(pokemon):
  
    def __init__(self, name, maxhp, type):
        super().__init__(name, maxhp, type)
        self.extraattack = 0
        self.moves = [tackle, heal]
        self.movenames = [tackle.name, heal.name]
        self.objectives = None
        self.currentsidequest = None
        self.skipmove = False
        self.chargemove = None

    def choose_move(self):
        print ('What move do you want {} to use?!'.format(self.name))
        print ('--------------------')
        for move in self.moves:
            if isinstance(move, specialmove):
                print (move.name + "     pp: " + str(move.pp))
            else:
                print (move)
        print ('--------------------')
        while True:
            move = input().lower()
            if move not in self.movenames:
                print ('Enter a valid move!')
                continue
            break
        for x in range(len(self.moves)):
            if move == self.moves[x].name:
                index = x
                break
        move = self.moves[index]
        return move
               
    def attack(self, enemy):
        print ('It is your turn!')
        if self.skipmove ==True:
            print ("{} used skull bash and dealt {} damage to {}!".format(self.name, chargemove.amount, enemy.name))
            enemy.hp -= chargemove.amount
            self.skipmove = False
            return None
        move = self.choose_move()
        if isinstance(move, specialmove):
            while True:
                if move.pp>0:
                    if move.type == 'heal':
                        heal = move.amount
                        print ('{} has healed for {}!'.format(self.name, heal))
                        self.hp += heal
                        move.pp -= 1
                        if self.hp>self.maxhp:
                            self.hp = self.maxhp
                        break
                    if move.type == 'passive':
                        amount = move.amount
                        print ('{} has increased his attack!'.format(self.name))
                        self.extraattack += amount
                        move.pp -= 1
                        break
                    if move.type == 'charge':
                        self.skipmove = True
                        print ("{} is charging up".format(self.name))
                        break
                else:
                    print ("You have no pp left for {}! Enter another move!".format(move))
                    move = self.choose_move()
        else:        
            if move.type == 'damage':
                attack = move.amount+self.extraattack
                if is_effective(self, enemy):
                    attack += 2
                enemy.hp = enemy.hp-attack
                if enemy.hp<=0:
                    print ('{} has knocked out {}'.format(self.name, enemy.name))
                    return True
                else:
                    print ('{} has attacked {} for {} damage'.format(self.name, enemy.name, attack))
                    return False 

    def level_up(self):
        print ('{} leveled up!'.format(self.name))
        print ('You have gained 3 hp points! ')
        self.maxhp += 3
        
    def addmove(self, move):
        self.moves.append(move)
        self.movenames.append(move.name)
        
    def heal(self):
        self.hp = self.maxhp
        for move in self.moves:
            if isinstace(move, specialmove):
                move.pp = move.maxpp
        
gameinfo1 = ['Welcome to the game!', 'The objective of this game is to defeat \
the boss and escape the locked room.', 'You have to escape by battling pokemon. \
If you beat all the guards, you can face the boss!', 'When you beat a pokemon, \
you level up gaining 3 health points. Other pokemon attack within a range, but \
your pokemon is special where it can have different attacks that do different \
damage and effects, but most of these attacks are only available through \
sidequests.', 'Each pokemon is of a different type. There are grass,fire and water kinds.\
Grass is super effective on water, water is super effective on fire and fire is \
super effective on grass! There are also pokemon with no type that are only super \
effective against other pokemon with no type. Type super effectiveness \
increases damage!']

gameinfo2 = ['You have waken up in a room with no apparent exit other than two doors','You have no idea what \
has happened, only that you were on your way to the prestigeous Pokemon Academy for \
your first day of middle school with your very first pokemon.', 'Now, you appear to be in a locked room and only have that \
pokemon with you to help you escape. While thinking about this situation, you can not help but wonder; why did this happen \
to me? Where do these doors lead? How could I have ever ended up in this situation...']
        
class Sidequest():
    def __init__(self, objective, reward):
        self.objective = objective
        self.reward = reward
        
    def start(self):
        print ("You have started a sidequest!")
        time.sleep(1)
        print ("In order to complete this quest you have to defeat {} pokemon".format(self.objective))
        starterpokemon.objectives = 0
        starterpokemon.currentsidequest = self
        
    def complete(self):
        print ("Congratulations you have completed this sidequest!")
        print ("You have earned the move {}!".format(self.reward))
        starterpokemon.addmove(self.reward)    
    
def getstarterpokemon():
    starterpokemonname=input("Enter your pokemon name: ") #Players can choose their pokemon's name
    ptype=0 #arbitrary value to enter the while loop
    types=['fire','water','grass'] #list of all the types to make sure entered type is valid
    while ptype not in types:
        ptype=input("Enter your pokemon's type (fire,water,grass): ").lower()#Players choose their pokemon's type
        if ptype not in types:
            print('Not a valid type! Enter either fire, water or grass exactly.')#If an invalid type, ask for the type again
    return starter_pokemon(starterpokemonname, 50, ptype)

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
       
def battle(pokemon1, pokemon2):
    print('   / __  )  /   |   /__  __/__  __/ /  /     /  ___/')
    print('  / __  |  / /| |    / /    / /    /  /     /  __/   ')  
    print(' / /_/ )  / ___ |   / /    / /    /  /___  /  /__   ')
    print('/_____/  /_/  |_/  /_/    /_/    /_____/  /_____/   ')
    print('{} versus {}!'.format(pokemon1.name.upper(), pokemon2.name.upper()))
    if is_effective(pokemon1, pokemon2):
        print ('{} has a type advantage over {}!'.format(pokemon1.name, pokemon2.name))
    elif is_effective(pokemon2, pokemon1):
        print ('{} has a type advantage over {}!'.format(pokemon2.name, pokemon1.name))
    while True:
        x = pokemon1.attack(pokemon2)
        if x==True:
            pokemon1.level_up()
            if starterpokemon.objectives!=None:
                starterpokemon.objectives += 1
                if starterpokemon.objectives == starterpokemon.currentsidequest.objective:
                    starterpokemon.currentsidequest.complete()
            return True
            break
        x = pokemon2.attack(pokemon1)
        if x==True:
            print ('{} fainted!'.format(starterpokemon.name))
            print ( "YOU LOSE")
            sys.exit()
    self.extraattack = 0

wild1 = wildpokemon('Bidoof', random.randint(30, 40), 8,'None')
wild2 = wildpokemon('Poliwag', random.randint(40, 45), 7, 'water')
wild3 = wildpokemon('Magikarp', random.randint(30, 35), 5, 'water')
wild4 = wildpokemon('Growlithe', random.randint(45, 50), 8, 'fire')
wild5 = wildpokemon('Vulpix', random.randint(40, 50), 7, 'fire')
wild6 = wildpokemon('Oddish', random.randint(30, 45), 6, 'grass')
wild7 = wildpokemon('Tangela', random.randint(40, 50), 7, 'grass')
guard1 = wildpokemon('Vaporeon', 45, 10, 'water')
guard2 = wildpokemon('Leafeon', 40, 11, 'grass')
guard3 = wildpokemon('Flareon', 45, 11, 'fire')
boss = wildpokemon('Meowth', 55, 14, 'psychic')

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

def sidequestroom():
    swordstance = specialmove("swordstance", "passive", 2, 10)
    skullbash = specialmove("skull bash", "charge", 25, 10)
    quest1 = Sidequest(1, skullbash)
    quest1.start()
    
def room1():#Where you can level up your pokemon, then you go into the guard room.
    print('Here you can level up your pokemon if you win a battle.')
    wildencounter()
    print ('You come across a huge hole and the only ways to get across are to walk over an old bridge or to walk around the hole')
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
    if 'yes' in command or 'heal' in command:
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
    time.sleep(1)
    battle(starterpokemon, wild)
    wild.heal()

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
    global starterpokemon
    for dialogue in gameinfo1:
        print (dialogue)
    starterpokemon = getstarterpokemon()
    for dialogue in gameinfo2:
        print (dialogue)
    sidequestroom()
    startingroom()
    
main()
