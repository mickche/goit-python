fahrenheit_temps = [32, 68, 100, 212]

celsius_temps = list(map(lambda f: (f - 32) * 5/9, fahrenheit_temps))

print(celsius_temps)