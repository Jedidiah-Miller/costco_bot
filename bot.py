from request_handler import RequestHandler
from html_parser import HtmlParser
from notifications import Twilio
from endpoints import product_page, order_online
# from datetime import datetime


class Bot:


    def __init__(self) -> None:
        self.session = RequestHandler()
        self.parser = HtmlParser()
        self.count = 0


    def check_item_in_stock(self, page_html):
        product_not_found_title = self.parser.get_title(page_html)
        return 'product not found' not in product_not_found_title.string.lower()


    def check_item_in_stock_order_by_number(self, page_html):
        out_of_stock_span = self.parser.get_class_elements(page_html, tag="span", class_name="server-error")
        return len(out_of_stock_span) == 0


    def check_product_page(self):
        page_html = self.session.get_page_html(product_page)
        if self.check_item_in_stock(page_html):
            self.send_notification()
            print('In stock!')
        else:
            print("Out of stock still -- product page")


    def check_order_by_item_number_page(self):
        page_html = self.session.get_page_html(order_online)
        if self.check_item_in_stock_order_by_number(page_html):
            self.send_notification()
            print('In stock!')
        else:
            print("Out of stock still -- order by item number")


    def send_notification(self):
        twilio_client = Twilio()
        twilio_client.send_notification()