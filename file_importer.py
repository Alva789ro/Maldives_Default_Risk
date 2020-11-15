import xlsxwriter
import pandas as pd
import numpy as np
import mysql.connector

real_gdp=pd.read_excel(r'xxxxxx', sheet_name='Sheet1')
nominal_gdp = pd.read_excel(r'xxxxxxx', sheet_name='Sheet2')
gdp_pcapita =pd.read_excel(r'xxxxxx', sheet_name='Sheet3')
inflation = pd.read_excel(r'xxxxxxx', sheet_name='Sheet4')
blnet = pd.read_excel(r'xxxxxx', sheet_name='Sheet5')
a_balance = pd.read_excel(r'xxxxxxx', sheet_name='Sheet6')


mydb = mysql.connector.connect(
    host = "xxxxxxx",
    user = "xxxxxx",
    passwd = "xxxxxxx",
    database = "xxxxx"
)

mycursor = mydb.cursor()

sqlformula1 = "INSERT INTO realgdp VALUES(%s, %s)"
for i, e in zip(real_gdp['year'], real_gdp['YTYchange']):
    mycursor.execute(sqlformula1, [i,e])

sqlformula2 = "INSERT INTO nominalgdp VALUES(%s, %s, %s)"
for i, e, f in zip(nominal_gdp['year'], nominal_gdp['NominalGDP'], nominal_gdp['YTYchange']):
    mycursor.execute(sqlformula2, [i,e,f])

sqlformula3 = "INSERT INTO gdppercapita VALUES(%s, %s)"
for i, e in zip(gdp_pcapita['year'], gdp_pcapita['YTYchange']):
    mycursor.execute(sqlformula3, [i,e])

sqlformula4 = "INSERT INTO inflation VALUES(%s, %s)"
for i, e in zip(inflation['year'], inflation['YTYchange']):
    mycursor.execute(sqlformula4, [i,e])

sqlformula5 = "INSERT INTO lendingborrowingnet VALUES(%s, %s, %s)"
for i, e, f in zip(blnet['year'], blnet['net'], blnet['YTYchange']):
    mycursor.execute(sqlformula5, [i,e,f])

sqlformula6 = "INSERT INTO accountbalance VALUES(%s, %s, %s)"
for i, e, f in zip(a_balance['year'], a_balance['balance'], a_balance['YTYchange']):
    mycursor.execute(sqlformula6, [i,e,f])


mydb.commit()
