# main algorithm
import math

class GIS:
	def __init__(self, name, x, y):
		self.x = x
		self.y = y
		self.name = name


def distance(a, b):
	return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def main():
	a = GIS("a",4,3)
	b = GIS("b",0,0)
	c = GIS("c",5,1)
	d = GIS("d",5,1)
	points = [a,b,c,d]
	print(distance(points[2], points[3]))

if __name__ == "__main__":
    # execute only if run as a script
    main()