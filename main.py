import datetime as datetime
import sqlite3
import database
import counter
import analyze



def greeting():
    '''initial interface menu set up: 1) View Habit list and Add a Habit to do 2) View Habits 3) Record a Habit 4) Check Status 5) Analytics'''
    menu = "\nHello! What would you like to do?\nSelect from the menu."
    print(menu)
    selection = input("\n 1) View and Add a Habit on Your List \n 2) Record a Habit \n 3) Check Status \n 4) Analytics \n")
    if selection == str(1):
        '''directs to adding a habit in to-do list
        Habit.view_habit_list()'''
        '''allows user to select and add habits to own list'''
        select_habit()
         
    elif selection == str(2):
        '''records/checks off habit in list'''
        Habit.check_habit()
        back()

    elif selection == str(3):
        '''check user level and points status'''
        print(User.check_level())
        print(User.check_points())
        
    elif selection == str(4):
        '''returns data analytics'''
        print(Habit.analytics())
        print(back())
    else:
        return "Invalid key."
    return selection

def back():
    '''calling back with input "X" will return user to the main menu'''
    exit = input("Press X to go back to Main Menu \n")
    if exit == "X" or "x":
        greeting()
    else:
        print("\n invalid key\n")
    print(exit)


user_todo_list= {}

class User:
    '''creating a user class for name, user level and points accumulated'''
    def __init__(self, name, level, points):
        self.name = name
        self.level = level
        self.points = points

    def __str__(self):
        '''prints out user info including points and level'''
        return "Hello {}! You currently have {} points and at level {}. Keep going!".format(self.name, self.points, self.level)

        
    def check_level(User):
        '''returns the current level of the user'''
        return "Your current level is at {}".format(User.level)

    def check_points(User):
        '''returns the current points accumulated by the user'''
        return "You currently have {} points.\nMaintain your habits and record them everyday to get more points.".format(User.points)


def select_habit():
    """this is the input section of 2) Add a Habit to do menu"""
    ###should have the ability to Edit delete items from list too###
    ###weekly input was not added and returned properly to habit_todo_list, pls check###
    ###needs some editing for the db addition###
    print("\n Select 4 Habits to add to your list. \n")

    def numerated_daily_habit():
        for i, item in enumerate(Habit.daily_habit_set):
            print(i, item)

    numerated_daily_habit()
    
    habit_todo_1 = input(">>Enter the number of the Habit you want to add on your list. \n")
    if int(habit_todo_1) <= len(Habit.daily_habit_set):
        selected_habit1 = Habit.daily_habit_set[int(habit_todo_1)]
        user_todo_list[1] = selected_habit1
        database.create_tables(database)
        start_date = str(datetime.date)
        database.add_counter(database.get_data_connection(), selected_habit1, start_date)
        print("\n {} has been added to your list. \n".format(selected_habit1))
    else:
        print("Invalid input.")
    
    habit_todo_2 = input(">>Enter the number of the Habit you want to add on your list. \n")
    if int(habit_todo_2) <= len(Habit.daily_habit_set):
        selected_habit2 = Habit.daily_habit_set[int(habit_todo_2)]
        user_todo_list[2] = selected_habit2
        start_date = str(datetime.date)
        database.create_tables(database)
        database.add_counter(database.get_data_connection(), selected_habit2, start_date)
        print("\n {} has been added to your list. \n".format(selected_habit2))
    else:
        print("Invalid input.")

    habit_todo_3 = input(">>Enter the number of the Habit you want to add on your list. \n")
    if int(habit_todo_3) <= len(Habit.daily_habit_set):
        selected_habit3 = Habit.daily_habit_set[int(habit_todo_3)]
        user_todo_list[3] = selected_habit3
        start_date = str(datetime.date)
        database.create_tables(database)
        database.add_counter(database.get_data_connection(), selected_habit3, start_date)
        print("\n {} has been added to your list. \n".format(selected_habit3))
    else:
        print("Invalid input.")

    habit_todo_4 = input(">>Enter the number of the Habit you want to add on your list. \n")
    if int(habit_todo_4) <= len(Habit.daily_habit_set):
        selected_habit4 = Habit.daily_habit_set[int(habit_todo_4)]
        user_todo_list[4] = selected_habit4
        database.create_tables(database)
        start_date = str(datetime.date)
        database.add_counter(database.get_data_connection(), selected_habit4, start_date)
        print("\n {} has been added to your list. \n".format(selected_habit4))
    else:
        print("Invalid input.")
    
    

    def numerated_weekly_habit():
        for i, item in enumerate(Habit.weekly_habit_set):
            print(i, item)

    numerated_weekly_habit()

    habit_todo_5 = input(">>Enter the number of the Weekly Habit you want to add on your list. \n")
    if int(habit_todo_5) <= len(Habit.weekly_habit_set):
        selected_habit5 = Habit.weekly_habit_set[int(habit_todo_5)]
        user_todo_list[5] = selected_habit5
        start_date = str(datetime.date)
        database.create_tables(database)
        database.add_counter(database.get_data_connection(), selected_habit5, start_date)
        print("\n {} has been added to your list. \n".format(selected_habit5))
    elif int(habit_todo_5) >= len(Habit.weekly_habit_set):
        print("Number out of range")
        selected_habit5 = 0
        selected_habit5 = Habit.weekly_habit_set[int(habit_todo_5)]
        user_todo_list[5] = selected_habit5
    else:
        print("Invalid input.")

    print("This is your selected habit list:")
    print(user_todo_list)
    back()
    

   
 
    

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
        

    
    def __str__(self):
        """returns information about the Habit being called"""
        return "{name} : {frequency}. \nAccomplishing this will earn you {points} points. \n".format(name = self.name, frequency = self.frequency, points = self.points)
    
    def check_habit():
        '''confirm if habit is done
        User.view_habits_list: returns a view of selected habits by the user
        '''
        print("Which of these habits have you done today?\n")
        database.get_data_connection()
        print(database.output_table())
        
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
    def analytics():
        print(database.output_table())
        



    

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

print(kim)
greeting()
