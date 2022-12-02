with open("day01_input.txt") as f:
    text = f.read()
    s = text.split("\n")
    first = 0
    second = 0
    third = 0
    total = 0
    elf = 0
    value = []
    for i in s:
        if i == "":
            elf += 1
            value.append(total)
            if total > first:
                third = second
                second = first
                first = total
            total = 0
        else:
            total += int(i)
    print(first, second, third, elf, first + second + third)
    value = sorted(value)
    print( value[-1] + value[-2] + value[-3])