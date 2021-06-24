#Second half of chaper four
#4-3
for number in range (1,21):
    print (number)
print ()

counting = range (1,1001,2)
for numbers in counting:
    print (numbers)
print ()

#4-4
counting_numbers = list (range (1,51))
print (counting_numbers)
print ()

#4-5
squares = []
for numbers in range (1,11):
    square = numbers **2
    squares.append (square)
print (squares)
print ()

multiply = []
for number in range (1, 11):
    multiplies = number *2
    multiply.append (multiplies)
print (multiply)
print ()

total_number = range (1,1000000)
print (min (total_number))
print (max (total_number))
print (sum (total_number))
print ()

#4-6
for odd_numbers in range (1,13,2):
    print (odd_numbers)
print ()

#4-7
multi = []
for number in range (1,30):
    multis = number *3
    multi.append (multis)
print (multi)
print ()

#4-8
cube = []
for value in range (1,11):
    cubes = value **3
    cube.append (cubes)
print (cube)
print ()

#4-9
cubed = [count**3 for count in range (1,11)]
print (cubed)
print ()

#4-10
flowers = ['marigolds', 'nastirtum', 'calendula', 'sunflower', 'coreiopsis', 'rudabeckia']
print (flowers[0:3])
print ()

for flower in flowers [:]:
    print(flower.title())

print ("\nMy favorite flowers are ")

for flower in flowers [4:6]:
    print(flower.title())
print ()

#copying a list
pottedplants = flowers[:]
print (pottedplants)
pottedplants.append('bee balm')
print (pottedplants)
print ()


#4-10b
beer_types =['berliner weisse', 'kolsch', 'marzen', 'lager', 'maibock', 'helles', 'pilsner', 'dunkel', 'gose']
beer_message = 'The next beer styles in the list are:'
print (beer_message)
print (beer_types [0:3])
print ()
print (beer_message)
print (beer_types [3:6])
print ()
print (beer_message)
print (beer_types [6:])
print ()

#4-11/12
favorite_pizza = ['margherita', 'greek', 'pepperoni']
pizza_message = 'I am very hungry and pizza sounds great. I am looking forward to completing this chapter!'
for favorite_pizzas in favorite_pizza:
    print (favorite_pizzas)
print ()
print (pizza_message)
print ()

best_pizza = favorite_pizza [:]
print (best_pizza)
print ()

favorite_pizza.append ('veggie')
for favorites in favorite_pizza [3:]:
    print (f'Another type of pizza I like is {favorites.title()} Pizza')
print ()

best_pizza.append ('pineapple & pepper')
print ('I think the best pizzas are:')
for best in best_pizza:
    print (best.title())
print ()

#4-13
summer_activities = ('hiking', 'kayaking', 'biking', 'swimming', 'gardening')
print ('A few summer activies are:')
for activities in summer_activities:
    print (activities.title())
for summer in summer_activities [1:2]:
    print (f'\nMy favorite thing to do in the summer is {summer}!\n')

summer_activities = ('swimming', 'gardening')
for favorite_things in summer_activities:
    print (f'\n{favorite_things.title()} is something I can do close to home!\n')