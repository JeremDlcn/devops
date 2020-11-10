import mysql.connector
 
conn = mysql.connector.connect(host="mysql-leonelal.alwaysdata.net",
                               user="leonelal_devops", password="devopspassword", 
                               database="leonelal_devops")
cursor = conn.cursor()
 
cursor.execute("""
   LOAD DATA INFILE 'CSV_Files/sdiscounts.csv' 
   INTO TABLE discounts 
""")
 
conn.close()

LOAD DATA INFILE 'c:/tmp/discounts.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



   CREATE TABLE IF NOT EXISTS Produits (
      ref int(6) NOT NULL,
      nom varchar(100) DEFAULT NULL,
      stock int(4) DEFAULT NULL,
      prix float(5,2) DEFAULT NULL,
      PRIMARY KEY(ref),
      CHECK (stock>=0)
      );