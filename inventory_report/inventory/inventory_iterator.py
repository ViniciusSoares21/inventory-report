from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data) -> None:
        self.index = 0
        self.data = data

    def __next__(self):
        try:
            item = self.data[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return item
