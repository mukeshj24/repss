
class Employee:
    def __init__(self,name, department):
        self.name=name
        self.dept=department
    
    def greet(self):
        print(f"welcome to the {self.name}  dept : {self.dept}")