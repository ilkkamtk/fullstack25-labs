import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv
from api.v1.cats.cats_routes import cats_bp

load_dotenv()

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_prefix=1)

# Register blueprints
app.register_blueprint(cats_bp)

@app.get("/")
def index():
    return "Welcome to my REST API!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=os.getenv("PORT"), debug=os.getenv("FLASK_DEBUG"), use_reloader=os.getenv("FLASK_RELOADER"))