from app import create_app
from app.config import ProductionConfig


app = create_app()
if __name__ == '__main__':
    app.run()
