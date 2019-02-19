cities = ["Bangalore", "Mumbai", "Delhi"]

with open("cities.txt", "w") as city_file:
    for city in cities:
        print(city, file=city_file)  # this is file argument
        # print(city, file=city_file, flush=True)  # flush parameter is needed if you want the data to be written
        # faster but now a days computers are super fast, so er don't need it


with open("cities.txt", "r") as jabb:
    for line in jabb:
        print(line, end="")  # this is end argument to the function
