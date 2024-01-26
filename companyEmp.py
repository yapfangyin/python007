class Employee:
    #Initialiser#
    def __init__(self, first_name, last_name, emp_number):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_number = emp_number
        
    #Getter
    @property #decorator - still need this as it only shows the object in memory
    def print_emp_info(self):
        print(f"{self.emp_number}: {self.first_name} {self.last_name}")
    
    #Setter
    def first_name(self, var):
        self.first_name = var
        
    def last_name(self, var):
        self.last_name = var
        
    def emp_number(self, var):
        self.emp_number = var
