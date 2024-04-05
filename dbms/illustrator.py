import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from math import ceil

def get_month_days():
    month = datetime.now().month
    year = datetime.now().year
    
    # if month is Jan, Mar, May, Jul, Aug, Oct, Dec then no. of days is 31
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return [i+1 for i in range(31)]
    # if month is Apr, Jun, Sep, Nov then no. of days is 30
    if month in [4, 6, 9, 11]:
        return [i+1 for i in range(30)]
    else:
        # checking for leap year to get the no. of days in Feb
        if (year % 400 == 0) and (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
            return [i+1 for i in range(29)]
        else:
            return [i+1 for i in range(28)]
        
def unwrap(item):
    dates = []
    val = []
    for row in item:
        dates.append(row[0])
        val.append(row[1])
    return dates, val

def extrapolate(point=0, m=155):
    date:str = str(datetime.now().date())
    est_days1 = ceil((7840 - point)/m)
    est_days2 = ceil((15680 - point)/m)
    est_point1 = est_days1*m + point
    est_point2 = est_days2*m + point
    est_date1 = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=est_days1)
    est_date2 = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=est_days2)
    est_date_itr = [date, est_date1.strftime('%Y-%m-%d'), est_date2.strftime('%Y-%m-%d')]
    return est_date_itr, [est_point1, est_point2], [est_days1, est_days2]

def main():
    try:
        # connecting to the database
        cnt = sqlite3.connect('test.db')
        cursor = cnt.cursor()

        plt.figure(figsize=[9, 5])
        plt.tight_layout()
        month_days = get_month_days()

        # plotting line graph of total points collected in the given month
        plt.subplot(2, 1, 1)
        data1 = cursor.execute(f"SELECT * FROM TEST WHERE date LIKE '%-{datetime.now().month:02}-%'").fetchall()
        dates, val1 = unwrap(data1)
        dates1 = [int(i[8:10]) for i in dates]
        plt.plot(dates1, val1, marker='o')
        plt.xticks(month_days)
        plt.xlim(left=month_days[0]-1, right=month_days[-1]+1)
        plt.ylim(bottom=0)
        plt.grid()
        plt.title(f'points acumulated for month of {datetime.now().strftime('%B')}', fontweight='bold', fontsize=10)
        plt.xlabel('dates->')
        plt.ylabel('points->', rotation='vertical')

        # plotting bar graph of points increased in last 7 days
        plt.subplot(2, 2, 3)
        data2 = cursor.execute('SELECT * FROM (SELECT * FROM TEST ORDER BY date DESC LIMIT 8) ORDER BY date').fetchall()
        dates2, val = unwrap(data2)
        dates2 = dates2[1:]
        val2 = [val[i+1] - val[i] for i in range(len(dates2))]
        plt.bar(dates2, val2, color='lightgreen', edgecolor='green')
        for i in range(len(val2)):
            plt.text(i, val2[i], f'{val2[i]}', ha='center', fontsize=8, color='black',
                     bbox={'boxstyle':'round', 'fc':'lightgreen', 'ec':'green', 'alpha':0.4})
        plt.xticks(rotation=30, ha='right')
        plt.grid(axis='y')
        plt.title('points acumulated in last 7 days', fontweight='bold', fontsize=10)

        # plotting line graph of extrapolation of potential dates to achieve the targets
        plt.subplot(2, 2, 4)
        point = cursor.execute('SELECT points FROM TEST ORDER BY date DESC LIMIT 1').fetchall()[0][0]
        dates3, val3, days = extrapolate(point=point)
        if point < 7840:
            point_itr = [point, val3[0], val3[1]]
            dates_itr = dates3
            plt.plot(dates_itr, point_itr, 'o--m')
            plt.xlabel(f'desired goal of 7840 reached in {days[0]} days\ndesired goal of 15680 reached in {days[1]} days')
        elif 7840 < point < 15680:
            point_itr = [val3[0], point, val3[1]]
            dates_itr = [dates3[1], dates3[0], dates3[2]]
            plt.plot(dates_itr, point_itr, 'o--m')
            plt.xlabel(f'desired goal of 15600 reached in {days[1]} days')
        else:
            point_itr = [val3[0], val3[1], point]
            dates_itr = [dates3[1], dates3[2], dates3[0]]
            plt.plot(dates_itr, point_itr, 'o--m')
            plt.xlabel('you reached your goal')
        plt.grid()
        plt.title('extrapolation', fontweight='bold', fontsize=10)

        plt.subplots_adjust(hspace=0.5, bottom=0.156)
        plt.show()
        cursor.close()

    except sqlite3.Error as err:
        print(f'error occured: {err}')

    finally:
        if cnt:
            cnt.close()

if __name__ == '__main__':
    main()