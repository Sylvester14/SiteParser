from parsers import AksonParserBuilder, CategoryParser
from saves import CsvBufferSaveManager

products_file_path = "files/products.csv"
url = "https://akson.ru/kostroma/c/kraski/"

def main():
    save_manager = CsvBufferSaveManager(products_file_path)
    parser : CategoryParser = AksonParserBuilder(save_manager).build()
    
    parser.parse(url)
    save_manager.save_file()

if __name__ == "__main__":
    main()
