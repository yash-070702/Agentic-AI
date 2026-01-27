import matplotlib.pyplot as plt 

fig,ax=plt.subplots()

ar1=[1,2,3,4,5,6,7]
ar2=[4,5,0,9,10,11,12]
ar3=[1,4,6,9,8,7,2]

# ax.plot(ar1,ar2,marker='o',color='g',label="practice")
# ax.plot(ar2,ar3,marker='*',color='r',label='again_practice')
# ax.set_title("Practice Plot")
# ax.set_xlabel('x lalala')
# ax.set_ylabel('y lalala')
# ax.legend()
# ax.grid()
# plt.show()

ax.bar(x-widthar1,ar2)
ax.bar(ar1,ar3)
ax.set_title("Practice Plot")
ax.set_xlabel('x lalala')
ax.set_ylabel('y lalala')
ax.legend()
ax.grid(axis='y')
plt.show()


plt.show()
