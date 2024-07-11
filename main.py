import time
import random
contestants = []
for contestant in range(1, 456 + 1):
    contestants.append(contestant)


def greenlight1():
    print("! GREEN LIGHT !")
    global moved_green
    moved_green = random.sample(contestants, round(0.8 * len(contestants)))
    print(f"Moved: {moved_green}")
    static_contestants = []
    for num in contestants:
        if num not in moved_green:
            static_contestants.append(num)
    print(f"Static: {static_contestants}")
    print("Eliminated: None")
    print(" ")


def redlight1():
    print("! RED LIGHT !")
    moved_red = random.sample(contestants, round(0.05 * len(contestants)))
    print(f"Moved: {moved_red}")
    for num in contestants:
        if num in moved_red:
            contestants.remove(num)
    print(f"Static: {contestants}")
    print(f"Eliminated: {moved_red}")
    print(" ")


def greenlight2():
    print("! GREEN LIGHT !")
    global moved_green2
    moved_green2 = random.sample(contestants, round(0.8 * len(contestants)))
    winning_contestants1 = []
    for player in moved_green2:
        if player in moved_green:
            winning_contestants1.append(player)
    for contest4nt in contestants:
        if contest4nt in winning_contestants1:
            contestants.remove(contest4nt)
    print(f"Moved: {moved_green2}")

    static_contestants = []
    for num in contestants:
        if num not in moved_green2:
            static_contestants.append(num)
    print(f"Static: {static_contestants}")
    print(f"Won: {winning_contestants1}")
    print("Eliminated: None")
    print(" ")


def redlight2():
    print("! RED LIGHT !")
    moved_red2 = random.sample(contestants, round(0.05 * len(contestants)))
    print(f"Moved: {moved_red2}")
    for num in contestants:
        if num in moved_red2:
            contestants.remove(num)
    print(f"Static: {contestants}")
    print(f"Eliminated: {moved_red2}")
    print(" ")


def greenlight3():
    print("! GREEN LIGHT !")
    moved_green3 = random.sample(contestants, round(0.8 * len(contestants)))
    global winning_contestants2
    winning_contestants2 = []
    for player in moved_green3:
        if player in moved_green or player in moved_green2:
            winning_contestants2.append(player)
    for contest4nt in contestants:
        if contest4nt in winning_contestants2:
            contestants.remove(contest4nt)
    print(f"Moved: {moved_green3}")
    static_contestants = []
    for num in contestants:
        if num not in moved_green3:
            static_contestants.append(num)
    print(f"Static: {static_contestants}")
    print(f"Won: {winning_contestants2}")
    print("Eliminated: None")
    print(" ")


def redlight3():
    print("! RED LIGHT !")
    eliminated_players = []
    for player in contestants:
        if player not in winning_contestants2:
            eliminated_players.append(player)
    print(f"Eliminated: {eliminated_players}")


greenlight1()
time.sleep(5)
redlight1()
time.sleep(5)
greenlight2()
time.sleep(5)
redlight2()
time.sleep(5)
greenlight3()
time.sleep(5)
redlight3()

