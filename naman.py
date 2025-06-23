class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Mike", "Olsen")
x.printname()
     
class Student(Person):
  def __init__(self,fname, lname,mname):
    Person.__init__(self,fname,lname)
    self.mastname = mname

  def printname(self):
   # Person.printname(self)
    print(self.firstname,self.lastname,self.mastname)
  
x = Student("Mike", "Olsen","tyson")
x.printname()