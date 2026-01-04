# Part 1
dial = 50
count = 0
with open("day1_input.txt", 'r') as file:
    for line in file:
        num = int(line[1:])
        
        if (line[0] == 'L'):
            dial -= num
        if (line[0] == 'R'):
            dial += num
        
        while (dial < 0 or dial > 99):
            if (dial < 0):
                dial += 100
            if (dial > 99):
                dial -= 100
        
        if (dial == 0):
            count += 1
print(count)

# Part 2
dial = 50
count = 0
with open("day1_input.txt", 'r') as file:
    for line in file:
        num = int(line[1:])
        
        for i in range(num):
            if (line[0] == 'L'):
                dial -= 1
            if (line[0] == 'R'):
                dial += 1
            
            if (dial < 0 or dial > 99):
                if (dial < 0):
                    dial += 100
                if (dial > 99):
                    dial -= 100
            
            if (dial == 0):
                count += 1
print(count)