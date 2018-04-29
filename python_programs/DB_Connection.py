import sys
import math
import pandas as pd
import numpy
from numpy import arange
import pyspark as ps
from pyspark.sql import SQLContext

import pandas as pd
from pandas import Series, DataFrame
import pypyodbc

class fetch_item:
    """
    This is fetching class for records, later didn't need to use it.
    """
    def __init__(self, Billed_CustomerID, SalesPartnerCode, Billed_TransactionDate, Billed_RevenueAmount):
        self.Billed_CustomerID = Billed_CustomerID
        self.SalesPartnerCode = SalesPartnerCode
        self.Billed_TransactionDate = Billed_TransactionDate
        self.Billed_RevenueAmount = Billed_RevenueAmount


conn = pypyodbc.connect('Driver={SQL Server};'
                        'Server=ASHBIZDB022;'
                        'Database=YPC_BI_DW;'
                        "'uid=CORP\\virendrapatel;pwd=xxxxxxx")

cur = conn.cursor()
sql_query = " SELECT top 2000  Billed_CustomerID, SalesPartnerCode,  Billed_TransactionDate,  Billed_RevenueAmount FROM YPC_BI_DW.dbo.D_YPC_BillingTransaction;"

# results = cur.execute(sql_query).fetchall()
# total_count = len(results)

results = []
results = cur.execute(sql_query)
results = cur.fetchone()
final_result = DataFrame
lst_1 = []
lst_2 = []
dict1 = {}
while results:
    if results is not None:
        try:
            # print("Your Audit result is " + str(results[0]) + " " + str(results[1]) + " lives in " + str(results[2]))
            # d_frame = pd.DataFrame(results[0],results[1], results[2], columns=list['SalesPartnerCode', 'Billed_TransactionDate','Billed_RevenueAmount'])
            ft = fetch_item(results[0],results[1], results[2], results[3])
            # lst_1.append(ft.Billed_CustomerID)
            # lst_1.append(ft.SalesPartnerCode)
            # lst_1.append(ft.Billed_TransactionDate)
            # lst_1.append(ft.Billed_RevenueAmount)
            # lst_2.append(lst_1)
            dict1 = {'Billed_CustomerID': results[0], 'SalesPartnerCode': results[1], 'Billed_TransactionDate': results[2], 'Billed_RevenueAmount': results[3]}
            lst_1.append(dict1)
            # intermediate_df = pd.DataFrame.add(list(ft.))

            results = cur.fetchone()
        except TypeError:
            continue
# print(lst_1)
# print(lst_2)
intermediate_df = pd.DataFrame(lst_1)
# intermediate_df = pd.DataFrame.from_records(lst_1, index=None, columns=list['Billed_CustomerID','SalesPartnerCode', 'Billed_TransactionDate','Billed_RevenueAmount'])
# intermediate_df = pd.DataFrame(lst_1, columns=list['Billed_CustomerID','SalesPartnerCode', 'Billed_TransactionDate','Billed_RevenueAmount'])
print(intermediate_df)
print ('Closing the connection')
conn.close()
print ('End of the program')

print(intermediate_df.groupby(['Billed_CustomerID','Billed_TransactionDate'])['Billed_RevenueAmount'].sum())

# d_frame = pd.DataFrame(data=dict, index=arange(total_count))
# d_frame = d_frame.sort_values()s
# print('0.0')
# print(final_result)
# print('0.1')
# sc = ps.SparkContext()
# print('1')
# spark_df = SQLContext(sc)
# print(spark_df)
# print('2')
# spark_df.createDataFrame(final_result).show()
# print('3')
# # cur.execute(sql_query)
#

