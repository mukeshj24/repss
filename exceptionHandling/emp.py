import datetime import datetime
class Employee:
    def __init__(self,name, department):
        self.name=name
        self.dept=department
    
    def greet(self):
        print(f"welcome to the {self.name}  dept : {self.dept}")

    def join (self):
        date=self.datetime()
        print(f"self.name" is joined on {date}")

