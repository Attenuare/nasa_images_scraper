from datetime import datetime
from pathlib import Path
from io import StringIO
import csv
import os


class DataBox(object):
    """
        Class used to manipulate archives and make
        a output in csv, and also read from a csv file
    """
    def __init__(self):
        self.files_dict = dict()
        self.file = None
        self.typing = str()
        self.parameters = None

    def get_specific_file(self) -> None:
        while True:
            files_list = os.listdir()
            self.files_dict = {files_list.index(file) + 1: file for file in os.listdir() if '.csv' in file or '.PDF' in file}
            print('Wich file to you want to input: ')
            count_csv = 0
            for element in self.files_dict.items():
                if '.csv' in element[1].lower():
                    print(f'\t{element[0]} - {element[1]}')
                    count_csv += 1
            if count_csv > 0:
                file_name = int(input("Enter a number: "))
                if file_name in self.files_dict.keys():
                    self.file = self.files_dict[file_name]
                    break
                else:
                    print('Wrong number! Try again!\n')
                    continue
            else:
                print("There's no csv file in this directory")
                break

    def verify_path_file(self, file: str or None = None) -> bool:
        if file:
            self.file = file
        if self.file:
            my_path = os.getcwd()
            my_path = my_path.replace('\\', '/')
            destiny = Path(my_path + f'/{self.file}')
            if destiny.is_file():
                return True
            else:
                return False
        else:
            raise ValueError('Need file name to verifys his path')

    def convert_results_to_dict(self) -> None:
        if len(self.results) > 0:
            temp_results = list()
            fieldnames = self.results[0]
            for element in self.results[1:]:
                temp_dict = dict()
                for _, key in enumerate(fieldnames):
                    try:
                        possible_value = element[_]
                    except IndexError:
                        possible_value = str()
                    temp_dict[key] = possible_value
                temp_results.append(temp_dict)
            if (len(self.results) - 1) == len(temp_results):
                self.results = temp_results

    def manipulating_data(self, **kwargs) -> list[str] or None:
        """
            Method used for in and out data, shifting modes of csv trought
            receiving parameter in function calling, if need it to get in
            data used typing 'r' or out data typing 'a'.
        """
        self.typing = kwargs.get('typing', '-')
        if self.typing == '-':
            self.typing = 'r'
        self.fieldnames = kwargs.get('fieldnames', '-')
        if self.fieldnames == '-' and self.typing == 'a':
            raise ValueError('Need fieldnames to add in csv file')
        if not self.file:
            self.file = kwargs.get('filename', '-')
        if self.file == '-':
            raise ValueError('Need the files name')
        self.parameters = kwargs.get('parameter', '-')
        if self.parameters == '-' and self.typing == 'a':
            raise ValueError('Need parameters to save into the csv')
        self.file = f'{self.file}.csv' if '.csv' not in self.file else self.file
        if self.typing == 'a':
            if not self.verify_path_file():
                with open(self.file, 'a', encoding='utf8', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(self.fieldnames)
            with open(self.file, self.typing, encoding='utf8', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(self.parameters)
        elif self.typing == 'r':
            while True:
                if self.file is not None and self.verify_path_file():
                    break
                self.file = str(input("Enter the name of the file without the .csv extention: \n")).replace(".csv", "")
                self.file = f'{self.file}.csv' if '.csv' not in self.file else self.file
                if self.verify_path_file() is False:
                    print(f'File {self.file} do not existis, try again!')
                    continue
                else:
                    break
            with open(self.file, self.typing, encoding='utf8') as csv_file:
                reader = csv.reader(csv_file)
                self.results = [parameter for parameter in reader]

    def save_occurrence_information(self, product_dict: dict[str], file_name: str = None) -> None:
        if file_name:
            self.file = file_name
        else:
            date = datetime.now().date()
            self.file = f'output_generic_file_{date}'
        if self.verify_path_file(f'{self.file}.csv') is False:
            need_headers = True
        else:
            need_headers = False
        with open(self.file, 'a', encoding='utf8', newline='') as csv_file:
            fieldnames = list(product_dict.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if need_headers is True:
                writer.writeheader()
            writer.writerow(product_dict)

    def generate_csv(self, term_list: list, have_dicts: bool = False) -> StringIO:
        '''
            Generating a csv file in memory, withou passing trough a
            directory from the machine
        '''
        csv_buffer = StringIO()
        if have_dicts:
            fieldnames = list(term_list[0].keys())
            writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writeheader()
            [writer.writerow(occurrence) for occurrence in term_list]
        else:
            writer = csv.writer(csv_buffer, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(['ean'])
            [writer.writerow([term]) for term in term_list]
        return csv_buffer
