person={}

while True :
    name =input('name:')
    age=input('age:')
    person[name]=age
    another=input('another y/n:')
    if another == 'y' :
        continue;
    else :
        break
ages=list(person.values())

for age in set(ages):
    count=ages.count(age)
    print(f'{age} years old - {count}')