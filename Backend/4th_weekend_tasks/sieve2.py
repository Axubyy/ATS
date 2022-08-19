class Employee:
    def __init__(self, name, id) -> None:
        self.id = id
        self.name = name


class Payroll:
    def __init__(self) -> None:
        self.employees = []

    def calculate_payroll(self):
        for employee in self.employees:
            print(employee.id)
            print(employee.name)


class SalaryEmployee:
    def calculate_payroll(self):
        return


class DailyEmployee:
    def calculator_payroll(self):
        return


emp = Employee(2, 'Ekene')
p = Payroll()
p.calculate_payroll()
