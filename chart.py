from flask import Flask
#from bokeh.embed import 
from bokeh.plotting import figure   
from bokeh.embed import autoload_static

from flask import render_template
from bokeh.resources import CDN

app = Flask("G")




@app.route("/")
def ganu():
    return "Ganesha"



@app.route("/chart")
def chart():
    
    plot = figure()
    plot.circle([1,2], [3,4])

    js,tag = autoload_static(plot,CDN,"./some.js")
    return render_template("chart.html",tag=tag,js=js)

if __name__ == "__main__":
    app.run(debug=True)
