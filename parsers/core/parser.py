from abc import ABC
import requests as req
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0"
}

class Parser(ABC):
    soup: BeautifulSoup
    url: str
    
    def __init__(self, url: str):
        self.url = url
        text = req.get(url, HEADERS).text
        self.soup = BeautifulSoup(text, "lxml")
