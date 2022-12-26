from lesson_02.ht_template.job2.dal import raw_data, json_to_avro
from lesson_02.ht_template.job2.dal.raw_data import get_raw_data
from lesson_02.ht_template.job2.dal.json_to_avro import convert_json_to_avro

def save_json_to_avro(raw_dir: str, stg_dir: str) -> None:

    # 1. get data from the path
    print("\tI'm in get_raw_data(" + raw_dir + ") function!")
    raw_data = get_raw_data(path=raw_dir)

    # 2. save data to new path in avro
    if raw_data[0:35] == '[Errno 2] No such file or directory':
        print("\tI'm skip convert_json_to_avro(raw_data, " + stg_dir + ") function because there is no file on raw_dir")
    elif raw_data[0:35] == "{'message': 'No data found for date":
        print("\tI'm skip convert_json_to_avro(raw_data, " + stg_dir + ") function because there is no data in file: sales_" + raw_dir[-10:] + ".json")
    else:
        print("\tI'm in convert_json_to_avro(raw_data, " + stg_dir + ") function!")
        convert_json_to_avro(raw_data, stg_dir)

    pass
