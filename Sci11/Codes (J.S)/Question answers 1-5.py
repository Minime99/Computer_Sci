
print ("   ")
for x in range(101):
    print(x)
    
GENE1="ATGTTGATGTG"
GENE2=GENE1[9:]
GENE3=GENE1[0:2]
GENE4=GENE1[2]+GENE1[4]+GENE1[6]+GENE1[8]+GENE1[10]
GENE5=GENE1[0:3]+GENE1[8:11]
print(GENE1,GENE2,GENE3,GENE4,GENE5)


page = ["this is","a city","on fire"]
for line in page:
    sentences = line + "."
    print (sentences)


d = {"France":"Paris","Belgium":"Brussels","Mexico":"Mexico City","Argentina":"Buenos Aires","China":"Beijing"}
import collections
d = sorted (d)
print (d)


months = [
    'January',
    'Feburary',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']
        
year  = input('Year: ')
month = input('Month (1-12): ')
day   = input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

ordinal = day + endings[day_number-1]
print month_name + ' ' + ordinal + ', ' + year






