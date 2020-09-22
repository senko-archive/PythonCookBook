import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/save", methods=["POST"])
def save_to_db():
    req_data = request.get_json()
    #return req_data["data"]
    return "OK"


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
