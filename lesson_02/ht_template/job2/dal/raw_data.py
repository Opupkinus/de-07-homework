from typing import List, Dict, Any
import os


def get_raw_data(path: str) -> str:
    """

    :rtype: object
    """

    try:
        open_raw_data = open(path + '/sales_' + path[-10:] + '.json', 'r')
        print('get_raw_data_OPEN_FILE_IN_DIRECTORY: ' + os.path.join(path, 'sales_' + path[-10:] + '.json'))
        raw_data = open_raw_data.read()
        print('get_raw_data_READ_FILE: sales_' + path[-10:] + '.json')

    except FileNotFoundError as error:
        raw_data = str(error)
        print('get_raw_data_FILE_NOT_FOUND_IN: ' + raw_data)

    return raw_data
