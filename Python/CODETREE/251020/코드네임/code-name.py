MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))


class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

    def __str__(self):
        return f"{self.codename} {self.score}"

agents = []
for i in range(MAX_N):
    agents.append(Agent(codenames[i], scores[i]))

min_agent = min(agents, key=lambda agent: agent.score)
print(min_agent)