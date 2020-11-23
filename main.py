from flask import Flask, render_template, url_for, request
import json
from models import values

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


# display data for initialisation
@app.route('/data')
def data():
    """
    docstring
    """
    data = []
    for i in range(1,6):
        data.append(values(i,1))
    return json.dumps(data)



@app.route('/robot')
def unit():
    unit = request.args.get('unit') 
    robot = request.args.get('robot')

    data = values(unit, robot)
    return data



# running the app
if __name__ == "__main__":
    app.run(port=2900, debug=True)