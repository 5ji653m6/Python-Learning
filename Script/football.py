class PartyAnimal:
 x = 0
 name = ""
 def __init__(self,z):
  self.name = z 
  print self.name, "constructed"

 def party(self):
  self.x = self.x + 1
  print self.name, "party count", self.x

class FootballFan(PartyAnimal):
 points = 0
 def touchdown(self):
  self.points = self.points + 7
  self.party()
  print self.name, "points", self.points

#FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal. We call the FootballFan is the child class of the PartyAnimal class, in which FootballFan inherit all methods of that in PartyAnimal.

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown() # this line of code is from the class of FootballFan, and the outcome contain the party count + 1 because touchdown includes the instance of party.

'''
Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Jim party count 2
Jim points 7
'''
