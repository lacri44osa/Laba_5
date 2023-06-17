class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Client:
    def __init__(self, client):
        self.client = client

class EmployeeList(Employee):
    def __init__(self, name, lastname, client):
        super().__init__(name, lastname)
        self.client = client.client

    def printer(self):
        print(f'{self.name} {self.lastname}: {self.client}')

client = Client("Sara")
e = EmployeeList(name="Tom", lastname="Smith", client=client)
e.printer()
