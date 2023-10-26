print("1. Write a Python program to print the following string in a specific format (see the output)")
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print("2. Write a Python program to find out what version of Python you are using")
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

print("3. Write a Python program to display the current date and time")
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print("4. Write a Python program that calculates the area of a circle based on the radius entered by the user")
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

print("5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them")
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

print("6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers")
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

print("7. Write a Python program that accepts a filename from the user and prints the extension of the file")
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

print("8. Write a Python program to display the first and last colors from the following list")
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

print("9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)")
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

print("10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn")
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

print("11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s)")
print(abs.__doc__)

print("12. Write a Python program that prints the calendar for a given month and year")
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

print("13. Write a Python program to print the following 'here document'")
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

print("14. Write a Python program to calculate the number of days between two dates")
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

print("15. Write a Python program to get the volume of a sphere with radius six")
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

print("16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference")
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
print(difference(22))
print(difference(14))

print("17. Write a Python program to test whether a number is within 100 of 1000 or 2000")
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

print("18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum")
def sum_thrice(x, y, z):
    sum = x + y + z  
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

print("19. Write a Python program to get a newly-generated string from a given string where 'Is' has been added to the front. Return the string unchanged if the given string already begins with 'Is'")
def new_string(text):
    if len(text) >= 2 and text [:2] == "Is":
        return text
    return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty")) 

print("20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string")
def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result
print(larger_string('abc', 2))
print(larger_string('.py', 3)) 

print("21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user")
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

print("22. Write a Python program to count the number 4 in a given list")
def list_count_4(nums):
    count = 0  
    for num in nums:
        if num == 4:
            count = count + 1
        return count
print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

print("23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2")
def substring_copy(text, n):
    flen = 2
    if flen > len(text):
        flen = len(text)
    substr = text[:flen]
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));

print("24. Write a Python program to test whether a passed letter is a vowel or not")
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

print("25. Write a Python program that checks whether a specified value is contained within a group of values")
print("Solution-1")
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
print("Solution-2")
def is_group_member(group_data, n):
    return n in group_data
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

print("26. Write a Python program to create a histogram from a given list of integers")
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
            output += '*'
            times = times - 1
        print(output)
histogram([2, 3, 6, 5])

print("27. Write a Python program that concatenates all elements in a list into a string and returns it")
def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
print(concatenate_list_data([1, 5, 12, 2]))

print("28. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence")
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)
		
print("29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2")
print("Solution-1")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
print("Solution-2")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print(color_list_1)
print(color_list_2)
print("\nDifferenct of color_list_1 and color_list_2:")
print(color_list_1 - color_list_2)
print("\nDifferenct of color_list_2 and color_list_1:")
print(color_list_2 - color_list_1)

print("30. Write a Python program that will accept the base and height of a triangle and compute its area")
b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = b*h/2
print("area = ", area)

print("31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers")
print("Solution-1")
def gcd(x, y):
    gcd = 1   
    if x % y == 0:
        return y   
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break 
    return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))
print("Solution-2")
def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))
print("Solution-3")
from functools import reduce
from math import gcd as _gcd
def gcd(nums):
    return reduce(_gcd, nums)
nums = [336, 360]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [12, 17]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [4, 6]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [24, 30, 36]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))

print("32. Write a Python program to find the least common multiple (LCM) of two positive integers")
print("Solution-1")
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
print(lcm(4, 6))
print(lcm(15, 17))
print("Solution-2")
from functools import reduce
from math import gcd
def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
print(lcm([12, 7]))  
print(lcm([1, 3, 4, 5])) 
print(lcm([4, 6]))  
print(lcm([15, 17]))
print("Solution-3")
from fractions import gcd
def lcm(a, b):
    return (a * b) // gcd(a,b) 
print(lcm(4, 6))
print(lcm(15, 17))

print("33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero")
def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))

print("34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20")
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))

print("35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5")
def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))

print("36. Write a Python program to add two objects if both objects are integers")
def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

print("37. Write a Python program that displays your name, age, and address on three different lines")
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()

print("38. Write a Python program to solve (x + y) * (x + y)")
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))

print("39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years")
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

print("40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)")
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)

