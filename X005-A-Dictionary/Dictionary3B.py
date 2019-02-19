locations = {0: "At the centre!",
             1: "At the hill",
             2: "In the valley"}
exits = [{"Q": 0},
         {"W": 2, "Q": 0},
         {"E": 1, "Q": 0}]  # this is a set of dictionaries

loc = 1
availableExits = ", ".join(exits[loc].keys())

print(locations[loc])

print(availableExits)
direction = "W"
if direction in exits[loc]:
    loc = exits[loc][direction]
    print(locations[loc])
else:
    print("You cant go in that direction")
