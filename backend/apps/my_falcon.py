import falcon

class HelloResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nHello Falcon!!\n')

def create_app():
    app = falcon.API()
    hello = HelloResource()
    app.add_route('/', hello)
    app.add_route('/falcon', hello)
    return app