print("41. Write a Python program to check whether a file exists")
print("Solution-1")
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))
print("Solution-2")
import os.path
print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))
print("Solution-3")
my_file = open('main.py')
try:
    my_file.close()
    print("File found!")
except FileNotFoundError:
    print("File not found!")

print("42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS")
print("Solution-1")
# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)
print("Solution-2")
import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)

print("43. Write a Python program to get OS name, platform and release information")
print("Solution-1")
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())
print("Solution-2")
import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())

print("44. Write a Python program to locate Python site packages")
import site; 
print(site.getsitepackages())

print("45. Write a Python program that calls an external command")
print("Solution-1")
from subprocess import call
call(["ls", "-l"])
print("Solution-2")
import os
print(os.system('ls -l'))
print("Solution-3")
import psutil
print(psutil.cpu_count())

print("46. Write a Python program to retrieve the path and name of the file currently being executed")
import os
print("Current File Name : ",os.path.realpath(__file__))
print("Solution-1")
import multiprocessing
print(multiprocessing.cpu_count())
print("Solution-2")
import os
print(os.cpu_count())

print("47. Write a Python program to find out the number of CPUs used")
print("Solution-1")
import multiprocessing
print(multiprocessing.cpu_count())
print("Solution-2")
import os
print(os.cpu_count())

print("48. Write a Python program to parse a string to float or integer")
print("Solution-1")
n = "246.2458"
print(float(n))
print(int(float(n)))
print("Solution-2")
def test(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
print(test('12'))
print(test('233.12'))

print("49. Write a Python program to list all files in a directory")
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
print(files_list)

print("50. Write a Python program to print without a newline or space")
print("Solution-1")
for i in range(0, 10):
    print('*', end="")
print("\n")
print("Solution-2")
import functools
printf = functools.partial(print, end="")
for i in range(0, 10):
    printf('*')
    i = 0
print("Solution-3")
i=0
while i<10 :
    print('*',end='')
    i = i+1
	
print("51. Write a Python program to determine the profiling of Python programs")
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

print("52. Write a Python program to print to STDERR")
# from __future__ import print_function
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
eprint("abc", "efg", "xyz", sep="--")

print("53. Write a Python program to access environment variables")
print("Solution-1")
import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')
print("Solution-2")
import os
for data in os.environ:
    print(data)
    print('-'*15)
    print(os.environ[data])
    print('='*30)
print("Solution-3")
import os
for item, value in os.environ.items():
    print('{}: {}'.format(item, value))

print("54. Write a Python program to get the current username")
print("Solution-1")
import getpass
print(getpass.getuser())
print("Solution-2")
import os
import pwd
def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]
print(get_username())

print("55. Write a Python program to find local IP addresses using Python's stdlib")
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

print("56. Write a Python program to get the height and width of the console window")
def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th
print('Number of columns and Rows: ',terminal_size())

print("57. Write a Python program to get the execution time of a Python method")
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time
n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

print("58. Write a Python program to sum the first n positive integers")
print("Solution-1")
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)
print("Solution-2")
n = int(input("Input an integer: "))
result = sum(range(n+1))
print("Sum of the first", n ,"positive integers:",result)

print("59. Write a Python program to convert height (in feet and inches) to centimeters")
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm)

print("60. Write a Python program to calculate the hypotenuse of a right angled triangle")
print("Solution-1")
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )
print("Solution-2")
def test(x, y):
    h = (x**2 + y**2)**0.5
    return h
print(test(3,4))
print(test(3.5,4.4))

print("61. Write a Python program to convert the distance (in feet) to inches, yards, and miles")
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0
print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)

print("62. Write a Python program to convert all units of time into seconds")
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))
time = days + hours + minutes + seconds
print("The  amounts of seconds", time)

print("63. Write a Python program to get an absolute file path")
print("Solution-1")
def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))
print("Solution-2")
from pathlib import Path
p = Path("main.py").resolve()
print(p)

print("64. Write a Python program that retrieves the date and time of file creation and modification")
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

print("65. Write a Python program that converts seconds into days, hours, minutes, and seconds")
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

print("66. Write a Python program to calculate the body mass index")
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

print("67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure")
print("Solution-1")
kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))
print("Solution-2")
kpa= float(input("Input the pressure in kilopascals > "))
pressure_in_psi = round(kpa * 0.145038,3)
pressure_in_mmHg = round(kpa * 7.50062, 3)
pressure_in_atmp = round(kpa * 0.0098692382432766,3)
print(f"Pressure = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")

