import matplotlib.pyplot as plt

"""salary= [67666,46500,41000]
department=["IT","HR","Sales"]

plt.bar(department,salary)
plt.show()"""

#histogram

"""salaries=[30000, 45000,60000,75000,9000,52000,68000,48000]
plt.hist(salaries,bins=5)
plt.show()"""

 #scatterd
#departments=["sales", "HR", "IT", "IT", "Finance", "Sales", "IT", "HR"]

id=[1,2,3,4,5,6,7,8,]

salary=[30000,45000,60000,75000,90000,52000,68000,48000]

plt.scatter(id, salary)
plt.xlabel(id)
plt.ylabel(salary)
plt.show()