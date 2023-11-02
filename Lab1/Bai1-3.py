print("1. Python program to check if a string is palindrome or not")
print("Solution-1")
# function which return reverse of a string
def isPalindrome(s):
	return s == s[::-1]
# Driver code
s = "malayalam"
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")
print("Solution-2")
# function to check string is
# palindrome or not
def isPalindrome(str):
	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True
# main function
s = "malayalam"
ans = isPalindrome(s)
if (ans):
	print("Yes")
else:
	print("No")
print("Solution-3")
# function to check string is
# palindrome or not
def isPalindrome(s):
	# Using predefined function to
	# reverse to string print(s)
	rev = ''.join(reversed(s))
	# Checking if both string are
	# equal or not
	if (s == rev):
		return True
	return False
# main function
s = "malayalam"
ans = isPalindrome(s)
if (ans):
	print("Yes")
else:
	print("No")
print("Solution-4")
# Python program to check
# if a string is palindrome
# or not
x = "malayalam"
w = ""
for i in x:
	w = i + w
if (x == w):
	print("Yes")
else:
	print("No")
print("Solution-5")
# Python program to check
# if a string is palindrome
# or not
st = 'malayalam'
j = -1
flag = 0
for i in st:
	if i != st[j]:
		flag = 1
		break
	j = j - 1
if flag == 1:
	print("NO")
else:
	print("Yes")
print("Solution-6")
# Recursive function to check if a
# string is palindrome
def isPalindrome(s):

	# to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)

	# if length is less than 2
	if l < 2:
		return True

	# If s[0] and s[l-1] are equal
	elif s[0] == s[l - 1]:

		# Call is palindrome form substring(1,l-1)
		return isPalindrome(s[1: l - 1])

	else:
		return False

# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)

if ans:
	print("Yes")

else:
	print("No")

print("2. Python program to check whether the string is Symmetrical or Palindrome")
print("Solution-1")
# Python program to demonstrate
# symmetry and palindrome of the
# string
# Function to check whether the
# string is palindrome or not
def palindrome(a):
	# finding the mid, start 
	# and last index of the string
	mid = (len(a)-1)//2	 #you can remove the -1 or you add <= sign in line 21 
	start = 0			 #so that you can compare the middle elements also.
	last = len(a)-1
	flag = 0
	# A loop till the mid of the
	# string
	while(start <= mid):
		# comparing letters from right
		# from the letters from left
		if (a[start]== a[last]):
			start += 1
			last -= 1
		else:
			flag = 1
			break
	# Checking the flag variable to 
	# check if the string is palindrome
	# or not
	if flag == 0:
		print("The entered string is palindrome")
	else:
		print("The entered string is not palindrome")
# Function to check whether the
# string is symmetrical or not	 
def symmetry(a):
	n = len(a)
	flag = 0
	# Check if the string's length
	# is odd or even
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2
	start1 = 0
	start2 = mid
	while(start1 < mid and start2 < n):
		
		if (a[start1]== a[start2]):
			start1 = start1 + 1
			start2 = start2 + 1
		else:
			flag = 1
			break
	# Checking the flag variable to 
	# check if the string is symmetrical
	# or not
	if flag == 0:
		print("The entered string is symmetrical")
	else:
		print("The entered string is not symmetrical")
# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)
print("Solution-2")
string = 'amaama'
half = int(len(string) / 2)
first_str = string[:half]
second_str = string[half:]
# symmetric
if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')
# palindrome
if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')
print("Solution-3")
# Python program to check whether the string is Symmetrical or Palindrome
import re
input_str = "amaama"
reversed_str = input_str[::-1]
if input_str == reversed_str:
	print("The entered string is symmetrical")
else:
	print("The entered string is not symmetrical")
if re.match("^(\w+)\Z", input_str) and input_str == input_str[::-1]:
	print("The entered string is palindrome")
else:
	print("The entered string is not palindrome")
print("Solution-4")
# code
string ="malayalam"
print("the string is palindrome" if string==reversed(string) else "the string is not palindrome")

print("3. Reverse words in a given String in Python")
print("Solution-1")
# Python code
# To reverse words in a given string
# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# appending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))
print("Solution-2")
# Function to reverse words of string 
def rev_sentence(sentence): 
	# first split the string into words 
	words = sentence.split(' ') 
	# then reverse the split string list and join using space 
	reverse_sentence = ' '.join(reversed(words)) 
	# finally return the joined string 
	return reverse_sentence 
