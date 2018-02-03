from flask import Flask,render_template, request
import numpy as np
from keras.models import load_model


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

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        app.vars['n1'] = request.form['number1']
        app.vars['n2'] = request.form['number2']

        app.vars['sumManual'] = findManualSum(app.vars['n1'], app.vars['n2'])

        app.vars['sumNeural'] = findNeuralSum(app.vars['n1'], app.vars['n2'])

        return render_template('index.html', )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)