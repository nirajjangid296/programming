basic_salary = float(input("Enter the Basic Salary: "))
hra = 0.20 * basic_salary
ta = 0.05 * basic_salary
da = 0.10 * basic_salary
gross_salary = basic_salary + hra + ta + da
if gross_salary < 300000:
    tax_rate = 0
elif gross_salary <= 1000000:
    tax_rate = 10
elif gross_salary <= 2500000:
    tax_rate = 20
else:
    tax_rate = 30
income_tax = (tax_rate / 100) * gross_salary
print("Gross Salary:", gross_salary)
print("Income Tax Rate:", tax_rate, "%")
print("Income Tax Amount:", income_tax)
