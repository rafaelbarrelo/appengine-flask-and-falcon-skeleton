from werkzeug.wsgi import DispatcherMiddleware

from apps.my_flask import create_app as create_site
from apps.my_falcon import create_app as create_api

app = create_site()
api = create_api()

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,  # servido em /
    {
        '/api': api
    }
)
