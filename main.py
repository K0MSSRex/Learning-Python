# 0 1 2 3 4 5 6 7 8 9 10
# H e l l o  W o r l d

print('Hello World'[-3])

name = "Sam"
# name[0] = 'P'
last_letter = name[1:]
print (last_letter)
print('P' + last_letter)
z = "z"
print(z * 10)
x = "Hello World"
xl = x.lower()
xs = x.split()
xss1 = x.split('o')
xss2 = x.split('l')
print(xl)
print(xs)
print(xss1)
print(xss2)

s = 'Sammy'
print(s[2:])

myname = 'Jose'
print("Hello " + myname + " are you gay?")


#.format
print('This is a test string ig {}'.format('INSERTED'))

print('The {} {} {}'.format('killed','queer','I'))
print('The {1} {2} {0}'.format('killed','queer','I'))
print('The {q} {i} {k}'.format(k ='killed',q='queer',i='I'))

queer = 1000
print("Result of queer purge is around {qe}".format(qe=queer))

result = 100/777
print(result)
print('The result totaled up to {r:0.3f}'.format(r=result))

#(f'{variable}) (f-strings)
name = 'John'
age = 47
print(f'{name} is {age} years old!')


#Lists

my_list = [4,5,6]
my_listt = ['one','two','four']
print(my_list)
print (len(my_list))
print(my_listt[0])
print(my_list + my_listt)
p = '22'
new_list = my_list + my_listt
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
my_listt.reverse()
print(my_listt)


#Dictionary

my_dict = {'key1':'abc','key2':'xyz'}
print('The first three letters of the alphabet are: ' + my_dict['key1'])
print('The last three letters of the alphabet are: ' + my_dict['key2'])

d = {'k1':['a','b','c','d']}
mylist = d['k1']
letter = mylist[2]
print(letter.upper)
print(d['k1'][3].upper())
d['k3'] = 4762
print(d)
print(d.values())
print(d.items())

t = (1,2,3)
pp = [1,2,3]
print(type(t))
print(type(pp))

t = ('one',2,3.1)
print(t[1:])

print(t.index(2))

#Sets
myset = set()
print (myset)
myset.add(2)
myset.add(2)
print (myset)
meinlist = [1,2,3,3,3,3,3,3,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,]
set2 = set(meinlist)
print(set2)

#Booleans

print(type(False))
print(type(True))
print(1 > 1)
print(1 == 2)

#I/O with basic files
Meth = 'bad for you'
x = open('test.txt', 'w') #
x.write('Meth is ' + Meth)
x.close()

#Comparison Operators

#Equal
print(2 == 2)
print(2 == 1)
print('hello' == 'bye')
print('Bye' == 'bye')
print('2' == 2)
print(2.0 == 2)

#Not Equal
print(3 != 3)
print(3 != 4)

#Greater than
print(1 > 2)
print(2 > 1)
print(2 >= 2)

#Chaining Comparison Operators

print(3 < 4 < 5)
print('--------')
print (1 < 2 and 2 < 3)
print('--------')
print (3 == 3 or 2 == 3)
print('--------')
print(not(1 == 1))
print('--------')

#Control flow (elif and else)
Math1 = True

if Math1:
    print('1 is equal to 1!')
else:
    print('1 is not equal to 1!')

loc = 'Bank'

print('--------')
if loc == 'Car Shop':
    print('Cars are sick asf!')
elif loc == 'Bank':
    print('Money is so cool!')
else:
    print('I am stupid')


name = 'Bob'
print('--------')
if name == 'Molly':
    print('Hi Molly')
elif name == 'Bob':
    print('Hi '+ name)
else:
    print("What is your name?")
print('--------')

# For Loops

my_iterable = [5,6,8,6,7,8,9,6,4,3]
for item_name in my_iterable:
    print(item_name)
print('--------')


#While Loops
x = 0
while x < 10:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN 10")
    print('--------')


# break (breaks out of closest enclosing loop)
# continue (goes to top of closest enclosing loop)
# pass (does nothing at all)

x = [1,2,3]
for item in x:
    pass
print("end of script")
print('--------')

mystring = 'Joey'

for letter in mystring:
    if letter == 'e': # skips the letter 'e'
        continue
    print(letter)
print('--------')

for letter in mystring:
    if letter == 'e': # if letter 'e' stops printing rest
        break
    print(letter)
print('--------')

x = 0

while x < 10:
    if x == 2:
        break
    print(x)
    x += 1

print('--------')

# Useful Operators

for num in range(0,11,2):
    print(num)
print('--------')

print(list(range(0,13,3)))
print('--------')


index_count = 0
word = 'abcdefg'

for letter in enumerate(word):

    print(word[index_count])
    index_count += 1

print('--------')

word = 'abcdefg'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

print('--------')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)
