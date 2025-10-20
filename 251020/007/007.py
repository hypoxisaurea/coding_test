secret_code, meeting_point, time = input().split()
time = int(time)

class Secret:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

me = Secret(secret_code, meeting_point, time)

print(f"secret code : {me.secret_code}")
print(f"meeting point : {me.meeting_point}")
print(f"time : {me.time}")