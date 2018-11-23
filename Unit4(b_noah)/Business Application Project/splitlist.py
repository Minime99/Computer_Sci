f = open('voters.txt', 'r')
voterlist = []
for name in f.readlines():
    voterlist.append([name.split()[0], name.split()[1]])
print(voterlist)


'''
cd Desktop/Atom/'Computer_Sci.'/'Unit4(b_noah)'/'Business Application Project'
'''
