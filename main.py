from config import get_parser, get_save_manager
import argparse

default_products_file_path = "files/products.csv"
default_url = "https://akson.ru/kostroma/c/kraski/"

def main():
    # Консольные аргументы
    argument_parser = argparse.ArgumentParser(description="Парсинг товаров с сайта")
    argument_parser.add_argument("--file", help="Выходной файл", default=default_products_file_path)
    argument_parser.add_argument("--url", help="Ссылка на категорию", default=default_url)
    argument_parser.add_argument("--max-workers", help="Максимальное число потоков", type=int)
    argument_parser.add_argument("--max-pages", help="Максимальное число страниц", type=int)
    
    args = argument_parser.parse_args()
    
    # Максимальное число страниц
    max_page = int(args.max_pages if args.max_pages is not None else -1)
    # Максимальное число потоков
    max_workers = int(args.max_workers if args.max_workers is not None else 10)
    # Путь к файлу сохранения
    file = args.file
    # Путь к категории
    url = args.url
    
    save_manager = get_save_manager(file)
    parser = get_parser(save_manager)
    
    parser.parse(url, max_page=max_page, max_workers=max_workers)
    save_manager.save_file()
    
    print(f"Данные успешно записаны в файл: {args.file}")

if __name__ == "__main__":
    main()