print("68. Write a Python program to calculate sum of digits of a number")
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)

print("69. Write a Python program to sort three integers without using conditional statements and loops")
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

print("70. Write a Python program to sort files by date")
print("Solution-1")
import glob
import os
files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))
print("Solution-2")
import os
os.chdir('d:')
result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
print('\n'.join(map(str, result)))

print("71. Write a Python program to get a directory listing, sorted by creation date")
print("Solution-1")
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
# regular files, insert creation date
data = ((stat[ST_CTIME], path)
for stat, path in data if S_ISREG(stat[ST_MODE]))
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
print("Solution-2")
import os
import time
paths = ["%s %s" % (time.ctime(t),f) for t, f in
sorted([(os.path.getctime(x),x) for x in os.listdir(".")])]
print("Directory listing, sorted by creation date:")
for x in range(len(paths)):
    print(paths[x],)
	
print("72. Write a Python program to get the details of the math module")
print("Solution-1")
# Imports the math module
import math            
#Sets everything to a list of math module
math_ls = dir(math) # 
print(math_ls)
print("Solution-2")
import math
print("Details of math module:\n")
help(math)

print("73. Write a Python program to calculate the midpoints of a line")
print('\nCalculate the midpoint of a line :')
x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))
x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))
x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print()
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print()

print("74. Write a Python program to hash a word")
print("Solution-1")
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
word=input("Input the word be hashed: ")
word=word.upper()
coded=word[0]
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print() 
print("The coded word is: "+coded)
print()
print("Solution-2")
int_num = 112
flt_num = 23.99
text_val = 'Python Exercises'
print("Original integer value:",int_num)
print ("Hash value of the said integer value: " + str(hash(int_num)))
print("Original float value:",flt_num)
print ("Hash value of the said float value: " + str(hash(flt_num)))
print("Original text:",text_val)
print ("Hash value of the said text: " + str(hash(text_val)))

print("75. Write a Python program to get the copyright information and write Copyright information in Python code")
print("Solution-1")
import sys
print("\nPython Copyright Information")
print(sys.copyright)
print()
print("Solution-2")
print("Python copyright information:\n")
print(copyright)
print("Solution-3")
__author__ = "Software Authors Name"
__copyright__ = "Copyright (C) 2004 Author Name"
__license__ = "Public Domain"
__version__ = "1.0"
print("copyright information in Python code:\n")

print("76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script")
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

print("77. Write a Python program to test whether the system is a big-endian platform or a little-endian platform")
import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()

print("78. Write a Python program to find the available built-in modules")
print("Solution-1")
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))
print("Solution-2")
help('modules')

print("79. Write a Python program to get the size of an object in bytes")
import sys
str1 = "one"
str2 = "four"
str3 = "three"
x = 0
y = 112
z = 122.56
print("Size of ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("Size of ",str2,"=",str(sys.getsizeof(str2))+ " bytes")
print("Size of ",str3,"=",str(sys.getsizeof(str3))+ " bytes")
print("Size of",x,"=",str(sys.getsizeof(x))+ " bytes")
print("Size of" ,y,"="+str(sys.getsizeof(y))+ " bytes")
L = [1, 2, 3, 'Red', 'Black']
print("Size of",L,"=",sys.getsizeof(L)," bytes")
T = ("Red", [8, 4, 6], (1, 2, 3))
print("Size of",T,"=",sys.getsizeof(T)," bytes")
S = {'apple', 'orange', 'apple', 'pear'}
print("Size of",S,"=",sys.getsizeof(S)," bytes")
D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of",D,"=",sys.getsizeof(S)," bytes")

print("80. Write a Python program to get the current value of the recursion limit")
print("Solution-1")
import sys
print()
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())
print()
print("Solution-2")
import sys
print("Call sys.getrecursionlimit() to get the current recursion limit:")
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
print("\nCall sys.setrecursionlimit(n) to change the recursion limit to n operations:")
sys.setrecursionlimit(1001)
new_recursion_limit = sys.getrecursionlimit()
print(new_recursion_limit)

