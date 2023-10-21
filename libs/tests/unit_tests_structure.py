import sys
import os
my_path = os.getcwd().replace('\\', '/')
sys.path.append(my_path.replace('/libs/tests', str()))
from libs.context.nasa_context import NasaContext
from pathlib import Path
import unittest


class TestStructureMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.nasa_context = NasaContext('sun')
        self.nasa_context.extracting_specific_term()
        self.my_path = my_path
        self.csv_data = dict()
        self.csv_keys = ['title', 'description', 'image_link']

    def testing_file_creation(self) -> None:
        self.assertEqual(Path(self.my_path + f"/output_nasa_images_{self.nasa_context.search_term}.csv").is_file(), True)

    def testing_csv_file(self) -> None:
        self.nasa_context.data_box.manipulating_data(filename=f'output_nasa_images_{self.nasa_context.search_term}.csv')
        self.assertEqual(type(self.nasa_context.data_box.results), list)
        self.nasa_context.data_box.convert_results_to_dict()
        self.csv_data = self.nasa_context.data_box.results
        self.assertEqual(type(self.nasa_context.data_box.results), list)

    def testing_keys_from_file_csv(self) -> None:
        self.testing_csv_file()
        self.assertEqual(type(self.csv_data[0]), dict)
        self.assertEqual(list(self.csv_data[0].keys()), self.csv_keys)

    def testing_images_links_filled(self) -> None:
        self.assertGreater(len(self.nasa_context.all_images_links), 0)

    def testing_images_links_http_protocol(self) -> None:
        self.assertEqual('http' == self.nasa_context.all_images_links[0][:4], True)

    def testing_images_links_downloading(self) -> None:
        self.nasa_context.all_images_links = self.nasa_context.all_images_links[:4]
        self.nasa_context.download_all_results_images()
        all_files = [_ for _ in Path(self.my_path + '/nasa_images').iterdir()]
        self.assertEqual(len(all_files), len(self.nasa_context.all_images_links))

    @classmethod
    def tearDownClass(self) -> None:
        os.system(f'rm ./output_nasa_images_{self.nasa_context.search_term}.csv')
        os.system(f'rm ./nasa_images')

if __name__ == '__main__':
    unittest.main()
