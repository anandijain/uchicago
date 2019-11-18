'''
allows one to book a room 

auth is going to be weird

how to avoid using selenium?
ideally https://www.lib.uchicago.edu/api/v2/pages/ send direct http requests

{
    "id": 6475,
    "meta": {
        "type": "public.StandardPage",
        "detail_url": "https://www.lib.uchicago.edu/api/v2/pages/6475/",
        "html_url": "https://www.lib.uchicago.edu/reg/reg-spaces/",
        "slug": "reg-spaces",
        "first_published_at": "2017-05-10T14:20:01.936162-05:00"
    },
    "title": "Spaces & Services"
},

'''
import time
import datetime

import requests as r
from selenium import webdriver

API_ROOT = 'https://www.lib.uchicago.edu/api/v2/pages/'
ROOT = 'https://rooms.lib.uchicago.edu/'
REG_SFX = 'reserve/regensteingroupstudies'
CRERAR_SFX = '/reserve/crerar'

CONFIG = {
    'location': 'reg',  # one of ['reg', 'crerar']
    'date': '11/25/2019',
    'start_time': '18',  # army time
    'end_time': '19.5' 
}   


BOOK_ROOM_JSON = {
    "id": 6474,
    "meta": {
        "type": "redirects.RedirectPage",
        "detail_url": "https://www.lib.uchicago.edu/api/v2/pages/6474/",
        "html_url": "https://www.lib.uchicago.edu/reg/reg-spaces/book-room/",
        "slug": "book-room",
        "first_published_at": "2017-05-10T14:16:30.503876-05:00"
    },
    "title": "Book a Room"
}


def base_driver(screen=None):
    '''
    screen is either None, 'full', or 'min'
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options=chrome_options)

    if not screen:
        pass
    elif screen == 'full':
        driver.maximize_window()
    elif screen == 'min':
        driver.minimize_window()

    return driver

def click_go_to_date(driver):
    btn_class = 'fc-goToDate-button' # fc-button fc-button-primary'
    cal_class = 'datepicker' # datepicker-dropdown dropdown-menu datepicker-orient-left datepicker-orient-top'
    btn = driver.find_element_by_class_name(btn_class)
    btn.click()
    cal = driver.find_element_by_class_name(cal_class)
    all_dates = cal.find_elements_by_tag_name('data-date')
    for d in all_dates:
        print(d)


def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000)


def get_data_date(v=False):
    date_to_get = CONFIG['date']
    dt = datetime.datetime.strptime(date_to_get, '%m/%d/%Y')
    epoch_time = unix_time_millis(dt)
    if v:
        print(dt)
        print(epoch_time)
    return epoch_time

def get_url():
    if CONFIG['location'] == 'reg':
        url = ROOT + REG_SFX
    else:
        url = ROOT + CRERAR_SFX
    return url

def init_browser():
    url = get_url()
    driver = base_driver()
    driver.get(url)
    return driver

def main():
    '''

    '''
    d = init_browser()
    data_date = get_data_date()

    click_go_to_date(d)
    time.sleep(3)





if __name__ == "__main__":
    main()
