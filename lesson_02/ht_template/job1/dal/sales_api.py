from typing import List, Dict, Any
import requests
import os


def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :return: list of records
    """
    secret_key = os.environ.get("API_AUTH_TOKEN")
    api_url = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'

    page = 1
    params_api_sales = {
        'date': date,
        'page': page
    }
    auth_api_sales = {
        'Authorization': secret_key
    }
    request_answer = list()
    data = list()

    while str(request_answer)[13:50] != "You requested page that doesn't exist":

        params_api_sales['page'] = page

        api_sales = requests.get(url=api_url,
                                 params=params_api_sales,
                                 headers=auth_api_sales
                                 )

        data.extend(request_answer)
        status_code = api_sales.status_code
        request_answer = api_sales.json()

        if status_code == 404:
            print('get_sales_STATUS_CODE: ', status_code)
            print('get_sales_REQUEST: ', request_answer)
            if str(request_answer)[13:50] == "You requested page that doesn't exist":
                return data
            elif str(request_answer)[13:35] == "No data found for date":
                return request_answer
        else:
            print('get_sales_PAGE: ', page)
            print('get_sales_STATUS_CODE: ', status_code)
            print('get_sales_REQUEST: ', request_answer)

            page += 1
