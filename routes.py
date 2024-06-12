from views import homepage
from auth import register, login, logout




def configure_routes(app):
    app.add_url_rule('/', 'homepage', homepage)
    app.add_url_rule('/logout', 'logout', login, methods=["POST", "GET"])
    app.add_url_rule('/login', 'login', login, methods=["POST", "GET"])
    app.add_url_rule('/register', 'register', register, methods=["POST", "GET"])

