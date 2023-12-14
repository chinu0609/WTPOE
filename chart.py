from flask import Flask
#from bokeh.embed import 
from bokeh.plotting import figure   
from bokeh.embed import autoload_static
import pandas as pd
from flask import render_template
from bokeh.resources import CDN
from bokeh.layouts import column
app = Flask("G")




@app.route("/")
def ganu():
    return "Ganesha"



@app.route("/chart")
def chart():
    #from csv
    df = pd.read_csv("advertising.csv")   
    
    plot1 = figure(height  = 350)
    #plot.circle([1,2], [3,4])
    plot1.circle(df["TV"],df["Sales"])
    plot2 = figure(height = 350)
    plot2.circle(df["Newspaper"],df["Sales"])
    plot3 = figure(height = 350)
    plot3.circle(df["Radio"],df["Sales"])
    
    js,tag = autoload_static(column(plot1,plot2,plot3),CDN,"./some.js")
    return render_template("chart.html",tag=tag,js=js)

if __name__ == "__main__":
    app.run(debug=True)
