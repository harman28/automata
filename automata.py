import sys
from PIL import Image

grid = []
row = []
tempRow = []
rule = []
length = 0

#calculates cell from rule string, position of new cell, and previous row
def calcCell(ruleString,position,prevRow):
	binaryString = ""
	for pos in range(position,position+3):
		pos = pos-1
		if pos < 0:
			pos = len(prevRow)-1
		elif pos >= len(prevRow):
			pos = 0
		binaryString += str(prevRow[pos])
	return ruleString[int(binaryString,base=2)]

if (len(sys.argv) < 3):
	print 'Syntax: automata.py [initial state] [rule string] [iterations]'
	print 'The intial state and the rule string should be binary strings.'
	print 'Using default values.'
	print ''

	row = [0,0,0,0,1,0,0,0,0]
	rule = [0,1,1,1,1,0,1,0]
	iters = 15

else:	
	for letter in sys.argv[1]:
		row.append(int(letter))
	for bit in sys.argv[2]:
		rule.append(int(bit))
	iters = int(sys.argv[3])

width = len(row)
height = iters+1
img = Image.new('RGB', (width,height))

grid.append(row)
length = len(row)

for i in range(iters): #i being the number of rows in cell grid
	for j in range(length): #j being the number of cells in row
		tempRow.append(calcCell(rule,j,grid[i]))
	grid.append(tempRow)
	tempRow = []

for eachRow in grid:
	print eachRow

pixelGrid = []
pixelRow = []
for i in range(0,len(grid)):
	for j in range(0,len(grid[i])):
		if grid[i][j] == 1:
			pixelGrid.append((0,0,0))
		else:
			pixelGrid.append((255,255,255))

img.putdata(pixelGrid,0,0)
img = img.resize((width*5,height*5))
img.save('img.png')