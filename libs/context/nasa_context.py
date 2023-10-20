from libs.app.data_manipulation_class import DataBox
from libs.app.nasa_images_class import NasaMedia
from pathlib import Path
from io import BytesIO
from PIL import Image
from tqdm import tqdm
import warnings
import PIL
import csv
import os


class NasaContext(object):
    """
        Class used to manage the context
        from the app that conect to the Nasa API
    """
    def __init__(self, search_term: str):
        self.my_path = os.getcwd().replace('\\', '/')
        self.nasa_app = NasaMedia()
        self.data_box = DataBox()
        self.search_term = search_term

    def downloading_images(self, image_link: str) -> list['PIL.JpegImagePlugin.JpegImageFile', int]:
        """
            Get a list of images links and download this images 
            and save in a diretory from the OS
        """
        if image_link.startswith('http'):
            binary_image = self.nasa_app.send_requisitons_requests(image_link)
            if not self.nasa_app.available:
                return
            file_image = Image.open(BytesIO(binary_image.content))
        else:
            return
        return [file_image, binary_image.status_code]

    def save_image(self, binary_image: 'PIL.JpegImagePlugin.JpegImageFile', index_image: int) -> bool:
        if not Path(self.my_path + "/nasa_images").is_dir():
            os.mkdir(Path(self.my_path + '/nasa_images'))
        binary_image.save(f'{self.my_path + "/nasa_images"}/{self.scraper.parameter}_{index_image}.jpg')
        return Path(f'{self.my_path + "/nasa_images"}/{self.scraper.parameter}_{index_image}.jpg').is_file()

    def extracting_specific_term(self) -> None:
        self.nasa_app.set_parameter(self.search_term)
        self.nasa_app.extract_information()
        if len(self.nasa_app.results) > 0:
            for occurrence in tqdm(self.nasa_app.results, desc='Processing results'):
                data = occurrence.get('data', list())
                links = occurrence.get('links', [{'href': str()}])
                if data and len(data) > 0:
                    result_occurrence = {
                        'title': data[0].get('title', str()),
                        'description': data[0].get('description', str()),
                        'image_link': links[0].get('href')
                    }
                    self.data_box.save_occurrence_information(result_occurrence,\
                    f'output_nasa_images_{self.search_term.lower().replace(" ", "_")}')
