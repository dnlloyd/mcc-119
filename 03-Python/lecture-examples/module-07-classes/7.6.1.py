import random


class Patient:
  admitted = True

  def __init__(self, fname, lname, age, ss, critical_condition=None):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss
    self.critical_condition = critical_condition

  def name(self):
    return self.fname + ' ' + self.lname
  
  def set_critical_condition(self, condition):
    self.critical_condition = condition
  
  def is_critical(self):
    if self.critical_condition is not None:
      return True
    else:
      return False
    
  def __str__(self):
    details = f"Name: {self.fname} {self.lname}\n"
    details += f"Age: {self.age}\n"
    details += f"Social security #: {self.ss}\n"
    details += f"Critical conditions: {self.critical_condition}"

    return details


## Main
patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789')

print(patient01)  # but the default __str__ method is really ugly, so lets override it

### All objects a printable because of the built in __str__ method
# my_string = "Hello"
# my_list = [5, "dan"]

# print(my_string)
# print(my_list)


