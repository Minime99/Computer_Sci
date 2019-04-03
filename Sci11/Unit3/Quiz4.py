# # REVIEW:
# write out a number from 1 to n using a for and while
nn = int(input("give a natural number"))
for x in range(1, nn+1):
    print(x)

tick = 1
nn = int(input("give a natural number"))
while tick < nn+1:
    print(tick)
    tick = tick + 1

# # REVIEW:
# write a number in reverse using both a for and while
nn = int(input("give a natural number to write in reverse"))
for x in range(nn, 0, -1):
    print(x)

nn = int(input("give a natural number to write in reverse"))
while nn > 0:
    print(nn)
    nn = nn - 1