print("81. Write a Python program to concatenate N strings")
print("Solution-1")
list_of_colors = ['Red', 'White', 'Black']  
colors = '-'.join(list_of_colors)
print()
print("All Colors: "+colors)
print()
print("Solution-2")
# Concatenating With the + Operator
print("Concatenating With the + Operator:")
list_of_colors = ['Red', 'White', 'Black'] 
colors = list_of_colors[0]+'-'+list_of_colors[1]+'-'+list_of_colors[2]
print("All Colors: "+colors)

print("82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)")
print("Solution-1")
s = sum([10,20,30])
print("\nSum of the container: ", s)
print()
print("Solution-2")
nums = [10,20,30]
print("Original container:")
print(nums)
print(type(nums))
print("Sum of all items of the said container:", sum(nums))
print("Solution-3")
def dict_sum(nums):     
    num_sum = 0
    for i in nums:
        num_sum = num_sum + nums[i]     
    return num_sum
nums = {'a': 100, 'b':200, 'c':300, 'd':120}
print("Original container:")
print(nums)
print(type(nums))
print("Sum of all items of the said container:", dict_sum(nums))
print("Solution-4")
nums = {7, 4, 9, 1, 3, 2}
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))
print("Solution-5")
nums = (7, 4, 9, 1, 3, 2)
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))

print("83. Write a Python program to test whether all numbers in a list are greater than a certain number")
print("Solution-1")
num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()
print("Solution-2")
def test(nums, n):
    return(all(x > n for x in nums))      
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list numbers:")
print(nums)
n = 12
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))
n = 5
print("\nCheck whether all numbers of the said list greater than",n)
print(test(nums, n))

print("84. Write a Python program to count the number of occurrences of a specific character in a string")
print("Solution-1")
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))
print("Solution-2")
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
ctr = 0 
for c in s:
    if c == 'o':
        ctr = ctr + 1
print(ctr)
print("Solution-3")
from collections import Counter
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
ctr = Counter(s) 
print (str(ctr['o']))
print("Solution-4")
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
ctr = sum(map(lambda x : 1 if 'o' in x else 0, s))
print(ctr)
print("Solution-5")
import re
s = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
ctr = len(re.findall("o", s))
print(ctr)

print("85. Write a Python program to check whether a file path is a file or a directory")
import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()

print("86. Write a Python program to get the ASCII value of a character")
print()
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))
print()

print("87. Write a Python program to get the size of a file")
print("Solution-1")
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()
print("Solution-2")
import os
file_size = os.stat('main.py')
print("\nThe size of abc.txt is :",file_size.st_size,"Bytes")
print("Solution-3")
import os
file = open('main.py')
file.seek(0, os.SEEK_END)
print("The size of main.py is :", file.tell(), "bytes")

print("88. Given variables x=30 and y=20, write a Python program to print '30+20=50'")
print("Solution-1")
x = 30
y = 20
print("\n%d+%d=%d" % (x, y, x+y))
print()
print("Solution-2")
x = 30
y = 20
print("{0}+{1}={2}".format(x, y, x+y))
print("Solution-3")
x = 30
y = 20
print("{}+{}={}".format(x, y, x + y))

print("89. Write a Python program to perform an action if a condition is true")
print("Solution-1")
n=1
if n == 1:
    print("\nFirst day of a Month!")
print()
print("Solution-2")
n = float(input("Input a number: "))
if (n == 1):
    print("First day of a Month!")
else:
    print()

print("90. Write a Python program to create a copy of its own source code")
def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("untitled0.py", "z.py")
        with open('z.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')

print("91. Write a Python program to swap two variables")
print("Solution-1")
a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()
print("Solution-2")
x = 34
y = 56
print("Initial Value of x =", x)
print("Initial Value of y =", y)
temp = x
x = y
y = temp
print("\nAfter swaping value of x =", x)
print("After swaping value of y =", y)

print("92. Write a Python program to define a string containing special characters in various forms")
print()
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')
print()

