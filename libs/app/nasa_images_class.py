from request_manager.manager import RequestManager


class NasaMedia(RequestManager):
    """
        Class used to extract information
        of specific medias from the Nasa API
    """
    def __init__(self, parameter: str or None=None):
        super(NasaMedia, self).__init__()
        self.parameter = parameter
        self.primordial_link = 'https://images-api.nasa.gov/search'
        self.results = list()
        self.count_items = int()
        self.all_occurrences = list()
        self.params = {
            'q': str(),
            'page': str(),
            'media_type': 'image',
            'year_start': 1920,
            'year_end': 2023,
        }

    def set_parameter(self, parameter: str or None=None) -> None:
        if parameter:
            self.parameter = parameter
        if not self.parameter:
            raise ValueError('Need to add a parameter')

    def extract_information(self, page: int=1) -> None:
        self.params['q'] = self.parameter
        self.params['page'] = page
        self.results = list()
        self.count_items = str()
        self.send_requisitons_requests(self.primordial_link)
        if self.availiable:
            self.results = self.response.json()
            if 'collection' in self.results.keys():
                self.results = self.results['collection']
                self.count_items = self.results.get('metadata', dict()).get('self.results', str())
                self.results = self.results.get('items')
