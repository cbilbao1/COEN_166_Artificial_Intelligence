#Exercise 10.2

class PersonClass: # define a class object
    def basicinfo(self, name, age): 
    self.name=name 
    self.age=age
    def display(self): 
    print(self.name, '\n', self.age, '\n')
class StudentClass(PersonClass): # inherits basicinfo and display
    def moreinfo(self, university, major): # create moreinfo 
    print(self.name + ' is a ' + major + ' student ' + 'from ' + university)
student=StudentClass() # make one instance 
student.basicinfo('Cathy', 20)
student.display()
student.moreinfo('Santa Clara University', 'CSE')