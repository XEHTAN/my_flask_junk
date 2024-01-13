from application import app
from role_router import create_role


if __name__ == '__main__':
    app.run(debug=True, port=8000)