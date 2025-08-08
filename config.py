from saves import CsvBufferSaveManager, ISaveManager
from parsers import AksonParserBuilder, CategoryParser

def get_save_manager(file_args: str) -> ISaveManager:
    return CsvBufferSaveManager(file_args)

def get_parser(save_manager: ISaveManager) -> CategoryParser:
    return AksonParserBuilder(save_manager).build()
