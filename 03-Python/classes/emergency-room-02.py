class Patient:
  def __init__(self, fname, lname, age, ss):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss

  def name(self):
    return self.fname + ' ' + self.lname 


patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789')
patient02 = Patient('Marsha', 'Brady', 67, '987-65-4321')

print(patient01.name())
print(patient02.name())
