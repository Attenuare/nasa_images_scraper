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
    def __init__(self, search_term: str, save_image_flag: bool=bool()):
        self.my_path = os.getcwd().replace('\\', '/')
        self.nasa_app = NasaMedia()
        self.data_box = DataBox()
        self.search_term = search_term
        self.save_image_flag = save_image_flag
        self.all_images_links = list()

    def downloading_images(self, image_link: str) -> list['PIL.JpegImagePlugin.JpegImageFile', int]:
        """
            Get a list of images links and download this images 
            and save in a diretory from the OS
        """
        if image_link.startswith('http'):
            self.nasa_app.send_requisitons_requests(image_link)
            if not self.nasa_app.availiable:
                return
            file_image = Image.open(BytesIO(self.nasa_app.response.content))
        else:
            return
        return [file_image, self.nasa_app.response.status_code]

    def save_image(self, binary_image: 'PIL.JpegImagePlugin.JpegImageFile', index_image: int) -> bool:
        if not Path(self.my_path + "/nasa_images").is_dir():
            os.mkdir(Path(self.my_path + '/nasa_images'))
        binary_image.save(f'{self.my_path + "/nasa_images"}/{self.search_term}_{index_image}.jpg')
        return Path(f'{self.my_path + "/nasa_images"}/{self.search_term}_{index_image}.jpg').is_file()

    def extracting_specific_term(self) -> None:
        self.nasa_app.set_parameter(self.search_term)
        self.nasa_app.extract_information()
        if len(self.nasa_app.results) > 0:
            for index, occurrence in enumerate(tqdm(self.nasa_app.results, desc='Processing results')):
                data = occurrence.get('data', list())
                links = occurrence.get('links', [{'href': str()}])
                if data and len(data) > 0:
                    result_occurrence = {
                        'title': data[0].get('title', str()),
                        'description': data[0].get('description', str()),
                        'image_link': links[0].get('href')}
                    self.all_images_links.append(result_occurrence['image_link'])
                    self.data_box.save_occurrence_information(result_occurrence,\
                    f'output_nasa_images_{self.search_term.lower().replace(" ", "_")}')
            if self.save_image_flag:
                self.download_all_results_images()

    def download_all_results_images(self) -> None:
        if len(self.all_images_links) > 0:
            for index, image_link in enumerate(tqdm(self.all_images_links, desc='Downloading images')):
                binary_image = self.downloading_images(image_link)
                self.save_image(binary_image[0], index)
