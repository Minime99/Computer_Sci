health = 100

while (health > 0):
    x = input("hit?")
    if x == "yes":
        health = health-10
        print("hit! health is", health)
    else:
        print("no hit health is", health)
if health == 0:
    print("you are dead")
