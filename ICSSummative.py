'''File name: Summative
Author: Rayton Lin & Andrew Xue
Teachers: Mr.Saleem
Date created:May 9th,2018
Date modified: May 29th,2018
Python Version: 3.6
'''
import time
import random
import sys

def pause(n):
    time.sleep(n)

class pokemon():

    def __init__(self, name, maxhp, type):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.type = type
        
    def heal(self):
        self.hp = self.maxhp
        
      

class basicmove():#Determines properties of basic moves
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
        
    def __str__(self):
        return self.name
    
class specialmove():#Determines properties of special moves
   
    def __init__(self, name, type, amount, pp, description=None):
        self.name = name
        self.type = type
        self.amount = amount
        self.maxpp = pp
        self.pp = pp
        self.description = description
        
    def __str__(self):
        return self.name
    
tackle = basicmove('tackle', 'damage', 7)
heal = specialmove('heal', 'heal', 15, 5)
swordstance = specialmove("swordstance", "passive", 2, 5, "Increases your attack by 2 for the rest of the battle")
skullbash = specialmove("skull bash", "charge", 20, 5, "Charge up for 1 turn and deal 20 damage next turn")
toughskin = specialmove("tough skin", "passive", 2, 5, "Take 2 less damage from the opponent's attack for the rest of the battle")
judgement = basicmove('judgement','damage',14)
class wildpokemon(pokemon):#Determines stats and properties of the wild pokemon

    def __init__(self, name, maxhp, maxattack, type):
        super().__init__(name, maxhp, type)
        self.maxattack = maxattack
        self.hp = maxhp

    @property
    def minattack(self):
        return round(self.maxattack*0.7)

    def attack(self, enemy):
        attack = random.randint(self.minattack, self.maxattack)-enemy.defense
        if attack<0:
            attack = 0
        enemy.hp = enemy.hp-attack
        if enemy.hp<=0:
            print ('{} has knocked out {}'.format(self.name, enemy.name))
            return True
        else:
            print ('{} has attacked {} for {} damage'.format(self.name, enemy.name, attack))
            return False
        
class starter_pokemon(pokemon):#Configures stats and properties of the starter pokemon
  
    def __init__(self, name, maxhp, type):
        super().__init__(name, maxhp, type)
        self.extraattack = 0
        self.moves = [tackle, heal]
        if self.type=='water':
            tackle.name = "water gun"
        elif self.type =='fire':
            tackle.name = "ember"
        else: 
            tackle.name = "razor leaf"
        self.movenames = [tackle.name, heal.name]
        self.objectives = None
        self.currentsidequest = None
        self.skipmove = False
        self.chargemove = None
        self.defense = 0

    def choose_move(self, enemy):
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
            if move=='stats':
                print (format(self.name.upper(), '15s') + str(self.hp) + '/' + str(self.maxhp))
                selfpercent = round((self.hp/self.maxhp)*20)
                selfhp1 = ['■' for x in range(selfpercent)]
                selfhp2 = ['_' for x in range(20-selfpercent)]
                hpbar = ''.join(selfhp1 + selfhp2)
                print (hpbar)
                print (format(enemy.name.upper(), '15s') + str(enemy.hp) + '/' + str(enemy.maxhp))
                enemypercent = round((enemy.hp/enemy.maxhp)*20)
                enemyhp1 = ['■' for x in range(enemypercent)]
                enemyhp2 = ['_' for x in range(20-enemypercent)]
                hpbar = ''.join(enemyhp1 + enemyhp2)
                print (hpbar)
                print ("Enter a move!")
                continue
            elif move not in self.movenames:
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
            print ("{} used skull bash and dealt {} damage to {}!".format(self.name, self.chargemove.amount, enemy.name))
            enemy.hp -= self.chargemove.amount
            if enemy.hp<=0:
                print ("{} has knocked out {}!".format(self.name, enemy.name))
                return True
            self.skipmove = False
            return None
        move = self.choose_move(enemy)
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
                        if move.name == "swordstance":
                            print ("{} has increased his attack!".format(self.name))
                            self.extraattack += amount
                        elif move.name == "tough skin":
                            print ("{} has increased it's defense!".format(self.name))
                            self.defense += 2
                        move.pp -= 1
                        break
                    if move.type == 'charge':
                        self.skipmove = True
                        self.chargemove = move
                        print ("{} is charging up".format(self.name))
                        move.pp -= 1
                        break
                else:
                    print ("You have no pp left for {}! Enter another move!".format(move))
                    move = self.choose_move(enemy)
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
            if isinstance(move, specialmove):
                move.pp = move.maxpp

    def reset_buffs(self):
        self.extraattack = 0
        self.defense = 0
        
