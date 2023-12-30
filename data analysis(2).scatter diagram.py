import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig,ax =plt.subplots()
x_values=range(1,1001)
y_values=[x**2 for x in x_values]
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)  # 's' is used to set up the size of point  'c' is used to set up the color of point and you can use c=(0,0.8,0) to set up color(rgb)
ax.set_title('square number',fontsize=24)                        #cmap是用于颜色映射，y值越大，颜色越深，c等于y值
ax.set_xlabel('value',fontsize=14)
ax.set_ylabel('the value of square number',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0,1100,0,1100000])   #set the range of axis(坐标轴)
plt.savefig('document name',bbox_inches='tight')   #save the picture,the first parameter is the picture name,the second parameter is used to wipe of blank space
plt.show()