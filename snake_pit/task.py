from abc import ABC, abstractmethod
from multiprocessing import Pool
from random import shuffle
import itertools
import uuid

class Task(ABC):

    def __init__(self):
        self._id = uuid.uuid1()
        self._results = None
        self._total = 0
        self._pool = Pool()
        self._mResult = None
        self._cancelled = False
    
    @property
    def id(self):
        return self._id
    
    def __getDoneNumber(self):
        return self._total - self._mResult._number_left
        
    @property
    def progress(self):
        return {
            'done' : self.__getDoneNumber(),
            'total' : self._total}
    @property
    def done(self):
        if self._results:
            self._pool.close()
            self._pool.join()
            return True
        return False
    
    @property
    def results(self):  
        if self.done:
            self._results.update({'cancelled' : self._cancelled})
            return self._results
        return None
    
    @property
    def status(self):
        return {'cancelled' : self._cancelled}
        
    def cancel(self):
        if self.done:
            return
        self._cancelled = True
        self._pool.close()
        self._pool.join()
        
    @abstractmethod
    def _parallelStep(iterableArg):
        pass
    
    @abstractmethod
    def _processResult(results):
        pass
    
    @abstractmethod
    def _createIterableList(self, *args):
        pass
        
    def _callback(self, results):
        self._results = Task._processResult(results)
    
    def run(self, *args):
        iterableArgList = self._createIterableList(args);
        self._mResult = self._pool.map_async(Task._parallelStep, iterableArgList, callback=self._callback, chunksize=1)
        self._total = self._mResult._number_left
