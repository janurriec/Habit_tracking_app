import datetime as datetime
import sqlite3
import db
import counter
import analyze



def greeting():
    '''initial interface menu set up: 1) Add a habit 2) Add a Habit to do 3) View Habits 4) Record a Habit 5) Check Status 6) Analytics'''
    menu = "\nHello! What would you like to do?\nSelect from the menu."
    print(menu)
    selection = input("\n 1) View Habits Menu \n 2) Add a Habit to do \n 3) View Your Habits list \n 4) Record a Habit \n 5) Check Status \n 6) Analytics \n")
    if selection == str(1):
        '''directs to adding a habit in to-do list'''
        Habit.view_habit_list()
        back()
            
    elif selection == str(2):
        '''allows user to select and add habits to own list'''
        select_habit()
        back()
            
    elif selection == str(3):
        '''view habits list'''
        User.view_habits_list()
        back()
         
    elif selection == str(4):
        '''records/checks off habit in list'''
        Habit.check_habit()
        back()

    elif selection == str(5):
        '''check user level and points status'''
        print(User.check_level())
        print(User.check_points())
        
    elif selection == str(6):
        '''returns data analytics'''
        print(back())
    else:
        return "Invalid key."
    return selection

def back():
    '''calling back with input "X" will return user to the main menu'''
    exit = input("Press X to go back to Main Menu")
    if exit == "X" or "x":
        greeting()
    else:
        print("\n invalid key\n")
    print(exit)

    

def select_habit():
    """this is the input section of 2) Add a Habit to do menu"""
    ###should have the ability to Edit delete items from list too###
    ###weekly input was not added and returned properly to habit_todo_list, pls check###
    ###needs some editing for the db addition###
    User.user_todo_list = {}
    print("\n Select 4 Habits to add to your list. \n")

    def numerated_daily_habit():
        for i, item in enumerate(Habit.daily_habit_set):
            print(i, item)

    numerated_daily_habit()
    
    habit_todo_1 = input(">>Enter the number of the Habit you want to add on your list. \n")
    if int(habit_todo_1) <= len(Habit.daily_habit_set):
        selected_habit = Habit.daily_habit_set[int(habit_todo_1)]
        User.user_todo_list[1] = selected_habit
        print("\n {} has been added to your list. \n".format(selected_habit))
        counter.add_counter(db, selected_habit, None)
        db.add_counter(db, selected_habit, datetime)
    else:
        print("Invalid input.")
    

    

    def numerated_weekly_habit():
        for i, item in enumerate(Habit.weekly_habit_set):
            print(i, item)

    numerated_weekly_habit()

    habit_todo_5 = input(">>Enter the number of the Weekly Habit you want to add on your list. \n")
    if int(habit_todo_5) <= len(Habit.weekly_habit_set):
        selected_habit = Habit.weekly_habit_set[int(habit_todo_5)]
        User.user_todo_list[5] = selected_habit
        print("\n {} has been added to your list. \n".format(selected_habit))
    else:
        print("Invalid input.")
    db.add_counter(db, select_habit, None)

    print("\nThese are the habits you need to do:\n")
    print(User.user_todo_list)
        

class Habit:
    '''Creating a Habit class to store info and methods for habits created
    Daily_habit_set and weekly habit set - groups the habits by frequency
    '''
    daily_habit_set = []
    weekly_habit_set = []
    
    def __init__(self, name, frequency, points):
        '''stores more information about the Habit
        name- name of the Habit
        frequency- defines how frequent user should do the habit
        points - points accumulated by the user for accomplishing a habit. this ties to the gamification of the system.'''
        self.name = name
        self.frequency = frequency
        self.points = points
        if frequency == "daily": 
            Habit.daily_habit_set.append(self.name)
        elif frequency == "weekly":
            Habit.weekly_habit_set.append(self.name)

    def view_habit_list():
        '''view pre-made Habits list'''
        print("These are the Habits you can improve upon:")
        print("DAILY TASK:\n")
        for i, habit in enumerate(Habit.daily_habit_set, 1):
            print(f"{i} {habit}")
        print("WEEKLY TASK:\n")

        for i, habit in enumerate(Habit.weekly_habit_set, 1):
            print(f"{i} {habit}")
        back()

    
    def __str__(self):
        """returns information about the Habit being called"""
        return "{name} : {frequency}. \nAccomplishing this will earn you {points} points. \n".format(name = self.name, frequency = self.frequency, points = self.points)
    
    def chosen_habit(self):
        """confirmation that habit has been added to list"""
        print("You have added {} in your Habit list.".format(self.name))

    def check_habit():
        '''confirm if habit is done
        User.view_habits_list: returns a view of selected habits by the user
        '''
        print("Which of these habits have you done today?\n")
        User.view_habits_list()

        for item in User.view_habits_list:
            print("have you done {}?".format(item))
            answer = input()
            now = datetime.datetime.now
            if answer == "Y" or "y":
                counter.increment_counter()
                db.increment_counter(db, item, now)
                User.points += Habit.points
                print("You have earned points from doing this habit.\n")
            else:
                print("You need to work on your habits.")


        '''for item in enumerate(User.user_todo_list):
            print("have you done {}".format(item))
            answer = input()
            if answer == "Y":
                counter.increment_counter()
                User.points += Habit.points
                print("You have earned {} points from doing this habit. \n".format(Habit.points))
            else:
                print("You need to work on your habits.")

        for item in User.user_todo_list[4]:
            print("have you done {}".format(item))
            answer = input()
            if answer == "Y":
                counter.increment_counter()
                User.points += Habit.points
                print("You have earned {} points from doing this habit. \n".format(Habit.points))
            else:
                print("You need to work on your habits.")
        '''
        


class User:
    user_todo_list= {}
    '''creating a user class for name, user level and points accumulated'''
    def __init__(self, name, level, points):
        self.name = name
        self.level = level
        self.points = points

    def __str__(self):
        '''prints out user info including points and level'''
        return "You currently have {} points and at level {}. Keep going!".format(self.points, self.level)
    
    def view_habits_list():
        print(User.user_todo_list)

    def check_level(User):
        '''returns the current level of the user'''
        return "Your current level is at {}".format(User.level)

    def check_points(User):
        '''returns the current points accumulated by the user'''
        return "You currently have {} points.\nMaintain your habits and record them everyday to get more points.".format(User.points)

    

drink_water = Habit("Drink water", "daily", 5)
read_book = Habit("Read 5 pages", "daily", 5)
workout = Habit("Do a physical activity", "daily", 5)
do_chores = Habit("Do household chores", "daily", 5)
eat_on_time = Habit("Eat meal on time", "daily", 5)
take_meds = Habit("Take medication on time", "daily", 5)
write_journal = Habit("Write daily journal", "daily", 5)
learn_1hr = Habit("Study for one hour", "daily", 5)

go_to_therapy = Habit("Go to therapy", "weekly", 10)
do_fun_stuff = Habit("Do something for myself", "weekly", 10)
go_long_walk = Habit("Go for a long walk", "weekly", 10)
learn_new_skill = Habit("Learn a new skill", "weekly", 10)

kim = User("Kim", 1, 0)

greeting()
