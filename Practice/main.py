import datetime
import random
import math
from getpass import getpass
import newModule

'''
Run Python programs
1. Make a Python program that prints your name.
2. Make a program that displays the lyrics of a song.
'''
def nameAndLyrics():
  print("Clair Houlihan\n")

  # Give me the night
  lyrics = "Whenever dark has fallen\n\
  You know the spirit of the party\n\
  Starts to come alive\n\
  Until the day is dawning\n\
  You can throw out all your blues\n\
  And hit the city lights\n"

  print(lyrics)

'''
Variables
1. Make a program that displays several numbers.
2. Make a program that solves and shows the summation of 64 + 32.
3. Do the same as in 2, but make it sum x + y.
'''
def variables(x, y):
  for i in range(0, 10):
    print(i)
  
  print("")

  print((64+32))

  print((x+y))

'''
Strings
1. Make a program that displays your favourite actor/actress.
2. Try to print the word „lucky‟ inside s.
3. Try to print the day, month, year in the form “Today is 2/2/2016”.
'''

def strings():

  actor = "Eliot Page"

  print(actor)

  temp = actor.split(' ')

  luckyActor = temp[0] + " lucky " + temp[1]

  print(luckyActor)

  dateToday = datetime.datetime.now()

  print("Today is %d/%d/%d" % (dateToday.day, dateToday.month, dateToday.year))

'''
String replace
1. Try the replace program
2. Can a string be replaced twice? (Yes)
3. Does replace only work with words or also phrases? (As long as it is a string, it will work)
'''

def stringReplace():
  name = "Clair Kendall Houlihan"

  newname = name.replace(" ", ",")

  print(newname)

'''
String find
1. Find out if string find is case sensitive (It is)
2. What if a query string appears twice in the string? (It will return the first occurance of it)
3. Write a program that asks console input and searches for a query.
'''

def stringFind():
  name = "Clair Kendall Houlihan"

  print(name.find("Kendall"))

  console = input("Enter a value: ")

  if console.find("Clair") != -1:
    print("My name is in your query!")
  else:
    print("My name was not in your query :(")

'''
String join
1. Create a list of words and join them, like the example above.
2. Try changing the separator string from a space to an underscore.
'''

def stringJoin():
  words = ["This", "is", "a", "list"]

  joinedWords = " ".join(words)
  print(joinedWords)

  print(joinedWords.replace(" ", "_"))

'''
String split
1. Can a string be split on multiple characters? (Yes, you can split based of a sequence of characters)
2. Can you split a string this string?: World,Earth,America,Canada
3. Given an article, can you split it based on phrases? (Yes)
'''

def stringSplit():
  string = "World,Earth,America,Canada"
  tokens = string.split(",")

  for word in tokens:
    print(word)


'''
Random numbers
1. Make a program that creates a random number and stores it into x.
2. Make a program that prints 3 random numbers.
3. Create a program that generates 100 random numbers and find the frequency of each
number.
'''

def randomNumbers():
  x = random.randint(0, 10)

  print(x)

  print("")

  i = 0

  while(i<3):

    print(random.randint(0, 100))

    i += 1

  i = 0

  print("")

  numberOccurances = {}

  while (i < 100):

    rand = random.randint(0,100)

    if(rand not in numberOccurances):
      numberOccurances[rand] = 1
    else:
      numberOccurances[rand] += 1

    i += 1

  print(numberOccurances)

'''
Keyboard input
1. Make a program that asks a phone number.
2. Make a program that asks the users preferred programming language.
'''

def keyboardInput():
  phone = input("Please Enter Your Phone Number: ")
  print("Your number is %s" % (phone))

  language = input("Plese Enter Your preferred programming language: ")
  print("Your prefered programming language is %s" % (language))

'''
If statements
1. Make a program that asks the number between 1 and 10 if the number is out of range the program should display “invalid number”.
2. Make a program that asks a password.
'''

def ifStatements():

  num = int(input("Enter a number between 1-10: "))

  if(num in range(1, 10)):
    print("Valid Number")
  else:
    print("Invalid Number")

  password = getpass()

  if(password != ""):
    print("Received a password")
  else:
    print("Did not receive a password")

'''
For loops
1. Make a program that lists the countries in the set
clist = ['Canada','USA','Mexico','Australia']
2. Create a loop that counts from 0 to 100
3. Make a multiplication table using a loop
4. Output the numbers 1 to 10 backwards using a loop
5. Create a loop that counts all even numbers to 10
6. Create a loop that sums the numbers from 100 to 200
'''
  
