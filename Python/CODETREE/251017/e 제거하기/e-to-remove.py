string = input()
idx = string.find('e')

string_list = list(string)
string_list.pop(idx)

string = ''.join(string_list)
print(string)