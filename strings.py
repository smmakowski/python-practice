# concat and multiply strings

name = 'baconman'

print('I am ' + name + "!" * 3) # '' and "" acceptable

# access index for string

print(name[0])
print(name[-8]) # negative index start from end and work back (-1 == last char)

# select subsequence of string with :

print(name[2:5]) # selects start:end(exclusive) 'con'
print(name[5:]) # prints start:<end of string> if end ommited
print(name[:5]) # selects <start>:end if start ommitted
print(name[0:2+3]) #put expressions in index ranges

# upper and lowercase
uppercase = name.upper()

print(uppercase)
print(uppercase.lower())

# finding strings

print(name.find('bacon')) # returns index of substring start in str
print(name.find('bacon', 1)) # returns idx of sub in search from startIdx (case-sensitive)

# note: evert string in python begins with '' (empty string)

# converting numbers to strings

num = 1931312
print(str(num))

# rounding numbers
pi = 3.14
print(str(round(pi)))

# getting the length of a string
print(len(name))

# replacing substrings
sentence = 'I have bacon on my bacon inside my bacon with my bacon'
replacement = 'eggs'

print(sentence.replace('bacon', replacement, 1))
# .replace(old, new[, max Occurences])

# using [::-1]

def assertEqual(a, b) :
	if a == b :
		return True
	else :
		return False

def isPalindrome(word) :
	return word == word[::-1] # -1 means 1 step back (reads backwards)

string1 = 'tacocat!'
string2 = 'tacocat'

if assertEqual(isPalindrome(string1), False) and assertEqual(isPalindrome(string2), True) :
  print('All tests for isPalindrome() have passed')
