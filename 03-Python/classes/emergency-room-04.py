class Patient:
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


class Doctor:
  def __init__(self, fname, lname, specialty, on_call=False):
    self.fname = fname
    self.lname = lname
    self.specialty = specialty
    self.on_call = on_call

  def name(self):
    return self.fname + ' ' + self.lname


## Class instantiations
doctor01 = Doctor('Hawkeye', 'Pierce', 'Cardiologist')
doctor02 = Doctor('Greg', 'House', 'Neurologist')

patient01 = Patient('Dan', 'Lloyd', 49, '123-45-6789')
patient02 = Patient('Marsha', 'Brady', 67, '987-65-4321')
patient03 = Patient('Bob', 'Marley', 36, '555-67-1267')
patient04 = Patient('Janet', 'Reno', 78, '010-43-9998')

## Main
patient01.set_critical_condition('stroke')
patient03.set_critical_condition('pneumonia')

patients = [patient01, patient02, patient03, patient04]

doctor01.on_call = True
doctors = [doctor01, doctor01]

doctor_on_call = None

for doctor in doctors:
  if doctor.on_call:
    doctor_on_call = doctor01

for patient in patients:
  if patient.is_critical():
    print(f'Patient {patient.name()} is in critical condition: {patient.critical_condition}')
    
print(f'The doctor on call is {doctor_on_call.name()} ({doctor_on_call.specialty})')
