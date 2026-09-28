module_name = "Student Details"

name = "rohan"
age = 20
course = "Computer Science"
marks = 85
percentage = 85.5
passed = True

print("Module Name:", module_name)
print("\nVariables:")

for variable, value in locals().copy().items():
    if variable != "module_name" and not variable.startswith("__"):
        print(variable, "=", value)