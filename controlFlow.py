import functions
test = functions.test

def bigger(a, b) :
	a if a > b else b # python verison of ternary <a expression> if <condition> else <b expresion>

test(bigger(5, -1), 5, 'bigger() should return first argument if it is greater.')
test(bigger(25, 998), 998, 'bigger() should return second argument if it is greater.')