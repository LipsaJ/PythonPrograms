from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.level += 3
print(tim)

tim.level += 1
print(tim)

tim.level -= 2
print(tim)

tim.score = 500
print(tim)
