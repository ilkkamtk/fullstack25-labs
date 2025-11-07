import os
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv
from api.v1.cats.cats_routes import cats_bp
from api.v1.users.users_routes import users_bp
from api.utils.db import mongo_connect

load_dotenv()

app = Flask(__name__)

# by default flask will serve static files from static/ folder, the url will then be: <protocol>://<host>:<port>/static/<file>, such as http://127.0.0.1:3000/static/test.html
# if you want to serve from the root, such as http://127.0.0.1:3000/test.html, set the static_url_path parameter when initialising flask
#app = Flask(__name__, static_url_path="/", template_folder="static")
# if you want to use render_template method with static files, set template_folder. NOTE: this is not the correct way!
#app = Flask(__name__, static_url_path="/", template_folder="static")

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
