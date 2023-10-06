#1
my_dict = {'name': 'Ahmed',
           'age': 20,
           'job': 'Engineer'}

print(my_dict.values())
print(my_dict.keys(), "\n")
print(my_dict['name'])
print("\n")
my_dict['age'] = 32
my_dict.update({"workplace": "GSG"})
print(my_dict, "\n")

#2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
mydict = {}

for k, v in my_tuple:
    mydict[v] = k

print(mydict, "\n")

#3
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict, "\n")

#4
dict = {'num1': 648, 'num2': 4194, 'num3': 60}
max0 = max(dict.values())
min0 = min(dict.values())
print(max0)
print(min0, "\n")

#5
my_dict0 = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
key_0 = 'ID' in my_dict
print(key_0, "\n")

#6
Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'],
                 'Market Share %': [27.99, 15.9, 9.36, 6.67]
                 }
list_dict = []
item = len(Languages2023['Programming Language'])
for x in range(item):
    new_item = {
        'Programming Language': Languages2023['Programming Language'][x],
                'Market Share %': Languages2023['Market Share %'][x]
                }
    list_dict.append(new_item)

print(list_dict)