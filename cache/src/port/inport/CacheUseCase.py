import abc


class CacheService(metaclass=abc.ABCMeta):
    """interface demonstrating the cacheservice

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.
    """

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def put(self, key, value):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass

    @abc.abstractmethod
    def evict(self, key):
        pass

    @abc.abstractmethod
    def clear(self):
        pass
