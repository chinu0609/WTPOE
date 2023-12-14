




from bokeh.embed import autoload_static
from bokeh.plotting import figure
from bokeh.resources import CDN

plot = figure()
plot.circle([1,2], [3,4])
print(autoload_static(plot,CDN,"./"))
