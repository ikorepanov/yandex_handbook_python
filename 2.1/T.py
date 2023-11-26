# total_weight, total_price, first_price, second_price = int(input()), int(input()), int(input()), int(input())

total_weight = 32
total_price = 285
first_price = 300
second_price = 240

second_weight = int(total_weight * (total_price - first_price) / (second_price - first_price))
first_weight = int(total_weight - second_weight)

print(first_weight, second_weight)