print("93. Write a Python program to get the Identity, Type, and Value of an object")
print("Solution-1")
x = 34
print("\nIdentity: ",x)
print("\nType: ",type(x))
print("\nValue: ",id(x))
print("Solution-2")
#Define two variables with some values
a = 34
b = 33
print('a = ',a)
print('b = ',b)
#Define another vairable c which is equal to a
c = a
print("Compare a and b:")
print(a is b)
print("\nMemory address of a:")
print(id(a))
print("Memory address of b:")
print(id(b))
print("\nCompare the said memory address:")
print(id(a) == id(b))
print("\nCompare b and c:")
print(b is c)
print("Memory address of c:")
print(id(c))

print("94. Write a Python program to convert the bytes in a given string to a list of integers")
print("Solution-1")
x = b'Abc'
print()
print("\nConvert bytes of the said string to a list of integers:")
print(list(x))
print()
print("Solution-2")
S = "The quick brown fox jumps over the lazy dog."  
print("Original string:")
print(S)
nums = []
print("\nConvert bytes of the said string to a list of integers:")
for chr in S:
    nums.append(ord(chr))
print(nums)

print("95. Write a Python program to check whether a string is numeric")
print("Solution-1")
str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
print("Solution-2")
# Doesn't work for floats
text = input("Input a word or numbers: ")
if text.isdigit():
   print("The input value is numbers.")
else:
   print("The input value is string.")

print("96. Write a Python program to print the current call stack")
import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()

print("97. Write a Python program to list the special variables used in the language")
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()

print("98. Write a Python program to get system time")
print("Solution-1")
import time
print()
print(time.ctime())
print()
print("Solution-2")
import datetime
print(datetime.datetime.now())

print("99. Write a Python program to clear the screen or terminal")
import os
import time
# for windows
# os.system('cls')
os.system("ls")
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')

print("100. Write a Python program to get the name of the host on which the routine is running")
print("Solution-1")
import socket
host_name = socket.gethostname()
print("Host name:", host_name)
print("Solution-2")
import platform
host_name = platform.uname()[1]
print("Host name:", host_name )
print("Solution-3")
import os
host_name = os.uname().nodename
print("Host name:", host_name)

print("101. Write a Python program to access and print a URL's content to the console")
print("Solution-1")
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
print("Solution-2")
import requests
data = requests.get('https://google.com/')
print(data.text)

print("102. Write a Python program to get system command output")
import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)

print("103. Write a Python program to extract the filename from a given path")
import os
print()
print(os.path.basename('/users/system1/student1/homework-1.py'))
print()

print("104. Write a Python program to get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current process")
import os
print("\nEffective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
print()

print("105. Write a Python program to get the users environment")
print("Solution-1")
import os
print()
print(os.environ)
print()
print("Solution-2")
import os
import pprint
# User's environment variables
u_env_var = os.environ
print("User's Environment variable:")
pprint.pprint(dict(u_env_var), width = 1)
print("Solution-3")
import os
host_name = os.environ['HOSTNAME']
print("HOSTNAME:", host_name)
python_path = os.environ.get('PYTHONPATH')
print("Python Path:", python_path)

print("106. Write a Python program to divide a path by the extension separator")
import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	
print("107. Write a Python program to retrieve file properties")
import os.path
import time
print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

print("108. Write a Python program to find the path to a file or directory when you encounter a path name")
import os.path
for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
	
print("109. Write a Python program to find the path to a file or directory when you encounter a path name")
print("Solution-1")
num = float(input("Input a number: "))
if num > 0:
    print("It is positive number")
elif num == 0:
    print("It is Zero")
else:
    print("It is a negative number")
print("Solution-2")
n = float(input('Input a number: '))
print('Number is Positive.' if n > 0 else 'It is Zero!' if n == 0 else 'Number is Negative.')
print("Solution-3")
n = float(input("Input a number: "))
if n >= 0:
    if n == 0:
        print("It is Zero!")
    else:
        print("Number is Positive number.")
else:
    print("Number is Negative number.")
   
print("110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function")
print("Solution-1")
num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
print("Solution-2")
num_list = [45, 55, 60, 37, 100, 105, 220]
print("Original list:",num_list)
# use anonymous function to filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers of the said list divisible by 15 are:",result)
print("Solution-3")
num_list = [45, 55, 60, 37, 100, 105, 220]
print("Original list:",num_list)
print("\nNumbers of the said list divisible by 15 are:")
print(str(''.join(filter(lambda x: x, str(list([i for i in num_list if i % 15 == 0]))))))

print("111. Write a Python program to make file lists from the current directory using a wildcard")
print("Solution-1")
import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))
print("Solution-2")
from pathlib import Path
for path in Path("/").glob("*.*"):
    print(path)

