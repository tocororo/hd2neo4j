import json


class Data_Iterator:
    def __init__(self, data, stop_at: int | None = None):
        self.data = json.loads(data)
        self.stop_at = stop_at
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.stop_at and self.position == self.stop_at:
            raise StopIteration

        return self.data[self.position]
