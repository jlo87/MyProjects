# Shows a simple zig zag animation.

# Press Ctrl-C to stop the program.

import time
indentSize = 0 # How many spaces to indent.

DELAY = 0.05 # Uppercase Constant variable.
INDENT_CHARACTER = ' ' # The DELAY and INDENT_CHARACTER constants will make things easier to change on the fly.

while True: # The main program loop.
	# Zip to the right 20 times:
	for i in range(20):
		indentSize += 1 # Shortcut for indentSize = indentSize + 1
		indentation = INDENT_CHARACTER * indentSize
		print(indentation + '********')
		time.sleep(DELAY) # Pause for 50 milliseconds.

	# Zag to the left 20 times:
	for i in range(20):
		indentSize -= 1 # Shortcut for indentSize = indentSize - 1
		indentation = INDENT_CHARACTER * indentSize
		print(indentation + '********')
		time.sleep(DELAY) # Pause for 50 milliseconds.
