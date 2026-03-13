# CREATE A PROGRAM THAT ALLOWS YOU TO ADD 2 NUMBERS
# PYTHON IS DYNAMICALLY TYPED

# PARTS OF A PROGRAM
# 1 - INPUT DATA
# 2 - PROCESS
# 3 - OUTPUT DATA


''' 
print("*********************");
print("Data types program 1");
print("*********************");

# 1 - INPUT DATA
num_1 = 1
num_2 = 2

# 2 - PROCESS
sum = num_1 + num_2

# 3 - OUTPUT DATA
print("The sum is: ", sum);
'''



print("*********************");
print("Data types program 2");
print("*********************");

# 1 - INPUT DATA
num = 3
print(type(num))
num_1 = int(input("Enter first value: ")) # INTEGER
#num_1 = (input("Enter first value"))    # STRING
print(type(num_1))
num_2 = int(input("Enter second value: "))
print(type(num_2))

# 2 - PROCESS
sum = num_1 + num_2
print(type(sum))

# 3 - OUTPUT DATA
print("The sum is: ", sum);     # con coma se concatena 
print("The sum is: "+ str(sum));# con suma no se puede sumar letra con número 


