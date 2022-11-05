class Grandparents:
    height = 170
    age = 60
    sick = "COVID"
class Parents(Grandparents):
     age = 40
class Children(Parents):
     height = 150
     def __init__(self):
         print(self.sick)
         print(self.age)
         print(self.height)
daun = Children()