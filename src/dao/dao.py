import pickle
from abc import ABC, abstractmethod
import os


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self._datasource = datasource
        self._cache = (
            {}
        )
        try:
            self._load()
        except FileNotFoundError:
            self._dump()
        self._load()

    def _dump(self):
        pickle.dump(self._cache, open(self._datasource, "wb"))
    
    def _load(self):
        self._cache = pickle.load(open(self._datasource, "rb"))
    
    def add(self, key, obj):
        self._cache[key] = obj
        self._dump()
    
    def update(self, key, obj):
        try:
            if self._cache[key] is not None:
                self._cache[key] = obj
                self._dump()
        except KeyError:
            raise KeyError(f"Chave {key} não encontrada para update")

    def get(self, key):
        try:
            return self._cache[key]
        except KeyError:
            return None
        
    def remove(self, key):
        try:
            del self._cache[key]
            self._dump()
        except KeyError:
            raise KeyError(f"Chave {key} não encontrada para remover")
    
    def get_all(self):
        return self._cache.values()
