
file_path = "data.txt"
max_val = 0
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

    if current_val > max_val:
        max_val = current_val
    
    current_val = 0

print("The elf carrying the most calories carrys " + str(max_val) + " calories!")       