if __name__ == "__main__": 
	input = 'geeks quiz practice code'
	print (rev_sentence(input)) 
print("Solution-3")
# Function to reverse words of string
import re
def rev_sentence(sentence):
	# find all the words in sentence
	words = re.findall('\w+', sentence)
	# Backward iterate over list of words and join using space
	reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
	# finally return the joined string
	return reverse_sentence
if __name__ == "__main__":
	input = 'geeks quiz practice code'
	print (rev_sentence(input))
print("Solution-4")
# initializing string
string = "geeks quiz practice code"
# creating an empty stack
stack = []
# pushing words onto the stack
for word in string.split():
	stack.append(word)
# creating an empty list to store the reversed words
reversed_words = []
# popping words off the stack and appending them to the list
while stack:
	reversed_words.append(stack.pop())
# joining the reversed words with a space
reversed_string = " ".join(reversed_words)
# printing the reversed string
print(reversed_string)
#This code is contributed by Edula Vinay Kumar Reddy
print("Solution-5")
def reverse_words(string):
	# split the string into a list of words
	words = string.split()
	# initialize an empty string to store the reversed words
	reversed_string = ''
	# loop through the words in reverse order and append them to the reversed string
	for i in range(len(words)-1, -1, -1):
		reversed_string += words[i] + ' '
	# remove the extra space at the end of the reversed string and return it
	return reversed_string.strip()
# example usage
string = "geeks quiz practice code"
reversed_string = reverse_words(string)
print(reversed_string) # output: "code practice quiz geeks"
print("Solution-6")
# Python program for the above approach
# Function to reverse the words in string
def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1
# Function to reverse the string
def reverse_string(s):
	s = list(s)
	start, end = 0, len(s) - 1
	reverse_word(s, start, end)
	start = end = 0
	# Iterate over the string S
	while end < len(s):
		if s[end] == ' ':
			reverse_word(s, start, end - 1)
			start = end + 1
		end += 1
	# Reverse the words
	reverse_word(s, start, end - 1)
	return ''.join(s)
# Driver Code
S = "geeks quiz practice code"
print(reverse_string(S))

print("4. Ways to remove i’th character from string in Python")
print("Solution-1")
# Initializing String
test_str = "GeeksForGeeks"
# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')
# Printing string after removal
# removes all occurrences of 'e'
print("The string after removal of i'th character( doesn't work) : " + new_str)
# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)
# Printing string after removal
# removes first occurrences of s
print("The string after removal of i'th character(works) : " + new_str)
print("Solution-2")
str = 'Geeks123For123Geeks'
print(str.translate({ord(i): None for i in '123'}))
print("Solution-3")
def remove_ith_character(s, i):
	# Base case: if index is 0, 
	# return string with first character removed
	if i == 0:
		return s[1:]
	# Recursive case: return first character 
	# concatenated with result of calling function 
	# on string with index decremented by 1
	return s[0] + remove_ith_character(s[1:], i - 1)
# Test the function
test_str = "GeeksForGeeks"
new_str = remove_ith_character(test_str, 2)
print("The string after removal of ith character:", new_str)
# This code is contributed by Edula Vinay Kumar Reddy
print("Solution-4")
test_str = "GeeksForGeeks"
# Removing char at pos 3
new_str = ""
for i in range(len(test_str)):
	if i != 2:
		new_str = new_str + test_str[i]
# Printing string after removal
print ("The string after removal of i'th character : " + new_str)
print("Solution-5")
# Initializing String
test_str = "GeeksForGeeks"
# Removing char at pos 3
# using slice + concatenation
new_str = test_str[:2] + test_str[3:]
# Printing string after removal
# removes ele. at 3rd index
print ("The string after removal of i'th character : " + new_str)
print("Solution-6")
# Initializing String
test_str = "GeeksForGeeks"
# Removing char at pos 3
# using join() + list comprehension
new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])
# Printing string after removal
# removes ele. at 3rd index
print ("The string after removal of i'th character : " + new_str)
print("Solution-7")
def remove_char(s, i):
	b = bytearray(s, 'utf-8')
	del b[i]
	return b.decode()
