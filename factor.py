# Create a function that accepts an input and determines all factors of the number.

number = int(input("enter a number"))
# number = str(number)
# print("1 ," + number)

# if (number % 2 > 0):
#     print("2")
# if(number % 3 > 0):
#     print("3")

# range = [1-100]
factor = []

for i in range(2,number):
    if(number % i  ==0):
        factor.append(i)

print("1", factor, number)