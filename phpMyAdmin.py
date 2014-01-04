import sqlite3
dbName = "d:/work/wxBus/DBFiles/beijing"
sqlCon = sqlite3.connect(dbName)
cu = sqlCon.cursor()
cu.execute("select * from lines")
print cu.fetchone()
