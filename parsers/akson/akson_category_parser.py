from ..core.category_parser import CategoryParser

class AksonCategoryParser(CategoryParser):
    def _get_page_url(self, url: str, page_number: int) -> str:
        return url + "?page=" + str(page_number)

    def _get_page_count(self) -> int:
        page_elements = self._soup.find_all("a", class_="router-link-active router-link-exact-active group flex h-full w-full items-center justify-center")
        return int(page_elements[-1].string)
