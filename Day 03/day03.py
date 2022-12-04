with open("Day 03\day03_input.txt") as f:
    contents = f.readlines()
    first_priorities = 0
    for content in contents:
        first_part = content[0: (len(content)//2)]
        second_part = content[len(content)//2 : ]
        for content in first_part:
            if content in second_part:
                if ord(content) > 97 and ord(content) < 123:
                    first_priorities += ord(content) -96
                else:
                    first_priorities += ord(content) - 38
                break
    print("Sum of priorities of part 1 is", first_priorities)
    # Second Part
    index = 0
    second_priorities = 0
    for three_rucksacks in contents:
        three_rucksacks = contents[index:index +3]
        if index == len(contents):
            break
        index += 3
        for rucksack in three_rucksacks:
            for character in rucksack:
                if character in three_rucksacks[1] and character in three_rucksacks[2]:
                    if ord(character) > 97 and ord(character) < 123:
                        second_priorities += ord(character) -96
                        break
                    else:
                        second_priorities += ord(character) - 38
                    break
            break
    print("Sum of priorities of part 2 is", second_priorities)
