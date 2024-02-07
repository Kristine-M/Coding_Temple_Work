#1.1
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")
    
#1.2
mood = input("How do you feel today? ")

if  mood == "happy":
    print("Thats great to hear!")
if mood == "sad":
    print("I hope your day gets better!")
    
#1.3
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")
    
#2.1
# Python, oh Python, so clear and so neat (given)
# With every new challenge, you're hard to beat.(given)

# slithering python going around
# but this one doesn’t make a sound
# coding all day and night
# taking its skill to a whole new height 

#2.2
'''
Python, in the realm of code you shine,(given)
With simplicity and grace, you're truly divine.(given)

Closer to the goal with every line,
You dress the app to the nines.
With every function which you sign,
Doing everything with such shine.
For many applications, you're the spine. 
'''

#2.3
# This line is from my first poem
# slithering python going around.

# This line is from my multi-line poem
'''
You dress the app to the nines.
'''

#3.1
PI = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

#4.1
variable_a = "Hello, World!" #string
variable_b = 23 #integer
variable_c = 3.14 #float
variable_d = True #float

print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))

#5.1
dynamic_variable = "This is a string"
print(type(dynamic_variable))

dynamic_variable = 100
print(type(dynamic_variable))

dynamic_variable = 25.5
print(type(dynamic_variable))

#6.1
eggs = 5
milk = 3
carrot = 1
print(eggs + milk + carrot)

#6.2
savings = 1000
interest = 0.4
yearly_savings = savings + (savings * interest)

#6.3
length = 6 #example given number
width = 7 #example given number

area = length * width

perimeter = (length * 2) + (width * 2)

#7.1
a = 2
b = 3

temp = a
a = b
b = temp

if (a == 3):
    if (b == 2):
        print("swapped")
        
#7.2
num = input("input a possible perfect sqr: ")
poss_sqr = num ** (1/2)

if (poss_sqr ** 2) == num:
    print("It is a perfect square")
    
#8.1

cloudy = True
rain = True
sunny = True

if cloudy and rain:
    print("take umbrella")
else:
    print("leave umbrella at home")

if rain or sunny:
    print("take umbrella")
    
#8.2
problem_1 = 3 + 6 * 2
problem_2 = (3 + 6)* 2

print(problem_1)
print(problem_2)

if problem_1 == problem_2:
    print("match")
else:
    print("different")
    
#8.3
temp = 20 + 3 - 4
is_winter = True

if temp == 19 and is_winter:
    print("wear coat")
else:
    print("wear shorts")


    







