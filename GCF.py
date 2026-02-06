
# Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.

number1 = int(input("enter number 1: "))

number2 = int(input("enter number 2: "))

factor1 = [1, number1]
factor2 = [1, number2]

for i in range(2,number1):
    if(number1 % i  ==0):
        factor1.append(i)


for i in range(2,number2):
    if(number2 % i  ==0):
        factor2.append(i)

print(factor1, factor2)

common = []

for i in factor1:
    if i in factor2:
        common.append(i)

gcf = str(max(common))
print("Greatest common factor: " + gcf)

    