from typing import List, Dict, Any
import os
import shutil


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    # TODO: implement me
    mode = 0o777

    try:
        os.makedirs(path, mode)
        print('save_to_disk_CREATE_DIRECTORY: ' + path)
    except OSError as error:
        shutil.rmtree(path)
        print('save_to_disk_DELETE_EXISTING_DIRECTORY: ' + path[-10:])
        os.makedirs(path, mode)
        print('save_to_disk_CREATE_DIRECTORY: ' + path)

    open(os.path.join(path, 'sales_' + path[-10:] + '.json'), 'w').write(str(json_content))
    print('save_to_disk_WRITE_DATA_IN: ' + 'sales_' + path[-10:] + '.json')

    pass
