import random


#	CREATE 2D ARRAY AS INITIAL GRID
grid = [[ random.randint(0,1) for x in range(0,10)] for y in range(0,10)]

#print(grid)

automate(grid)





#	UPDATE TO NEW GRID
def automate(originalGrid):
	for x in grid:
		grid[x] = calculate(grid[x])
		pass


	pass


#	RULE FUNCTION
def calculate(originalGrid):
	
	pass





