# input is user input
inputnumber = input("what is the number?")
outputnumber = ''
for c in inputnumber:
    s = int(c)**2  # ** means to the power
    outputnumber = outputnumber + str(s)
    print(s)

# takes the numbers inputed and then gives the product (*)
number1 = input("Firstnumber?")
number2 = input("Secondnumber?")
product = int(number1)*int(number2)
print("The product is:", product)
