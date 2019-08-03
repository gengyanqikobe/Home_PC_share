







from pyecharts.charts import Bar


bar = Bar()
bar.add_xaxis(['一月','二月','三月'])
bar.add_yaxis('温度',[5,10,15])

bar.render()