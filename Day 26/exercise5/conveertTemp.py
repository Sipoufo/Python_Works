weather_c = {
    "Monday": 12,
    "Thursday": 14,
    "Wednesday": 15,
    "Tuesday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

result = {key: ((val*9/5)+32) for (key, val) in weather_c.items()}

print(result)