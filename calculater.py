print()
print("Welcome to Calculator...")
print()
print("Choose what you want to do....")
print("Choose 1 to Multiply two numbers")
print("Choose 2 to Add two numbers")
print("Choose 3 to Substract two numbers")
print("Choose 4 to Devide two numbers")
print("type your choosen option here Enter 1/2/3/4")
option = int(input())
if option == 1:
    number_1 = int(input("input first number:"))
    number_2 = int(input("input sencond number:"))
    print("your result is =>")
    print(number_1*number_2)

elif option == 2:
    number_1 = int(input("input first number:"))
    number_2 = int(input("input sencond number:"))
    print("your result is =>")
    print(number_1+number_2)

elif option == 3:
    number_1 = int(input("input first number:"))
    number_2 = int(input("input sencond number:"))
    print("your result is =>")
    print(number_1-number_2)
elif option == 4:
    number_1 = int(input("input first number:"))
    number_2 = int(input("input sencond number:"))
    print("your result is =>")
    print(number_1/number_2)
else:
    print("choose from given options")

