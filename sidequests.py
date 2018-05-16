class sidequest(): #After creating instance of class, assign it to a pokemon 
  
  def __init__(self, name, reward):
    self.name = name
    self.reward = reward #Reward should be a function so when we complete the sidequest, we call the function
    
  def complete_sidequest():
    reward()
     
class NPC():
  
  def __init__(self, name):
    self.name = name
    self.questlist = []
    self.sidequest = self.questlist[random.randint(0, len(self.questlist)-1)]
      
  def talk():
    print (dialogue)
    command = input('Accept Quest?(Enter Yes or No)').lower()
    if command == 'yes':
      starterpokemon.start_sidequest(sidequest)
                                                   
 class pokemon():

    def __init__(self, name, hp, attack, type):
        self.maxhp = hp
        self.name = name
        self.hp = hp
        self.maxattack = attack
        self.type = type
        self.sidequest = None #New attribute sidequest
        self.passive = None

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
       
    def start_sidequest(self, sidequest):
        self.sidequest = sidequest
        
    def complete_sidequest(self):
        self.sidequest.complete_sidequest()
        
    def passive(self):
        passive()
        
                                                   
      
      
                    

               
