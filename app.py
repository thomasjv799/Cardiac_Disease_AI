from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import numpy as np
import pickle

model = pickle.load(open("models/cardio.pkl", "rb"))

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"
mongo = PyMongo(app)
user_collection = mongo.db.users


@app.route("/", methods=["POST", "GET"])
def new():
    return render_template("ui.html")


'''
@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
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
        if datax != "" and data1 != "" and data2 != "" and data3!="" and data4!="" and data5!="" and data6!="" and data7!=""and data8!=""and data9!=""and data10!=""and data11!="":
            users = user_collection.insert_one({"name": datax, "age":data1, "gender": data2, "height": data3, "weight": data4, "syst_pressure":data5, "diast_pressure":data6, "cholestrol":data7, "glucose":data8, "smoker":data9, "alcoholic": data10, "active":data11})
            return ("data added to the database")
    else:
        return ("Kindly fill the form")

'''


@app.route("/read")
def read_data():
    users = (user_collection.find())
    return render_template('index.html', users=users)


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

    if datax != "" and data1 != "" and data2 != "" and data3!="" and data4!="" and data5!="" and data6!="" and data7!=""and data8!=""and data9!=""and data10!=""and data11!="" :
        users = user_collection.insert_one({"name": datax, "age":data1, "gender": data2, "height": data3, "weight": data4, "syst_pressure":data5, "diast_pressure":data6, "cholestrol":data7, "glucose":data8, "smoker":data9, "alcoholic": data10, "active":data11})
        #return ("data added to the database")

    return render_template("ui.html", statement=statement())


if __name__ == "__main__":
    app.run()












