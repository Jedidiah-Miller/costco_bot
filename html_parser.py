from bs4 import BeautifulSoup



class HtmlParser:


    def __init__(self):
        pass


    def get_title(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        title = soup.find("title")
        return title.string


    def get_class_elements(self, page_html, tag = "span", class_name = "server-error"):
        soup = BeautifulSoup(page_html, 'html.parser')
        return soup.find_all(tag, {"class": class_name})