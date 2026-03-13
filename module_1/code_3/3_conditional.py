# CALCULATOR
# CREATE A PROGRAM THAT ALLOWS YOU TO ADD, SUBTRACT, MULTIPLY AND DIVIDE 2 NUMBERS.

# PARTS OF A PROGRAM
# 1 - INPUT DATA
# 2 - PROCESS
# 3 - OUTPUT DATA


'''
print("*********************");
print("    Conditional 1    ");
print("*********************");


# 1 - INPUT DATA
num_1 = int(input("number 1: "))
num_2 = int(input("number 2: "))
operation = input("Enter operation (+ - x /): ")

# 2 - PROCESS
if operation == "+":
    result = num_1 + num_2
else:
    result = num_1 -num_2

# 3. OUTPUT DATA
'''
#print(f"{num_1} {operation} {num_2} = {result}")


'''
'''
print("*********************");
print("    Conditional 2    ");
print("*********************");


# 1 - INPUT DATA
num_1 = int(input("number 1: "))
num_2 = int(input("number 2: "))
operation = input("Enter operation (+ - x /): ")

# 2 - PROCESS
if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "X":
    result = num_1 * num_2
elif operation == "/":
    result = num_1  / num_2
else:
    print("error")
    exit()

# 3 - OUTPUT DATA
print(f"{num_1} {operation} {num_2} = {result}")