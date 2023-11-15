class Patient:
  admitted = True  ### 7.4.1 class attribute

  def __init__(self, fname, lname, age, ss, critical_condition=None):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.ss = ss
    self.critical_condition = critical_condition

  def name(self):
    return self.fname + ' ' + self.lname
  
  ### 7.5.1 Instance methods
  def set_critical_condition(self, condition):
    self.critical_condition = condition
  
  def is_critical(self):
    if self.critical_condition is not None:
      return True
    else:
      return False 


## Main
patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789')
patient02 = Patient('Marsha', 'Brady', 67, '987-65-4321')
patient03 = Patient('Bob', 'Marley', 36, '555-67-1267')
patient04 = Patient('Janet', 'Reno', 78, '010-43-9998')

### 7.3.2 passing args to instance methods
### 7.3.3 setting instance attrs
### 7.5.1 instance methods
patient01.set_critical_condition('stroke')
patient03.set_critical_condition('cardiac arrest')

patient03.admitted = False  # overrides class attribute for this instance only

patients = [patient01, patient02, patient03, patient04]

for patient in patients:
  if patient.is_critical() and patient.admitted:  ### 7.4.1 class attribute
    print(f'Patient {patient.name()} is in critical condition: {patient.critical_condition}')

# Let's say the hospital is closing down, we can access all instances via the class attribute
# Patient.admitted = False

# for patient in patients:
#   print(patient.admitted)
