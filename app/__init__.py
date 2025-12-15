from flask import Flask
from flask_cors import CORS
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from src.utils.config import FLASK_SECRET_KEY

# tạo Flask application
def create_app():

    # Tạo Flask app
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    app.config['JSON_AS_ASCII'] = False  # Để hiển thị tiếng Việt
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    print("✓ Flask app created successfully")
    
    return app