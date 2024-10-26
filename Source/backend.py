class Backend:
    def __init__(self, player):
        self.player = player
    
    # add the backend post request routes to the flask app
    def addBackendRoutes(app):
        # add a post request for the /api/changemoney
        @app.route('/api/changemoney', methods=['POST'])
        def changeMoney():
            # placeholder
            return ""

        # return the app
        return app