gameinfo1 = ['Welcome to the game!', 'The objective of this game is to defeat \
the boss and escape the locked room.', 'You have to escape by battling pokemon. \
If you beat all the guards, you can face the boss!', 'When you beat a pokemon, \
you level up gaining 3 health points. Other pokemon attack within a range, but \
your pokemon is special where it can have different attacks that do different \
damage and effects, but most of these attacks are only available through \
sidequests. If you type stats when in a battle, you can see the health of both pokemon in battle.', 'Each pokemon is of a different type. There are grass,fire and water types.\
Grass is super effective on water, water is super effective on fire and fire is \
super effective on grass! There are also pokemon with no type that are only super \
effective against other pokemon with no type. Type super effectiveness \
increases damage!']

gameinfo2 = ['You have waken up in a room with no apparent exit other than two doors','You have no idea what \
has happened, only that you were on your way to the prestigeous Pokemon Academy for \
your first day of middle school with your very first pokemon.', 'Now, you appear to be in a locked room and only have that \
pokemon with you to help you escape. While thinking about this situation, you can not help but wonder; Why did this happen \
to me? Where do these doors lead? How could I have ever ended up in this situation...']
        
class Sidequest():#Determines when the sidequest starts and ends, and gives the reward
    def __init__(self, objective, reward):
        self.objective = objective
        self.reward = reward
        
    def start(self):
        print ("You have started a sidequest!")
        time.sleep(1)
        print ("In order to complete this quest you have to defeat {} pokemon".format(self.objective))
        print ("*****************")
        print ("REWARD: {}".format(self.reward))
        print (self.reward.description)
        print ("*****************")
        starterpokemon.objectives = 0
        starterpokemon.currentsidequest = self
        
    def complete(self):
        print ('..................................................')
        print ("Congratulations you have completed this sidequest!")
        print ("You have earned the move {}!".format(self.reward))
        print ('..................................................')        
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
    
def is_effective(pokemon1, pokemon2):#Determines if the pokemon's type is super effective
    if pokemon2.type in effectivedict[pokemon1.type]:
        return True
    return False
       
def battle(pokemon1, pokemon2):#Starts the battle sequence
    print('   / __  )  /   |   /__  __/__  __/ /  /     /  ___/')
    print('  / __  |  / /| |    / /    / /    /  /     /  __/  ')  
    print(' / /_/ )  / ___ |   / /    / /    /  /__   /  /__   ')
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
            starterpokemon.reset_buffs()
            return True
            break
        x = pokemon2.attack(pokemon1)
        if x==True:
            print ('{} fainted!'.format(starterpokemon.name))
            print ( "YOU LOSE")
            sys.exit()

snorlax = wildpokemon('Snorlax', 100, 2, 'None')
wild1 = wildpokemon('Bidoof', random.randint(10, 40), 8,'None')
wild2 = wildpokemon('Poliwag', random.randint(20, 45), 7, 'water')
wild3 = wildpokemon('Magikarp', random.randint(20, 35), 5, 'water')
wild4 = wildpokemon('Growlithe', random.randint(25, 50), 8, 'fire')
wild5 = wildpokemon('Vulpix', random.randint(20, 50), 7, 'fire')
wild6 = wildpokemon('Oddish', random.randint(10, 45), 6, 'grass')
wild7 = wildpokemon('Tangela', random.randint(20, 50), 7, 'grass')
guard1 = wildpokemon('Vaporeon', 15, 10, 'water')
guard2 = wildpokemon('Leafeon', 20, 11, 'grass')
guard3 = wildpokemon('Flareon', 25, 11, 'fire')
boss = wildpokemon('Meowth', 35, 14, 'psychic')
#Above are the pokemon you can encounter
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

quest1 = Sidequest(2, swordstance)
quest2 = Sidequest(2, skullbash)
quest3 = Sidequest(2, toughskin)
sidequestlist = [quest1, quest2, quest3]

def getsidequest():
    quest = sidequestlist[random.randint(0, len(sidequestlist)-1)]
    sidequestlist.remove(quest)
    return quest

def sidequestroom():#Starts a sidequests where you can get a new move
    quest = getsidequest()
    quest.start()

def ruins():
    print ('You see a treasure chest, but there is a sleeping snorlax sitting on it!')
    print ('Do you...')
    pause(1)
    print ('1. Attack snorlax with {}'.format(starterpokemon.name))
    print ('2. Look around for another way to move snorlax')
    command = input()
    if command == '1':
        print ('Snorlax wakes up and looks angry...')
        battle(starterpokemon, snorlax)
        print ('Congratulations, you defeated snorlax!')
    elif command == '2':
        print ('You find a mysterious flute and decide to play it')
        pause(1)
        print ('Snorlax starts sleepwalking and walks away from the chest!')
    print ('You walk up to the treasure chest and open it, you find a sidequest!')
    quest = getsidequest()
    print('This sidequest rewards you with the move {}!'.format(quest.reward.name))
    print(quest.reward.description)
    answer=input('Do you want to start this sidequest? Y/N WARNING: Accepting this sidequest deletes any current sidequest.')
    if answer.lower()=='y' or answer.lower=='yes':
        quest.start()
    else:
        print('You have declined the sidequest!')
