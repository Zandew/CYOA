import random
class pokemon():

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.maxattack = attack
        self.maxhp = hp

    @property
    def minattack(self):
        return round(self.maxattack*0.7)
        
    def level_up(self):
        print ("{} leveled up!".format(self.name))
        print ("You are given 10 stats to split on health and attack")
        while True:
            health = int(input("How many stats do you want to allocate on HP?"))
            if health>=0 and health<=10:
                break
        print ("You added {} points to health and {} points to attack".format(health, 10-health))
        self.hp += health
        self.maxhp += health
        self.maxattack += 10-health

    def heal(self):
        self.hp = self.maxhp
        
def attack(pokemon1, pokemon2):
    attack = random.randint(pokemon1.minattack, pokemon1.maxattack)
    pokemon2.hp = pokemon2.hp-attack
    if pokemon2.hp<0:
        print ('{} has knocked out {}'.format(pokemon1.name, pokemon2.name))
        return True
    else:
        print ('{} has attacked {} for {} damage'.format(pokemon1.name, pokemon2.name, attack))
        
def battle(pokemon1, pokemon2):
    knockout = False
    while True:
        knockout = attack(pokemon1, pokemon2)
        if knockout==True:
            break
        knockout = attack(pokemon2, pokemon1)
        if knockout==True:
            break
    pokemon1.heal()
    pokemon2.heal()
