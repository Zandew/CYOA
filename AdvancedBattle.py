import random
class pokemon():

    def __init__(self, name, hp, attack, type):
        self.name = name
        self.hp = hp
        self.maxattack = attack
        self.maxhp = hp
        self.type = type

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
        
    def level_up(self):
        print ('{} leveled up!'.format(self.name))
        print ('You have gained 3 hp points! ')
        self.maxhp += health
        
    def heal(self):
        self.hp = self.maxhp
        
class specialmove():
    
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount
        
tackle = specialmove('tackle', 'damage', 7)
heal = specialmove('heal', 'heal', 7)
        
class starterpokemon(pokemon):
  
  def __init__(self, name, maxhp, type):
        pokemon.__init__(self, name, maxhp, type)
        self.moves = [tackle.name, heal.name]
        
  def attack(self, enemy):
        print ('It is your turn!')
        print ('What move do you want {} to use?!'.format(self.name))
        print ('--------------------')
        for move in self.moves:
            print (move)
        print ('--------------------')
        while True:
            move = input().lower()
            if move not in self.moves:
                continue
            print ('{} used {}!'.format(self.name, move))
        if move.type == 'damage':
            attack = move1.amount
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
            heal = move1.amount
            print ('{} has healed for {}!'.format(self.name, heal))
            self.hp += heal
            if self.hp>self.maxhp:
                self.hp = self.maxhp
pikachu = starterpokemon('pikachu', '10', 'water')
bulbasaur = pokemon('bulbasaur', '20', '2', 'grass')
pikachu.attack('bulbasaur')
            
            
        
            
    
       
    
