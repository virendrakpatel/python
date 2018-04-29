import numpy as np
import pandas as pd
import json

from pandas import Series, DataFrame

json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""

json_data = json.loads(json_obj)

print(json_data)
print('------------------------------------')
print(type(json_data))

back_to_json = json.dumps(json_data)

print(back_to_json)
print('------------------------------------')
print(type(back_to_json))

dframe = DataFrame(json_data['diet'])

print(dframe)
print('------------------------------------')
print(type(dframe))



