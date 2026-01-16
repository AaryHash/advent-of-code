# Part 1
sum = 0
with open("2025/day2_input.txt", "r") as file:
    id_ranges = file.read().split(sep=',')
    for range in id_ranges:
        first_num = int(range.split(sep='-')[0])
        second_num = int(range.split(sep='-')[1])
        ptr = first_num
        while (ptr <= second_num):
            midpt = len(str(ptr)) // 2
            if (str(ptr)[0:midpt] == str(ptr)[midpt:]):
                sum += ptr
            ptr += 1
print(sum)