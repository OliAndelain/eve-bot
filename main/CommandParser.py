

# Command with one text argument
# Returns tuple of:
#	True/False	Does input contain command
#	text		The text after the command
def parse_for_text(input, command):
	if not input.lower().startswith(command.lower()):
		return (False, "")
	text=input[len(command):].strip()
	return (True, text)


# Command with one numeric argument
# Returns tuple of:
#	True/False	Does input contain command
#	True/False	Is argument a valid number
#	number		The number after the command
def parse_for_number(input, command):
	text_tuple=parse_for_text(input, command)
	if not text_tuple[0]:
		return (False, False, 0)
	if not text_tuple[1].isnumeric():
		return (True, False, 0)
	return (True, True, int(text_tuple[1]))
	
