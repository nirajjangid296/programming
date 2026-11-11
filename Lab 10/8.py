country_count = int(input())
capitals = {}

for i in range(country_count):
    country, capital = input().split()
    capitals[country] = capital

requested_country = input()
print(capitals.get(requested_country, "Not found"))
