from lesson_02.ht_template.job1.dal.sales_api import get_sales
from lesson_02.ht_template.job1.dal.local_disk import save_to_disk


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    # TODO: implement me

    # 1. get data from the API
    print("\tI'm in get_sales(" + date + ") function!")
    get_data = get_sales(date)

    # 2. save data to disk
    print("\tI'm in save_to_disk(" + date + ", " + raw_dir + ") function!")
    save_to_disk(get_data, raw_dir)

    pass
