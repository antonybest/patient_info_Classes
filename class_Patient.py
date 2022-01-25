"""
estimation key:
    name = patients name
    age = patients age
    sex: patient’s biological identification, 0 for male and 1 for female
    bmi: patient BMI
    num_of_children: number of children patient has
    smoker: patient smoking status, 0 for a non-smoker and 1 for a smoker
"""

class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):

    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):

    self.estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500

    print(f"\n{self.name}'s estimated insurance cost is {self.estimated_cost} dollars")

  def update_age(self, new_age):

    self.age = new_age

    print(f"\n{self.name} is now {self.age} years old")

    self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):

    self.num_children = new_num_children

    if self.num_children == 1:
      print(f"\n{self.name} has {self.num_children} child")

    if self.num_children > 1:
      print(f"\n{self.name} has {self.num_children} children")

    self.estimated_insurance_cost()

  def patient_profile(self):

    patient_information = {}

    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker

    return patient_information


patient_1 = Patient(name="John Doe", age= 25, sex=1, bmi=22.2, num_of_children=2, smoker=0)

try:
  patient_1.estimated_insurance_cost()
except TypeError:
  print("please enter a numerical value in order to receice an estimate!!")

patient_1.update_age(26)

patient_1.update_num_children(4)

if patient_1.sex == 1:
  patient_1.sex = "male"
if patient_1.sex == 0:
  patient_1.sex = "female"
if patient_1.smoker == 1:
  patient_1.smoker = "smoker"
if patient_1.smoker == 0:
  patient_1.smoker = "non-smoker"

print(f"\nOur patient {patient_1.name} is {patient_1.age}. He is a {patient_1.sex}, his bmi is {patient_1.bmi}. He has {patient_1.num_of_children} children and is a {patient_1.smoker}.")

print()
print(patient_1.patient_profile())

# -------------------- END OF FILE ----------------------------