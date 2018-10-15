for x in range(1, 101):
    print(x)

GENE1="ATGTTGATGTG"
GENE2=GENE1[9:11] #TG
GENE3=GENE1[0:2] #AT
GENE4=GENE1[2] + GENE1[4] + GENE1[6] + GENE1[8] + GENE1[10] #GTAGG
GENE5=GENE1[0] + GENE1[1] + GENE1[2] + GENE1[8] + GENE1[9] + GENE1[10] #ATGGTG
print(GENE1)
print(GENE2)
print(GENE3)
print(GENE4)
print(GENE5)

PAGE = ['line 1 is good but', 'line 2 is better', 'and also. line 3', 'line 4 is also good.']
for line in PAGE:
    print(line)
    if '.' in line:
        for c in line:
            if c == '.':
                break

d = {'France':'Paris','Belgium':'Brussels','Mexico':'Mexico City','Argentina':'Buenos Aires','China':'Beijing'}
#d=sorted(d)
for x in d:
    print(x, d[x])



# Print out a date, given year, month, and day as numbers
months = [
 'January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December'
]

# A list with one ending for each number from 1 to 31

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
 + ['st', 'nd', 'rd'] + 7 * ['th'] \
 + ['st']
year = raw_input('Year: ')
months = raw_input('Month (1-12): ')
day = raw_input('Day (1-31): ')
month_number = int(months)
day_number = int(day)

# Remember to subtract 1 from month and day to get a correct index

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)

#An example of a session with this program might be as follows:

'''Year: 1974
Month (1-12): 8
Day (1-31): 16
August 16th, 1974'''

#The last line is the output from the program.
