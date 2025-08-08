from ..core import ParserBuilder, CategoryParser
from ..akson import AksonCategoryParser, AksonPageParser, AksonProductParser

class AksonParserBuilder(ParserBuilder):
    def build(self) -> CategoryParser:
        return AksonCategoryParser(AksonPageParser(AksonProductParser()))

