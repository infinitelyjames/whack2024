import os, Source.player as player, time
from flask import Flask, render_template
from Source.background import create_thread

MONTHS_DURATION = 30 # How many seconds to spend on each month in the game

class App:
    """
    Initialise all the game state variables.
    Note, for the purpose of this, we are using placeholders.
    """
    def __init__(self):
        #Create a player instance:
        gamePlayer = player.Player("John", 10000)
    
    # update all images displayed on the home page
    def updateAllImages(self):
        pass

    def background(self):
        while True:
            self.updateAllImages()
            print("Background thread is running")
            time.sleep(10)

    def spawnBackground(self):
        create_thread(self.background, ())
    
    def addGETRoutes(self):
        # a simple page that says hello
        @self.app.route('/')
        def index():
            return render_template('index.html', current_account_cash=1000)
    
    def addPOSTRoutes(self):
        @self.app.route('/api/buyshare', methods=['POST'])
        def buyShare():
            # return not implemented with status code 501
            return "Not implemented", 501
        @self.app.route('/api/sellshare', methods=['POST'])
        def sellShare():
            # return not implemented with status code 501
            return "Not implemented", 501

    def addRoutes(self):
        if (self.app == None): raise Exception("App not initialised")
        self.addGETRoutes()
        self.addPOSTRoutes()
        

    def run(self, test_config=None):
        # create and configure the app
        self.app = Flask(__name__, instance_relative_config=True, static_folder='../static', template_folder='../templates')
        self.app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(self.app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            self.app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            self.app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass        

        # Add the routes
        self.addRoutes()

        # Spawn the background thread
        self.spawnBackground()

        

        self.app.run()

    @staticmethod
    def start():
        App().run()