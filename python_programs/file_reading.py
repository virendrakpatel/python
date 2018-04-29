import sys
import collections
from pyspark import SparkConf
from pyspark.context import SparkContext



find_word = 'DEBUG'
i_read = open("application_log.log.3",'r')

worldset = []
world_dict = {}
cnt = 0
str = ''
# print(collections.Counter(i_read.read().replace(' ','').split("|")))

# for line_no, r in enumerate(i_read):
#     worldset = r.split("|")
#     str = "".join(worldset).replace(' ','')
#     print(str)
#     if find_word in str:
#         cnt += 1
# print(cnt)

for line_no, r in enumerate(i_read):
    worldset = r.replace(' ','').split("|")
    # str = "".join(worldset)
    # print(worldset)
    if find_word in worldset:
        cnt += 1
print(cnt)



# print(collections.Counter(i_read))

sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))
textfile = sc.textFile("application_log.log.3") \
            .map(lambda line: line.split("|")) \
            .collect()
print(type(textfile))
print(textfile)

# .map(lambda line: line.split("|")) \
#     .filter(lambda line: len(line) > 0) \
    # .map(lambda line: (line[0], line[1], line[2], line[3]))\



