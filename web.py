import numpy as np
import pandas as pd
import pickle


def predictTitanic(params):

	with open('model_titanic.pickle', mode='rb') as fp:
		forest = pickle.load(fp)
	
	params = params.reshape(1,-1)
	pred = forest.predict(params)
	return pred

def getSurvive(titanic_id):
    if titanic_id == 0: return "Death" 
    elif titanic_id == 1: return "Survive" 
    else: return "Error"

from flask import Flask, render_template, request, flash, send_from_directory, jsonify
import os

# App config.
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods = ['GET', 'POST'])
def titanicPred():

    if request.method == 'POST':

        ticket = [request.form['ticket']]
        gender = request.form['gender']
        age = request.form['age']
        sibsp = request.form['sibsp']
        parch = request.form['parch']
        fare = request.form['fare']
        embarked = request.form['embarked']
        title = request.form['title']
        familysize = int(request.form['sibsp']) + int(request.form['parch']) + 1
        if familysize == 1:
            isalone = 1
        else:
            isalone = 0
        df = pd.DataFrame({ 'Pclass' : ticket,
                        'Sex' : gender,
                        'Age' : age,
                        'SibSp' : sibsp,
                        'Parch' : parch,
                        'Fare' : fare,
                        'Embarked' : embarked,
                        'Title' : title,
                        'FamilySize' : familysize,
                        'IsAlone' : isalone
                         })
        train_data = df.values

        pred = predictTitanic(train_data)
        result = getSurvive(pred)

        return jsonify({'result': result})

    else:
        return render_template('titanicPred.html')


if __name__ == "__main__":
    app.debug = True
    #app.run(host='0.0.0.0')
    app.run()
    
    
