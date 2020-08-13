# TitanicAI

This is a generic simple AI web application of using model random forest classifier. Using data of kaggle tutrial Titanic dataset, you can predict survive or death in titanic situation according to your input of form data.
The model is trained by random forest classifier in scikit-learn and saved as "model_titanic.pickle"

# Usage
This website is developed and tested on Windows10 with Python 3.7.8 You need Python, flask, scikit-learn and their dependencies to run the website. You also need Jupyter Notebook to retrain the model.
library version
- Flask              1.1.2
- Flask-Cors         3.0.8
- numpy              1.19.1
- pandas             1.1.0

1.Copy the repository
```
git clone https://github.com/Okra666/titanicAI.git
```
2.Run website by flask
```
python web.py
```
3.You can access the website on port 5000. ie: http:/<server adress>/:5000/
4.To retrain the model, edit "train_titanic.ipynb" and save the model as "model_titanic.pickle".