def forLoops():
  clist = ['Canada','USA','Mexico','Australia']

  for listing in clist:
    print(listing)

  for num in range(0,100):
    print(num, end=' ')

  print("")

  for mult1 in range(1,13):
    for mult2 in range(1, 13):
      print(mult1 * mult2, end=' ')

    print("")

  for num in range(10, 1):
    print(num, end=' ')

  print("")

  for num in range(0, 10):
    if(num % 2 == 0):
      print(num, end=' ')

  print("")

  summation = 0
  for num in range(100, 200):
    summation += num

  print(summation)

'''
While loops
1. Make a program that lists the countries in the set below using a while loop.
clist = ["Canada","USA","Mexico"]
2. What‟s the difference between a while loop and a for loop? A for loop has its iterative value inside the call of it, a while loop only has the condition it will exit on when called.
3. Can you sum numbers in a while loop? Yes
4. Can a for loop be used inside a while loop? Yes, this is called a nested loop
'''

def whileLoops():
  clist = ["Canada","USA","Mexico"]
  i = 0

  while(i < len(clist)):
    print(clist[i], end=' ')
    i += 1

  print("")

  i = 1
  summation = 0

  while(i in range(1,11)):
    summation += i
    i += 1
  print(summation)

  '''
  Functions
1. Make a function that sums the list mylist = [1,2,3,4,5]
2. Can functions be called inside a function? Yes
3. Can a function call itself? (hint: recursion) Yes, this is called recursion
4. Can variables defined in a function be used in another function? (hint: scope) Yes, if you have a function that calls another, the function will see the local variables that are in the function calling it
  '''

def functions(mylist):
  summation = 0
  for num in mylist:
    summation += num
  print(summation)

  def recursionFactorial(f):
    if f == 1:
      return 1
    else:
      return f * recursionFactorial(f-1)

  print(recursionFactorial(5))

  a = 2

  def scope():
    print(a)

  scope()

'''
Lists
1. Make a program that displays the states in the U.S.
states = [ 'Alabama', .. ,'Wyoming' ]
2. Display all states starting with the letter M
'''

def lists():
  states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

  for state in states:
    print(state, end=' ')

  print("\n")

  for state in states:
    if state[0] == 'M':
      print(state)
    else:
      continue

'''
List operations
1. Given the list y = [6,4,2] add the items 12, 8 and 4.
2. Change the 2nd item of the list to 3.
'''

def listOperations():

  y = [6, 4, 2]

  y.append(12)
  y.append(8)
  y.append(4)

  y[1] = 3

  print(y)

'''
Sorting list
1. Given a list with pairs, sort on the first element
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
2. Now sort on the second element
'''

def sortingList():
  x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
  x.sort()
  print(x)

  x.sort(key = lambda x: x[1])
  print(x)

'''
Range function
1. Create a list of one thousand numbers
2. Get the largest and smallest number from that list
3. Create two lists, an even and odd one.
'''

def rangeFunction():

  thousand = range(1, 1000)

  min = 1000
  max = 0

  for element in thousand:
    if element < min:
      min = element
      continue
    elif element > max:
      max = element
      continue

  print("max: %d" % (max))
  print("min: %d" % (min))
  
  even = []
  odd = []

  for element in range(0, 11, 2):
    even.append(element)

  for element in range(1, 11, 2):
    odd.append(element)

  print(even)
  print(odd)

'''
Dictionary
1. Make a mapping from countries to country short codes
2. Print each item (key and value)
'''

def dictionary():
  countries = {'United States of America' : 'USA', 'Germany' : 'GER', 'France' : 'FRA', 'United Kingdom' : 'UK'}

  for country in countries:
    print("%s : %s" % (country, countries[country]))

'''
Read file
1. Read a file and number every line
2. Find out what the program does if the file doesn‟t exist. *Throws a file not found exception*
3. What happens if you create a file with another user and try to open it? *Gives another IOException*
'''
def readFile():

  file = open("txt.txt", "r")

  i = 1

  for line in file:
    print("%d %s" % (i, line), end='')
    i += 1

  print("")

  file.close()

'''
Write file
1. Write the text “Take it easy” to a file
2. Write the line open(“text.txt”) to a file
'''

def writeFile():
  file = open("txt.txt", "a")

  file.write("Take it easy")
  file.write("open(\"text.txt\")")

