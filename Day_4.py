#### First task


with open('input_day4.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]
    
counter = 0
for elt in data:
    elf1, elf2 = elt.split(",")
    elf1_start, elf1_end = elf1.split("-")
    elf2_start, elf2_end = elf2.split("-")
    
    if (int(elf1_start) >= int(elf2_start)) and (int(elf1_end) <= int(elf2_end)):
        counter += 1
    elif (int(elf2_start) >= int(elf1_start)) and (int(elf2_end) <= int(elf1_end)):
        counter += 1

print(counter)


#### Second task


with open('input_day4.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]
    
counter = 0
for elt in data:
    elf1, elf2 = elt.split(",")
    elf1_start, elf1_end = elf1.split("-")
    elf2_start, elf2_end = elf2.split("-")
    
    if (int(elf1_end) >= int(elf2_start)) and (int(elf1_end) <= int(elf2_end)):
        counter += 1
    elif (int(elf2_end) >= int(elf1_start)) and (int(elf2_end) <= int(elf1_end)):
        counter += 1

print(counter)

#Adding a comment