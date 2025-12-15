from app import create_app
from src.utils.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

# Tạo Flask app
app = create_app()

if __name__ == '__main__':
    print("="*70)
    print("STARTING SALARY PREDICTION WEB APPLICATION")
    print("="*70)
    print(f"Server running at: http://{FLASK_HOST}:{FLASK_PORT}")
    print(f"Debug mode: {FLASK_DEBUG}")
    print("="*70)
    print("\nNhấn CTRL+C để dừng server\n")
    
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG
    )