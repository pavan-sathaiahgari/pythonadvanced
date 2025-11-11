# Write a program to generate a Multiplication table using While Loop.
# Build the function which can take custom numbers.

# n = int(input('Enter number for multiplication ='))

# def table(n):
#     a = 1
#     while a < 11:
#         print((n), "x", (a), "=", (n * a))
        
#         a = a + 1
# n = int(input('Enter number for multiplication ='))

# table(n)




# def table(n):
#     a = 1
#     while a < 11:
#         print(f'{n} x {a} = {n * a}')
#         a = a + 1
# n = int(input('Enter number for multiplication ='))

# table(n)




# def table(n):
#     if n % 2 == 0:
#         a = 1
#         while a < 11:        
#             print(f'{n} x {a} = {n * a}')
#             a = a + 1
#     else:
#         print('pls enter a even num')
# table(6)




def table(n):
    if n % 2 != 1:
        a = 0
        while a < 11:
            print(f'{n} x {a} = {n * a}')
            a = a + 1
    else:
        print("The given number is odd")  

table(4)      