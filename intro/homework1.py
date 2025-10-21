while True:
    start_str = input("Enter the start of the range: ").strip()
    if start_str.lstrip('-').isdigit():
        start_num = int(start_str)
        break
    else:
        print("Error! Please enter an integer.")

while True:
    end_str = input("Enter the end of the range: ").strip()
    if end_str.lstrip('-').isdigit():
        end_num = int(end_str)
        break
    else:
        print("Error! Please enter an integer.")

while True:
    step_str = input("Enter the step (press Enter for default): ").strip()
    if step_str == "":
        increment = 1
        break
    elif step_str.lstrip('-').isdigit():
        increment = int(step_str)
        if increment > 0:
            break
        else:
            print("Step must be a positive number.")
    else:
        print("Error! Please enter a number or press Enter.")

if start_num <= end_num:
    for n in range(start_num, end_num + 1, increment):
        print(n, end=" ")
else:
    for n in range(start_num, end_num - 1, -increment):
        print(n, end=" ")
print()
