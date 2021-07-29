from flask import Flask, render_template, request
import numpy as np
import joblib

model = joblib.load("models/lgb_cardio_dummy.pkl ")

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def new():
    return render_template("ui.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    datax = request.form["x"]
    data1 = float(request.form["a"])
    data2 = float(request.form["b"])
    data3 = float(request.form["c"])
    data4 = float(request.form["d"])
    data5 = float(request.form["e"])
    data6 = float(request.form["f"])
    data7 = float(request.form["g"])
    data8 = float(request.form["h"])
    data9 = float(request.form["i"])
    data10 = float(request.form["j"])
    data11 = float(request.form["k"])
    features = np.array(
        [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]
    )
    pred = model.predict([features])

    def statement():
        if pred == 0:
            return "Result:- Hi {}, the model has predicted that you do not have cardiac disease. However stay healthy and exercise daily".format(
                datax
            )
        elif pred == 1:
            return "Result:- Hey {}, the model has predicted that there is high for you to have cardiac related disease. Maintain diet, stay fit and if any discomfort consult doctor.".format(
                datax
            )

    return render_template("ui.html", statement=statement())


if __name__ == "__main__":
    app.run()
