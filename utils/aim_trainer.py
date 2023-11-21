import random
import time

for i in range(200):
    print("o", end="")

while True:
    spaces = random.randint(2, 200)
    for i in range(spaces):
        print(" ", end="")
    print("X")
    for i in range(202-spaces):
        print(" ", end="")
    print("\n")
    time.sleep(1)
