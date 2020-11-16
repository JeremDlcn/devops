import mysql.connector
 
f = open("CSV_Files/fichier2.csv", "r")
print(f.read())

conn = mysql.connector.connect(host="mysql-leonelal.alwaysdata.net",
                               user="leonelal_devops", password="devopspassword", 
                               database="leonelal_devops")
cursor = conn.cursor()
 
cursor.execute("""  
   LOAD DATA LOCAL INFILE 'CSV_Files/paramunite_4_8_1605021651.csv' 
   INTO TABLE resultats
   CHARACTER SET latin1
   FIELDS TERMINATED BY ',' 
   ENCLOSED BY '"'
   LINES TERMINATED BY '\r\n'
   IGNORE 1 ROWS;
""")
conn.commit()
 
conn.close()

 
 