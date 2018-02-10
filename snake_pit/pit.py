import Task

class Pit:
    "Controls inititalization and polling of tasks."

    def __init__(self):
        self.activeTasks = {}
    
    def startTask(args):
        task = Task()
        self.activeTasks.update({str(task.id) : task})
        task.run(args)
        return task.id
    
    def done(self,taskID):
        if taskID in self.activeTasks:
            return self.activeTasks[taskID].done
            
    def results(self, taskID):
        if taskID in self.activeTasks:
            return self.activeTasks.pop(taskID).results
    
    def status(self, taskID):
        if taskID in self.activeTasks:
            return self.activeTasks[taskID].status
            
    def progress(self,taskID):
        if taskID in self.activeTasks:
            return self.activeTasks[taskID].progress
            
    def cancel(self,taskID):
        if taskID in self.activeTasks:
            return self.activeTasks[taskID].cancel()

    def cleanup(self,taskID):
        if taskID in self.activeTasks:
            self.activeTasks.pop(taskID)