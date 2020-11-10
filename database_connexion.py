import mysql.connector
 
conn = mysql.connector.connect(host="mysql-leonelal.alwaysdata.net",
                               user="leonelal_devops", password="devopspassword", 
                               database="leonelal_devops")
cursor = conn.cursor()
 
cursor.execute("""
   CREATE TABLE IF NOT EXISTS Produits (
      ref int(6) NOT NULL,
      nom varchar(100) DEFAULT NULL,
      stock int(4) DEFAULT NULL,
      prix float(5,2) DEFAULT NULL,
      PRIMARY KEY(ref),
      CHECK (stock>=0)
      );
""")
 
conn.close()