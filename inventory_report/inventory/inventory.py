from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def read_csv(path: str):
        with open(path) as file:
            users_reader = csv.DictReader(file)
            users_list_dic = []
            for list_users in users_reader:
                users_list_dic.append(list_users)

        return users_list_dic

    def read_json(path: str):
        with open(path) as file:
            return json.load(file)

    def read_xml(path: str):
        file = ET.parse(path)
        value_file = file.getroot()
        data_result = []
        for value in value_file.findall('record'):
            object = {}
            for element in value.iter():
                object[element.tag] = element.text
            data_result.append(object)
        return data_result

    def csv_report(self, path, type):
        data_csv = self.read_csv(path)
        if type == 'simples':
            return SimpleReport.generate(data_csv)
        if type == 'completo':
            return CompleteReport.generate(data_csv)

    def json_report(self, path, type):
        data_json = self.read_json(path)
        if type == 'simples':
            return SimpleReport.generate(data_json)
        if type == 'completo':
            return CompleteReport.generate(data_json)

    def xml_report(self, path, type):
        data_xml = self.read_xml(path)
        if type == 'simples':
            return SimpleReport.generate(data_xml)
        if type == 'completo':
            return CompleteReport.generate(data_xml)

    @classmethod
    def import_data(self, path: str, type):
        print(path)
        if '.csv' in path:
            return self.csv_report(self, path, type)

        if '.json' in path:
            return self.json_report(self, path, type)

        if '.xml' in path:
            return self.xml_report(self, path, type)
