class PartyAnimal:
 x = 0
 
 def __init__(self):
  print "I am constructed" #constructor is more often used in the class, usually is to set a initial variables in the construct to get it right. Definition of constructor: in a object-oriented program in a class is a special block of statements called when an object is created 

 def party(self):
  self.x = self.x + 1
  print "So far", self.x
 
 def __del__(self):
  print "I am destructed", self.x

an = PartyAnimal()

an.party()
an.party()
an.party()
