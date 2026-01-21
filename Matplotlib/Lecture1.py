import matplotlib.pyplot as plt



# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# y2= [1, 4, 9, 16, 25]

#Line Plot Example

# fig,axes=plt.subplots(1,2,figsize=(10,5))
# axes[0].plot(x,y,color='g',marker='o',linestyle='--',linewidth=3,markersize=8,label='Linear Growth')
# axes[0].set_title('Line Plot')
# axes[0].set_xlabel('X-axis')
# axes[0].set_ylabel('Y-axis')
# axes[0].grid(True)
# axes[0].legend()


###########################
###########################

#Scatter Plot Example


# axes[1].scatter(x,y,color='g',marker='o',label='Data Points')
# axes[1].set_title('Scatter Plot')
# axes[1].set_xlabel('X-axis')
# axes[1].set_ylabel('Y-axis')
# axes[1].grid(True)
# axes[1].legend()
# plt.show()


###########################
###########################

#Multiple Lines in One Plot Example
#and multiple scatter points

# fig , ax = plt.subplots(1,2,figsize=(8,6))
# ax[0].plot(x,y,color='b',marker='o',linestyle='-',linewidth=2,markersize=6,label='Linear Growth')
# ax[0].plot(x,y2,color='r',marker='s',linestyle='--',linewidth=2,markersize=6,label='Quadratic Growth')

# ax[0].set_title('Multiple Lines Plot')
# ax[0].set_xlabel('X-axis')
# ax[0].set_ylabel('Y-axis')
# ax[0].grid(True)
# ax[0].legend()
# # Scatter Plot with Multiple Series
# ax[1].scatter(x,y,color='b',marker='o',label='Linear Data Points')
# ax[1].scatter(x,y2,color='r',marker='s',label='Quadratic Data Points')
# ax[1].set_title('Scatter Plot with Multiple Series')            
# ax[1].set_xlabel('X-axis')
# ax[1].set_ylabel('Y-axis')
# ax[1].grid(True)
# ax[1].legend()

# plt.show()


###########################
###########################

#Bar Chart Example


# categories = ['A', 'B', 'C', 'D']
# values = [10, 25, 15, 30]

# fig,ax=plt.subplots(figsize=(8,6))
# ax.bar(categories,values,color=['r','g','b','y'],edgecolor='black')
# ax.set_title('Bar Chart Example')
# ax.set_xlabel('Categories')
# ax.set_ylabel('Values')
# ax.grid()
# plt.show()

###########################
###########################

#mutli bar chart


# import numpy as np

# labels = ['A', 'B', 'C']
# x = np.arange(len(labels))

# data1 = [20, 35, 30]
# data2 = [25, 32, 34]

# width = 0.35

# fig, ax = plt.subplots()

# ax.bar(x - width/2, data1, width, label='Group 1')
# ax.bar(x + width/2, data2, width, label='Group 2')

# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()

# plt.show()

###########################
###########################

# data = [12, 15, 14, 10, 18, 20, 22, 19, 15, 14, 16, 17]

# fig, ax = plt.subplots()

# ax.hist(
#     data,
#     bins=6,
#     color='skyblue',
#     edgecolor='black',
#     alpha=0.8
# )

# ax.set_title("Histogram Example")
# ax.set_xlabel("Values")
# ax.set_ylabel("Frequency")
# ax.grid(axis='y')

# plt.show()

###########################
###########################

#mutiple histogram

# data1 = [10, 12, 14, 15, 16, 18, 20]
# data2 = [8, 9, 11, 13, 15, 17, 19]

# fig, ax = plt.subplots()

# ax.hist(data1, bins=5, alpha=0.6, label='Data 1')
# ax.hist(data2, bins=5, alpha=0.6, label='Data 2')

# ax.set_title("Histogram Example")
# ax.set_xlabel("Values")
# ax.set_ylabel("Frequency")
# ax.grid(axis='y')

# ax.legend()
# plt.show()

###########################
###########################

#Pie Chart Example

# labels = ['A', 'B', 'C', 'D']
# sizes = [25, 35, 20, 20]
# explode = [0.1, 0.1, 0.1, 0.1]

# fig, ax = plt.subplots()
# ax.pie(
#     sizes,
#     labels=labels,
#     shadow=True,
#     colors=['lightcoral', 'lightskyblue', 'lightgreen', 'gold'],
#     autopct='%1.1f%%',
#     explode=explode,
#     startangle=90
# )
# ax.axis('equal')
# ax.set_title('Pie Chart Example')
# plt.show()

###########################
###########################

#Multiple Pie Charts Example
# labels = ['A', 'B', 'C']
# sizes1 = [30, 50, 20]
# sizes2 = [40, 30, 30]
# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# ax[0].pie(
#     sizes1,
#     labels=labels,
#     autopct='%1.1f%%',
#     startangle=90,
#     colors=['lightcoral', 'lightskyblue', 'lightgreen']
# )
# ax[0].set_title('Pie Chart 1')
# ax[1].pie(
#     sizes2,
#     labels=labels,
#     autopct='%1.1f%%',
#     startangle=90,
#     colors=['lightcoral', 'lightskyblue', 'lightgreen']
# )
# ax[1].set_title('Pie Chart 2')
# plt.show()
###########################
###########################

#box plot example
data = [ [12, 15, 14, 10, 18, 20, 22],
         [8, 9, 11, 13, 15, 17, 19],
         [14, 16, 15, 18, 20, 22, 24] ]

fig, ax = plt.subplots()
ax.boxplot(data, patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='blue'),
           medianprops=dict(color='red'))
ax.set_title("Box Plot Example")
ax.set_xlabel("Data Sets")
ax.set_ylabel("Values")
ax.set_xticklabels(['Set 1', 'Set 2', 'Set 3'])
ax.grid()
plt.show()





