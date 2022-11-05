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

class Wow:
    def _wow(self):
        print('Wow')
    def _hello(self):
        print('Hello')
some_obj = Wow()
some_obj._hello()
some_obj._wow()

