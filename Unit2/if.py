x = 42  # 42 is even
if x % 2 == 0:  # “If” statements only follow the instructions of the following code when the boolean returned is true. “Else” can be added on to run if the previous boolean had been false.
    print('even')
else:
    print('odd')

x = 42
if x % 2 == 0:  # the % symbol means the Remainder of
    print('even')
else:
    print('odd')

x = input("what is your name?")  # if what you input is "noah" then your last name is Fedosoff
if x == "noah":
    print("your last name is Fedosoff")
else:
    print("who are you?")

food = "spam"
if food == "spam":
    print("ummm, my favorite!")
    print("I feel like saying it 100 times")
    print(100 * (food + "! "))

food = "cookies"
if food == "spam":
    print("ummm, my favorite!")
else:
    print("i must have spam!")

x = 43
y = 43

if x < y:
    print("what?")
elif x > y:
    print("really?")
else:
    print("they are the same!")

print("a or b?")
choice = input("what do you choose?")
if choice == "a":
    print("you said a")
elif choice == "b":
    print("you said b")
else:
    print("no")
x = 6
if 0 < x:
    if x > 10:
        print("x is a positive single digit")
