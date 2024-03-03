from urllib import request
import json
from datetime import datetime


u1 = 'https://cloud.oktell.studio/api/token/v1/3bfd6646a3e96207c1d630a79629aaa2?license'
u2 = 'https://cloud.oktell.studio/api/token/v1/3bfd6646a3e96207c1d630a79629aaa2'


def get_date_lic(url: str) -> datetime:
    with request.urlopen(url) as response:
        html = response.read()
    return datetime.fromtimestamp(json.loads(html)['data']['license']['until'])


def solve_div_days(date_lic: datetime) -> int:
    return (date_lic - datetime.now()).days


def set_data_post(days: int) -> dict:
    # В задании ошибка, не учтено само значение в 7 дней
    # либо больше, либо меньше
    if div_days >= 7:
        values = {"days": div_days, "alarm": False}
    elif div_days < 7:
        values = {"days": div_days, "alarm": True}
    return values


def show_site_data(req: request.Request):
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == '__main__':
    date_lic = get_date_lic(u1)
    div_days = solve_div_days(date_lic=date_lic)
    data = json.dumps(set_data_post(div_days)).encode('utf-8')
    req = request.Request(u2, data=data,
                        headers={'content-type': 'application/json'})

    print('Время и дата окончания лицензии: ', date_lic.strftime(
                                                    '%H:%M %d/%m/%Y'))
    show_site_data(req)
