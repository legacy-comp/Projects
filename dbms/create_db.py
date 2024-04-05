import sqlite3

try:
    with open('data.txt', 'r') as fp:
        data = fp.readlines()
    try:
        cnt = sqlite3.connect('test.db')
        cursor = cnt.cursor()
        cursor.execute('DROP TABLE IF EXISTS TEST')
        cursor.execute('CREATE TABLE TEST(date varchar(10), points int)')
        for i in range(len(data)):
            data[i] = data[i].split(' ')
            data[i][1] = int(data[i][1].strip('\n'))
            cursor.execute("INSERT INTO TEST VALUES (?, ?)", (data[i][0], data[i][1]))
        cursor.close()

    except sqlite3.Error as err:
        print(f'error occured: {err}')

    finally:
        if cnt:
            cnt.commit()
            cnt.close()
    
except FileNotFoundError:
    print('Error: data file is not found')
