# 🟠 Task 4 — Employee Salary
# Ask for:
# - Employee name
# - Basic salary
# - HRA
# - Allowance
# Calculate:

# Total Salary = Basic Salary + HRA + Allowance


#CODE


emp_name  = input("Enter Employee Name :")
b_salary= int(input("Enter Basic Salary :"))
hra =  int (input("Enter HRA :"))
allowance = int(input("Enter Allowance :"))
salary = b_salary+hra+allowance
print()
print()
print("--------Employee Details----------")
print()
print("Employee : ",emp_name)
print("Basic Salary : ", b_salary)
print("HRA : ", hra)
print("Allowance : ",allowance)
print()
print("-------------------------------------------")
print("Total Salary :", salary)
print()
print("-------------------------------------------")

#OUTPUT

# Enter Employee Name :Menaga J
# Enter Basic Salary :45500
# Enter HRA :300
# Enter Allowance :200


# --------Employee Details----------

# Employee :  Menaga J
# Basic Salary :  45500
# HRA :  300
# Allowance :  200

# -------------------------------------------
# Total Salary : 46000

# -------------------------------------------
