class Patient:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname


### 7.2.2 & 7.2.4 Class instantiation and initialization
me = Patient('Dan', 'Lloyd')
you = Patient('Bob', 'Roberts')

print(me.fname)
print(you.lname)


### 7.2.3
# print(you.__dict__)

# you.age = 12
# print(you.__dict__)