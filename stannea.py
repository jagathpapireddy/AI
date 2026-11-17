import random
import math

def f(x):
    return x * x

x = float(input("Enter initial value: "))
T = float(input("Enter initial temperature: "))
cooling = float(input("Enter cooling rate (e.g. 0.95): "))

best = x

while T > 0.1:
    new_x = x + random.uniform(-1, 1)

    delta = f(new_x) - f(x)

    if delta < 0 or random.random() < math.exp(-delta / T):
        x = new_x

    if f(x) < f(best):
        best = x

    T = T * cooling

print("Best solution:", round(best, 4))
print("Minimum value:", round(f(best), 4))
