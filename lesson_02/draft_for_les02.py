import requests

params_api_sales = {
    'date': '2022-08-09',
    'page': 1
}

auth_api_sales = {
    'Authorization': '2b8d97ce57d401abd89f45b0079d8790edd940e6'
}

api_sales = requests.get(url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
                         params=params_api_sales,
                         headers=auth_api_sales
                         )

print('STATUS_CODE: ', api_sales.status_code)
print('REQUEST: ', api_sales.json())
