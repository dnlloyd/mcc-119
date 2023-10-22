class Person:
  def __init__(self, fname, lname, age, ss):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss


me = Person('Dan', 'Lloyd', 49, '123-45-6789')

print(me.fname)
print(me.age)
