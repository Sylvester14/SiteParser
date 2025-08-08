from ..core.product_parser import ProductParser 

class AksonProductParser(ProductParser):        
    def _parse_image(self) -> str:
        image = self._soup.find("img", class_="tablet:rounded-2 h-full w-full max-w-full max-h-full mobile-only:max-w-[420px] object-contain aspect-square image select-none")
        
        if image is None:
            raise Exception(f"Error ProductParser.parse(): image is None!. Product url: {self._url}")
        
        return image.get("src")


    def _parse_price(self) -> int:
        price_element = self._soup.find("div", class_="title-m-semibold text-headline")
        
        if(price_element is None):
            raise Exception(f"Error ProductParser._parse_price(): price is None!. Product url: {self._url}")
        
        price_string : str = price_element.string.split(" ₽ ")[0]
        price_number : int = int("".join(price_string.split(" ")))
        
        return price_number


    def _parse_name(self) -> str:
        name_element = self._soup.find("h1", class_="name title-s-bold text-headline")
        
        if(name_element is None):
            raise Exception(f"Error ProductParser._parse_name(): name is None!. Product url: {self._url}")
        
        return name_element.string
    
    def _parse_features(self) -> dict: 
        try:
            result = {}
            features_title = self._soup.find("h2", string="Характеристики")
            features_container = features_title.find_next_sibling()

            for feature_element_name in features_container.find_all("div", class_="prop-name body-l-regular text-secondary"):
                feature_name = feature_element_name.string
                feature_data = feature_element_name.find_next_siblings()[1].string
                result[feature_name] = feature_data
                
            return result
        except Exception as e:
            raise Exception(f"Error ProductParser._parse_features(): features parsing error!. Message: {e}. Product url: {self._url}")
            