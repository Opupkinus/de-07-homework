import requests
import os
import shutil
from fastavro import writer
import json
from lesson_02.ht_template.job1.dal import local_disk, sales_api
from lesson_02.ht_template.job1.dal.sales_api import get_sales
from lesson_02.ht_template.job1.dal.local_disk import save_to_disk
#from lesson_02.ht_template.job1.bll.sales_api import save_sales_to_local_disk
from lesson_02.ht_template.job2.dal.raw_data import get_raw_data
# from lesson_02.ht_template.job2.bll.convert_raw_data import save_json_to_avro
# import re
# raw_dir = "C:/Users/El Bruno/PycharmProjects/de-07-homework/lesson_02/path/to/my_dir/raw/sales/2022-08-13"
# stg_dir = "C:/Users/El Bruno/PycharmProjects/de-07-homework/lesson_02/path/to/my_dir/stg/sales/2022-08-13"
# save_json_to_avro(raw_dir, stg_dir)

BASE_DIR = os.environ.get("BASE_DIR")
print(BASE_DIR)
RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", "2022-08-09")
STG_DIR = os.path.join(BASE_DIR, "stg", "sales", "2022-08-09")
print(RAW_DIR)
print(STG_DIR)


#
# path = "C:/Users/El Bruno/PycharmProjects/de-07-homework/lesson_02/path/to/my_dir/raw/sales/2022-08-10"
# path_avro = 'C:/Users/El Bruno/PycharmProjects/de-07-homework/lesson_02/path/to/my_dir/stg/sales/2022-08-10'
# schema = {
#     'name': 'sales',
#     'type': 'record',
#     'fields': [
#         {'name': 'client', 'type': 'string'},
#         {'name': 'purchase_date', 'type': 'string'},
#         {'name': 'product', 'type': 'string'},
#         {'name': 'price', 'type': 'int'},
#     ],
# }
#
# raw_data = json.loads(get_raw_data(path).replace("\'", "\""))
# mode = 0o777
#
# try:
#     os.makedirs(path_avro, mode)
#     print('save_to_disk_CREATE_DIRECTORY: ' + path_avro)
# except OSError as error:
#     shutil.rmtree(path_avro)
#     print('save_to_disk_DELETE_EXISTING_DIRECTORY: ' + path_avro[-10:])
#     os.makedirs(path_avro, mode)
#     print('save_to_disk_CREATE_DIRECTORY: ' + path_avro)
#
# with open(os.path.join(path_avro, 'sales_' + path_avro[-10:] + '.avro'), 'wb') as out:
#     writer(out, schema, raw_data)

# get_sales = get_sales(date)
# print(get_sales)
#
# save_to_disk(get_sales, path)


# API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'
# SECRET_KEY = os.environ['SECRET_KEY']
# API_DATE = '2022-08-09'
#
# params_api_sales = {
#     'date': '2022-08-09',
#     'page': 5
# }
# auth_api_sales = {
#     'Authorization': SECRET_KEY
# }
#
# api_sales = requests.get(url=API_URL,
#                          params=params_api_sales,
#                          headers=auth_api_sales
#                          )
#
# print('STATUS_CODE: ', api_sales.status_code)
# print('REQUEST: ', api_sales.json())
# a = api_sales.json()
#
#
# #######################
# #######################
#
# parent_dir = os.getcwd()
# directory = "path\\to\\o\\my_dir\\raw\\sales\\"+API_DATE
# path = os.path.join(parent_dir, directory)
# mode = 0o777
#
# try:
#     os.makedirs(path, mode)
# except OSError as error:
#     shutil.rmtree(path)
#     os.makedirs(path, mode)
#
# open(os.path.join(path, 'sales_'+API_DATE+'.json'), 'w').write(SECRET_KEY)


