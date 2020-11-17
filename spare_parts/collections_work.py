import collections
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