print("112. Write a Python program to remove the first item from a specified list")
print("Solution-1")
color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
del color[0]
print("After removing the first color:")
print(color)
print("Solution-2")
color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
print("\nAfter removing the first element from the said list:")
new_color = color[1:]
print(new_color)
print("Solution-3")
color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
print("\nAfter removing the first element from the said list:")
color.remove("Red")
print(color)
print("Solution-4")
def tail(lst):
    return lst[1:] if len(lst) > 1 else lst
print(tail([1, 2, 3, 4]))
print(tail([1]))
print(tail(["Red", "Black", "Green", "White", "Orange"]))

print("113. Write a Python program that inputs a number and generates an error message if it is not a number")
print("Solution-1")
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
print("Solution-2")
x = 1.23
x_int = x.is_integer()
print("Check if x is an integer!")
print(x_int)
y= 1.0
y_int = y.is_integer()
print("Check if y is an integer!")
print(y_int)  
print("Solution-3")
x = 1.0
x_int = isinstance(x, int)
print("Check if x is an integer!")
print(x_int)
y = 1
y_int = isinstance(y, int)
print("Check if y is an integer!")
print(y_int)

print("114. Write a Python program to filter positive numbers from a list")
print("Solution-1")
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums)
print("Solution-2")
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
print("Positive numbers in the said list: ")
for pos_nums in nums:
   if pos_nums > 0:
      print(pos_nums, end = " ")
print("Solution-3")
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
pos_nums = [n for n in nums if n> 0]
print("Positive numbers in the said list: ",*pos_nums)

print("115. Write a Python program to compute the product of a list of integers (without using a for loop)")
print("Solution-1")
from functools import reduce
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = reduce( (lambda x, y: x * y), nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)
print("Solution-2")
import math
 # Python version 3.9.
nums = [10, 20, 30,]
print("Original list numbers:")
print(nums)
nums_product = math.prod(nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)

print("116. Write a Python program to print Unicode characters")
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()

print("117. Write a Python program to prove that two string variables of the same value point to the same memory location")
str1 = "Python"
str2 = "Python"
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()

print("118. Write a Python program to create a bytearray from a list")
print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()

print("119. Write a Python program to round a floating-point number to a specified number of decimal places")
print("Solution-1")
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()
print("Solution-2")
order_amt = 212.374
print("\nThe total order amount comes to {:0.6f}".format(order_amt))
print("\nThe total order amount comes to {:0.2f}".format(order_amt))

print("120. Write a Python program to format a specified string and limit the length of a string")
str_num = "1234567890"
print("Original string:",str_num)
print('%.6s' % str_num)
print('%.9s' % str_num)
print('%.10s' % str_num)

print("121. Write a Python program to determine if a variable is defined or not")
try:
    x = 1
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
try:
    y
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")

print("122. Write a Python program to empty a variable without destroying it")
print("Solution-1")
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())
print("Solution-2")
def Empty_Var(lst):
    return [type(i)() for i in lst]
lst = ["python",{"x":12},[10,12,"sfsd"], (4,5), 200]
print("Original objects:")
print(lst)
print("\nEmpty the said variables without destroying it:")
print(Empty_Var(lst))

print("123. Write a Python program to determine the largest and smallest integers, longs, and floats")
import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 

print("124. Write a Python program to check whether multiple variables have the same value")
print("Solution-1")
x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")  
print("Solution-2")
def multiple_variables_equality(*vars):
    for x in vars:
        if x != vars[0]:
            return "All variables have not same value."
    return "All variables have same value."
print(multiple_variables_equality(2,3,2,2,2,2))
print(multiple_variables_equality(10,10,10,10))
print(multiple_variables_equality(-3,-3,-3,-3))  

print("125. Write a Python program to sum all counts in a collection")
print("Solution-1")
import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))
print("Solution-2")
nums = [2,2,4,6,6,8,6,10,4]
print(len(nums))

print("126. Write a Python program to get the actual module object for a given object")
print("Solution-1")
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))
print("Solution-2")
import inspect
def add(x, y):
    return x + y
print(inspect.getmodule(add))

