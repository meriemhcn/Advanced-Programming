cities = []
while True:
    city_name = input("Enter a city name (or type 'stop' to end): ")
    if city_name.lower() == 'stop':
        break
    else:
        cities.append(city_name)

city_population = [(city, len(city) * 1000000) for city in cities]
city_population.sort(key=lambda x: x[1], reverse=True)

for city, population in city_population:
    print(f"The city of {city} has a population of {population} citizens.")
