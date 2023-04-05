from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def read_csv(path: str):
        with open(path) as file:
            users_reader = csv.DictReader(file)
            users_list_dic = []
            for list_users in users_reader:
                users_list_dic.append(list_users)

        return users_list_dic

    @classmethod
    def import_data(cls, path):
        verify_path = '.csv' in path
        if not verify_path:
            raise ValueError('Arquivo inválido')
        data_csv = cls.read_csv(path)
        return data_csv