'''
Nested loops
1. Given a tic-tac-toe board of 3x3, print every position
2. Create a program where every person meets the other
persons = [ “John”, “Marissa”, “Pete”, “Dayton” ]
3. If a normal for loop finishes in n steps O(n), how many steps has a nested loop? No, generally, for a nested loop, it finishes in O(n^2) for 2 loops, and increasing for each new loop
'''

def nestedLoops():
  for i in range(1, 4):
    print("[", end=' ')
    for j in range (1, 4):
      print("_", end=' ')
    print("]")

  persons = ["John", "Marissa", "Pete", "Dayton"]

  for person1 in persons:
    for person2 in persons:
      print(person1 + " -> " + person2)

  '''
  Slices
1. Take a slice of the list below:
pizzas = [“Hawai”,”Pepperoni”,”Fromaggi”,”Napolitana”,”Diavoli”]
2. Given the text “Hello World”, take the slice “World”
  '''

def slices():

  pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana","Diavoli"]
  print(pizzas[2:4])

  text = "Hello World"

  print(text[6:])

'''
Multiple return
1. Create a function that returns a,b and a+b
2. Create a function that returns 5 variables
'''

def multipleReturn():

  def multiReturn():
    a = 3
    b = 4
    return a, b, a+b

  print(multiReturn())

  def return5vars():
    c = 1
    d = 2
    e = 3
    f = 4
    g = 5
    return c, d, e, f, g

  print(return5vars())

'''
Scope
1. Add a function reduce amount that changes the variable balance
2. Create a function with a local variable
'''

def scopeAlso():

  x = 100

  def reduce(x):
    global y
    y = x - 50

  reduce(x)

  print(y)


'''
Time and date
1. Print the date in format year-month-day
'''

def timeAndDate():

  dateToday = datetime.datetime.now()
  print("Today is %d-%d-%d" % (dateToday.year, dateToday.month, dateToday.day))

'''
Try except
1. Can try-except be used to catch invalid keyboard input? Yes, ex: if you are expecting an int as input, you can try around the input, and catch the not an int exception
2. Can try-except catch the error if a file can‟t be opened? Yes, you can catch the exception
3. When would you not use try-except? There are situations where using the try-except is a bad idea, i.e. trying to catch a stackOverflow exception is generally a bad idea.
'''



'''
Class
1. Can you have more than one class in a file? Yes, it is possible to have multiple classes in a file
2. Can multiple objects be created from the same class? Yes, a class can create multiple objects within it
3. Can objects create classes? No, they cannot
4. Using the code above, create another object
5. Add a method to the class: location()
'''

class cat:

  def __init__(self, breed):
    self.breed = breed
    self.age = 1

  def location():
    x, y = 50
    return x, y

  def getAge():
    return age
  def setAge(self, age):
    self.age = age

'''
Getter and setter
1. Add a variable age and create a getter and setter (added this to the class above since it made the most sense)
2. Why would you use getter and setter methods? Controlled access, with getters and setters, you can control how others access variables in classes
'''

'''
Modules
1. Import the math module and call the sin function
2. Create your own module with the function snake()
'''

def modules():
  print(math.sin(90))
  newModule.snake()
  

'''
Inheritance
1. Create a new class that inherits from the class App
2. Try to create a class that inherits from two super classes (multiple inheritance)
'''

class App(object):
  def start(self):
    print('Starting')

class DisApp(object):
  def start(self):
    print("Starting")

class Apple(App):
  def getVersion(self):
    print('Apple version')

class Linux(App, DisApp):
  def getLinuxVersion(self):
    print('Linux version')


'''
Static method
1. Can a method inside a class be called without creating an object? Yes, you can create a method and call it directly
2. Why does not everybody like static methods? Static methods go against the paradigm of OOP. So those who like to stick to OOP do not like to use static methods.
'''

'''
Iterable
1. What is an iterable? An iterable is any object that can be iterated over (you can go one by one through)
2. Which types of data can be used with an iterable? You can store any type of object in an Iterable
'''

'''
Classmethod
1. What is a classmethod? A class method is shared amongst the different objects in an application
2. How does a classmethod differ from a staticmethod? class methods are called either from instances of the class, or from the class itself, where static methods are juist called from the class itself.
'''

'''
Multiple inheritance
1. Do all programming languages support multiple inheritance? No, Java for example does not support multiple inheritance
2. Why would you not use multiple inheritance? Multiple inheritance is dangerous because if you have a method shared across two classes, it can cause a conflict.
3. Is there a limit to the number of classes you can inherit from? There is no limit to the number of classes you can inherit from
'''