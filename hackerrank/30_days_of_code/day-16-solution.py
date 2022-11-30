
if __name__ == '__main__':
	# Read input from stdin (always string)
	S = input().strip()

	# use exceptiion handling
	try:
		# Try to convert input to integer
		S = int(S)
	except:
		# Print message if an exception happens
		print("Bad String")
	else:
		# If everything goes fine, print integer value
		print(S)
