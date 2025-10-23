from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_prefix=1)

@app.get("/")
def index():
    return "Welcome to my REST API!"

@app.get("/api/v1/cat")
def get_cat():
    cat = [{
        "cat_id": "sadg",
        "name": "Mittens",
        "birthdate": "2001-03-11",
        "weight": 8,
        "owner": "sdfgfg",
        "image": "https://place-hold.it/320x240&text=Cat"
    }]
    return cat


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)