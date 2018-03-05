import test
test = test.test
# functions to test

def sum(*args) : # args is none or more numbers
	total = 0
	if len(args) == 0 : # prints notification if no args
		print('No numbers passed into sum().')
	elif len(args) == 1 :
		total = args[0]
		print('Only one number entered into sum(). Number is ' + str(total) + '.')
	else :
		for i in range(0, len(args)) :
			total += args[i]
		print('Sum is: ' + str(total) + '.')

	return total

def square(n) :
	return n * n

#takes two strings as inputs and returns string that is firstInput + two repetitions of second + first input

def abbaize(str1, str2) :
	return str1 + str2 * 2 + str1 # string multiplication works in python

# run tests
test(sum(2, 4), 6, 'sum() should sum two numbers')
test(sum(), 0, 'sum() should return 0 if no arguments')
test(sum(-5), -5, 'sum() should return number passed if only one argument')
test(sum(2, 5, -5, 9, 10, 0.5), 21.5, ' sum() should return sum of two or more numbers')
test(square(5), 25,'square() should return argument squared')
test(abbaize('bacon', 'man'), 'baconmanmanbacon', 'abbaize() should take two strings and ouput first + second + second + first')








