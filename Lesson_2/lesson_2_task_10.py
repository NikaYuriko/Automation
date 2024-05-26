
def bank(x, y):
    for x in range(1, y+1):
        count = x + (x/10)
        x = count
    print(round(count, 3))
bank(20000, 12)


