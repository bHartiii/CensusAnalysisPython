import abc


class CSVLoaderInterface(abc.ABC):

    def __init__(self, header, path):
        self.path = path
        self.header = header

    @abc.abstractmethod
    def record_counter_in_csv(self):
        pass
