from flask import Flask, render_template, request
import pickle
from xgboost import XGBRegressor
import numpy as np

app = Flask(__name__)
region_pkl = pickle.load(open('label_encoder.pkl', 'rb'))
cus_mat_pkl = pickle.load(open('cus-mat.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        region = str(request.form['region'])
        re=region_pkl.transform([region])
        day =int(request.form['day'])
        month = int(request.form['month'])
        cus = str(request.form['cus'])
        # mat = request.form['mat']
        cus_mat= cus
        cu=cus_mat_pkl.transform([cus_mat])
        data = np.array([[re[0], day, month, cu[0]]])
        model = pickle.load(open('xgboost_model.pkl', 'rb'))
        prediction = model.predict(data)[0]
        return render_template('index1.html', prediction=prediction)
	

if __name__ == '__main__':
    app.run()
