with open("day02_input.txt") as f:
    global total
    total = 0
    def check(opponent, char, total):
        if opponent == "A":
            if char == "X":
                total += 3
            elif char == "Y":
                total += 6
        elif opponent == "B":
            if char == "Y":
                total += 3
            elif char == "Z":
                total += 6
        elif opponent == "C":
            if char == "Z":
                total += 3
            elif char == "X":
                total += 6
        return (total)
    def first_solution(total):
        games = f.readlines()
        for game in games:
            if game[2] == "X":
                total += 1
                total = check(game[0], "X",total)
            elif game[2] == "Y":
                total +=2
                total = check(game[0], "Y", total)
            else:
                total += 3
                total = check (game[0], "Z", total)
        return total
    # total = first_solution(total)
    print("The total points are", total)
    
    def second_solution(total):
        games = f.readlines()
        for game in games:
            if game[2] == "Y":
                total += 3
                if game[0] == "A":
                    total += 1
                elif game[0] == "B":
                    total += 2
                else: 
                    total += 3
            elif game[2] == "Z":
                total += 6
                if game[0] == "A":
                    total += 3
                elif game[1] == "B":
                    total += 1
                else:
                    total += 2
            else: 
                if game[0] == "A":
                    total += 3
                elif game[0] =="B":
                    total += 1
                else:
                    total += 2
        return total
    total = 0
    total = second_solution(total)
    print("The total points in part two are ", total)
