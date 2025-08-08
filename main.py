from parsers import AksonParserBuilder, CategoryParser
from saves import CsvBufferSaveManager
import os

products_file_path = "files/products.csv"
url = "https://akson.ru/kostroma/c/kraski/"

def main():
    save_manager = CsvBufferSaveManager(products_file_path)
    parser : CategoryParser = AksonParserBuilder(save_manager).build()
    
    parser.parse(url)
    save_manager.save_file()
    
    clear_console()
    print(f"Данные успешно записаны в файл: {products_file_path}")
    
    
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
