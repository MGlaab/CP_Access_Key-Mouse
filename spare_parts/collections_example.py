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

import pprint

button_list = []

for m in range(1,6):
    for b in range(1,6):
        button_list.append('m' + str(m) + 'b' + str(b))

print(button_list)
print(len(button_list))

fun_list = []

KeyPress = collections.namedtuple('KeyPress', ('inputtype', 'buttontopress'))

for f in range(0,25):
    fun_list.append(KeyPress('KEYBOARD', 'KeycodeA'))
print(len(fun_list))

lst_tuple = list(zip(button_list,fun_list))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lst_tuple)

print(len(lst_tuple))
