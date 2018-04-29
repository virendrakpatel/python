import numpy
from numpy import arange
import pyspark as ps
from pyspark.sql import SQLContext
import pandas as pd
import pandas.io.sql as psql
from pandas import Series, DataFrame
import pypyodbc

conn = pypyodbc.connect('Driver={SQL Server};'
                        'Server=ASHBIZDB022;'
                        'Database=YPC_BI_DW;'
                        "'uid=CORP\\virendrapatel;pwd=")

sql_query = " SELECT top 2000  Billed_CustomerID, SalesPartnerCode,  Billed_TransactionDate,  Billed_RevenueAmount FROM YPC_BI_DW.dbo.D_YPC_BillingTransaction;"

df = psql.read_sql(sql_query, conn)

print(df)
print("End of the program.")

print(df.groupby(['billed_customerid','billed_transactiondate'])['billed_revenueamount'].sum())


