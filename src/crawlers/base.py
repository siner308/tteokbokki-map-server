from src.apps.brand.models import Brand
from src.apps.place.models import Place
from src.utils.chromedriver import setup_chrome


class BaseCrawler:
    map_util = None
    crawler_name = None
    brand_name = None
    brand = None
    driver = setup_chrome()
    url = None

    def _set_brand(self):
        if not self.brand_name:
            raise NotImplementedError
        self.brand = Brand.objects.get(name=self.brand_name)

    def get_brand(self):
        if not self.brand:
            self._set_brand()
        return self.brand

    def set_next_page_url(self):
        raise NotImplementedError

    def get_place_data(self) -> [Place]:
        # return Place(name, description, latitude, longitude)
        raise NotImplementedError

    def run(self):
        if not self.driver:
            raise ModuleNotFoundError('selenium driver required')
        while True:
            self.set_next_page_url()
            print(self.url)
            places = self.get_place_data()
            if not len(places):
                break
            place_names = [place.name for place in places]
            exist_place_names = [place.name for place in Place.objects.filter(name__in=place_names)]
            new_places = [place for place in places if place.name not in exist_place_names]
            Place.objects.bulk_create(new_places)
            print('new %s places are created' % str(len(new_places)))
        print('%s finished' % self.crawler_name)