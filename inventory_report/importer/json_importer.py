from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def read_json(path: str):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def import_data(cls, path):
        verify_path = '.json' in path
        if not verify_path:
            raise ValueError('Arquivo inválido')
        data_json = cls.read_json(path)
        return data_json
