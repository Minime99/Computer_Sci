import random
def roll_die(sides):
    r = random.randrange(1, sides+1)
    return r

def take_turn(player):
    point=0
    keep_rolling=1
    print ("its your turn player "), player
    raw_input( "press enter to begin")
    while keep_rolling==1:
        r = roll_die(6)
        print ("you got a", r)
        if r == 1:
            point=0
            keep_rolling=0
        else:
            point += r
            print (" your total is", point)
            y= raw_input ("do you want to continue? y=yes n=no")
            if y== "y":
                keep_rolling= 1
            if y== "n":
                break
    print ("your turn is over")
    return point

def show_instructions():
    print ("To win one player has 100 or more points")
    print ()

def main():
    show_instructions()
    p1 = 0
    p2 = 0
    while p1<100 and p2<100:
        print (" Player points are:" +str(p1))
        print (" Player points are:" +str(p2))
        r = take_turn(1)
        p1 += r
        print ("Player points are:" +str(p1))
        print ("Player points are:" +str(p2))
        r = take_turn(2)
        p2 += r
        print (" The game is over")
        print (" Player points are:" +str(p1))
        print (" Player points are:" +str(p2))
    if p1>p2:
        print (" Player one is the winner")
    elif p2>p1:
        print ("player two is the winner")
    else:
        print (" Tie game")

main()
take_turn(1)
take_turn(2)
