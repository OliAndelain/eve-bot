import main.CommandParser as CommandParser

tests=0;

def test_CommandParser_text():
	global tests
	# input, command, expected
	data=[
		("notcmd arg", "cmd", (False, "")),
		("cmd arg", "cmd", (True, "arg")),
		("cmd arg", "CMD", (True, "arg")),
		("cmd seVeral args", "cmd", (True, "seVeral args")),
		("cmd    several  args  ", "cmd", (True, "several  args")),
	];
	
	for datum in data:
		output=CommandParser.parse_for_text(datum[0], datum[1])
		if output != datum[2]:
			print("FAILED test_CommandParser_text - for data set {} received {}".format(datum, output))
		tests=tests+1

def test_CommandParser_number():
	global tests
	# input, command, expected
	data=[
		("notcmd arg", "cmd", (False, False, 0)),
		("cmd arg", "cmd", (True, False, 0)),
		("cmd 7", "cmd", (True, True, 7)),
		("cmd 0", "cmd", (True, True, 0)),
		("cmd -13", "cmd", (True, False, 0)),
	];
	
	for datum in data:
		output=CommandParser.parse_for_number(datum[0], datum[1])
		if output != datum[2]:
			print("FAILED test_CommandParser_number - for data set {} received {}".format(datum, output))
		tests=tests+1

test_CommandParser_text()
test_CommandParser_number()
print("Run {} tests".format(tests))
