from flask import Flask, json, jsonify, request, make_response
from tensorflow import keras

app = Flask(__name__)
app.debug = True
security_model = keras.models.load_model("assets/securitymodel.h5")
walk_model = keras.models.load_model("assets/walkmodel.h5")
bus_model = keras.models.load_model("assets/busmodel.h5")

HEADERS = {
    "Access-Control-Allow-Origin": "*",
}

@app.route("/security", methods=["GET", "POST", "OPTIONS"])
def get_security_time():
    if request.method != "POST":
        return ("", 204, HEADERS)
    req_data = request.json
    print(req_data)
    print(req_data['dest_lat'])
    params = [[req_data['dest_lat'], req_data['dest_long'], 
        req_data['day_week'], req_data['day_month'], req_data['month']]]
    print(params)
    prediction = security_model.predict(params)[0][0]
    response = make_response(
                jsonify(
                    {"time": str(prediction)}
                ),
                200,
                HEADERS
            )
    return response

@app.route("/walk", methods=["GET", "POST", "OPTIONS"])
def get_walk_time():
    if request.method != "POST":
        return ("", 204, HEADERS)
    req_data = request.json
    print(req_data)
    print(req_data['dest_lat'])
    params = [[req_data['dest_lat'], req_data['dest_long'], 
        req_data['day_week'], req_data['day_month'], req_data['month'],
        req_data['distance']]]
    print(params)
    prediction = walk_model.predict(params)[0][0]
    response = make_response(
                jsonify(
                    {"time": str(prediction)}
                ),
                200,
                HEADERS
            )
    return response

@app.route("/bus", methods=["GET", "POST", "OPTIONS"])
def get_bus_time():
    if request.method != "POST":
        return ("", 204, HEADERS)
    req_data = request.json
    print(req_data)
    print(req_data['dest_lat'])
    params = [[req_data['dest_lat'], req_data['dest_long'], 
        req_data['day_week'], req_data['day_month'], req_data['month'],
        req_data['distance']]]
    print(params)
    prediction = bus_model.predict(params)[0][0]
    response = make_response(
                jsonify(
                    {"time": str(prediction)}
                ),
                200,
                HEADERS
            )
    return response