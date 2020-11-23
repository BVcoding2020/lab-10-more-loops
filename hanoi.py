def move(f,t) :
	print("Move disc from {} to {} !".format(f,t)) #.format is a method

def moveVia(f,v,t):
	move(f,v)  # function call to move(): move from step one to step two
	# at first , the destination is v
	move(v,t) # move from step 2 to step 3 (out of 3)
		# now, the origin is v, an the destination is t

	def hanoi(n,f,h,t):	
		# n - number of discs
		# f - fromt position
 		# h - helper position
		# t - target position
		if n == 0:
			pass # this is the BASE CASE!
		else:
			hanoi(n-1,f,t,h) # function call within the function definition! (the recursion!)
			move(f,t)
			hanoi(n-1,h,f,t)

	hanoi(4,"A","B","C") # the function call that gets things going!

	# based on a tutorial by Prof. Thorsten Altenkirch