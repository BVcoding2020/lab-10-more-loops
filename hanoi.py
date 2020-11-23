	def move(f,t) :
	print("Move disc from {} to {} !".format(f,t))

	move("A", "C")
	Move disc from A to C:

	def moveVin(f,v,t) :
		move(f,v)
		move(v,t)

	moveVin("A", "B", "C")
	Move disc from A to B:
	Move disc from B to C:

	def foo(x) :
		foo(x)

	foo(3)

	def hanoi(n,f,h,t) :
		hanoi(n-1,f,t,h)
		move(f,t)
		hanoi(n-1,h,f,t)

	hanoi(4,"A","B","C")