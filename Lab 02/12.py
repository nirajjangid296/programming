basic_salary = float(input("Enter the Basic Salary: "))
hra = 0.20 * basic_salary   
ta = 0.05 * basic_salary    
da = 0.10 * basic_salary
gross_salary = basic_salary + hra + ta + da
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("TA:", ta)
print("DA:", da)
print("Gross Salary:", gross_salary)