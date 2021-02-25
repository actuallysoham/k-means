# main algorithm
import math
import random
import copy
NUM_CLUSTER = 2 # hyperparam - pls to set accordingly


class Centroid:
	def __init__(self, idx, x, y):
		self.x = x
		self.y = y
		self.idx = idx

	def __repr__(self):
		return f"{self.idx}(x:{self.x}, y:{self.y})\n"

def distance(a, b):
	return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def change_in_centroids(old_centroids, centroids):
	for i in range(len(centroids)):
		if centroids[i].x != old_centroids[i].x or centroids[i].y != old_centroids[i].y:
			print("Not Same")
			print(centroids[i])
			print(old_centroids[i])
			return True # changed
	return False



def kmeans():

	#print(points)
	c1 = Centroid("b",4.6666667,1)
	c2 = Centroid("c",5,1)

	c3 = Centroid("b",4.6666667,1)
	c4 = Centroid("c",5,1)

	centroids  = [c1, c2]
	old_centroids = [c3, c4]

	print(old_centroids)
	print(centroids)

	if change_in_centroids(old_centroids, centroids):
		print("Go again")
	else:
		print("Yeet")


if __name__ == "__main__":
    kmeans()