from ..core.page_parser import PageParser
from urllib.parse import urlparse

class AksonPageParser(PageParser):
    def _get_products_url(self):
        parsed_url = urlparse(self._url)
        domain = parsed_url.scheme + "://" + parsed_url.netloc
        
        result = []
        
        link_elements = self._soup.find_all("a", class_="body-m-regular line-clamp-3 text-headline hover:text-theme-primary")
        
        for link_element in link_elements:
            result.append(domain + link_element.get("href"))
            
        return result
        
