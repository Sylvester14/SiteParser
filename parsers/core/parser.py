from abc import ABC
import requests as req
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0"
}

class Parser(ABC):
    _soup: BeautifulSoup
    _url: str
    
    def _set_url(self, url: str):
        self._url = url
        text = req.get(url, HEADERS).text
        self._soup = BeautifulSoup(text, "lxml")
