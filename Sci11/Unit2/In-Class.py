# 1.
for x in range(1, 101):
    print(x)
# 2.
GENE1 = str('ATGTTGATGTG')

GENE2 = GENE1[9:11]
print(GENE2)

GENE3 = GENE1[0:2]
print(GENE3)

GENE4 = GENE1[2] + GENE1[4] + GENE1[6] + GENE1[8] + GENE1[10]
print(GENE4)

GENE5 = GENE1[0:3] + GENE1[8] + GENE1[9] + GENE1[10]
print(GENE5)

# 3.
page = ["This is my name", "Its is naoh", "Keep going"]
for line in page:
    sentences = line + "."
    print(sentences)
# 4.

d = {"France": "Paris", "Belgium": "Brussels", "Mexico": "Mexico City",
     "Argentina": "Buenos Aires", "China": "Beijing"}
d = sorted(d)
print(d)

# 5.
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
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)
