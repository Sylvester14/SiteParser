from parsers import AksonParserBuilder, CategoryParser
import json

products_file_path = "files/products.csv"
url = "https://akson.ru/kostroma/c/kraski/"


def main():
    parser : CategoryParser = AksonParserBuilder().build()
    result = parser.parse(url)
    
    with open("files/test.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(result, ensure_ascii=False, indent=4))
    


if __name__ == "__main__":
    main()
