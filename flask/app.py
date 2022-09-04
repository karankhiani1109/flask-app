from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from models.Video import db
from routes.videos_bp import videos_bp
from routes.api_bp import api_bp
import logging
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db, compare_type=True)
app.register_blueprint(videos_bp, url_prefix='/videos/') 
app.register_blueprint(api_bp, url_prefix='/api')
logging.basicConfig(level=logging.DEBUG)
@app.route('/')
def index():
    return redirect("/videos", code=302)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)