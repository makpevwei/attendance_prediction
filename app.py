from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)[:, 1]

    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text= "PROBABILITY OF BEING ABSENT IS ; {}".format(output*100))

@app.route('/results',methods=["GET","POST"])
def results():

    data = request.get_json(force=True)
    prediction = model.predict_proba([np.array(list(data.values()))])[:, 1]

    output =  round(prediction[0], 2)
    return jsonify({'prediction': str(output*100)+"%"})

if __name__ == "__main__":
    app.run()
