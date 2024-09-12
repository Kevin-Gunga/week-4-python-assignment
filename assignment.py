class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f'name:{self.name}, age:{self.age}, gender:{self.gender}')
        
obj = Person('kevin', 25, 'male')
obj.introduce()