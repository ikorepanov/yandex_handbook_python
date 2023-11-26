warehouse_distance = int(input())
shop_distance = int(input())
speed = int(input())

result = (shop_distance - warehouse_distance) / speed

print('%.2f' % result)
