import requests as r
from bs4 import BeautifulSoup
from parsers import ProductParser
import csv

products_file_path = "files/products.csv"
page_template = "?page="
domain = "https://akson.ru"
url = "https://akson.ru/kostroma/c/kraski/"

headers = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0"
}

def main():
    req = r.get(url + page_template + "1", headers)
    src = req.text
    
    data = parse(src)
    save_to_csv(["url", "url_image"], data, products_file_path)
        
        
def parse(text: str) -> list[dict]:
    soup = BeautifulSoup(text, "lxml")
    
    result = []
    links = soup.find_all("a", class_="body-m-regular line-clamp-3 text-headline hover:text-theme-primary")
    
    for link in links:
        href = domain + link.get("href")
        result.append(ProductParser(url=href).parse())
        
    return result
        

def save_to_csv(columns: list[str], data: list[dict], file_path: str):
    with open(file_path, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns, lineterminator="\n")
        
        writer.writeheader()
        writer.writerows(data)


def save(text: str, file_path: str):
    with open(file_path, mode="w", encoding="utf-8") as file:
        file.write(text)

def save_lines(text_lines: list[str], file_path: str):
    with open(file_path, mode="w", encoding="utf-8") as file:
        for line in text_lines:
            file.write(line + "\n")



if __name__ == "__main__":
    main()
