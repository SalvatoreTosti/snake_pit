from abc import ABC, abstractmethod, ABCMeta
from task import Task

class Pit(ABC):
    "Controls inititalization and polling of tasks."

    def __init__(self):
        self._activeTasks = {}
    
    @property
    def activeTasks(self):
        return self._activeTasks
    
    def startTask(self, *args):
        taskAndArgs = self.instantiateTask(args)
        task = taskAndArgs[0]
        taskArgs = taskAndArgs[1]
        self._activeTasks.update({str(task.id) : task})
        task.run(taskArgs)
        return str(task.id)
 
    @abstractmethod
    def instantiateTask(self, args):
        pass
    
    def done(self, taskID):
        if taskID in self._activeTasks:
            return self._activeTasks[taskID].done
            
    def results(self, taskID):
        if taskID in self._activeTasks:
            return self._activeTasks.pop(taskID).results
    
    def status(self, taskID):
        if taskID in self._activeTasks:
            return self._activeTasks[taskID].status
            
    def progress(self, taskID):
        if taskID in self._activeTasks:
            return self._activeTasks[taskID].progress
            
    def cancel(self, taskID):
        if taskID in self._activeTasks:
            return self._activeTasks[taskID].cancel()

    def cleanup(self, taskID):
        if taskID in self._activeTasks:
            self._activeTasks.pop(taskID)