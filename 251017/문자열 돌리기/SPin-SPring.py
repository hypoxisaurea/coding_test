string = input()
length = len(string)

for i in range(length+1):
    print(string)
    string = string[-1] + string[0:length-1]