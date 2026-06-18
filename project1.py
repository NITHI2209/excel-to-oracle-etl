import pandas as pd
import oracledb

df = pd.read_excel("students.xlsx")

conn = oracledb.connect(
    user="sys",
    password="*******",
    dsn="localhost:1521/XEPDB1",
    mode=oracledb.AUTH_MODE_SYSDBA
)

cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO STUDENT
        (NAME, FATHER_NAME, DOB, QUALIFICATION)
        VALUES (:1, :2, :3, :4)
        """,
        (
            row["NAME"],
            row["FATHER_NAME"],
            row["DOB"],
            row["QUALIFICATION"]
        )
    )

conn.commit()

print("Data Inserted Successfully!")

cursor.close()
conn.close()
