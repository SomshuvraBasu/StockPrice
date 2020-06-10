import xlrd
import mysql.connector as m

def sq()

book = xlrd.open_workbook("StockPrices.xlsx")
sheet = book.sheet_by_name("sensex")

database = m.connect (host='localhost', user="root", passwd="1234", db="stock")

cursor = database.cursor()

query ="""INSERT INTO sensex (AdjClose, 90ma) VALUES(%s,%s)"""

for r in range (3, sheet.nrows):
    #date =sheet.cell(r,0).value
    AdjClose =sheet.cell(r,1).value
    Moving =sheet.cell(r,2).value

    values = (AdjClose, Moving)

    cursor.execute(query, values)

cursor.close()

database.commit()

print ("complete")
