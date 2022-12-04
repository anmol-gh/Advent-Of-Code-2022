with open("day01_input.txt") as f:
    text = f.read()
    s = text.split("\n")
    first = 0
    total = 0
    value = []
    for i in s:
        if i == "":
            value.append(total)
            total = 0
        else:
            total += int(i)
    value = sorted(value)
    print("The maximum calorie an individual elf is carrying is", value[-1])
    print("The sum of top 3 calories is", value[-1] + value[-2] + value[-3])