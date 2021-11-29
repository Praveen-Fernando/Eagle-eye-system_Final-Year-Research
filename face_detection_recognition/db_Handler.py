import mysql.connector as msql
from mysql.connector import Error


def return_data():
    try:
        conn = msql.connect(host='127.0.0.1', port=3306,
                            database='criminal_investigation', user='root',
                            password='')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            cursor.fetchone()
            # print("You're connected to database: ", record)
            cursor.execute("DROP TABLE IF EXISTS criminal_result;")
            # print("Existing Table Dropped")
            cursor.execute(
                "CREATE TABLE criminal_result(id int(11) NOT NULL, Name varchar(100) NOT NULL, Age int(11) NOT NULL,"
                " Gender varchar(100) NOT NULL, DOB date NOT NULL, Address varchar(100) NOT NULL, Blood_Group varchar(100) NOT NULL,"
                " NIC int(11) DEFAULT NULL,Height float NOT NULL, Crimes varchar(100) NOT NULL)")
            # print("Criminal Result Table Created")
            sql = "INSERT INTO criminal_investigation.criminal_result SELECT criminals_details.id,criminals_details.Name,criminals_details.Age,criminals_details.Gender, criminals_details.DOB,criminals_details.Address,criminals_details.Blood_Group,criminals_details.NIC,criminals_details.Height, criminals_details.Crimes " \
                  "FROM criminals LEFT JOIN criminals_details ON (criminals_details.id = criminals.cID)" \
                  "WHERE criminals.SNo = SNo = 1"
            cursor.execute(sql)
            print("Criminal Recognized & Values inserted")
            print("*** STEP 3 EXECUTED SUCCESSFULLY ***")
            conn.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

