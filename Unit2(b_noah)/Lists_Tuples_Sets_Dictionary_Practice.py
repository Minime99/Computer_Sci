'''List Practice'''

Food = ['Banana', 'Milk', 'Spinach']
print(Food)


Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
print(Food)


Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
Food.remove('Milk')
print(Food)

Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
Food.remove('Milk')
print(Food[1])


Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
Food.remove('Milk')
Food.insert(1, 'Strawberry')
print(Food)


Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
Food.remove('Milk')
Food.insert(1, 'Strawberry')
Food[0] = 'Yogurt'
print(Food)


Food = ['Banana', 'Milk', 'Spinach']
Food.append('Mango')
Food.remove('Milk')
Food.insert(1, 'Strawberry')
Food[0] = 'Yogurt'
print(Food)
print(len(Food))



'''Tuple Practice'''

Food = ('Banana', 'Milk', 'Spinach')
print(Food)


Food = ('Banana', 'Milk', 'Spinach')
print(Food[1])


Food = ('Banana', 'Milk', 'Spinach')
#Food[0] = 'Yogurt'
#It fails. You cannot change Tuples.
print(Food)


Food = ('Banana', 'Milk', 'Spinach')
print(len(Food))


#You would use a Tuple when you never want something to change. It is also generally faster.



'''Sets Practice'''

Food = {'Banana', 'Milk', 'Spinach'}
print(Food)


Food = {'Banana', 'Milk', 'Spinach'}
Food.add('Mango')
print(Food)


Food = {'Banana', 'Milk', 'Spinach'}
Food.add('Mango')
Food.add('Banana') #Adding a redundant item does nothing to change the set.
print(Food)


Food = {'Banana', 'Milk', 'Spinach'}
Food.add('Mango')
Food.add('Banana')
Food.remove('Milk')
print(Food)


#Sets do not have a proper order. You cannot change itself.



'''Dictionary Practice'''

Food = {'Banana':1, 'Milk':2, 'Spinach':3}
print(Food)


Food = {'Banana':1, 'Milk':2, 'Spinach':3}
print(Food['Banana'])


Food = {'Banana':1, 'Milk':2, 'Spinach':3}
Food['Banana'] = 4
print(Food['Banana'])


Food = {'Banana':1, 'Milk':2, 'Spinach':3}
Food['Banana'] = 4
print(Food['Banana'])
print(len(Food))


Food = {'Banana':1, 'Milk':2, 'Spinach':3}
Food['Banana'] = 4
Food['Strawberry'] = 5
print(Food['Banana'])
print(Food['Strawberry'])
print(len(Food))


Food = {'Banana':1, 'Milk':2, 'Spinach':3}
Food['Banana'] = 4
Food['Strawberry'] = 5
del Food['Milk']
print(Food['Banana'])
print(Food['Strawberry'])
print(len(Food))
