# main algorithm
import math
import random
import copy
import plotly.graph_objects as go
import pandas as pd

# ======================== LOADING DATASET

#dataset = pd.read_csv('Mall_Customers.csv',index_col='CustomerID')
#dataset = pd.read_csv('rental.csv')
dataset = pd.read_csv('data/crime.csv')
#print(dataset.head())
#print(dataset.info()) # Elementary EDA

NUM_CLUSTER = int(input("Specify number of clusters: ")) # Hyperparameter Input


# ======================== CLASS DEFINITIONS

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

# ======================== HELPER FUNCTIONS for K-MEANS

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

def visualize(points, centroids):
	plot_array=[]

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

# ======================== K-MEANS

def kmeans():
	
	X = dataset.iloc[:10000, [10]].values
	points = []
	for x in X:
		if type(x[0]) == float: # cleaning null values
			continue
		arr = x[0].strip('()').split(',')	
		arr[0] = int(float(arr[0])*1000)
		if arr[0] > 40000: # removing outliers
			continue
		arr[1] = int(float(arr[1])*1000)
		points.append(GIS("", arr[0], arr[1]))
		
	
	print(points[0:10])
	centroids = initiatize_centroids(points, NUM_CLUSTER)
	print(centroids)

	while(True):
		assign_centroid(points, centroids)
		old_centroids = copy.deepcopy(centroids) # to track change
		compute_centroid(points, centroids)
		if change_in_centroids(old_centroids, centroids) == False:
			break

	visualize(points, centroids)

# ======================== DRIVER CODE

if __name__ == "__main__":
    kmeans()

# ========================