def room3():
    print ('This room looks like an abandoned city, there is what looks like an entrance to a ruins')
    print ('Do you...')
    pause(1)
    print ('1. Enter the ruins')
    print ('2. Keep walking on the main track')
    command = input()
    if command =='1':
        ruins()
    elif command =='2':
        wildencounter()
    pokecenter()
    guardroom()
    
    
def room1():#Where you can level up your pokemon, then you go into the guard room.
    print('This room has a lot of tall grass, it looks like it contains a lot of wild pokemon.')
    wildencounter()
    print ('You come across a huge hole and the only ways to get across are to walk over an old bridge or to walk around the hole')
    print ('Do you...')
    pause(1)
    print ('1: Take the bridge')
    print ('2: Go around the hole')
    command = input()
    while True:
        if command=='1':
            print ('While you are taking the bridge, the bridge collapses, you fall down the hole and find a wild pokemon!!')
            wildencounter()
            print ('Luckily there is a ladder going up the hole, you take the ladder and reach the other side')
            break
        elif command=='2':
            print ('You crossed the hole safely')
            break
        else:
            print ('Enter a valid choice')
            command = input()
    pokecenter()
    room3()

        
        
def room2():#Where you can level up your pokemon
    print('This room looks like a swamp, it also looks like it contains many wild pokemon.')
    wildencounter()
    print ('You come across a huge pond and you have to get across')
    print ('Do you...')
    pause(1)
    print ('1. Swim across the pond')
    print ('2. Walk around the pond')
    command = input()
    while True:
        if command =='1':
            print ('While swimming, you encounter a wild pokemon!')
            wildencounter()
            break
        elif command =='2':
            break
        else:
            print('Enter 1 or 2 exactly!')
    print ('You have safely crossed the swamp!')
    room3()
       
def startingroom(): #This is the first room players end up in
    command=input('Both rooms look like they contain wild pokemon. Turn left or right?: ')
    if 'left' in command:
        room1()
    elif 'right' in command:
        room2()
    else:
        print('Please enter a valid direction!')
        startingroom()
        
def pokecenter():#You can heal your pokemon's health and pp here
    command = input('It looks like there is a Pokemon Center nearby, do you want to heal your pokemon?').lower()
    if 'yes' in command or 'heal' in command:
    	print ('Hello, and welcome to the Pokémon Center. We will heal your pokemon to full health.')
    	starterpokemon.heal()
    	pause(1)
    	print ('Please come again!')
        
def guardroom():#Enters the guard room, starting the first non-wild pokemon battle in the game
    print('This is the guard room! You have to face 3 pokemon back to back!')
    pause(1)
    guardbattle()
    pokecenter()
    room4()

def wildencounter():#Starts a wild pokemon battle
    index = random.randint(0, 6)
    wild = wildlist[index]
    print ('A wild {} appeared!'.format(wild.name))
    pause(1)
    battle(starterpokemon, wild)#Starts the battle
    wild.heal()

def guardbattle():#Prints the dialogue for the guards, then starts the battle
    for guard, dialogue in zip(guardlist, dialoguelist):
        print (dialogue)
        battle(starterpokemon, guard)#Starts the battle

def endingscene():#Prints the dialogue for the ending scene, then ends the game
    for dialogue in endingdialogue:
        print(dialogue)
        pause(2)
    sys.exit()        
        
def bossbattle():#Starts the final battle in the game and the hardest, the boss battle
    for dialogue in bossdialogue:#Prints the dialogue for the bosses
        print (dialogue)
        pause(2)
    battle(starterpokemon, boss)#Starts the battle
    endingscene()#When you win, it starts the ending scene

def room4():#This maze connects the boss battle to the guard room
    print("You have found yourself in a maze. You think that the boss will be at the end, but you aren't sure.")
    runningtotal=0
    while runningtotal<10:#The maze goes until the running total passes 10
        room=input("You see 3 rooms in front of you. Which numbered room do you go into?")
        while room!='1' and room!='2' and room!='3':
            print('That is not a valid room number!')
            room=input("You see 3 rooms in front of you. Which numbered room do you go into?")
        runningtotal+=int(room)
        if runningtotal%3==0:
            wildencounter()
            print('Looks like you need to keep moving.')
        elif runningtotal%3!=0 and runningtotal!=10:
            print('There is nothing in this room! Looks like you need to keep moving.')
    if runningtotal==10: #If the running total ends on 10, your pokemon gets a powerful move
        starterpokemon.addmove(judgement)
        print('Your pokemon now knows the strongest basic move, judgement!')
        print('You can see the boss!')
    else: #Otherwise, you go straight to the boss
        print('You found no treasure in this maze, but you can see the boss!')
    pokecenter()
    bossbattle()
def main():
    global starterpokemon #Makes starterpokemon a global variable used throughout the program
    for dialogue in gameinfo1: #Displays the first lines of text
        print (dialogue)
        pause(2)
    starterpokemon = getstarterpokemon()#Stores the properties of the starter pokemon
    for dialogue in gameinfo2:#Displays the next lines of text
        print (dialogue)
        pause(2)
    sidequestroom()#Starts a sidequest
    startingroom()#Starts the game in the starting room
    
main()#Starts the prologue
