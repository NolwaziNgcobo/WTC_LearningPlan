price = 50
total = 0

while total < price:
    print(f'Amount Due: {price - total}')
    coin = int(input('insert coin: '))


    if coin in [25, 10, 5]:
        total += coin

    else:
        continue
print(f'change Owed: {total - price}')