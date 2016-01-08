class PartyAnimal:
 x = 0
 name = ""
 def __init__(self,z): # constructor can have additional parameters. These can be used to setup instance variables for the particular instance of the class, in this case, z is the variable and the alias of the name that is given in PartyAnimal
  self.name = z
  print self.name, "constructed"
 def party(self):
  self.x = self.x + 1
  print self.name, "party count", self.x
 

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

#we call the j & s multiple independent instance, becuase the j and s were originally assigned to PartyAnimal given the name of "Sally" and "Jim" respectively. As a consequence, in the Sally case, 
