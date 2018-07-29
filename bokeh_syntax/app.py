from flask import Flask, render_template, request
from bokeh.embed import components
from bokeh.plotting import figure

import numpy as np

app = Flask(__name__)

# Create the main plot
def create_figure():
    width = 10
    points = np.random.randn(width)
    plot = figure()
    plot.line(range(width), points)

    return plot

@app.route('/')
def index():
    # Create the plot
    plot = create_figure()

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("template.html", script=script, div=div)

# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)
