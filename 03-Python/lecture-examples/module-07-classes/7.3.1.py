class Patient:
  def __init__(self, fname, lname, age, ss):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss

  def name(self):
    return self.fname + ' ' + self.lname


# patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789')
# patient02 = Patient('Marsha', 'Brady', 67, '987-65-4321')

### 7.3.1 Class methods
# print(patient01.name())
# patient02_name = patient02.name()
# print(patient02_name)
