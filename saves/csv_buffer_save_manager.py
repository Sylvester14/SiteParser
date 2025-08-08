from .save_manager import ISaveManager
import json
import csv
import threading

class CsvBufferSaveManager(ISaveManager):
    __file_path: str
    __temp_file_path: str
    __feature_headers: set
    __lock: threading.Lock
    
    def __init__(self, file_path: str, temp_file_path: str = "./files/temp/temp.jsonl"):
        self.__file_path = file_path
        self.__temp_file_path = temp_file_path

        self.__lock = threading.Lock()
        self.__feature_headers = set()
        self.__clear_temp_file()
        
    
    def __clear_temp_file(self):
        open(self.__temp_file_path, "w").close()
    
    def add_to_buffer(self, objects: list[dict]):
        with self.__lock:
            with open(self.__temp_file_path, "a", encoding="utf-8") as file:
                for object in objects:
                    # Сохранение заголовков характеристик
                    for feature_key in object["features"].keys():
                        self.__feature_headers.add(feature_key)
                    
                    file.write(json.dumps(object, ensure_ascii=False) + "\n")

    def save_file(self):
        static_headers = ["name", "price", "url", "url_image"]
        feature_headers = sorted(self.__feature_headers)
        
        headers = []
        headers.extend(static_headers)
        headers.extend(feature_headers)
        
        with open(self.__file_path, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            
            with open(self.__temp_file_path, "r", encoding="utf-8") as temp_file:
                for line in temp_file:
                    line = line.strip()
                    decoded_product : dict = json.loads(line)
                    
                    url : str = decoded_product.get("url")
                    url_image : str = decoded_product.get("url_image")
                    name : str = decoded_product.get("name")
                    price : str = decoded_product.get("price")
                    
                    features : dict = decoded_product.get("features")
                    
                    row = {
                        "url": url,
                        "url_image": url_image,
                        "name": name,
                        "price": price
                    }
                    
                    for feature_header in feature_headers:
                        row[feature_header] = features.get(feature_header, "")
                    
                    writer.writerow(row)
