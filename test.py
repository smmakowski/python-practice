# test assert functions for export
def test(actual, expected, test: str) : # takes function call; args type only in python3
	if actual == expected :
		print('Passed test: "' + test + '".')
	else :
		print('Failed test: "' + test +'". Expected "' + str(expected) + '" but got "' + str(actual) + '".')
