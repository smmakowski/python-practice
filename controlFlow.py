import test

# function returns a or b depending on what is bigger
def bigger(a, b) :
	return (a if a > b else b) # returns result of ternary expression

def is_friend(name) : # returns true if name (case insensitve) is in list of friends
	friends = ['Ryan', 'Ted', 'James']

	for i in range(0, len(friends)) :
		if name.upper() == friends[i].upper() :
			return True

	return False

def starts_with_d_or_n(word) : # returns true if word starts with d or n case insensitive
	return (True if word[0].upper() == 'D' or word[0].upper() == 'N' else False)

def one_to_n(n) : # returns range 1 to n inclusives
	rng = []
	i = 0

	while i < n :
		i += 1
		rng.append(i)

	return rng

def factorial(n) : # returns factorial
	if n <= 1 : 
		return 1

	factorial = n
	while n > 2 :
		n -= 1
		factorial *= n

	return factorial

def break_statement() : # while condition should reurn 4 (just to ilustrate breaks)
	i, j = 0, 1 # multiple assignment with commas

	while i < 10 : 
		if (i == 4 and j == 3) : # and bool operator
			break; # break works same as js

		i += 2
		j += 1

	return i

def find_bacon(string) : # returns true if 'bacon' is found instring case insensitive
	return (True if string.upper().find('BACON') > -1 else False)

# python verison of ternary <a expression> if <condition> else <b expresion>

test.test(bigger(5, -1), 5, 'bigger() should return first argument if it is greater.')
test.test(bigger(25, 998), 998, 'bigger() should return second argument if it is greater.')
test.test(is_friend('ryAn'), True, 'is_friend() should return True if name(case-insensitive) is in friends array')
test.test(is_friend('Bob'), False, 'is_friend() should return alse if name not in array')
test.test(starts_with_d_or_n('delicious'), True, 'start_with_d_or_n() should return true if d or n')
test.test(starts_with_d_or_n('negligence'), True, 'start_with_d_or_n() should return True if d or n')
test.test(starts_with_d_or_n('Ambiences'), False, 'start_with_d_or_n() should return False if d or n')
test.test_array(one_to_n(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'one_to_n() returns array with range 1 ... n (inclusive)')
test.test(factorial(5), 120, 'factorial() should return n! if number >= 2')
test.test(factorial(5), 120, 'factorial() should return 1 if number <= 1')
test.test(break_statement(), 4, 'break_statement() should return 4')
test.test(find_bacon('wheres the BaCon for I am bacon man'), True, 'find_bacon() shoud return True if bacon found')
test.test(find_bacon('wheres the muffin for I am muffin man'), False, 'find_bacon() shoud return False if bacon found')


