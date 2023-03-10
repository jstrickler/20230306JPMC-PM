import sqlite3

file_path = "DATA/wombats.txt"

try:
    # x = 5 / 0
    with open(file_path) as file_in:
        for raw_line in file_in:
            print(raw_line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err)  # log error, etc
except Exception as err:
    print(str(err).upper())

nums = [0, 800, 80, 1000, 32, '123',  255, 400, 'ABC', 5, 5000]
for num in nums:
    try:
        result = 10000 / num
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    else:
        print(result)

try:
    conn = None
    conn = sqlite3('wombats.db')
    cursor = conn.cursor()
except sqlite3.Error as err:
    print(err)
else:
    cursor.execute("select 1 == 1")
finally:
    if conn:
        conn.close()



print("ALL DONE")
