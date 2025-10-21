n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Info:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
    
informations = []
for i in range(n):
    info = Info(name[i], street_address[i], region[i])
    informations.append(info)

last_human = max(informations, key=lambda info:info.name)

print(f"name {last_human.name}")
print(f"addr {last_human.address}")
print(f"city {last_human.region}")