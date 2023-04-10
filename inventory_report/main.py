import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

arguments = sys.argv


def main():
    if len(arguments) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return None

    if '.csv' in arguments[1]:
        report = InventoryRefactor(CsvImporter)
    if '.json' in arguments[1]:
        report = InventoryRefactor(JsonImporter)
    if '.xml' in arguments[1]:
        report = InventoryRefactor(XmlImporter)

    return print(report.import_data(
        arguments[1], arguments[2]),
        file=sys.stdout
    )
