import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return None

    if '.csv' in sys.argv[1]:
        report = InventoryRefactor(CsvImporter)
    if '.json' in sys.argv[1]:
        report = InventoryRefactor(JsonImporter)
    if '.xml' in sys.argv[1]:
        report = InventoryRefactor(XmlImporter)

    return sys.stdout.write(report.import_data(
        sys.argv[1], sys.argv[2])
    )
