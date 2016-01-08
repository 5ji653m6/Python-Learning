class PartyAnimal:
 x = 0
 
 def party(self):
  self.x = self.x + 1
  print "So far", self.x

an = PartyAnimal()

print "Type", type(an)
print "Dir", dir(an)


# code will print out the type of the "an"m which has been assigned to the classPartyAnimal we created. And it turns out that the "an" is an object (or instance) and the method include the "party" and "x" that we defined in the PartyAnimal class.
'''
Type <type 'instance'>
Dir ['__doc__', '__module__', 'party', 'x']
'''
