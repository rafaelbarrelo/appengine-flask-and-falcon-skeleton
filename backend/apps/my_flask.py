from flask import Flask, abort, Blueprint

bp = Blueprint('my_flask_bp', 'my_flask')

def create_app():
    app = Flask("my_flask")
    app.config['DEBUG'] = True
    app.register_blueprint(bp)
    return app

@bp.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

@bp.route('/')
def index():
    return 'Use: <br />/flask <br />/api/falcon'

@bp.route('/flask')
def flask():
    return 'Hello Flask! =)'


