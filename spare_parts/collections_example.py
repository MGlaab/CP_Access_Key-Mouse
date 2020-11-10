import collections

Person = collections.namedtuple('Person', ('name', 'age', 'gender'))

ben = Person(name='Ben', age=8, gender='boy')
harper = Person('Harper', age=6, gender='girl')

friends_list = (ben,harper)


for f in friends_list:
    print(f.name, "is a", f.age, "year old", f.gender, ".")


KeyPress = collections.namedtuple('KeyPress', ('inputtype', 'buttontopress'))

m1b1 = KeyPress('KEYBOARD', 'KeycodeA')

print(m1b1.inputtype)
