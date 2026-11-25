#init is a method or constructor executes as objects get created
class Dog:

  def __init__(self,name,age):
    self.name=name
    self.age= age
    

my_dog= Dog("gru",15)

print(my_dog.name)

class Cat(Dog):
 def __init__(self,name,colour):
    super().__init__(name,"age")
    #self.name=name
    #self.eye=eye
    self.colour=colour

obj =Cat("meow","2")
print(obj.name,age)
print(obj.eye)
