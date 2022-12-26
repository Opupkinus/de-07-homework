import json
import os
import shutil
from typing import List, Dict, Any
from fastavro import writer


def convert_json_to_avro(raw_data: List[Dict[str, Any]], path: str) -> None:
    schema = {
        'name': 'sales',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'},
        ],
    }

    raw_data = json.loads(raw_data.replace("\'", "\""))

    mode = 0o777

    try:
        os.makedirs(path, mode)
        print('save_json_to_avro_CREATE_DIRECTORY: ' + path)
    except OSError as error:
        shutil.rmtree(path)
        print('save_json_to_avro_DELETE_EXISTING_DIRECTORY: ' + path[-10:])
        os.makedirs(path, mode)
        print('save_json_to_avro_CREATE_DIRECTORY: ' + path)

    with open(os.path.join(path, 'sales_' + path[-10:] + '.avro'), 'wb') as out:
        try:
            writer(out, schema, raw_data)
            print('save_json_to_avro_WRITE_DATA_IN: ' + 'sales_' + path[-10:] + '.avro')
        except FileNotFoundError as error:
            print('get_raw_data_FILE_NOT_FOUND_IN: ' + error)

    pass