print("127. Write a Python program to check whether an integer fits in 64 bits")
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
	
print("128. Write a Python program to check whether lowercase letters exist in a string")
print("Solution-1")
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))
print("Solution-2")
def lower_case_str(text):
    ctr = 0
    for char in text:
        if(ord(char) >= 97 and ord(char) <= 122):
            ctr = ctr + 1
    if (ctr>0):
        return True
str1 = 'A8238i823acdeOUEI'
print("Original string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'PYTHON'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'javascript'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
print("Solution-3")
def lower_case_str(text):
    if text.islower():
        return True
    return False
print("Check if all input alphabets are small!")
str1 = 'A8238i823acdeOUEI'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'PYTHON'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))
str1 = 'javascript'
print("\nOriginal string:",str1)
print("Lowercase letters exist in the said string: ",lower_case_str(str1))

print("129. Write a Python program to add leading zeroes to a string")
print("Solution-1")
str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
str1 = str1.rjust(8, '0')
print(str1)
str1 = str1.rjust(10, '0')
print(str1)
print("Solution-2")
str1='122.22'
print("Original String: ",str1)
print("\nAdded trailing zeros:")
f_text = '{:<08}'
str1 = f_text.format(str1)
print(str1)
f_text = '{:<010}'
str1 = f_text.format(str1)
print(str1)
print("\nAdded leading zeros:")
str1='122.22'
f_text = '{:>08}'
str1 = f_text.format(str1)
print(str1)
f_text = '{:>010}'
str1 = f_text.format(str1)
print(str1)

print("130. Write a Python program that uses double quotes to display strings")
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

print("131. Write a Python program to split a variable length string into variables")
print("Solution-1")
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)
print("Solution-2")
var_list = ['a', 'b', 'c', 'd', 'e']
v, w, x, y, z = var_list
print(v, w, x, y, z)

print("132. Write a Python program to list the home directory without an absolute path")
import os.path
print(os.path.expanduser('~'))

print("133. Write a Python program to calculate the time runs (difference between start and current time) of a program")
from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)
timer(5)
timer(15)

print("134. Write a Python program to input two integers on a single line")
print("Solution-1")
print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)
print("Solution-2")
a, b = [int(a) for a in input("Input the value of a & b: ").split()]
print("The value of a & b are:",a,b)

print("135. Write a Python program to print a variable without spaces between values")
print("Solution-1")
x = 30
print('Value of x is "{}"'.format(x))
print("Solution-2")
x = 30
print("Value of x is \"%i\"" % x)
print("Solution-3")
x = 30
print("Value of x is "+'\"' + str(x) + '\"')

print("136. Write a Python program to find files and skip directories in a given directory")
print("Solution-1")
import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])
print("Solution-2")
import os
user_path = 'd:/'
for fname in os.listdir(user_path):
    path = os.path.join(user_path, fname)
    if os.path.isdir(path):
        # skip directories
        continue
    # print the file names
    print(fname)

print("137. Write a Python program to extract a single key-value pair from a dictionary into variables")
print("Solution-1")
d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)
print("Solution-2")
dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
print("Extract specific key, value")
x, y = list(dict.items())[0]
print(x, y)
x, y = list(dict.items())[3]
print(x, y)

print("138. Write a Python program to convert true to 1 and false to 0")
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)

print("139. Write a Python program to validate an IP address")
print("Solution-1")
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
print("Solution-2")
import re
ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check_ip_address(user_ip):
    if(re.search(ip_regex, user_ip)):
        return "Valid Ip address"        
    else:
        return "Invalid Ip address"
user_ip = "10.0.0.0"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip = "10.255.255.255"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip = "192.168.255.0"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip = "266.1.0.2"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip = "01.102.103.104"
print("\n",user_ip,"->",check_ip_address(user_ip))

print("140. Write a Python program to convert an integer to binary that keeps leading zeros")
x = 12
print(format(x, '08b'))
print(format(x, '010b'))

