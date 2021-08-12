import time
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
from endpoints import product_page, order_online


import secrets  # from secrets.py in this folder

def headers():
    return {
        "Referer": "https://costco.com/",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }

def get_page_html(url):
    page = requests.get(url, headers=headers())
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    product_not_found_title = soup.find("title")
    return 'product not found' not in product_not_found_title.string.lower()


def check_item_in_stock_order_by_number(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_span = soup.find_all("span", {"class": "server-error"})

    return len(out_of_stock_span) == 0


def setup_twilio_client():
    return Client(secrets.TWILIO_ACCOUNT_SID, secrets.TWILIO_AUTH_TOKEN)

def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        messaging_service_sid=secrets.MESSAGING_SERVICE_SID,
        body=f"Callaway Golf Clubs are in stock! -- open --  {product_page}",
        to=secrets.MY_PHONE_NUMBER
    )


def check_inventory():
    # first page
    page_html = get_page_html(product_page)
    if check_item_in_stock(page_html):
        send_notification()
        print('In stock!')
    else:
        print("Out of stock still -- product page")
    # second page
    page_html = get_page_html(order_online)
    if check_item_in_stock_order_by_number(page_html):
        send_notification()
        print('In stock!')
    else:
        print("Out of stock still -- order by item number")



def run():
    count = 0
    while True:
        print('---------------------', count)
        check_inventory()
        count += 1
        time.sleep(30)  # Wait a minute and try again



run()