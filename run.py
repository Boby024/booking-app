from src.app import create_app
from src.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(threaded=Config.FLASK_THREADED, host=Config.FLASK_HOST, port=Config.FLASK_PORT)
