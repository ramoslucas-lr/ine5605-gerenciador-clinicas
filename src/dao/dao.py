import pickle
from abc import ABC, abstractmethod
import os


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.__cache = (
            {}
        )
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
        self._load()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))
    
    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, "rb"))
    
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()
    
    def update(self, key, obj):
        try:
            if self.__cache[key] is not None:
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            raise KeyError(f"Chave {key} não encontrada para update")

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None
        
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise KeyError(f"Chave {key} não encontrada para remover")
    
    def get_all(self):
        return self.__cache.values()
