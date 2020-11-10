from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # developpement refresh

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='None',
)


# Routes

@app.route('/')
def funcname():
    """
    docstring
    """
    return render_template("index.html")