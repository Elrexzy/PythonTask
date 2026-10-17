list_employees = [("John", "IT", 50000), ("Jane", "HR", 45000), ("Mike", "IT", 60000), ("Sara", "Finance", 70000)]

for name, department, salary in list_employees:
      print("Nmae: ", name)
      print("Department: ", department)
      print("Salary: ", salary)

employees = []      
for name, department, salary in list_employees:     
      if department == "IT":
            employees.append(department)
print(employees)

for name, department, salary in list_employees:
      if salary > 55000:
            employees.append(salary)
print(employees)
