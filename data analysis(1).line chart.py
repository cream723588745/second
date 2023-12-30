import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]    #appoint input_values and output_values
squares=[1,4,9,16,25]
plt.style.use('seaborn')
fig, ax=plt.subplots()   #f ig表示整张图片，ax表示图片中的各个图表
ax.plot(input_values,squares,linewidth=3)  # linewidth用于设置线条宽度  fontsize设置字体大小
ax.set_title("square number",fontsize=24)
ax.set_xlabel("figure",fontsize=14)
ax.set_ylabel("the square of figure",fontsize=14)
ax.tick_params(axis='both',labelsize=14)  #tick_params设置刻度样式
plt.show()