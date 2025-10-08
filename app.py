from flask import Flask

app = Flask(__name__)

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
    return catx


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)