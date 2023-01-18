import json
from abc import abstractmethod


class BaseConfigurationSection:
    @property
    @abstractmethod
    def __attr__(self):
        raise NotImplementedError

    def to_dict(self):
        return {k: self.__getattribute__(k) for k in self.__attr__}

    def to_object(self):


foo = BaseConfigurationSection()
print(foo.to_dict())