# Example usage
s = "hello world"
i = 4
s = remove_char(s, i)
print(s)
print("Solution-8")
#initializing the string
s="GeeksforGeeks"
#if you wanted to remove "G" of 0th index
s1=s.removeprefix("G")
#if you wanted to remove "f"
s2=s[:5]+s[5:].removeprefix("f")
print(s1)
print(s2)

print("5. Python | Check if a Substring is Present in a Given String")
print("Solution-1")
# Take input from users 
MyString1 = "A geek in need is a geek indeed"
if "need" in MyString1: 
	print("Yes! it is present in the string") 
else: 
	print("No! it is not present") 
print("Solution-2")
text = "Geeks welcome to the Geek Kingdom!"
if "Geek" in text: 
	print("Substring found!") 
else: 
	print("Substring not found!") 
if "For" in text: 
	print("Substring found!") 
else: 
	print("Substring not found!")
print("Solution-3")
# input strings str1 and substr 
string = "geeks for geeks" # or string=input() -> taking input from the user 
substring = "geeks" # or substring=input() 
# splitting words in a given string 
s = string.split() 
# checking condition 
# if substring is present in the given string then it gives output as yes 
if substring in s: 
	print("yes") 
else: 
	print("no")
print("Solution-4")
def check(string, sub_str): 
	if (string.find(sub_str) == -1): 
		print("NO") 
	else: 
		print("YES") 
# driver code 
string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str) 
print("Solution-5")
def check(s2, s1): 
	if (s2.count(s1) > 0): 
		print("YES") 
	else: 
		print("NO") 
s2 = "A geek in need is a geek indeed"
s1 = "geeks"
check(s2, s1) 
print("Solution-6")
any_string = "Geeks for Geeks substring "
start = 0
end = 1000
print(any_string.index('substring', start, end)) 
print("Solution-7")
s="geeks for geeks"
s2="geeks"
print(["yes" if s2 in s else "no"]) 
print("Solution-8")
s="geeks for geeks"
s2="geeks"
x=list(filter(lambda x: (s2 in s),s.split())) 
print(["yes" if x else "no"]) 
print("Solution-9")
a = ['Geeks-13', 'for-56', 'Geeks-78', 'xyz-46'] 
for i in a: 
	if i.__contains__("Geeks"): 
		print(f"Yes! {i} is containing.")
print("Solution-10")
def is_substring(string, substring): 
	for i in range(len(string) - len(substring) + 1): 
		if string[i:i+len(substring)] == substring: 
			return True
	return False
string = "A geeks in need is a geek indeed"
substring = "geeks"
print(is_substring(string,substring)) 
print("Solution-11")
import re 
MyString1 = "A geek in need is a geek indeed"
if re.search("need", MyString1): 
	print("Yes! it is present in the string") 
else: 
	print("No! it is not present") 
print("Solution-12")
#Python program to check if a substring is present in a given string 
import operator as op 
s="geeks for geeks"
s2="geeks"
if(op.contains(s,s2)): 
	print("yes") 
else: 
	print("no")

print("6. Python – Words Frequency in String Shorthands")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("7. Python – Convert Snake case to Pascal case")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("8. Find length of a string in python (4 ways)")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("9. Python program to print even length words in a string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("10. Python program to accept the strings which contains all vowels")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("11. Python | Count the Number of matching characters in a pair of string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("12. Remove all duplicates from a given string in Python")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("13. Python – Least Frequent Character in String")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("14. Python | Maximum frequency character in String")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("15. Python | Program to check if a string contains any special character")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("16. Generating random strings until a given string is generated")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("17. Find words which are greater than given length k")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("18. Python program for removing i-th character from a string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("19. Python program to split and join a string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("20. Python | Check if a given string is binary string or not")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("21. Python program to find uncommon words from two Strings")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("22. Python – Replace duplicate Occurrence in String")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("23. Python – Replace multiple words with K")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("24. Python | Permutation of a given string using inbuilt function")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("25. Python | Check for URL in a String")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("26. Execute a String of Code in Python")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("27. String slicing in Python to rotate a string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("28. String slicing in Python to check if a string can become empty by recursive deletion")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("29. Python Counter| Find all duplicate characters in string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")

print("30. Python – Replace all occurrences of a substring in a string")
print("Solution-1")
print("Solution-2")
print("Solution-3")
print("Solution-4")
