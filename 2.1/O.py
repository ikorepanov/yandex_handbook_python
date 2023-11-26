hours = int(input())
minutes = int(input())
delivery_time = int(input())

# hours = 8
# minutes = 0
# delivery_time = 65

new_minutes = minutes + delivery_time
additional_hours = new_minutes // 60
additional_minutes = (new_minutes - additional_hours * 60) % 100

some = hours + additional_hours
some_some = some // 24
result = (some - 24 * some_some) % 100

# result = 0.45
# additional_minutes = 0.81

print('%.2d' % result, ':', '%.2d' % additional_minutes, sep='')
