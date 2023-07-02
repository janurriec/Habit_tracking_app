from db import get_counter_data


def calculate_count(db, counter):
    '''calculate_count- calculates the count of the counter
    db - initializes database connection
    counter - name of the counter present in db
    returns the length of the counter increment events''' 
    data = get_counter_data(db, counter)
    return len(data)

