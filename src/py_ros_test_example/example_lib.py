class Counter(object):
    def __init__(self):
        self._counter = 0

    def next(self):
        self._counter += 1

    def previous(self):
        self._counter -= 1

    def get(self):
        return self._counter
