import random

money = 1000
rounds = 0
while money > 0 and rounds < 10: 
    rounds += 1
    money += 50 if random.random() < 0.5 else -50
    print(f" {rounds} {money}")

if money <= 0:
    print(f" {rounds} ")
else:
    print(f"{rounds} {money}.")
