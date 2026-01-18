import numpy as np
# from scipy.spatial import distance

# # -----------------------------------------
# # Define two points (vectors) in 2D space
# # -----------------------------------------
# p1 = np.array([1, 2])
# p2 = np.array([4, 6])

# # -----------------------------------------
# # Euclidean Distance (L2 norm)
# # -----------------------------------------
# # Measures the straight-line distance between two points
# # Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
# d = distance.euclidean(p1, p2)
# print(d)

# # -----------------------------------------
# # Chebyshev Distance (L-infinity norm)
# # -----------------------------------------
# # Maximum absolute difference between coordinates
# # Formula: max(|x2 - x1|, |y2 - y1|)
# d2 = distance.chebyshev(p1, p2)

# # -----------------------------------------
# # Cosine Distance
# # -----------------------------------------
# # Measures the angle between two vectors (direction difference)
# # Value range: 0 (same direction) to 1 (orthogonal/opposite)
# # Formula: 1 - cosine similarity
# d3 = distance.cosine(p1, p2)

# # -----------------------------------------
# # Print the remaining distances
# # -----------------------------------------
# print(d2)
# print(d3)

###############################################


# import numpy as np
# from scipy.spatial.distance import pdist, squareform

# # ------------------------------------------------
# # Scenario:
# # An agent has multiple states (points in space)
# # and wants to compute distances between ALL states
# # ------------------------------------------------

# # Each row represents a point/state in 2D space
# points = np.array([
#     [0, 0],   # State 1
#     [1, 1],   # State 2
#     [2, 2]    # State 3
# ])

# # ------------------------------------------------
# # pdist():
# # Computes pairwise distances between all points
# # Returns distances in condensed (1D) form
# # ------------------------------------------------

# # ------------------------------------------------
# # squareform():
# # Converts condensed distance vector into
# # a full square distance matrix
# # ------------------------------------------------

# distances = squareform(pdist(points))

# # ------------------------------------------------
# # Final result:
# # distances[i][j] = distance between point i and j
# # Diagonal values are 0 (distance to itself)
# # ------------------------------------------------

# print(distances)


#######################################################




# import numpy as np
# from scipy.spatial import KDTree

# # ------------------------------------------------
# # Define a set of points in 2D space
# # Each row represents one point (x, y)
# # ------------------------------------------------
# points = np.array([
#     [2, 3],
#     [5, 4],
#     [9, 6],
#     [4, 7],
#     [8, 1]
# ])

# # ------------------------------------------------
# # Create a KDTree from the given points
# # This preprocesses the data for fast searching
# # ------------------------------------------------
# tree = KDTree(points)

# # ------------------------------------------------
# # Query the KDTree with a new point [5, 5]
# # The tree finds the nearest neighbor efficiently
# # ------------------------------------------------
# dist, idx = tree.query([5, 5])

# # ------------------------------------------------
# # dist = distance from query point to nearest point
# # idx  = index of the nearest point in the 'points' array
# # ------------------------------------------------
# print("Distance to nearest point:", dist)

# # ------------------------------------------------
# # Retrieve the nearest point using the returned index
# # ------------------------------------------------
# nearest_point = points[idx]
# print("Nearest point to [5,5]:", nearest_point)

#######################################################

