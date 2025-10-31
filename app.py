import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv
from api.v1.cats.cats_routes import cats_bp
from api.v1.users.users_routes import users_bp
from api.utils.db import mongo_connect

load_dotenv()

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_prefix=1)

# Register blueprints
app.register_blueprint(cats_bp)
app.register_blueprint(users_bp)

@app.get("/")
def index():
    return "Welcome to my REST API! Api endpoints can be found under /api/v1"


if __name__ == "__main__":
    mongo_connect()
    app.run(host="127.0.0.1", port=os.getenv("PORT"), debug=os.getenv("FLASK_DEBUG"), use_reloader=os.getenv("FLASK_RELOADER"))
