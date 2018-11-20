word = raw_input("what do you want to search")  # sets input
# open the file and reads all of it
f = open("/Users/noahfedosoff_S/Documents/Projects/Unit4/In_Class_Book.txt").read()
print(f.count(word))  # based on what you input this will give you a count
