import random
class pokemon():

    def __init__(self, name, maxhp, type):
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.type = type
        
effectivedict = {'water': ['fire'],
                 'fire': ['grass'],
                 'grass': ['water'],
                 'None': ['None'],
                 'psychic': ['fire', 'water', 'grass', 'None']}
    
def is_effective(pokemon1, pokemon2):
    if pokemon2.type in effectivedict[pokemon1.type]:
        return True
    return False    

class specialmove():
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
        
    def __str__(self):
        return self.name
                
tackle = specialmove('tackle', 'damage', 7)
heal = specialmove('heal', 'heal', 7)

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
        
class starterpokemon(pokemon):
  
    def __init__(self, name, maxhp, type):
        super().__init__(name, maxhp, type)
        self.moves = [tackle, heal]
        self.movenames = [tackle.name, heal.name]

        
    def attack(self, enemy):
        print ('It is your turn!')
        print ('What move do you want {} to use?!'.format(self.name))
        print ('--------------------')
        for move in self.moves:
            print (move)
        print ('--------------------')
        while True:
            move = input().lower()
            if move not in self.movenames:
                print ('Enter a valid move!')
                continue
            print ('{} used {}!'.format(self.name, move))
            break
        for x in range(len(self.moves)):
            if move == self.moves[x].name:
                index = x
                break
        move = self.moves[index]
        if move.type == 'damage':
            attack = move.amount
            if is_effective(self, enemy):
                attack += 2
            enemy.hp = enemy.hp-attack
            if enemy.hp<=0:
                print ('{} has knocked out {}'.format(self.name, enemy.name))
                return True
            else:
                print ('{} has attacked {} for {} damage'.format(self.name, enemy.name, attack))
                return False 
        if move.type == 'heal':
            heal = move.amount
            print ('{} has healed for {}!'.format(self.name, heal))
            self.hp += heal
            if self.hp>self.maxhp:
                self.hp = self.maxhp

    def level_up(self):
        print ('{} leveled up!'.format(self.name))
        print ('You have gained 3 hp points! ')
        self.maxhp += health

    def heal(self):
        self.hp = self.maxhp
        
pikachu = starterpokemon('pikachu', 10, 'water')
bulbasaur = wildpokemon('bulbasaur', 20, 2, 'grass')
pikachu.attack(bulbasaur)
            
            
        
            
    
       
    
