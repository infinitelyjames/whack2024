import os, Source.player as player, time, Source.parser as data
from flask import Flask, render_template, request
from Source.background import create_thread
import traceback

MONTHS_DURATION = 5 # How many seconds to spend on each month in the game
MONTH_COUNT_LIMIT=18*12 # 18 years
STARTING_YEAR = 2005

class App:
    """
    Initialise all the game state variables.
    Note, for the purpose of this, we are using placeholders.
    """
    def __init__(self):
        #Create a player instance:
        self.gamePlayer = player.Player.loadDefaultPlayer()
        data.DataManager.loadFromFile()
        self.nextMonthStartsTimestamp = time.time()
        self.monthCount = 0
    
    def getMonth(self):
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][self.monthCount % 12]

    def getYear(self):
        return STARTING_YEAR + self.monthCount // 12

    def getDate(self):
        return f"1st {self.getMonth()} {self.getYear()}"
    
    # update all images displayed on the home page
    def updateAllImages(self):
        data.DataManager.displayAllResults(self.monthCount)
        self.gamePlayer.makePieChart()
    
    def incrementMonth(self):
        if (self.monthCount >= MONTH_COUNT_LIMIT): return
        self.monthCount += 1
        self.gamePlayer.accounts[1].updateInterest(self.monthCount)
        # TODO: add interest and change stocks
        # TODO: implement logic to prevent going beyond the timeframe of the data
    
    def updatePlayerStockValues(self):
        for i in self.gamePlayer.stocks:
            i.setSharePrice(data.DataManager.getStockPrice(self.monthCount, i.name))
    
    def updateSalary(self):
        self.gamePlayer.salaryUpdate()

    def background(self):
        self.updateAllImages()
        while True: # hella nah but for now
            try:
                print(f"INFO[Background Thread]: Starting month {self.monthCount}")
                self.nextMonthStartsTimestamp = time.time() + MONTHS_DURATION
                time.sleep(MONTHS_DURATION)
                self.incrementMonth()
                self.updatePlayerStockValues()
                self.updateAllImages()
            except Exception as e:
                print(f"ERROR[Background Thread]: {e}. Iteration failed, retrying in 5 seconds")
                traceback.print_exc()
                time.sleep(5)

    def spawnBackground(self):
        create_thread(self.background, ())
    
    def addGETRoutes(self):
        # a simple page that says hello
        @self.app.route('/')
        def index():
            return render_template(
                'index.html', 
                monthCount=self.monthCount,
                current_account_cash=1000, 
                accounts=self.gamePlayer.accounts, 
                dateText=self.getDate(),
                playerShares=self.gamePlayer.stocks,
                nextMonthStartsTimestamp=self.nextMonthStartsTimestamp,
                allShares=data.DataManager.dataDict,
            )
    
    def addPOSTRoutes(self):
        @self.app.route('/api/buyshare', methods=['POST'])
        def buyShare():
            print("INFO: Buying share")
            data = request.json
            name = data['name']
            price = data['price']
            print(f"INFO: Buying {name} for {price}")
            try:
                price = float(price)
            except:
                return "Invalid price", 400
            self.gamePlayer.buyShares(name, 1, price)
            return "Success", 200
        @self.app.route('/api/sellshare', methods=['POST'])
        def sellShare():
            print("INFO: Selling share")
            data = request.json
            name = data['name']
            price = data['price']
            print(f"INFO: Selling {name} for {price}")
            try:
                price = float(price)
            except:
                return "Invalid price", 400
            self.gamePlayer.sellShares(name, 1, price)
            return "Success", 200

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