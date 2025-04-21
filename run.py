from src.app import create_app
from src.config import DevConfig, ProdConfig

app = create_app(DevConfig)

if __name__ == '__main__':
    app.run()
