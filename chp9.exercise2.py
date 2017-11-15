#Luke Doughty-Rosas


class Employee:

    def __init__(self):
        self.name = ''
        self.ID_number = 0
        self.department = ''
        self.job_title = ''

    def set_info(self):
        self.name = input('Enter Employee: ')
        self.ID_number = input('Enter ID Number: ')
        self.department = input('Enter Department: ')
        self.job_title = input('Enter job Title: ')
        return [self.name, self.ID_number, self.department, self.job_title]

    def get_info(self):
        print('Name: %s\n'
            'ID Number: %s\n'
            'Department: %s\n'
            'Job Title: %s\n' %
            (self.name, self.ID_number, self.department, self.job_title)) 
    
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
empList = [emp1, emp2, emp3]
i = 0

emp1.set_info()
emp2.set_info()
emp3.set_info()


for each in empList:
    each.get_info()

