from flask import Flask
from config.config import Config
from db.schema import mongo
from app.user import get, add, update, delete

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)   
    
    app.register_blueprint(get.user_bp)
    app.register_blueprint(add.user_bp)
    app.register_blueprint(update.user_bp)
    app.register_blueprint(delete.user_bp)
    
    return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)
