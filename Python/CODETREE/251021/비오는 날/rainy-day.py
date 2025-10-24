n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Rain:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def __str__(self):
        return f"{self.date} {self.day} {self.weather}"

forecasts = []
for i in range(n):
    forecast = Rain(date[i], day[i], weather[i])
    forecasts.append(forecast)

forecasts.sort(key=lambda forecast:forecast.date)

for i in range(n):
    if forecasts[i].weather == 'Rain':
        print(forecasts[i])
        break