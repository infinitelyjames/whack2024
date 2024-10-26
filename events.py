import random

class Event:
    def __init__(self, title : str, description : str, probability : float, callback):
        self.title = title
        self.description = description
        self.probability = probability
        self.callback = callback
    
    def trigger(self):
        self.callback()
    
    def randomTrigger(self):
        if random.random() < self.probability:
            self.trigger()
    

class EventManager:
    def __init__(self, events=[]):
        self.events = events
    
    def randomlyTriggerEvents(self):
        for event in self.events:
            event.randomTrigger()

# testing code
if __name__ == "__main__":
    def testCallback():
        print("Test callback")
    
    event = Event("Test event", "This is a test event", 0.5, testCallback)
    event.trigger()
    event.randomTrigger()
    
    eventManager = EventManager([event])