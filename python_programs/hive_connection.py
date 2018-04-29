from pyhive import presto

cursor = presto.connect(host='host.example.com',
                    port=8081,
                    username='USERNAME:PASSWORD').cursor()

sql = 'select * from table limit 10'

cursor.execute(sql)

print(cursor.fetchone())
print(cursor.fetchall())