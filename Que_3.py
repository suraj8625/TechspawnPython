Employee = ["Amit","Manish","Mahi","Kirti","Mafin"]
Salary = [20000,30000,20000,40000,25000]
print("Original key list is : " + str(Employee))
print("Original value list is : " + str(Salary))
res = {}
for key in Employee:
    for value in Salary:
        res[key] = value
        Salary.remove(value)
        break
print("Resultant dictionary is : " + str(res))


