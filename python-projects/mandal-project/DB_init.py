import sqlite3
import time

############### Settings ####################
#DB Name
DB_NAME = "mandal_sensor.db"

#SQL File with Table Schema and Initialization Data
SQL_File_Name = "voltage_current.sql"
##############################################
#Connect or Create DB File
conn = sqlite3.connect(DB_NAME)

#Read Table Schema into a Variable and remove all New Line Chars
TableSchema=""
with open(SQL_File_Name, 'r') as SchemaFile:
    for query in SchemaFile:
        if query:
            time.sleep(2) # need to update the timing as well
            print("Executing script {}".format(query))
            conn.execute(query)

print("All done")
conn.commit()

# Check the table
cursor = conn.execute("SELECT * from voltage_current")
for row in cursor:
    print("id = ", row[0])
    print("voltage = ", row[1])
    print("current = ", row[2])
    print("date = ", row[3])
    print("*" * 10)
    print()

conn.close()
