def pages(numbers):
    list = [200, 230, 10, 30, 40, 50, 600, 344, 5234, 564, 645, 36, 457, 464, 3, 526463, 4234]
    a = 0

    for x in range(1000):
        lst = list[x]

        a += int(numbers / lst)
        numbers = int(numbers % lst)

        if numbers > 0:
            return a


print(pages(433454))
print(pages(53421))
