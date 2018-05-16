class sidequest(): #After creating instance of class, assign it to a pokemon 
  
  def __init__(self, name, reward):
    self.name = name
    self.initiated = False
    self.reward = reward #Reward should be a function so when we complete the sidequest, we call the function
    
  def start_sidequest():
    self.initiated = True #Whenever battle finishes (or any other event), checks if player has active sidequest
    
  def complete_sidequest():
    reward()
     
class NPC():
  
  def __init__(self, name):
    self.name = name
    self.questlist = []
    self.sidequest = self.questlist[random.randint(0, len(self.questlist)-1]
      
  def talk():
    print (dialogue)
    command = input('Accept Quest?(Enter Yes or No)').lower()
    if command == 'yes':
      self.sidequest.start_sidequest()
      
      
                    

               