print("141. Write a python program to convert decimal to hexadecimal")
print("Solution-1")
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))
print("Solution-2")
def dechimal_to_Hex(n):   
    x = (n % 16)
    ch = ""
    if (x < 10):
        ch = x
    if (x == 10):
        ch = "A"
    if (x == 11):
        ch = "B"
    if (x == 12):
        ch = "ch"
    if (x == 13):
        ch = "D"
    if (x == 14):
        ch = "E"
    if (x == 15):
        ch = "F"
    if (n - x != 0):
        return dechimal_to_Hex(n // 16) + str(ch)
    else:
        return str(ch)
dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]
print("Dechimal numbers:")
print(dechimal_nums)
print("\nHexadechimal numbers of the said dechimal numbers:")
print([dechimal_to_Hex(x) for x in dechimal_nums])
print("Solution-3")
def dechimal_to_Hex(dechimal_nums):
    digits = "0123456789ABCDEF"
    x = (dechimal_nums % 16)
    rest_part = dechimal_nums // 16
    if (rest_part == 0):
        return digits[x]
    return dechimal_to_Hex(rest_part) + digits[x]
dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]
print("Dechimal numbers:")
print(dechimal_nums)
print("\nHexadechimal numbers of the said dechimal numbers:")
print([dechimal_to_Hex(x) for x in dechimal_nums])

print("142. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string")
print("Solution-1")
def test(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0
str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
print("Solution-2")
def test(str1):
    temp=[]
    for x in str1:
        if (x=='0'):
            temp.append('0')
        else:
            temp.pop()
    return not temp
str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

print("143. Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system")
import struct
print(struct.calcsize("P") * 8)

print("144. Write a Python program to check whether a variable is an integer or string")
print(isinstance(25,int) or isinstance(25,str))
print(isinstance([25],int) or isinstance([25],str))
print(isinstance("25",int) or isinstance("25",str))

print("145. Write a Python program to test if a variable is a list, tuple, or set")
print("Solution-1")
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')    
else:
    print('Neither a list or a set or a tuple.')
print("Solution-2")
def check_type(nums):
    if isinstance(x, tuple)==True:
        return 'The variablex is a tuple'
    elif isinstance(x, list)==True:
        return 'The variablex is a list'
    elif isinstance(x, set)==True:
        return 'The variablex is a set'
    else:
        return 'Neither a list or a set or a tuple.'
x = ['a', 'b', 'c', 'd']
print(check_type(x))
x = {'a', 'b', 'c', 'd'}
print(check_type(x))
x = ('tuple', False, 3.2, 1)
print(check_type(x))
x = 100
print(check_type(x))

print("146. Write a Python program to find the location of Python module sources")
print("Solution-1")
import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))
print("Solution-2")
import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)

print("147. Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user")
def multiple(m, n):
    return True if m % n == 0 else False
print(multiple(20, 5))
print(multiple(7, 2))

print("148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers")
def max_min(data):
    l = data[0]
    s = data[0]
    for num in data:
        if num> l:
            l = num
        elif num< s:
            s = num
    return l, s
print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

print("149. Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number")
print("Solution-1")
def sum_of_cubes(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
    return total
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
print("Solution-2")
def sum_of_cubes(n):
    if n < 0:
        raise ValueError('n must be positive number!')
    return n*n*(n*n-2*n+1)/4
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(6))
print("Solution-3")
def sum_of_cubes(n):
    result = 0
    if n > 0:
        for i in range(n):
            result += i * i * i
        return result
    elif n <= 0:
        raise ValueError('n must be positive number!')
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))
print("Sum of cubes smaller than the specified number: ",sum_of_cubes(6))

print("150. Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values")
print("Solution-1")
def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if  i != j:
                product = nums[i] * nums[j]
            if product & 1:
                return True
    return False          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
print("Solution-2")
import itertools
def pair_nums_odd(nums):
    uniquelist = set(nums)
    result =[]
    for n in itertools.combinations(uniquelist, 2):
        if ((n[0] * n[1]) % 2 == 1):
            temp = str(n[0]) + " * " + str(n[1])
            result.append(temp)
    return result
dt1 = [2, 4, 6, 8]
print("Original sequence:")
print(dt1)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt1))
dt2 = [1, 6, 4, 7, 8]
print("\nOriginal sequence:")
print(dt2)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt2))
dt3 = [1, 3, 5, 7, 9]
print("\nOriginal sequence:")
print(dt3)
print("Distinct pair of numbers whose product is odd present in the said sequence:") 
print(pair_nums_odd(dt3))