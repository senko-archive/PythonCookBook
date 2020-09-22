import requests
import random
import flask
from flask import jsonify, request

api_url_base = "https://baconipsum.com/api/"
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api")
def get_bacon_ipsum():
    response = get_random_bacon_ipsum()
    return str(response.json())


def get_random_bacon_ipsum(format="json"):
    paras = random.randint(3,10)
    request_url = api_url_base+f"?type=meat-and-filler&paras={paras}&format={format}"
    response = requests.get(request_url)
    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5001)
