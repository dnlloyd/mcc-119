import locale
locale.setlocale( locale.LC_ALL, '' )

class Hospital:
  org = "MCC Medical Center"

  def __init__(self, campus, name, address):
    self.campus = campus
    self.name = name
    self.address = address
  
  @classmethod
  def change_org(cls, new_org):
    cls.org = new_org


# subclass
class MapleWoods(Hospital):
  def fee(self, age, income, children):
    fee = (income / age) * 100 / children

    return fee


# subclass
class Penn(Hospital):
  def fee(self, age, income):
    fee = (income / age) * 150

    return fee


###### Main
# Hospital instantiations for Maple Woods
math_clinic = MapleWoods('Maple Woods', 'The Math Clinic', '2601 NE Barry Rd')
comp_sci_psychiatry = MapleWoods('Maple Woods', 'The Comp-Sci institute of Psychiatry', '2575 NE Barry Rd')

# Hospital instantiations for Penn Valley
humanities_physical_therapy = Penn('Penn Valley', 'The Humanities department of Physical Therapy', '3201 SW Trafficway')

print(f'Campus locations for {Hospital.org}')
print('--------------------------------------------')
print(f'Maple Woods Math Clinic: {math_clinic.address}')
print(f'Maple Woods Comp-Sci Psychiatry {comp_sci_psychiatry.address}')
print(f'Penn Valley Humanities Physical Therapy: {humanities_physical_therapy.address}')
print('')

print('Student Costs')
print('--------------------------------------------')
cost_for_martha = math_clinic.fee(22, 10000, 3)
print(f'Marsha:  {locale.currency(cost_for_martha)} ({math_clinic.campus})')

cost_for_shelley = math_clinic.fee(35, 75000, 1)
print(f'Shelley: {locale.currency(cost_for_shelley)} ({math_clinic.campus})')

cost_for_janet = humanities_physical_therapy.fee(45, 95000)
print(f'Janet:   {locale.currency(cost_for_janet)} ({humanities_physical_therapy.campus})')
