from .parser import Parser

class ProductParser(Parser):
    def parse(self) -> dict:
        image = self.soup.find("img", class_="tablet:rounded-2 h-full w-full max-w-full max-h-full mobile-only:max-w-[420px] object-contain aspect-square image select-none")
        
        if image is None:
            raise Exception(f"Error ProductParser.parse(): image is None!. Product url: {self.url}")
        
        image_url = image.get("src")
        
        return {
            "url": self.url,
            "url_image": image_url
        }
