from flask import Flask,render_template, request
import numpy as np
from keras.models import load_model
import time


app = Flask(__name__)
app.vars = {}

app.vars['model'] = load_model('model-development/additionNet.h5')

def findNeuralSum(a, b):
    X = np.array([[a,b]])
    #result = estimator.predict(X)
    result = app.vars['model'].predict_classes(X)
    return int(result[0])

def findManualSum(a, b):
    return a+b

def timeFormat(elapsedSecs):
    return "in %.2E sec." % elapsedSecs

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        app.vars['n1'] = int(request.form['number1'])
        app.vars['n2'] = int(request.form['number2'])

        startTime = time.time()
        sumManual = findManualSum(app.vars['n1'], app.vars['n2'])
        timeManual = time.time()-startTime

        startTime = time.time()
        sumNeural = findNeuralSum(app.vars['n1'], app.vars['n2'])
        timeNeural = time.time()-startTime


        timeNeuralDisplay = timeFormat(timeNeural)
        timeManualDisplay = timeFormat(timeManual)

        return render_template('index.html', sumManual = sumManual, sumNeural = sumNeural, timeManual = timeManualDisplay, timeNeural = timeNeuralDisplay, n1 = app.vars['n1'], n2 = app.vars['n2'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)