import mysql.connector
import os
import shutil
import time

# Opening CSV files
list_csv_files = os.listdir('CSV_Files')

for filecsv in list_csv_files:
    data_file = open('CSV_Files/%s' % filecsv, 'r')
    print(data_file.read())

    conn = mysql.connector.connect(host="mysql-leonelal.alwaysdata.net",
                                   user="leonelal_devops", password="devopspassword",
                                   database="leonelal_devops")
    cursor = conn.cursor()

    cursor.execute("""
      LOAD DATA LOCAL INFILE 'CSV_Files/""" + filecsv + """'
      INTO TABLE resultats
      CHARACTER SET latin1
      FIELDS TERMINATED BY ',' 
      ENCLOSED BY '"'
      LINES TERMINATED BY '\r\n'
      IGNORE 1 ROWS;
   """)
    conn.commit()

    conn.close()
    data_file.close()

for filecsv in list_csv_files:
    shutil.move('CSV_Files/%s' % filecsv, 'Used_CSV/%s' % filecsv)
