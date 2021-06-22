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
print ("My favorite flowers are ")
for flower in flowers [:]:
    print(flower.title())
print ("My favorite flowers are ")
for flower in flowers [4:6]:
    print(flower.title())
print ()

#copying a list
pottedplants = flowers[:]
print (pottedplants)
pottedplants.append('bee balm')
print (pottedplants)