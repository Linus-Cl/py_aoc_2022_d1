
file_path = "data.txt"
max_val_1 = 0
max_val_2 = 0
max_val_3 = 0
current_val = 0
data = open(file_path, 'r')
last_elf = False
line_val = 0

while not last_elf:
    
    line_val = data.readline()

    while not line_val == '\n':
        current_val += int(line_val.strip())
        line_val = data.readline()

        if line_val == 'end':
            last_elf = True
            line_val = '\n'

    if current_val > max_val_3:
        if current_val > max_val_2:
            if current_val > max_val_1:
                max_val_3 = max_val_2
                max_val_2 = max_val_1
                max_val_1 = current_val
            else:
                max_val_3 = max_val_2
                max_val_2 = current_val    
        else:
            max_val_3 = current_val       
    
    current_val = 0

print("The top 3 elfs carrying the most calories carry " + str(max_val_1 + max_val_2 + max_val_3) + " calories!")       
