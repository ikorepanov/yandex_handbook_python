# good = str(input())
# price = int(input())
# weight = int(input())
# money = int(input())

good, price, weight, money = input(), int(input()), int(input()), int(input())

# good = 'черешня'
# price = 2
# weight = 3
# money = 10

total = weight * price
change = money - total

price_result = f'{weight}кг * {price}руб/кг'
total_result = f'{total}руб'
money_result = f'{money}руб'
change_result = f'{change}руб'

print(f'{"=" * 16}Чек{"=" * 16}')
print(f'{"Товар:" : <10}{good : >25}')
print(f'{"Цена:" : <10}{price_result : >25}')
print(f'{"Итого:" : <10}{total_result : >25}')
print(f'{"Внесено:" : <10}{money_result : >25}')
print(f'{"Сдача:" : <10}{change_result : >25}')
print("=" * 35)
