import sqlite3
from datetime import datetime, timedelta

# user variables (format:-> %Y-%m-%d)
start_date = '2024-04-01'
curr_date = '2024-04-08'

def increment_date(date:str) -> str:
    temp = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)
    return temp.strftime('%Y-%m-%d')

try:
    cnt = sqlite3.connect('test.db')
    cursor = cnt.cursor()
    
    try:
        cursor.execute('CREATE TABLE TEST(date varchar(10), points int)')
    except sqlite3.Error:
        pass

    while start_date < curr_date:
        entry = int(input(f'enter data of date {start_date}: '))
        cursor.execute('INSERT INTO TEST VALUES (?, ?)', (start_date, entry))
        start_date = increment_date(start_date)
    cursor.close()

except sqlite3.Error as err:
    print(f'error occured: {err}')

finally:
    if cnt:
        cnt.commit()
        cnt.close()