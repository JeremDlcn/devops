import unittest
import mysql.connector

conn = mysql.connector.connect(
                host="mysql-leonelal.alwaysdata.net",
                user="leonelal_devops",
                password="devopspassword",
                database="leonelal_devops"
            )
try:
    test = conn.is_connected()
except: 
    test = False

class TypeTest(unittest.TestCase):

    def test_choice(self):

        self.assertTrue(test)

unittest.main()