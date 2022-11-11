




from prettytable import PrettyTable
import random
import pandas as pd

table = PrettyTable()


data = pd.read_csv('random_names_fossbytes.csv')

print(data)
for i in data:
    names = []
    name = []
    names.append(name)
    print(names)

table.field_names = ['Name', 'No', 'Status']
for i in range(1,1000):
    pd.DataFrame(table.add_row([random.choice(['Skeeper','Loyaltie', 'Moses', 'Jaicah']), random.randint(1,23), random.choice(['Married', 'Single'])]))

data = i

print(data)

