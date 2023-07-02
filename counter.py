from db import add_counter, increment_counter
import datetime as datetime


class Counter:

    def __init__(self, name: str, description: str, value: int):
        ''' Counter class counts the habit events entered
        name - name of the counter
        description - description of the counter'''
        self.name = name
        self.description = description
        self.count = 0

    def __str__(self):
        '''__str__ returns a description of the habit name being counted and the description
        self.name - name of the habit counter called
        self.description - description of the counter called'''
        return f"{self.name}, {self.description} "
    
    def reset(self):
        '''reset allows for resetting the counter to zero in case user wants to restart the count '''
        self.count = 0

    def increment(self):
        '''increment adds 1 new event to the habit being counted'''
        self.count += 1
        return self.count
    
    def increment_points(self, user):
        '''
        ##adding points to User.points when habit_event is recorded
        '''
        pass
    
    def store(self, db):
        '''store establishes the connection to the sqlite database
        db- calls the database to store data into
        '''
        add_counter(db, self.name, self.description)
        
    def add_habit_event(self, db, instance_date: str = None):
        '''add_habit_event allows to add and record the habit event into the data
        name - name of the counter
        description- description of the counter
        instance_date - records the date and time when the event was added'''
        increment_counter(db, self.name, self.description, instance_date= datetime.datetime.now)

    
