# main algorithm
import math
import random
import copy
import plotly.graph_objects as go

NUM_CLUSTER = int(input("Specify number of clusters: "))


# ========================

class GIS:
	def __init__(self, name, x, y):
		self.x = x
		self.y = y
		self.name = name
		self.centroid = None

	def __repr__(self):
		return f"{self.name}(x:{self.x}, y:{self.y}) -> Cluster: {self.centroid}"

class Centroid:
	def __init__(self, idx, x, y):
		self.x = x
		self.y = y
		self.idx = idx

	def __repr__(self):
		return f"{self.idx}(x:{self.x}, y:{self.y})\n"

def distance(a, b):
	return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def initiatize_centroids(points, n):
	centroids = []
	random_points = random.sample(points, n)
	idx = 0
	for point in random_points:
		centroids.append(Centroid(idx, point.x, point.y))
		idx += 1
	# inserted random n points in centroids
	return centroids

def change_in_centroids(old_centroids, centroids):
	for i in range(len(centroids)):
		if centroids[i].x != old_centroids[i].x or centroids[i].y != old_centroids[i].y:
			return True # changed
	return False

def assign_centroid(points, centroids):
	for point in points:
		min = 0
		for i in range(len(centroids)):
			if(distance(point, centroids[i]) < distance(point, centroids[min])):
				min = i
		point.centroid = centroids[min]

def compute_centroid(points, centroids):
	for centroid in centroids:
		x_sum = 0
		y_sum = 0
		count = 0
		for point in points:
			if point.centroid == centroid:
				x_sum += point.x
				y_sum += point.y
				count += 1
		if count > 0:
			centroid.x = x_sum/count
			centroid.y = y_sum/count



def kmeans():
	a = GIS("a",1,3)
	b = GIS("b",0,0)
	c = GIS("c",5,1)

	d = GIS("d",5,2)
	e = GIS("e",1,1)
	f = GIS("f",0,1)
	points = [a,b,c,d,e,f]
	#print(points)
	centroids = initiatize_centroids(points, NUM_CLUSTER)
	# print(centroids)

	while(True):
		#compute_ssd() # sum of squared distances
		assign_centroid(points, centroids)
		old_centroids = copy.deepcopy(centroids) # to track change
		compute_centroid(points, centroids)
		if change_in_centroids(old_centroids, centroids) == False:
			break

	plot_array=[]
	##Array of x and array of y corresponding to each centroid

	#plot_array = [C1, C2, C3]
	# 			[[[x-elements],[y-elements]],[[],[]]]
	#plot_array[centroid_position][x]

	for centroid in centroids:
		plot_array.append([[],[]])
		for point in points:
			if(point.centroid.x==centroid.x and point.centroid.y==centroid.y ):
				plot_array[len(plot_array)-1][0].append(point.x)
				plot_array[len(plot_array)-1][1].append(point.y)	

	colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(NUM_CLUSTER)]
	fig=go.Figure()
	for i in range(NUM_CLUSTER):
		fig.add_trace(go.Scatter(
	    x=plot_array[i][0],
	    y=plot_array[i][1],
	    marker=dict(color=colors[i], size=12),
	    mode="markers",
	    name="Cluster "+str(i+1),
		))
	fig.show()

if __name__ == "__main__":
    kmeans()
