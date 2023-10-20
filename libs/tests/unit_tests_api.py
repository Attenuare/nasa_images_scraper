import sys
sys.path.append('/home/usuario/Área de trabalho/leandro_alves/repositorys/nasa_images_scraper')
from libs.app.nasa_images_class import NasaMedia
import unittest


class TestAPIMethods(unittest.TestCase):
    def setUp(self):
        self.nasa_object = NasaMedia()
        self.testing_connection()
        self.json_keys = {'object': ['href', 'data', 'links'],
                         'sub_object': ['title', 'nasa_id', 
                         'date_created', 'media_type', 'description']}

    def testing_parameter_setting(self):
        self.nasa_object.set_parameter('sun')
        self.assertEqual(self.nasa_object.parameter, 'sun')

    def testing_connection(self):
        self.testing_parameter_setting()
        self.nasa_object.extract_information()
        self.assertEqual(self.nasa_object.response.status_code, 200)
        self.assertEqual(self.nasa_object.availiable, True)

    def testing_raising_parameter_error(self):
        with self.assertRaises(ValueError):
            self.nasa_object.parameter = None
            self.nasa_object.set_parameter()

    def testing_object_response(self):
        self.assertEqual(type(self.nasa_object.results), list)
        self.assertGreater(len(self.nasa_object.results), 0)

    def testing_sub_objects_from_response(self):
        self.assertEqual(type(self.nasa_object.results[0]), dict)

    def testing_keys_from_sub_objects_response(self):
        self.assertEqual(list(self.nasa_object.results[0].keys()), self.json_keys['object'])

    def testing_sub_objects_from_data_response(self):
        current_sub_keys = list(self.nasa_object.results[0]['data'][0].keys())
        for possible_key in self.json_keys['sub_object']:
            self.assertEqual(possible_key in current_sub_keys, True)

if __name__ == '__main__':
    unittest.main()
