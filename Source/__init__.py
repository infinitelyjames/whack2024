import os, Source.player as player, time, Source.parser as data, Source.events as events, Source.goals as goals
from flask import Flask, render_template, request
from Source.background import create_thread
import traceback

MONTHS_DURATION = 10 # How many seconds to spend on each month in the game
MONTH_COUNT_LIMIT=18*12 # 18 years
STARTING_YEAR = 2005
SALARY = 10000 # Yearly salary

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
        self.eventArr = [events.Event("Rent Increase", "Your rent increased!", 0.05, lambda: self.gamePlayer.rentIncrease()),
                    events.Event("Rent Decrease", "Your rent decreased!", 0.03, lambda: self.gamePlayer.rentDecrease()),
                    events.Event("Bill Increase", "Your bills increased!", 0.08, lambda: self.gamePlayer.billIncrease()),
                    events.Event("Bill Decrease", "Your bills decreased!", 0.04, lambda: self.gamePlayer.billDecrease()),
                    events.Event("Accident", "You had an accident!", 0.06, lambda: self.gamePlayer.accident()),
                    events.Event("Lottery Winner", "You won the lottery!", 0.005, lambda: self.gamePlayer.lotteryWinner())]
        self.petGoal = goals.Goal("Pet", "Buying a cute companion", 1000)
        self.carGoal = goals.Goal("Car", "Buy yourself an automobile", 5000)
        self.houseGoal = goals.Goal("House", "Get a deposit on your house", 50000)
        self.eManager = events.EventManager(self.eventArr)
    
    def getMonth(self):
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][self.monthCount % 12]

    def getYear(self):
        return STARTING_YEAR + self.monthCount // 12
    
    def getDateInYYYYMMDD(self):
        return f"{self.getYear()}{str((self.monthCount % 12)+1).zfill(2)}01"
    
    def getBBCNewsWayBackURL(self):
        return f"https://web.archive.org/web/{self.getDateInYYYYMMDD()}000000*/bbc.co.uk/news"

    def getDate(self):
        return f"1st {self.getMonth()} {self.getYear()}"
    
    # update all images displayed on the home page
    def updateAllImages(self):
        data.DataManager.displayAllResults(self.monthCount)
        self.gamePlayer.makePieChart()
    
    def incrementMonth(self):
        if (self.monthCount >= MONTH_COUNT_LIMIT): return False
        self.monthCount += 1
        self.gamePlayer.accounts[1].updateInterest(self.monthCount)
        return True
    
    def updatePlayerStockValues(self):
        for i in self.gamePlayer.stocks:
            i.setSharePrice(data.DataManager.getStockPrice(self.monthCount, i.name))
    
    def updateSalary(self):
        self.gamePlayer.salaryUpdate(SALARY, self.getYear())

    def background(self):
        self.updateAllImages()
        while True: # hella nah but for now
            try:
                print(f"INFO[Background Thread]: Starting month {self.monthCount}")
                self.nextMonthStartsTimestamp = time.time() + MONTHS_DURATION
                time.sleep(MONTHS_DURATION)
                if not self.incrementMonth(): break
                self.updatePlayerStockValues()
                self.updateSalary()
                self.updateAllImages()
                self.eManager.randomlyTriggerEvents()
            except Exception as e:
                print(f"ERROR[Background Thread]: {e}. Iteration failed, retrying in 5 seconds")
                traceback.print_exc()
                time.sleep(5)
        print("INFO[Background Thread]: Game over")

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
                netWorth=round(self.gamePlayer.calculateTotalMoney(),2),
                yearlySalary=SALARY,
                newsURL=self.getBBCNewsWayBackURL(),
                expensesPercentage=round(self.gamePlayer.expenses*100,2),
                eventHistoryItems=self.gamePlayer.eventHistory,
                totalStockChangeAbs=abs(round(self.gamePlayer.calculateStockGain(),2)),
                totalStockGainPercentage=round(self.gamePlayer.calculateStockGainPercentage(),2),
                stockGainOrLossText="gained" if self.gamePlayer.calculateStockGain() > 0 else "depreciated"
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
        # Transfer negative to current to move money from current to savings
        @self.app.route('/api/transfermoneytocurrent', methods=['POST'])
        def transferMoneyToCurrent():
            print("INFO: Transfer money to current")
            data = request.json
            amount = data['amount']
            print(f"INFO: Transferring {amount} to current")
            try:
                amount = float(amount)
            except:
                return "Invalid amount", 400
            self.gamePlayer.transferMoney(amount, "Savings Account", "Current Account")
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