class Hospital:
  org = "MCC Medical Center"

  def __init__(self, campus, name, address):
    self.campus = campus
    self.name = name
    self.address = address

  @classmethod
  def change_org(cls, new_org):
    cls.org = new_org

class MapleWoods(Hospital):
  def fee(self, age, income, children):
    fee = (income / age) * 100 / children

    return fee


###### Main
math_clinic = MapleWoods('Maple Woods', 'The Math Clinic', '2601 NE Barry Rd')

print(f'Campus locations for {Hospital.org}')
print('--------------------------------------------')
print(f'Maple Woods Math Clinic: {math_clinic.address}')

### 7.5.2 Class methods
# Hospital.change_org("KU Medical Center")

# print(f'Campus locations for {Hospital.org}')
# print('--------------------------------------------')
# print(f'Maple Woods Math Clinic: {math_clinic.address}')