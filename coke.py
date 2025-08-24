#price of the coke bottle and your starting total
price = 50
total = 0

#loop while the condition is true
while total < price:
    print(f'Amount Due: {price - total}')
    coin = int(input('insert coin: '))

    #accepted coins
    if coin in [25, 10, 5]:
        total += coin

    #ignore other coins
    else:
        continue
print(f'change Owed: {total - price}')