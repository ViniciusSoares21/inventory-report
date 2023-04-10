from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def read_xml(path: str):
        file = ET.parse(path)
        value_file = file.getroot()
        data_result = []
        for value in value_file.findall('record'):
            object = {}
            for element in value.iter():
                if element.tag != 'record':
                    object[element.tag] = element.text
            data_result.append(object)
        return data_result

    @classmethod
    def import_data(cls, path):
        verify_path = '.xml' in path
        if not verify_path:
            raise ValueError('Arquivo inválido')
        data_xml = cls.read_xml(path)
        return data_xml
