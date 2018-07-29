from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import requests

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def jinja_template():
    points = np.random.randn(10)
    plt.plot(points)
    plt.savefig("static/myfig.png")

    dictionary = {'team': 'Expero', 'project': 'machine learning'}
    image_location = 'static/myfig.png'
    return render_template('jinja_template.html', logo=image_location, content=dictionary)

@app.route('/API', methods = ['GET'])
def api():
    if request.method == 'GET':
        dictionary = {'var1':request.args.get('arg1'),
                      'var2':request.args.get('arg2')}
    return jsonify(dictionary)
# to access the above, use:
# http://127.0.0.1:5000/API?arg1=One&arg2=Two

if __name__ == '__main__':
    app.run()
