string = input()
length = len(string)

string = string[:1] + 'a' + string[2:]
string = string[:length - 2] + 'a' + string[length -1:]

print(string)