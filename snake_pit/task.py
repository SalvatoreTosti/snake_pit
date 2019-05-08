from abc import ABC, abstractmethod,ABCMeta
import multiprocessing
import os
import signal
from random import shuffle
import itertools
import uuid

class Task(ABC):

    def __init__(self):
        self._id = uuid.uuid1()
        self._results = None
        self._total = 0
        self._pool = multiprocessing.Pool()
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
            return self._results
        return None
    
    @property
    def status(self):
        return {'cancelled' : self._cancelled}
    
    def _kill(self):
        self._pool._state = multiprocessing.pool.TERMINATE
        self._pool._worker_handler._state = multiprocessing.pool.TERMINATE
        for process in self._pool._pool:
            os.kill(process.pid, signal.SIGKILL)
        while any(process.is_alive() for process in self._pool._pool):
            pass
        self._pool.terminate()
        
    def cancel(self):
        if self.done:
            return
        self._cancelled = True
        self._kill()
        
    @staticmethod
    @abstractmethod
    def _parallelStep(iterableArg):
        pass
    
    def _processResults(self, results):
        return results;
    
    def _createIterableList(self, args):
        return args;
        
    def _callback(self, args):
        self._results = self._processResults(args)
    
    def run(self, args):
        iterableArgList = self._createIterableList(args);
        func = type(self)._parallelStep #Work around since map_async requires static function
        self._mResult = self._pool.map_async(func, iterableArgList, callback=self._callback, chunksize=1)
        self._total = self._mResult._number_left
