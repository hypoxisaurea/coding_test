s, q = input().split()
q = int(q)

for i in range(q):
    query = list(input().split())

    if query[0] == '1':
        a = int(query[1]) - 1
        b = int(query[2]) - 1
        s_list = list(s)

        s_list[a], s_list[b] = s_list[b], s_list[a]
        s = ''.join(s_list)

    elif query[0] == '2':
        x = query[1]
        y = query[2]

        s = s.replace(x, y)

    print(s)