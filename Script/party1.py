class PartyAnimal:
 x = 0 #initial value, which is not callable in the PartyAnimal class, cuz it doesnt't have any function
 
 def party(self):
  self.x = self.x + 1
  print "So far", self.x

an = PartyAnimal()

an.party()
an.party()
an.party()

