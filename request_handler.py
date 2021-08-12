import requests
from endpoints import logon_form, product_page, order_online


class RequestHandler:


    headers = {
        "Referer": "https://costco.com/",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }


    def __init__(self):
        print('*** INITIALIZING REQUESTS SESSION ***')
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.get_login()
        print('*** INITIALIZED REQUESTS SESSION --> ', self.session)


    def get_login(self, url = logon_form):
        return self.session.get(url)


    def get_page_html(self, url = product_page):
        page = self.session.get(url)
        return page.content

