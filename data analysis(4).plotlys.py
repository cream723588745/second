from plotffff import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline
die_1=Die()
die_2=Die()

result=[]
for roll_nums in range(1000):
    m=die_1.roll()+die_2.roll()
    result.append(m)

frequencies=[]
for value in range(2,die_1.num_sides+die_2.num_sides+1):
    frequency=result.count(value)
    frequencies.append(frequency)
print(frequencies)

x_values=list(range(2,die_1.num_sides+die_2.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={'title':'result','dtick':1}
y_axis_config={'title':'frequency'}
my_layout=Layout(title='the result of throw two 1000 times 6D dices',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')