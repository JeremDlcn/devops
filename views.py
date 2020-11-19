from flask import Flask, render_template, url_for, request
import json
from models import Data,values

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # developpement refresh

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='None',
)


# Routes
@app.route('/')
def dashboard():
    """
    docstring
    """
    return render_template("index.html")

@app.route('/data')
def data():
    """
    docstring
    """
    value = values();
    # print(value)
    # data = {
    #     "bar": {
    #         "tempTank": value.tempTank,
    #         "tempExt": 10,
    #         "ph": 7,
    #         "k": 40
    #     },
    #     "lines": {
    #         "nacl": [1.5, 1.9, 1.8, 2.0],
    #         "bacteria": {
    #             "salmonelle": [17.5, 22.5, 22.8, 19.0, 43.0, 22.8, 14.0],
    #             "ecoli": [21.2, 30.0, 18.8, 38.8, 23.9, 20.0, 16.0],
    #             "listeria": [16.0, 21.0, 19.5, 17.8, 20.2, 44.0, 20.2]
    #         }
    #     },
    #     "weight": {
    #         "tank": 2500,
    #         "product": 200
    #     }

    # }
    data = {
        "bar": {
            "tempTank": 3,
            "tempExt": 10,
            "ph": 7,
            "k": 40
        },
        "lines": {
            "nacl": [1.5, 1.9, 1.8, 2.0],
            "bacteria": {
                "salmonelle": [17.5, 22.5, 22.8, 19.0, 43.0, 22.8, 14.0],
                "ecoli": [21.2, 30.0, 18.8, 38.8, 23.9, 20.0, 16.0],
                "listeria": [16.0, 21.0, 19.5, 17.8, 20.2, 44.0, 20.2]
            }
        },
        "weight": {
            "tank": 2500,
            "product": 200
        }

    }
    return json.dumps(data)

# running the app
if __name__ == "__main__":
    app.run(port=2900, debug=True)