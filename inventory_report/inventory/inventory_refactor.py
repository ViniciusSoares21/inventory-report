from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        for value in self.importer.import_data(path):
            self.data.append(value)

    def __iter__(self):
        return InventoryIterator(self.data)
