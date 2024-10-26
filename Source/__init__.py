import os, Source.player as player, time
from flask import Flask, render_template
from Source.background import create_thread

class App:
    def background(self):
        while True:
            print("Background thread is running")
            time.sleep(10)

    def spawnBackground(self):
        create_thread(self.background, ())


    def run(self, test_config=None):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True, static_folder='../static', template_folder='../templates')
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        #Create a player instance:
        gamePlayer = player.Player("John", 10000)

        # Spawn the background thread
        self.spawnBackground()

        # a simple page that says hello
        @app.route('/')
        def index():
            return render_template('index.html', current_account_cash=1000)

        app.run()

    @staticmethod
    def start():
        App().run()